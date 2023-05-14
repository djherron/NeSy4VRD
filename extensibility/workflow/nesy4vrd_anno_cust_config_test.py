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
                            'not defined for TEST set'
                          ]

step_1_predicate_name_adjustments = [
                                      'not defined for TEST set'
                                    ]

step_1_new_predicate_names = [
                              'not defined for TEST set'
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


# NOTE: for the 'test set' run of the NeSy4VRD workflow to which this
# sample configuration module applies, Step 3 is not needed, so
# the Step 3 variables are defined with empty lists. The expectation is
# that Step 3 will be skipped and not executed. But if it is inadvertently
# executed, since no annotation customisations have been configured here,
# Step 3 will have nothing to do.


# Specify an individual change: ['from_class', 'to_class']
from_class_to_class_1 = []

# Specify a list of image filenames to which the change applies
img_names_1 = []  # Step 3 not needed for this 'test set' run


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
                                  ['plane', 'airplane'], # 'plane' into 'airplane'
                                  ['coat', 'jacket'],    # 'coat' into 'jacket'
                                  ['road', 'street']     # 'road' into 'street'
                                 ]

# Here you can specify pairs of predicates to be merged. The pairs to 
# be merged are expressed in 2-element lists. For example, 
# ['predicate_A', 'predicate_B'] is an instruction to merge all instances of 
# predicate A into predicate B.  What actually happens is that all
# instances of the integer category ID for predicate A are changed to
# the integer category ID of predicate B.

step_4_predicates_to_merge = []



# NOTE: The merge pairs specified here should normally be IDENTICAL to 
# those specified in the configuration module for the 'training set' run of 
# your NeSy4VRD workflow.  That is, if you decide to merge object classes,
# you very likely you want to do the same merging in the annotations of
# both the training set and test set images.


#%% Step 5 config parameters

# Here you can specify instances of visual relationship 'types' to be
# removed from the annotations of all images.

step_5_vrs_to_remove = [
                        ('sky', 'in', 'sky'),
                        ('sky', 'has', 'sky'),
                        ('sky', 'with', 'sky'),
                        ('sky', 'behind', 'sky'),
                        ('sky', 'contain', 'sky'),
                        ('wheel', 'on', 'wheel')
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

# When transforming the original VRD visual relationship annotations into the
# NeSy4VRD visual relationship annotations, we used the annotation
# customisation instruction text file associated with Step 7 to remove
# the entries for specific images from the annotations dictionary. These
# images had annotations, but we found them to either be highly broken and
# problematic, and/or the images to weak in terms of available objects for
# the situation to be reasonably recoverable. Sometimes the images were
# rotated by 90 degrees as well. We opted to do a 'logical delete' of such
# images and remove their entries from the annotations dictionary so they
# would not be processed during training or inference or performance
# evaluation. We used the annotation customisation instruction text file 
# associated with Step 7 to gather all such removals of specific images
# into one place, for subsequent easy reference, if and when required. 

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
                        
    [('wheel', 'on', 'motorcycle'), ('wheel', 'attached to', 'motorcycle')],
    [('wheel', 'on', 'car'), ('wheel', 'attached to', 'car')],
    [('wheel', 'on', 'truck'), ('wheel', 'attached to', 'truck')],
    [('wheel', 'on', 'bus'), ('wheel', 'attached to', 'bus')],    
    [('wheel', 'on', 'van'), ('wheel', 'attached to', 'van')],
    [('wheel', 'on', 'cart'), ('wheel', 'attached to', 'cart')],
    [('wheel', 'on', 'train'), ('wheel', 'attached to', 'train')],
    [('wheel', 'on', 'plane'), ('wheel', 'attached to', 'plane')],
    [('wheel', 'on', 'airplane'), ('wheel', 'attached to', 'airplane')],
    [('wheel', 'on', 'skateboard'), ('wheel', 'attached to', 'skateboard')],
    [('clock', 'on', 'building'), ('clock', 'attached to', 'building')],
    [('clock', 'on', 'tower'), ('clock', 'attached to', 'tower')],
    [('hand', 'on', 'person'), ('person', 'has', 'hand')]
                
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



