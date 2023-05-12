#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:27:24 2021

@author: dave
"""

'''
This script implements Step 9 of the VRD annotations customisation process.

Step 9 of the process deals with managing changing a target vr to a new,
modified vr on a global basis.
'''

#%%

import os
import vrd_utils3 as vrdu3

# Engage the correct configuration file depending on whether you are running
# this Step 9 script to perform TRAINING set or TEST set VR annotation
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

print('Step 9: processing begins ...')
print()

#%% process the vr changes

if len(vrdcfg.step_9_from_vr_to_vr) > 0:
    print('Processing of global vr transformations begins ...')
    print()

for vr_pair in vrdcfg.step_9_from_vr_to_vr:
    from_vr, to_vr = vr_pair

    if not from_vr[0] in vrd_objects:
        raise ValueError(f'Subject name not recognised: {from_vr[0]}')
    if not from_vr[1] in vrd_predicates:
        raise ValueError(f'Predicate name not recognised: {from_vr[1]}')
    if not from_vr[2] in vrd_objects:
        raise ValueError(f'Object name not recognised: {from_vr[2]}')

    objects_swap_positions = None
    if from_vr[0] == to_vr[0] and from_vr[2] == to_vr[2]:
        objects_swap_positions = False
    elif from_vr[0] == to_vr[2] and from_vr[2] == to_vr[0]:
        objects_swap_positions = True
    else:
        raise ValueError(f'from_vr -> to_vr specification not valid: {vr_pair}')

    if not to_vr[1] in vrd_predicates:
        raise ValueError(f'Predicate name not recognised: {to_vr[1]}')

    predicate_changes = True
    if from_vr[1] == to_vr[1]:
        predicate_changes = False

    if ((not objects_swap_positions) and (not predicate_changes)):
        raise ValueError(f'from_vr -> to_vr specification invalid: {vr_pair}')

    nchanged = vrdu3.change_vr_globally(from_vr, to_vr,
                                        objects_swap_positions,
                                        predicate_changes,
                                        vrd_img_names, vrd_anno,
                                        vrd_objects, vrd_predicates)

    print(f'{vr_pair} processed globally; {nchanged} vr instances changed')
    print()

if len(vrdcfg.step_9_from_vr_to_vr) > 0:
    print('Processing of global vr transformations complete')
    print()

#%% save customised annotations to file on disk

if len(vrdcfg.step_9_from_vr_to_vr) > 0:
    vrdu3.write_customised_annotations_to_file(vrd_anno, vrd_anno_path)
    print(f'Customised annotations saved to file: {vrd_anno_path}')

print()
print('Step 9: processing complete')
