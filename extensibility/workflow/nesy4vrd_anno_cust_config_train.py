#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module is a NeSy4VRD workflow configuration module.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

This module is an example of a NeSy4VRD workflow configuration file
designed to manage a 'training set' run of the NeSy4VRD workflow.
A 'training set' run of the workflow is one that targets customising the
NeSy4VRD annotations of VRD training set images.

A NeSy4VRD workflow configuration file defines configuration parameters
(pre-named Python variables) that are used by the Python scripts that
perform the successive steps of the NeSy4VRD workflow. The Python script
for each step of the workflow will import a user-designated configuration 
module (file) such as this and access the variables it needs for its
execution from within the configuration module.
'''

#%% directory and file config parameters

# List the directory names which, when joined, form a relative
# path to the directory containing the NeSy4VRD annotations files.
anno_dir = ['data', 'annotations']

# Specify the name of the JSON file holding the NeSy4VRD object class names.
object_classes_file = 'nesy4vrd_objects.json'

# Specify the name of the JSON file holding the NeSy4VRD predicate names.
predicates_file = 'nesy4vrd_predicates.json'

# Specify the name of the JSON file holding the NeSy4VRD visual
# relationship annotations for the 'trainging set' VRD images.
annotations_file = 'nesy4vrd_annotations_train.json'


#%% Step 1 config parameters

# Here you can specify the names of any new object classes you wish to
# introduce into the NeSy4VRD visual relationship annotations.
# Any such new object class names are appended to the end of the
# existing master list of object class names. This leaves all of the
# existing object class names undisturbed in their original positions in
# the master list, which means they retain their original integer category
# IDs. This is critical, because within the visual relationship 
# annotations, all object classes are specified by category ID, not by
# name. The newly introduced object class names automatically acquire
# unique category IDs by virtue of being appended to the end of the
# master list.

step_1_new_object_names = [
                           'new object class name 1',          
                           'new object class name 2',  
                           'new object class name 2'
                          ]


# Here you can specify adjustments to the names of existing predicates if,
# for any reason, you wish to do so.  Each adjustment is expressed with
# a 2-element list: ['current_name', 'adjusted_name'].
# Note that in any visual relationship annotation customisations specified
# in subsequent steps of the NeSy4VRD workflow, if you refer to one of these
# predicates you must do so by using the adjusted name, because the 
# original name will not be recognised as valid after Step 1 executes.

step_1_predicate_name_adjustments = [
                                     ['predicate name 1', 'adjusted predicate name 1'],
                                     ['predicate name 2', 'adjusted predicate name 2']
                                    ]

# Here you can specify the names of any new predicates you wish to
# introduce into the NeSy4VRD visual relationship annotations.
# Any such new predicate names are appended to the end of the
# existing master list of predicate names. This leaves all of the
# existing predicate names undisturbed in their original positions in
# the master list, which means they retain their original integer category
# IDs. This is critical, because within the visual relationship 
# annotations, all predicates are specified by category ID, not by
# name. The newly introduced predicate names automatically acquire
# unique category IDs by virtue of being appended to the end of the
# master list.

step_1_new_predicate_names = [
                              'new predicate name A',
                              'new predicate name B'
                             ]


#%% Step 2 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_2_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_02_instructions_train.txt'


# Here you can specify whether or not you want the protocol driver script 
# to actually save the customised annotations to disk, thus over-writing
# the annotations file that was loaded at the start of Step 2.  You really
# should save the customised annotations to disk if you wish to advance to
# subsequent steps of the NeSy4VRD workflow, because there may be many
# dependencies amongst the subsequent annotation customisations that 
# were crafted assuming these Step 2 customisations are in place. But if you
# just want to quality-check your annotation customisation instructions by
# having the driver script process them, without running the risk of 
# inadvertently implementing your customisations by actually over-writing 
# the annotations file, you can set this variable to False. This way, if you
# inadvertently execute the final cell of the protocol driver script, it
# won't matter because the script will know not to save the updated
# annotations to disk. 

step_2_save_customised_annotations = True


#%% Step 3 config parameters

# Here you can specify lists of image filenames within whose annotations
# you wish to change all instances of object class A to object class B.
#
# You need to do thorough analysis of the images and their annotations 
# first in order to build up the lists of image names for which it is safe
# to use this Step 3 'batch' approach to changing object class A to B.

# Specify an individual change using object class names: ['from_class', 'to_class']
from_class_to_class_1 = ['object_class_name_A', 'object_class_name_B']

# Specify a list of image filenames to which the change applies
img_names_1 = [

'5772517433_38c7350190_b.jpg',
'4879501986_378a112275_b.jpg',
'5701950713_2e50fcc667_b.jpg',
'9425058051_d588dca90a_o.jpg',
'140906489_98f524bf33_b.jpg',
'10010815684_efe23c9594_o.jpg'

]


# Aggregate your ['from_class', 'to_class'] pairs into a list

step_3_from_class_to_class = [
                              from_class_to_class_1
                             ]


# Aggregate your lists of image filenames into a list
#
# NOTE: take care to maintain the correct positional correspondence between 
# the entries in the two aggregate lists!!!

step_3_from_class_to_class_img_names = [
                                        img_names_1
                                       ]

#%% Step 4 config parameters

# Here you can specify pairs of object classes to be merged. The pairs to 
# be merged are expressed in 2-element lists. For example, 
# ['class_A', 'class_B'] is an instruction to merge all instances of 
# object class A into object class B.  What actually happens is that all
# instances of the integer category ID for object class A are changed to
# the integer category ID of object class B.

step_4_object_classes_to_merge = [
                                  ['obj_cls_name_A', 'obj_cls_name_B'], 
                                  ['obj_cls_name_C', 'obj_cls_name_D'],
                                  ['obj_cls_name_E', 'obj_cls_name_F']  
                                 ]

# Here you can specify pairs of predicates to be merged. The pairs to 
# be merged are expressed in 2-element lists. For example, 
# ['predicate_A', 'predicate_B'] is an instruction to merge all instances of 
# predicate A into predicate B.  What actually happens is that all
# instances of the integer category ID for predicate A are changed to
# the integer category ID of predicate B.
#
# We never merged any predicates when transforming the original VRD
# visual relationship annotations into the NeSy4VRD visual relationship
# annotations. But it is conceivable that someone may wish to do so. Many
# of the predicates have synonyms. For example: 'next to', 'beside'
# and 'adjacent to' can be interpreted as being synonyms.  In the NeSy4VRD
# OWL ontology, VRD-World, this 3-way synonym relationship is modeled by
# declaring each of the three OWL object properties that correspond to these
# three predicates as being owl:equivalentClass with one another.
#
# Note that the merging of predicates deemed to be synonyms is likely to
# have a powerful simplifying effect on relationship prediction. Such
# merging will significantly reduce the linguistic noise in the visual
# relationship annotations. Such simplification may or may not be 
# desired by the researcher.

step_4_predicates_to_merge = [
                              ['predicate_name_A', 'predicate_name_B'],
                              ['predicate_name_C', 'predicate_name_D']
                             ]


# NOTE: Whatever merges you specify here for Step 4 of a 'training set' run
# of your NeSy4VRD workflow should VERY LIKELY be replicated exactly for 
# Step 4 in the configuration module for the 'test set' run of your 
# NeSy4VRD workflow.  That is, if you decide to merge object classes,
# you very likely you want to do the same merging in the annotations of
# both the training set and test set images.


#%% Step 5 config parameters

# Here you can specify instances of visual relationship 'types' to be
# removed from the annotations of all images, globally. These VR 'types'
# are expressed using object class names and predicate names, like
# ('sky', 'in', 'sky').  Here we use Python tuples rather than Python lists 
# to specify the VR types to be removed.

step_5_vrs_to_remove = [
                        ('subject1', 'predicate1', 'object1'),
                        ('subject2', 'predicate2', 'object2'),
                        ('subject3', 'predicate3', 'object3')
                       ]


# NOTE: Whatever VR types you specify here for Step 5 of a 'training set' run
# of your NeSy4VRD workflow should very likely be replicated exactly for 
# Step 5 in the configuration module for the 'test set' run of your 
# NeSy4VRD workflow. You will likely want such customisations to be applied 
# identically across the annotations of both the training set and test set 
# images.


#%% Step 6 config parameters

# Step 6 does a global trawl of the NeSy4VRD annotations dictionary looking 
# for image entries with empty lists of annotations (i.e. for images that
# have no annotations at all). The entries for such images are removed 
# from the annotations dictionary. 
#
# Removing image entries from the annotations dictionary is
# equivalent to a 'logical delete' of the image from the dataset. The
# physical image on disk is not affected in any way.

# No annotation customisation configuration parameters are required here in 
# the configuration module to tell Step 6 what to do when you run it.


#%% Step 7 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_7_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_07_instructions_train.txt'


# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_7_save_customised_annotations = True


#%% Step 8 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_8_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_08_instructions_train.txt'


# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_8_save_customised_annotations = True


#%% Step 9 config parameters

# Here you can specify visual relationship types that you want to have
# transformed from type A to type B, on a global basis.  Each such
# instruction is expressed as a 2-element list, [(from_VR_type), (to_VR_type)],
# where the elements are 3-tuples: ('subject', 'predicate', 'object').

# The transformations supported are limited to those that can be
# accomplished on a global basis. This means limiting the transformations
# to those that can be realised without bounding boxes having to be 
# specified (which are inherently individualistic, and hence incompatible 
# with a global customisation operation).
#
# The only transformation types supported are those that conform to one
# of the following patterns:
#
# 1) [(a, p1, b), ((a, p2, b)], where objects 'a' and 'b' keep their 
#    positions and predicate p1 is changed to p2. (Note: this is equivalent
#    to a 'cvrpxx' NeSy4VRD protocol instruction.)
#    Example: [('wheel', 'on', 'train'), ('wheel', 'attached to', 'train')]
#
# 2) [(a, p1, b), (b, p2, a)], where objects 'a' and 'b' swap positions and
#    predicate p1 is changed to p2.
#    Example: [('hand', 'on', 'person'), ('person', 'has', 'hand')]
#
# 3) [(a, p, b), (b, p, a)], where objects 'a' and 'b' swap positions and
#    predicate p remains unchanged.
#
# Note: for patterns (2) and (3), where the 'subject' and 'object' objects 
# swap positions, both the object bounding boxes and the object category
# IDs are swapped!

step_9_from_vr_to_vr = [
                        
    [('classA', 'predicate1', 'classB'), ('classA', 'predicate2', 'classB')],
    [('classC', 'predicate3', 'classD'), ('classD', 'predicate4', 'classC')],
    [('classE', 'predicate5', 'classF'), ('classF', 'predicate5', 'classE')]
                
                        ]


# NOTE: Whatever VR transformations you specify here for Step 9 of a 
# 'training set' run of your NeSy4VRD workflow should very likely be 
# replicated exactly for Step 9 in the configuration module for the 
# 'test set' run of your NeSy4VRD workflow. You will likely want such 
# customisations to be applied identically across the annotations of both 
# the training set and test set images.


#%% Step 10 config parameters

# Step 10 does a global trawl of the NeSy4VRD annotations looking for
# exact duplicate visual relationships (VRs) within the annotations of images.
# If duplicates are detected, the duplicates are removed, leaving a single
# instance of the VR.

# No annotation customisation configuration parameters are required here in 
# the configuration module to tell Step 10 what to do when you run it.


#%% Step 11 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_11_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_11_instructions_train.txt'


# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_11_save_customised_annotations = True



