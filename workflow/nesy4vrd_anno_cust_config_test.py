#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module is a NeSy4VRD workflow configuration file.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

This module is an example of a NeSy4VRD workflow configuration file
designed to manage a 'test set' run of the NeSy4VRD workflow.
A 'test set' run of the workflow is one that targets customising the
annotations of VRD test set images.

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
# a 'test run' of the workflow (i.e. for a run that targets customisations
# to the annotations of test set VRD images). This is because, if you have
# modified object class or predicate names, or introduced new object class
# or predicate names, you will most likely have had to apply these
# customisations in Step 1 of your 'training set' run of the workflow, in
# which case the customisations will already be in place for your 'test run'
# of the workflow. Trying to reapply the same customisations a 2nd time is
# not only redundant, it will cause the Step 1 script to detect a problem
# and abort and report an error.

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

# The text file containing the VRD annotation customisation instructions
# for Step 2 of the test set VR annotation customisation process. This file
# must be in the current working directory, not the annotations directory.
step_2_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_2_instructions_test.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk (over-writing the current state of the annotations
# file defined above) or not. If you set this to False, you can safely run
# the driver script on the instructions file just to validate that all of
# your customisation instructions are interpretable and executable (given
# the current state of the VRD annotations).  Once you are happy with your
# instructions file, set this variable to True and the driver script will
# save the customised annotations to disk.
step_2_save_customised_annotations = True


#%% Step 3 config parameters

# Step 3 is NOT REQUIRED by the test set VR annotation customisation process.
# This is because, in the test set VR annotation customisation process, the 
# splitting out of instances of object class 'drinking glass' from object class 
# 'glasses' (eyeglasses) is handled manually, in Step 2, via hand-specified VR
# annotation customisation instructions specified in a text file, rather than
# enmass to a list of images specified by name.

step_3_from_class_to_class = [
                              'not defined for TEST set'
                             ]

step_3_from_class_to_class_img_names = [
                                        'not defined for TEST set'
                                       ]


#%% Step 4 config parameters

# Specify pairs of object classes and pairs of predicates to be merged, globally,
# across the VR annotations for all images within the test set of the
# VRD dataset.

# NOTE: The pairs specified here should be IDENTICAL to those specified for the 
# training set VR annotation customisation process. 

step_4_object_classes_to_merge = [
                                  ['plane', 'airplane'], # 'plane' into 'airplane'
                                  ['coat', 'jacket'],    # 'coat' into 'jacket'
                                  ['road', 'street']     # 'road' into 'street'
                                 ]

# Define from/to pairs of predicates to merge

step_4_predicates_to_merge = []


#%% Step 5 config parameters

# Step 5: remove instances of specific visual relationships globally

# list the ('subject', 'predicate', 'object') vr instances you wish to
# remove on a global basis (ie across the annotations for all images)

# NOTE: the VR patterns specified here in Step 5 should be identical for both
# the training set and test set VR annotation customisation processes!!!

step_5_vrs_to_remove = [
                        ('sky', 'in', 'sky'),
                        ('sky', 'has', 'sky'),
                        ('sky', 'with', 'sky'),
                        ('sky', 'behind', 'sky'),
                        ('sky', 'contain', 'sky'),
                        ('wheel', 'on', 'wheel')
                       ]

#%% Step 6 config parameters

# Step 6 does a global trawl of the VRD annotations dictionary looking for 
# keys (image names) with empty lists as values (ie zero annotations). 
# Images with zero visual relationship annotations are removed from the
# annotations dictionary because we cannot train on images that have no
# targets.  Removing image entries from the annotations dictionary is
# equivalent to a 'logical delete' of the image from the dataset. The
# physical image is not removed from the images directory.

# No annotation customisation configuration parameters are required for
# this step.


#%% Step 7 config parameters

# Step 7 removes unwanted/problematic images from the annotations dictionary. 
# The images are not physically removed from the image directory. But by
# removing their entries from the annotations dictionary, we logically remove
# them from the dataset.  They will never participate in testing or performance
# evaluation.

# Specify the text file containing the VRD annotation customisation 
# 'remove image' instructions for Step 7 of the annotation customisation 
# process.  The instructions file must be in the current working directory, 
# not the annotations data directory.
step_7_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_7_instructions_test.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk (over-writing the current state of the annotations
# file defined above) or not. If you set this to False, you can safely run
# the driver script on the instructions file just to validate that all of
# your customisation instructions are interpretable and executable (given
# the current state of the VRD annotations).  Once you are happy with your
# instructions file, set this variable to True and the driver script will
# save the customised annotations to disk.
step_7_save_customised_annotations = True


#%% Step 8 config parameters

# Step 8 applies further customisations to test set VR annotations, supplementary
# to those applied in Step 2.

# Specify the text file containing the VRD annotation customisation instructions
# for Step 8 of the annotation customisation process. This file must be
# in the current working directory, not the annotations directory.
step_8_vrd_anno_cust_instructions_file = 'not yet required for TEST set'

# Specify whether you want the driver script to save the customised 
# annotations to disk (over-writing the current state of the annotations
# file defined above) or not. If you set this to False, you can safely run
# the driver script on the instructions file just to validate that all of
# your customisation instructions are interpretable and executable (given
# the current state of the VRD annotations).  Once you are happy with your
# instructions file, set this variable to True and the driver script will
# save the customised annotations to disk.
step_8_save_customised_annotations = False


#%% Step 9 config parameters

# Step 9 transforms visual relationships on a global basis.

# Specify pairs of visual relationships, [from_vr, to_vr], where from_vr
# is to be transformed into to_vr.  Each vr transformation instruction is
# applied globally, across the annotations for all images.

# The number of supported transformations is limited to those that can be
# accomplished on a global basis, which means those transformations that
# can be realised without bounding boxes having to be specified (which are 
# inherently individualistic, and hence incompatible with a global 
# customisation approach).
#
# A global vr transformation instruction has a format consistent with one
# of the following patterns:
#
# 1) [(a, p1, b), ((a, p2, b)], where objects 'a' and 'b' keep their 
#    positions and predicate p1 is changed to p2; (nb: this is equivalent
#    to a 'cvrpxx' vr annotation customisation instruction)
#
# 2) [(a, p1, b), (b, p2, a)], where objects 'a' and 'b' swap positions and
#    predicate p1 is changed to p2
#
# 3) [(a, p, b), (b, p, a)], where objects 'a' and 'b' swap positions and
#    predicate p is unchanged
#
# note: in cases (2) and (3), where the 'subject' and 'object' objects 
# swap positions, both the integer object class labels and bboxes are 
# swapped!

# NOTE: the VR patterns specified here in Step 9 should be identical for both
# the training set and test set VR annotation customisation processes!!! 


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
#%% Step 10 config parameters

# Step 10 does a global trawl of the test set VRD annotations looking for
# duplicate visual relationships (VRs) within the set of annotations
# for each image. It removes any such duplicate vrs.

# No annotation customisation configuration parameters are required for
# this step.


#%% Step 11 config parameters

# Step 11 is not required for the test set VR annotation customisation process.

step_11_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_11_instructions_test.txt'

step_11_save_customised_annotations = True



















