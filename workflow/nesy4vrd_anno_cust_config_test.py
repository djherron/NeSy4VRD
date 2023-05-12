#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  23 18:37:23 2022

@author: dave
"""

'''
This module defines configuration parameters for the automated VRD dataset
visual relationship annotation customisation process. 

The configuration parameters defined in this script guide the customisation
of the visual relationship annotations of the VRD dataset 
TEST SET visual relationship annotations.

The VRD annotation customisation process is an ordered, multi-step, sequential 
process. Each step performs a particular category of annotation customisation
under the control of a separate, dedicated Python script.  This module 
defines the configuration parameters that control what these separate,
dedicated Python scripts actually do in terms of modifying the visual
relationship annotations of the VRD dataset (training or test).

This module reflects an annotation customisation process for the VRD
TEST SET that consists of a subset of the 11 steps defined for the
TRAINING SET annotation customisation process. A TEST SET annotation
customisation step that performs the same function as a TRAINING SET
annotation customisation step shares a common 'step number' with that
corresponding TRAINING SET annotation customisation step. The decision was
taken to keep the step numbers consistent in this way in order to bring
greater clarity to the process. Thus, the task performed by a 'step number'
is consistent across both the TRAINING SET and TEST SET annotation customisation
processes.  The TEST SET, however, did not require the same number of 
annotation customisation steps as the TRAINING SET (11). Hence, the sequence
of step numbers in the TEST SET annotation customisation process contains some
gaps between 1 and 11. 
'''

#%% directory and file config parameters

# The elements of this list are directory names which, when joined,
# form a relative path to the directory containing the customised
# VR annotations files.
anno_dir = ['data', 'annotations_customised']

object_classes_file = 'vrd_dh_objects.json'

predicates_file = 'vrd_dh_predicates.json'

# To begin with, the file specified here should be (contain) a copy of the
# original VRD dataset test set VR annotations. These will be progressively
# customised by the sequence of steps of the test set VR annotation
# customisation process.
annotations_file = 'vrd_dh_annotations_test.json'

#%% Step 1 config parameters

# Step 1 is NOT PERMITTED for customisation of the VRD dataset test set VR
# annotations.  Step 1 is performed only as part of the training set VR
# annotation customisation process because it manages amendments to the
# .json files defining the VRD object classes and predicates. The amendments
# applied during the training set VR annotation customisation process apply
# equally to all test set VR annotations.

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
step_2_vrd_anno_cust_instructions_file = 'vrd_anno_cust_2_instructions_test.txt'

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
step_7_vrd_anno_cust_instructions_file = 'vrd_anno_cust_7_instructions_test.txt'

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

step_11_vrd_anno_cust_instructions_file = 'vrd_anno_cust_11_instructions_test.txt'

step_11_save_customised_annotations = True



















