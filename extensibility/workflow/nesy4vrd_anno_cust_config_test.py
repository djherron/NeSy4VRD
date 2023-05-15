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
designed to manage a 'test set' run of the NeSy4VRD workflow.
A 'test set' run of the workflow is one that targets customising the
NeSy4VRD annotations of VRD test set images.

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
# relationship annotations for the 'test set' VRD images.
annotations_file = 'nesy4vrd_annotations_test.json'


#%% Step 1 config parameters

# Step 1 of the NeSy4VRD workflow is highly unlikely to be appropriate for
# a 'test set' run of the workflow (i.e. for a run that targets customising
# the annotations of test set VRD images). This is because, if you wish to
# modify object class or predicate names, or introduce new object class
# or predicate names, you will most likely have had to do so in Step 1
# of the 'training set' run of your NeSy4VRD workflow.  This is the default
# and expected scenario, and in this scenario your customisations to the
# master lists of object class names and/or predicate names will already
# be in place and need not be applied a second time.  Indeed, trying to
# apply such customisations a second time would fail, because the Step 1
# script would detect a problem and abort and report an error.

step_1_new_object_names = [
                            'not defined for test set run'
                          ]

step_1_predicate_name_adjustments = [
                                      'not defined for test set run'
                                    ]

step_1_new_predicate_names = [
                              'not defined for test set run'
                             ]


#%% Step 2 config parameters 

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_2_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_02_instructions_test.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_2_save_customised_annotations = True


#%% Step 3 config parameters

# Here you can specify lists of image filenames within whose annotations
# you wish to change all instances of object class A to object class B.
#
# You need to do thorough analysis of the images and their annotations 
# first in order to build up the lists of image names for which it is safe
# to use this Step 3 'batch' approach to changing object class A to B.


# Specify an individual change: ['from_class', 'to_class']
from_class_to_class_1 = ['object_class_name_A', 'object_class_name_B']

# Specify a list of image filenames to which the change applies
img_names_1 = [

'10218327826_907c2b49df_o.jpg',
'8168304300_dfe595eed0_o.jpg',
'290584551_7f219121ab_b.jpg',
'9272614085_8744b258ba_b.jpg'

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

step_4_predicates_to_merge = [
                              ['predicate_name_A', 'predicate_name_B'],
                              ['predicate_name_C', 'predicate_name_D']
                             ]


# NOTE: The merge pairs specified here should normally be IDENTICAL to 
# those specified in the configuration module for the 'training set' run of 
# your NeSy4VRD workflow.  That is, if you decide to merge object classes,
# you very likely you want to do the same merging in the annotations of
# both the training set and test set images.


#%% Step 5 config parameters

# Here you can specify instances of visual relationship 'types' to be
# removed from the annotations of all images.

step_5_vrs_to_remove = [
                        ('subject1', 'predicate1', 'object1'),
                        ('subject2', 'predicate2', 'object2'),
                        ('subject3', 'predicate3', 'object3')
                       ]


# NOTE: Whatever VR types you specify here for Step 5 of a 'test set' run
# of your NeSy4VRD workflow should very likely be replicated exactly for 
# Step 5 in the configuration module for the 'training set' run of your 
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

step_7_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_07_instructions_test.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_7_save_customised_annotations = True


#%% Step 8 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_8_vrd_anno_cust_instructions_file = 'none for test set run'

# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_8_save_customised_annotations = False


#%% Step 9 config parameters

# Here you can specify visual relationship types that you want to have
# transformed from type A to type B, on a global basis.  Each such
# instruction is expressed as a 2-element list: [(from_vr), (to_vr)].

step_9_from_vr_to_vr = [
                        
    [('classA', 'predicate1', 'classB'), ('classA', 'predicate2', 'classB')],
    [('classC', 'predicate3', 'classD'), ('classD', 'predicate4', 'classC')],
    [('classE', 'predicate5', 'classF'), ('classF', 'predicate5', 'classE')]
                
                        ]


# NOTE: Whatever VR transformations you specify here for Step 9 of a 
# 'test set' run of your NeSy4VRD workflow should very likely be 
# replicated exactly for Step 9 in the configuration module for the 
# 'training set' run of your NeSy4VRD workflow. You will likely want such 
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

step_11_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_11_instructions_test.txt'


# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_11_save_customised_annotations = True



