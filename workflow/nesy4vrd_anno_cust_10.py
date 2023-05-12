#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:27:24 2021

@author: dave
"""

'''
This script implements Step 10 of the VRD annotations customisation process.

Step 10 of the process finds duplicate visual relationships within the
set of vr annotations for each image and removes such duplicates. This is
a global operation.
'''

#%%

import os
import vrd_utils3 as vrdu3

# Engage the correct configuration file depending on whether you are running
# this Step 10 script to perform TRAINING set or TEST set VR annotation
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

print('Step 10: processing begins ...')
print()

#%% find and remove duplicate visual relationships

im_cnt = 0
vr_cnt = 0

for imname in vrd_img_names:
          
    imanno = vrd_anno[imname].copy() # we want a new object, not a 'view' object
    n_vrs = len(imanno)
    dup_vr_indices = []
    
    if n_vrs < 2:
        pass # no possibility of duplicates
    else:
        for idx1, vr1 in enumerate(imanno):
            for idx2 in range(idx1+1, n_vrs):
                vr2 = imanno[idx2]
                duplicates = vrdu3.check_if_vrs_are_duplicates(vr1, vr2)
                if duplicates:
                    dup_vr_indices.append(idx2)
   
    if len(dup_vr_indices) > 0:
        # eliminate duplicate references to duplicate vrs and sort the
        # resulting distinct indices in ascending order
        dup_vr_indices = sorted(list(set(dup_vr_indices)))
        
        # remove any duplicate vrs in DESCENDING order of vr index so that
        # no removal can invalidate the index of another duplicate vr yet
        # to be removed
        for idx in reversed(dup_vr_indices):
            del imanno[idx]
            vr_cnt += 1
        
        # overwrite old annos with new annos
        vrd_anno[imname] = imanno
        im_cnt += 1

print(f'number of images with duplicate vrs: {im_cnt}')

print(f'number of duplicate vrs removed: {vr_cnt}')


#%% save customised annotations to file on disk

if len(vrdcfg.step_9_from_vr_to_vr) > 0:
    vrdu3.write_customised_annotations_to_file(vrd_anno, vrd_anno_path)
    print(f'Customised annotations saved to file: {vrd_anno_path}')

print()
print('Step 10: processing complete')




