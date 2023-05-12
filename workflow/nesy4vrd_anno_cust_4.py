#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:26:48 2021

@author: dave
"""

'''
This script implements Step 4 of the VR annotations customisation process
for the VRD dataset.

Step 4 of the process manages the merging of pairs of object classes and
pairs of predicates.
'''

#%%

import os
import vrd_utils3 as vrdu3

# Engage the correct configuration file depending on whether you are running
# this Step 4 script to perform TRAINING set or TEST set VR annotation
# customisations.

import vrd_anno_cust_config_train as vrdcfg
#import vrd_anno_cust_config_test as vrdcfg

#%% get the VRD data

# Set the path to the directory in which the source VRD annotations data resides.
anno_dir = os.path.join('..', *vrdcfg.anno_dir)

# get an ordered tuple of the VRD object class names
path = os.path.join(anno_dir, vrdcfg.object_classes_file)
vrd_objects = vrdu3.load_VRD_object_class_names(path)

# get an ordered tuple of the VRD predicate names
path = os.path.join(anno_dir, vrdcfg.predicates_file)
vrd_predicates = vrdu3.load_VRD_predicate_names(path)

# get the VRD image annotations
vrd_anno_path = os.path.join(anno_dir, vrdcfg.annotations_file)
vrd_anno = vrdu3.load_VRD_image_annotations(vrd_anno_path)

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
