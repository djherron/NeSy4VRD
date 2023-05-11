#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script is part of NeSy4VRD. It is sample code for demonstrating one
potential scenario in which the NeSy4VRD visual relationship annotations
might be used in conjunction with the NeSy4VRD OWL ontology, VRD-World, an
RDF knowledge graph and OWL reasoning.

This script does the following:
* instantiates an empty RDFLib knowledge graph (KG)
* loads the NeSy4VRD VRD-World OWL ontology into the KG
* converts NeSy4VRD visual relationship annotations into RDF triples 
  and loads them into the KG
* uses the OWL reasoner of Python package OWLRL to materialise the KG
  (to infer new relationships between image objects that are entailed by 
   the visual relationship data triples in the presence of the 
   VRD-World ontology)
* uses a SPARQL query to extract the (potentially augmented) set of
  VR-related triples for each image from the KG
* converts the extracted triples back into (a potentially augmented set of) 
  NeSy4VRD visual relationship annotations
* saves the reconstituted (augmented) NeSy4VRD visual relationship annotations 
  to a disk file in JSON format

NOTE: This script is designed to be executed in an IDE, cell by cell. But
it can be run in batch mode.

DEPENDENCIES:
This module has dependencies on Python packages:
    RDFLib
    OWLRL
'''

#%% imports

from rdflib import Graph

from owlrl import DeductiveClosure, OWLRL_Semantics

import os
import json

import nesy4vrd_utils4 as vrdu4


#%% get the NeSy4VRD visual relationship annotations data

# set the path to the directory where the NeSy4VRD visual relationship
# annotations files reside
anno_dir = os.path.join('..', 'data', 'annotations')

# get the master list of NeSy4VRD object class names
vrd_objects_path = os.path.join(anno_dir, 'nesy4vrd_objects.json')
vrd_objects = vrdu4.load_NeSy4VRD_object_class_names(vrd_objects_path)

# get the master list of NeSy4VRD predicate names
vrd_predicates_path = os.path.join(anno_dir, 'nesy4vrd_predicates.json')
vrd_predicates = vrdu4.load_NeSy4VRD_predicate_names(vrd_predicates_path)

# get the desired set of NeSy4VRD visual relationship annotations
vrd_annotations_path = os.path.join(anno_dir, 'nesy4vrd_annotations_train.json')
vrd_anno = vrdu4.load_NeSy4VRD_image_annotations(vrd_annotations_path)

# get a list of the VRD image names from the NeSy4VRD annotations dictionary
vrd_img_names = list(vrd_anno.keys())


#%% convert NeSy4VRD object class and predicate names to VRD-World ontology names

ontoClassNames = vrdu4.convert_NeSy4VRD_classNames_to_ontology_classNames(vrd_objects)

ontoPropNames = vrdu4.convert_NeSy4VRD_predicateNames_to_ontology_propertyNames(vrd_predicates)


#%% initialise sequence numbers for individual objects to be loaded into KG

number_of_vrd_object_classes = len(vrd_objects)
vrdu4.initialise_object_sequence_numbers(number_of_vrd_object_classes)


#%% instantiate a new KG

kg = Graph()
print(f'Newly instantiated KG has {len(kg)} triples')


#%% specify a VRD-World OWL ontology with which to work

# set the name the VRD-World OWL ontology file to work with
target_ontology = 'vrd_world_v1.owl'

ontology_dir = os.path.join('..', 'ontology')
ontology_path = os.path.join(ontology_dir, target_ontology)

print(f"Ontology '{target_ontology}' is to be loaded into the KG")


#%% load the target VRD-World OWL ontology into the KG

kg.parse(ontology_path, format='ttl')
print(f"Ontology '{target_ontology}' loaded into KG")
print(f'The KG now has {len(kg)} triples')


#%% (optionally) prepare subsets of images for testing purposes

# NOTE: You can run this script against the full NeSy4VRD training and/or
#       test visual relationship annotations files.  But if you are just
#       exploring the functionality, you may wish to start by processing
#       the visual relationship annotations for a small subset of images
#       only.  Here you have an opportunity to establish that small
#       subset of images.
#
#       The image names used here are all associated with the NeSy4VRD
#       training set visual relationship annotations that live in file 
#       'nesy4vrd_annotations_train.json'.  If you loaded a different
#       annotations file they likely won't be recognised.

#img_name_subset = ['3493152457_8dde981cc9_b.jpg']
#
#img_name_subset = ['3493152457_8dde981cc9_b.jpg',
#                  '7764151580_182e10b9fe_b.jpg']
#
#img_name_subset = ['3493152457_8dde981cc9_b.jpg',
#                  '7764151580_182e10b9fe_b.jpg',
#                  '8013060462_4cdf330e98_b.jpg']

img_name_subset = ['8054281885_ebbbfa2672_b.jpg',
                  '5813297357_f210a455f9_b.jpg',
                  '470440265_7c5367260f_b.jpg',
                  '9862618725_b271b9973f_b.jpg',
                  '324950887_a2c8d26083_b.jpg']

# override the original (full) list of image names with your small subset
vrd_img_names = img_name_subset


#%%

print(f'We will be processing VRs for {len(vrd_img_names)} images')


#%%

# control whether or not to print detailed info to the console during
# processing; if you are processing the VRs for ALL images (or a large
# number, you will want to turn this off; otherwise, if you are
# processing just a small number of images, you find the information
# helpful)
verbose_mode = True

print(f'verbose mode is: {verbose_mode}')


#%% convert VR annotations into RDF triples and load into KG 

image_cnt = 0
total_object_cnt = 0
total_triple_cnt = 0

# maintain a list of the unique ids created to represent each VRD image
# when it is loaded into the KG; there will be positional correspondence
# between image_id entries in this list and image filename entries in
# the list (variable) named 'vrd_img_names'
kg_vrd_img_ids = []

# maintain a list of the counts of the number of human-annotated VRs
# per VRD dataset image; there will be positional correspondence
# between vr count entries in this list and image filename entries in
# the list (variable) named 'vrd_img_names'
vrd_img_vr_cnts = []

# maintain a list of dictionaries, one dictionary per image; the dictionary 
# for a particular image contains one entry for each object annotated 
# as appearing in the image; the 'key' for an entry is the object's bbox
# (in the form of a tuple); the 'value' is a list of 3 elements:
# [kg_object_id, kg_object_uriref, object_idx], where object_idx is the
# VRD object class label (integer index) identifying the object class of the 
# corresponding bbox
objects_per_image = []


# iterate over the images whose visual relationships we wish to process
for imname in vrd_img_names:
    
    imanno = vrd_anno[imname]
    image_objects = {}
    image_cnt += 1
    image_triple_cnt = 0
    
    if verbose_mode:
        print(f'\nprocessing image: {imname}')
    
    # create RDF triples describing the current VRD image object 
    # and add these to the KG
    results = vrdu4.build_triples_for_image(imname)
    kg_image_id, kg_image_uriref, triples = results
    kg_vrd_img_ids.append(kg_image_id)
    image_triple_cnt += len(triples)  
    for triple in triples:
        kg.add(triple)

    #
    # iterate over the VR annotations for the current image; convert
    # them into RDF triples and add them to the KG
    #

    vr_cnt = 0 

    for vr in imanno:
        
        vr_cnt += 1
        vr_triple_cnt = 0
        
        # get the elements of the current annotated VR 
        sub_idx = vr['subject']['category']
        sub_bbox = tuple(vr['subject']['bbox'])
        prd_idx = vr['predicate']
        obj_idx = vr['object']['category']
        obj_bbox = tuple(vr['object']['bbox'])
        
        # process the 'subject' object of the VR
        if sub_bbox in image_objects:
            # the triples defining this object have already been added to
            # the KG; just retrieve its URI for reuse below
            _, kg_subject_uriref, _ = image_objects[sub_bbox]
            triple_cnt = 0
        else:
            # this is the first time we've encountered this particular object,
            # so build triples for defining it and add them to the KG
            results = vrdu4.build_triples_for_object(sub_idx, sub_bbox,
                                                     ontoClassNames,
                                                     kg_image_uriref)
            kg_subject_id, kg_subject_uriref, triples = results
            triple_cnt = len(triples)
            image_objects[sub_bbox] = [kg_subject_id, kg_subject_uriref, sub_idx]
            for triple in triples:
                kg.add(triple)
        
        vr_triple_cnt += triple_cnt
        
        # process the 'object' object of the VR
        if obj_bbox in image_objects:
            # the triples defining this object have already been added to
            # the KG; just retrieve its URI for reuse below
            _, kg_object_uriref, _ = image_objects[obj_bbox]
            triple_cnt = 0
        else:
            # this is the first time we've encountered this particular object,
            # so build triples for defining it and add them to the KG            
            results = vrdu4.build_triples_for_object(obj_idx, obj_bbox,
                                                     ontoClassNames,
                                                     kg_image_uriref)
            kg_object_id, kg_object_uriref, triples = results
            triple_cnt = len(triples)
            image_objects[obj_bbox] = [kg_object_id, kg_object_uriref, obj_idx]
            for triple in triples:
                kg.add(triple)
        
        vr_triple_cnt += triple_cnt
        
        # link the 'subject' object to the 'object' object of the VR;
        # use the ontology object property that corresponds to the VRD
        # predicate in the annotated VR; the resulting single triple is the 
        # key triple that represents (expresses) the visual relationship 
        # between the particular ordered pair of objects referenced in the
        # current annotated VR
        triples = vrdu4.build_triple_linking_subject_to_object(kg_subject_uriref,
                                                               prd_idx,
                                                               kg_object_uriref,
                                                               ontoPropNames)
        vr_triple_cnt += len(triples)
        for triple in triples:
            kg.add(triple)
        
        image_triple_cnt += vr_triple_cnt
    
     
    # save the 'image_objects' dictionary for the current image; we'll reuse 
    # this info later when we extract triples from the expanded (materialised)
    # KG for this image and convert them back into VR annotations; 
    # the reason we use this tactic is simply for processing efficiency;
    # the reasoning (materialisation) of the KG won't invent new objects
    # or affect the bounding boxes of existing objects in any way;
    # so it's more efficient to keep track the bounding boxes for each 
    # object in a given image externally from the KG, and then reuse them
    # as appropriate when reconstituting the augmented set of visual
    # relationship annotations for each image.
    objects_per_image.append(image_objects)
    
    # save the number of VRs associated with the current image (prior to
    # KG materialisation)
    vrd_img_vr_cnts.append(vr_cnt)
    
    if verbose_mode:    
        print(f'triples loaded to KG for image: {image_triple_cnt}')
    
    total_triple_cnt += image_triple_cnt


print(f'\nNumber of images processed: {image_cnt}')

print(f'\nTotal VR-related triples loaded to KG: {total_triple_cnt}')

#%%

print(f'After loading the VR triples, the KG has {len(kg)} triples')


#%% expand (materialise) the KG

# configure the form of expansion (materialisation) we wish to perform
dc = DeductiveClosure(OWLRL_Semantics,
                      rdfs_closure = False,
                      axiomatic_triples = False,
                      datatype_axioms = False)

# perform the expansion (materialisation)
# (IE invoke OWL reasoning to infer all triples entailed by the current 
#  contents of the KG, given the inference semantics of the VRD-World
#  OWL ontology governing the KG and that data triples that have been
#  loaded into it.)
dc.expand(kg)

print(f'The expanded (materialised) KG has {len(kg)} triples')


#%% optionally, save the expanded KG

#filename = 'vrd_world_v1_loaded_and_materialised.ttl'

#kg.serialize(destination=filename, format='ttl')

#print(f"The expanded (materialised) KG was serialised to file '{filename}'")


#%% extract the augmented set triples and convert back to VR annotations

# maintain a dictionary to hold the KG-augmented list of visual relationships
# (VRs) for each image in the VRD dataset
vrd_anno_augmented = {}


# iterate over the image names whose visual relationships we wish to process
for idx, imname in enumerate(vrd_img_names): 
    
    # get the original VRs for the current image
    imanno = vrd_anno[imname]     

    # get the unique id used in the KG to represent the current VRD image
    kg_image_id = kg_vrd_img_ids[idx]
 
    # build a SPARQL query designed to retrieve the triples in the KG 
    # associated with the visual relationships for the current image
    query = vrdu4.assemble_SPARQL_query(imname, kg_image_id)

    if verbose_mode:    
        print(f"\nextracting triples from KG for image '{imname}'")
    else:
        if idx % 100 == 0:
            print(f"extracting VRs from KG for image idx {idx}")
    
    # execute the SPARQL query
    qres = kg.query(query)

    # The query result set is a set of (subObj, property, objObj) triples.
    # Each triple is an abstract representation of a unique visual relationship
    # associated with the current image. Some triples will be representations
    # of the original VRs; others will be representations of new VRs
    # inferred by the KG materialisation process.
    
    # NOTE: if you are processing the visual relationships for just a small 
    #       number of images, you may be interested to see the result set
    #       of the SPARQL query; if so, uncomment
    #
    #print(f"displaying extracted triples:")
    #for row in qres:
    #    print(f"{row.subObj} {row.property} {row.objObj}")
    #    print()
    
    # report the original number of VRs for the current image and the
    # new number of VRs after KG materialisation for comparison
    if verbose_mode:
        print(f"number of original VRs: {vrd_img_vr_cnts[idx]}")
        print(f"number of expanded VRs: {len(qres)}")
        print()
    
    # get the objects and their bboxes for current image that were saved earlier
    image_objects = objects_per_image[idx]
    
    # create an inverted dictionary keyed by the kg_object_id value
    # (nb: we can ignore the middle 'value' element, v[1],
    #      so each entry will be: 'kg_object_id : [bbox, obj_idx]')
    inverted_image_objects = { v[0]: [k, v[2]] for k, v in image_objects.items() }

    # establish a list to hold the soon-to-be reconstructed set of VRs 
    # for the current image
    imanno_aug = []

    # iterate over the triples extracted from the KG for the current image;
    # each one effectively corresponds to a distinct VR;
    # validate them and convert them from their KG representations back
    # into standard VR format
    for row in qres:
        
        # ensure the two objects in the current triple are DIFFERENT
        # (nb: if they're not different, something in the SPARQL query
        # used to extract triples from the KG is broken)
        if row.subObj == row.objObj:
            raise ValueError(f'subObj same as objObj on image f{imname}')
                
        # convert the KG URI for the property linking the two objects to its 
        # corresponding VRD predicate integer index representation
        # - nb: since the ontoPropNames have positional correspondence
        #   with the VRD predicate names, the index position of the 
        #   ontoProperty within the ontoPropNames list will be the
        #   correct VRD predicate integer label
        # - nb: if an ontoProperty is not recognised as valid, an Exception
        #   will automatically be thrown which stops processing
        ontoProperty = row.property.split('#')[1]
        prd_idx = ontoPropNames.index(ontoProperty)
        
        # convert the KG URI for the 'subject' object to its corresponding
        # representation as a pair: bbox and class label index
        kg_object_id = row.subObj.split('#')[1]
        sub_bbox, sub_idx = inverted_image_objects[kg_object_id]
        sub_bbox = list(sub_bbox)

        # convert the KG URI for the 'object' object to its corresponding
        # representation as a pair: bbox and class label index
        kg_object_id = row.objObj.split('#')[1]
        obj_bbox, obj_idx = inverted_image_objects[kg_object_id]
        obj_bbox = list(obj_bbox)

        # assemble the elements into the dictionary format used for 
        # representing visual relationship annotations
        vr = {'predicate': prd_idx,
              'object': {'category': obj_idx, 'bbox': obj_bbox},
              'subject': {'category': sub_idx, 'bbox': sub_bbox}}

        # add the VR to the list of VRs for the current image
        imanno_aug.append(vr)
    
    # save the list of reconstituted VRs for the current image in the master
    # dictionary of VRs for all images being processed
    vrd_anno_augmented[imname] = imanno_aug


print('Extraction of triples from KG and conversion to VRs complete')

#%% save augmented set of VR annotations to file on disk 

filename = 'nesy4vrd_annotations_train_augmented.json'
anno_augmented_dir = os.path.join('..', 'data', 'annotations')
path = os.path.join(anno_augmented_dir, filename)

with open(path, 'w') as fp:
    json.dump(vrd_anno_augmented, fp) 

print()
print(f'Augmented VR annotations saved to file: {path}')
print()
print('Processing completed successfully!')




