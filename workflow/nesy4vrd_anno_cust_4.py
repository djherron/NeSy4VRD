#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script performs Step 4 of the NeSy4VRD workflow.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

Step 4 of the NeSy4VRD workflow:
* manages the merging of pairs of object classes and pairs of predicates,
  globally, across all image entries in the annotations dictionary

Step 4 of the NeSy4VRD workflow may or may not be required. It depends on
the nature of the annotation customisations you wish to make.
'''

#%%

import os
import nesy4vrd_utils3 as vrdu3

# Import the appropriate NeSy4VRD workflow configuration module
# depending on whether we are doing a 'training set' or 'test set' run
# of the NeSy4VRD workflow.

import nesy4vrd_anno_cust_config_train as vrdcfg
#import nesy4vrd_anno_cust_config_test as vrdcfg

#%% get the NeSy4VRD annotations data

# set the path to the directory in which the source NeSy4VRD annotations 
# data files reside
anno_dir = os.path.join('..', *vrdcfg.anno_dir)

# get the NeSy4VRD object class names
path = os.path.join(anno_dir, vrdcfg.object_classes_file)
vrd_objects = vrdu3.load_NeSy4VRD_object_class_names(path)

# get NeSy4VRD predicate names
path = os.path.join(anno_dir, vrdcfg.predicates_file)
vrd_predicates = vrdu3.load_NeSy4VRD_predicate_names(path)

# get NeSy4VRD visual relationship annotations
vrd_anno_path = os.path.join(anno_dir, vrdcfg.annotations_file)
vrd_anno = vrdu3.load_NeSy4VRD_image_annotations(vrd_anno_path)

# get a list of the VRD image names from the annotations dictionary
vrd_img_names = list(vrd_anno.keys())

#%%

print('Step 4: processing begins ...')
print()

#%% process the object class merges, if anay

if len(vrdcfg.step_4_object_classes_to_merge) > 0:
    print('Processing of object class merges begins ...')
    print()

for pair in vrdcfg.step_4_object_classes_to_merge:
    from_name, to_name = pair

    if not from_name in vrd_objects:
        raise ValueError(f"Object class 'from name' not recognised: {from_name}")
    if not to_name in vrd_objects:
        raise ValueError(f"Object class 'to name' not recognised: {to_name}")
    
    vrdu3.merge_object_classes(from_name, to_name, vrd_img_names,
                               vrd_anno, vrd_objects, vrd_predicates)
    
    print(f'Merge of object class {from_name} into {to_name} complete')
    print()

if len(vrdcfg.step_4_object_classes_to_merge) > 0:
    print('Processing of object class merges complete')
    print()

#%% process the predicate merges, if any

if len(vrdcfg.step_4_predicates_to_merge) > 0:
    print('Processing of predicate merges begins ...')
    print()

for pair in vrdcfg.step_4_predicates_to_merge:
    from_name, to_name = pair

    if not from_name in vrd_predicates:
        raise ValueError(f"Predicate 'from name' not recognised: {from_name}")
    if not to_name in vrd_predicates:
        raise ValueError(f"Predicate 'to name' not recognised: {to_name}")

    vrdu3.merge_predicates(from_name, to_name, vrd_img_names,
                           vrd_anno, vrd_objects, vrd_predicates)

    print(f'Merge of predicate {from_name} into {to_name} complete')
    print()

if len(vrdcfg.step_4_predicates_to_merge) > 0:
    print('Processing of predicate merges complete')
    print()

#%% save customised annotations to file on disk

if len(vrdcfg.step_4_object_classes_to_merge) > 0 or \
   len(vrdcfg.step_4_predicates_to_merge) > 0:
    vrdu3.write_customised_annotations_to_file(vrd_anno, vrd_anno_path)
    print(f'Customised annotations saved to file: {vrd_anno_path}')

print()
print('Step 4: processing complete')
