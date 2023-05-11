#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module contains utility functions that support:
1) the loading of NeSy4VRD visual relationship annotations into an 
   RDFLib knowledge graph governed by the NeSy4VRD OWL ontology VRD-world,
   and
2) the extraction from that knowledge graph (via a SPARQL query) of all
   triples associated with specified images (so that they those triples
   can be converted back into NeSy4VRD visual relationship annotations).

A visual relationship annotation can be described informally as a 
(subject, predicate, object) 3-tuple, where both the 'subject' and
'object' objects are specified in terms of object classes (aka categories)
and bounding boxes 

Here's what a NeSy4VRD visual relationship annotation looks like when
it is loaded into Python from its .json file on disk:

{'predicate': 35,
 'object': {'category': 43, 'bbox': [376, 804, 133, 614]},
 'subject': {'category': 0, 'bbox': [149, 495, 267, 523]}}
    
The class of the 'subject' and 'object' objects is indicated by the
category ID. These integer category IDs are indices into the NeSy4VRD 
master list of object class names. 
The bounding boxes have format [ymin, ymax, xmin, xmax].
The integer 'predicate' ID is an index into the NeSy4VRD master list 
of predicate names.

In this example visual relationship, we have (subject, predicate, object)
category IDs of (0, 35, 43). This corresponds to (person, ride, horse).

DEPENDENCIES:
This module has dependencies on Python packages:
    RDFLib
'''

#%% imports

from rdflib.term import URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL, XSD

import sys
sys.path.insert(0, '../analysis')

import vrd_utils as vrdu
 

#%% global variables

# set the base URL to be used for knowledge graph (KG) resource URIs 
# (here we use that used in the NeSy4VRD VRD-World OWL ontology)
url_base = "http://www.semanticweb.org/nesy4vrd/ontologies/vrd_world#"


# Sequence numbers are used to generate unique names for all 
# individuals (owl:NamedIndividuals, such as images, objects and
# bounding boxes) pertaining to VRD image visual relationship 
# annotations that are loaded into the ABox of the KG 

start_seq_num = 10000

image_seq_num = start_seq_num
bbox_seq_num = start_seq_num

image_seq_num_key = 'image_seq_num'
object_seq_nums_key = 'object_seq_nums'
bbox_seq_num_key = 'bbox_seq_num'

seq_nums = {image_seq_num_key : image_seq_num,        
            bbox_seq_num_key : bbox_seq_num}


#%% 

def initialise_object_sequence_numbers(number_of_vrd_object_classes):
    
    object_seq_nums = [start_seq_num] * number_of_vrd_object_classes
    seq_nums[object_seq_nums_key] = object_seq_nums

    return


#%%

def load_NeSy4VRD_object_class_names(path):

    return vrdu.load_VRD_object_class_names(path)                  


#%%

def load_NeSy4VRD_predicate_names(path):

    return vrdu.load_VRD_predicate_names(path)
 
    
#%% 

def load_NeSy4VRD_image_annotations(path):

    return vrdu.load_VRD_image_annotations(path)


#%%

def convert_NeSy4VRD_classNames_to_ontology_classNames(vrd_objects):
    '''
    Convert each NeSy4VRD object class name to its corresponding VRD-World
    ontology class name.
    
    The VRD-World class names are all camel case, with the
    first word capitalised as well, and no spaces between words.
    '''
    
    onto_class_names = []
    
    for name in vrd_objects:
        name = name.lower()
        words = name.split()
        onto_class_name = ''
        for word in words:
            onto_class_name = onto_class_name + word.capitalize()
        onto_class_names.append(onto_class_name)

    return onto_class_names


#%%

def convert_NeSy4VRD_predicateNames_to_ontology_propertyNames(vrd_predicates):
    '''
    Convert each NeSy4VRD predicate name to its corresponding VRD-World 
    ontology object property name.
    
    The VRD-World ontology object property names are all camel case, with
    the first word uncapitalised, and no spaces between words.
    '''
    
    onto_property_names = []
    
    for name in vrd_predicates:
        name = name.lower()
        words = name.split()
        onto_property_name = ''
        for idx, word in enumerate(words):
            if idx == 0:
                onto_property_name = word
            else:
                onto_property_name = onto_property_name + word.capitalize()
        onto_property_names.append(onto_property_name)

    return onto_property_names   


#%%

def build_triples_for_image(imname):
    '''
    Construct and return the triples that will represent an individual
    VRD image within a KG.
    
    Parameters:
        imname : string - the filename of a VRD image
    
    Returns:
        image_id : string - the id assigned to represent the image in the KG
        image_uriref : string - the RDFLib URIRef for the image
        triples : list - of RDF triples in the RDFLib format used for
                  representing triples to be 'added' to a KG
    
    Note: the seq_numbers are updated here, 'in place'; that update  
    represents an essential supplementary 'return value' to be aware of.
    '''
    
    triples = []
 
    #
    # target triple: vrd:ImageNNNNN rdf:type owl:NamedIndividual
    #
    
    # the name of the class for representing images within the
    # class hierarchy of the VRD-World OWL ontology
    class_name = 'Image'

    # get the sequence number that will uniquely identify the new
    # individual VRD image within a KG
    seq_num_key = image_seq_num_key
    seq_nums[seq_num_key] += 1
    seq_num = seq_nums[seq_num_key]   
    
    # construct the triple
    image_id = class_name + str(seq_num)
    image_uriref = URIRef(url_base + image_id)
    triple = (image_uriref, RDF.type, OWL.NamedIndividual)
    triples.append(triple)
     
    #
    # example target triple: :ImageNNNNN rdf:type :Image
    #

    # construct the triple
    class_uriref = URIRef(url_base + class_name)
    triple = (image_uriref, RDF.type, class_uriref)
    triples.append(triple)

    #
    # example target triple:
    #   :ImageNNNNN rdfs:label '3493152457_8dde981cc9_b.jpg'^^xsd:string
    #

    # construct the triple
    literal = Literal(imname, datatype=XSD.string)
    triple = (image_uriref, RDFS.label, literal)
    triples.append(triple)
    
    return image_id, image_uriref, triples


#%%

def build_triples_for_object(cls_idx, bbox, ontoClassNames, image_uriref):
    '''
    Construct and return the triples for representing a new, individual
    object of a VRD image within a KG.
    
    Parameters:
        cls_idx : integer - the integer class label indicating the VRD object
                  class of the object represented by argument 'bbox'
        bbox : list of integers - the bounding box specification for a
               particular object in a particular VRD image
        ontoClassNames : list - ordered list of ontology class names
        image_uriref : string - the RDFLib URIREF for the particular VRD image
                       in which the object represented by arguments 'cls_idx'
                       and 'bbox' appears
    
    Returns:
        object_id : string - the id assigned to represent the object in the KG
        object_uriref : string - the RDFLib URIRef for the object
        triples : list - of RDF triples in the RDFLib format used for
                  representing triples to be 'added' to a KG
    
    Note: in the 'target triple' comments below, references to 'Person'
    are meant to be interpreted as representing any ontology class that 
    corresponds to a VRD object class.  We use the particular word 'Person'
    just for the clarity that might come from specificity.
    '''
    
    triples = []
    
    #
    # example target triple: :PersonNNNNN rdf:type owl.NamedIndividual
    #

    # get the name of the VRD-World class that corresponds to the 
    # category ID (NeSy4VRD object class index) for the current object   
    class_name = ontoClassNames[cls_idx]
    
    # get the sequence number that will uniquely identify the new
    # individual VRD image within a KG
    seq_num_key = object_seq_nums_key
    seq_nums[seq_num_key][cls_idx] += 1
    seq_num = seq_nums[seq_num_key][cls_idx] 

    # construct the triple
    object_id = class_name + str(seq_num)
    object_uriref = URIRef(url_base + object_id)
    triple = (object_uriref, RDF.type, OWL.NamedIndividual)
    triples.append(triple)

    #
    # example target triple: :PersonNNNNN rdf:type :Person
    #

    # construct the triple
    class_uri = URIRef(url_base + class_name)
    triple = (object_uriref, RDF.type, class_uri)
    triples.append(triple)


    #
    # example target triple: :ImageNNNNN :hasObject :PersonNNNNN
    #

    # construct the triple
    property_name = 'hasObject'
    property_uriref = URIRef(url_base + property_name)
    triple = (image_uriref, property_uriref, object_uriref)
    triples.append(triple)

    #
    # example target triple: :PersonNNNNN :sourceImage :ImageNNNNN
    #

    # construct the triple
    property_name = 'sourceImage'
    property_uriref = URIRef(url_base + property_name)
    triple = (object_uriref, property_uriref, image_uriref)
    triples.append(triple)

    #
    # example target triple: :BboxNNNNN rdf:type owl:NamedIndividual
    #

    # name of VRD-World class used for bounding boxes
    class_name = 'Bbox'

    # get the sequence number that will uniquely identify the bounding
    # box for the new, individual object
    seq_num_key = bbox_seq_num_key
    seq_nums[seq_num_key] += 1
    seq_num = seq_nums[seq_num_key]

    # construct the triple
    object_bbox_id = class_name + str(seq_num)
    object_bbox_uriref = URIRef(url_base + object_bbox_id)
    triple = (object_bbox_uriref, RDF.type, OWL.NamedIndividual)
    triples.append(triple)

    #
    # example target triple: :BboxNNNNN rdf:type :Bbox
    #

    # construct the triple
    class_uri = URIRef(url_base + class_name)
    triple = (object_bbox_uriref, RDF.type, class_uri)
    triples.append(triple)

    #
    # target triple: :BboxNNNNN :hasCoordinateYmin 'NNN'^^xsd:integer
    #

    # construct the triple
    property_name = 'hasCoordinateYmin'
    property_uri = URIRef(url_base + property_name)    
    literal = Literal(bbox[0], datatype=XSD.integer)
    triple = (object_bbox_uriref, property_uri, literal)
    triples.append(triple)

    #
    # example target triple: :BboxNNNNN :hasCoordinateYmax 'NNN'^^xsd:integer
    #

    # construct the triple
    property_name = 'hasCoordinateYmax'
    property_uri = URIRef(url_base + property_name)    
    literal = Literal(bbox[1], datatype=XSD.integer)
    triple = (object_bbox_uriref, property_uri, literal)
    triples.append(triple)

    #
    # example target triple: :BboxNNNNN :hasCoordinateXmin 'NNN'^^xsd:integer
    #

    # construct the triple
    property_name = 'hasCoordinateXmin'
    property_uri = URIRef(url_base + property_name)    
    literal = Literal(bbox[2], datatype=XSD.integer)
    triple = (object_bbox_uriref, property_uri, literal)
    triples.append(triple)

    #
    # example target triple: :BboxNNNNN :hasCoordinateXmax 'NNN'^^xsd:integer
    #

    # construct the triple
    property_name = 'hasCoordinateXmax'
    property_uri = URIRef(url_base + property_name)    
    literal = Literal(bbox[3], datatype=XSD.integer)
    triple = (object_bbox_uriref, property_uri, literal)
    triples.append(triple)

    #
    # example target triple: :PersonNNNNN :hasBbox :BboxNNNNN
    #

    # construct the triple
    property_name = 'hasBbox'
    property_uriref = URIRef(url_base + property_name)    
    triple = (object_uriref, property_uriref, object_bbox_uriref)
    triples.append(triple)

    return object_id, object_uriref, triples


#%%

def build_triple_linking_subject_to_object(subject_uriref,
                                           prop_idx,
                                           object_uriref,
                                           ontoPropNames): 
    '''
    Construct and return the single triple that links a 'subject'
    individual object with an 'object' individual object.
    
    Parameters:
        subject_uriref : string - the RDFLib URIREF for the particular 
                         object in a KG that is to be established as the
                         'subject' in a new RDF triple for a KG
        prop_idx : integer - the integer index that represents the ontology
                   object property that is to be used to link the 'subject'
                   and 'object' objects in a new RDF triple for a KG
        object_uriref : string - the RDFLib URIREF for the particular 
                        object in a KG that is to be established as the
                        'object' in a new RDF triple for a KG
        ontoPropNames : list - of object property names used in the KG for
                        linking ordered pairs of objects that represent
                        visual relationships between the two objects
    
    Returns:
        triples : list - a list containing a single RDF triple in the
                  RDFLib format used for representing triples to be 'added' 
                  to a KG
    '''
    
    triples = []
    
    #
    # example target triple:
    #   :Person10021 :nextTo :Person10024
    #
    
    property_name = ontoPropNames[prop_idx]

    # construct the triple
    property_uriref = URIRef(url_base + property_name)
    triple = (subject_uriref, property_uriref, object_uriref)
    triples.append(triple)

    return triples


#%% 

def assemble_SPARQL_query(imname, image_id):
    '''
    Construct a SPARQL query customised for the particular VRD image.
    
    The query is to be used for extracting from a KG all of the triples
    that link pairs of objects associated with the image.
    
    Parameters
    ----------
    imname : string
        The unique filename of a particular VRD dataset image.
    image_id : string
        The unique id used to represent the VRD image within the KG.
        This id is a concatenation of the ontology class name 'Image' 
        and a unique integer sequence number.

    Returns
    -------
    query : string
        A SPARQL query.
    
    Template for the target SPARQL query to be constructed
    ------------------------------------------------------
    query = "
    PREFIX vrd: <http://www.semanticweb.org/nesy4vrd/ontologies/vrd_world#>
    SELECT ?subObj ?property ?objObj
    WHERE {
        ?subObj ?property ?objObj .
        :imageN :hasObject ?subObj .
        :imageN :hasObject ?objObj .
        :imageN rdfs:label :imgFilenameLiteral .
        FILTER ( ?subObj != ?objObj ) 
    }
    "
    '''

    img_uri = "<" + url_base + image_id + "> "
    hasobject_prop_uri = "<" + url_base + "hasObject> "
    label_prop_uri = '<http://www.w3.org/2000/01/rdf-schema#label> '
    img_label_uri = '"' + imname + '"' + \
                    "^^<http://www.w3.org/2001/XMLSchema#string>"
    
    query = "PREFIX vrd: <" + url_base + "> " \
          + "SELECT ?subObj ?property ?objObj " \
          + "WHERE {" \
          + "?subObj ?property ?objObj . " \
          + img_uri + hasobject_prop_uri + "?subObj . " \
          + img_uri + hasobject_prop_uri + "?objObj . " \
          + img_uri + label_prop_uri + img_label_uri + " . " \
          + "FILTER ( ?subObj != ?objObj ) " \
          + "}"
    
    return query











