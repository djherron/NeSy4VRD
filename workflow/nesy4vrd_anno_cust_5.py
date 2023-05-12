#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:27:24 2021

@author: dave
"""

'''
This script implements Step 5 of the VRD annotations customisation process.

Step 5 of the process deals with managing the removal of specific
visual relationships from the image annotations for a designated VRD
dataset (train/test). The removals are applied globally across the
annotations for all images.  If there are no specific visual relationships
to be removed globally, Step 5 can be skipped.
'''

#%%

import os
import vrd_utils3 as vrdu3

# Engage the correct configuration file depending on whether you are running
# this Step 5 script to perform TRAINING set or TEST set VR annotation
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

print('Step 5: processing begins ...')
print()

#%% process the vr removals

if len(vrdcfg.step_5_vrs_to_remove) > 0:
    print('Processing of global vr removals begins ...')
    print()

for vr in vrdcfg.step_5_vrs_to_remove:
    sub_name, prd_name, obj_name = vr

    if not sub_name in vrd_objects:
        raise ValueError(f'Subject name not recognised: {sub_name}')
    if not prd_name in vrd_predicates:
        raise ValueError(f'Predicate name not recognised: {prd_name}')
    if not obj_name in vrd_objects:
        raise ValueError(f'Object name not recognised: {obj_name}')

    nremoved = vrdu3.remove_vr_globally(vr, vrd_img_names, vrd_anno,
                                        vrd_objects, vrd_predicates)

    print(f'vr {vr} removed globally; {nremoved} instances')
    print()

if len(vrdcfg.step_5_vrs_to_remove) > 0:
    print('Processing of global vr removals complete')
    print()

#%% save customised annotations to file on disk

if len(vrdcfg.step_5_vrs_to_remove) > 0:
    vrdu3.write_customised_annotations_to_file(vrd_anno, vrd_anno_path)
    print(f'Customised annotations saved to file: {vrd_anno_path}')

print()
print('Step 5: processing complete')
