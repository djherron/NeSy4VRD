#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:28:00 2021

@author: dave
"""

'''
This script implements Step 6 of the VRD annotations customisation process.

Step 6 of the process removes images with zero annotations from the VRD
annotations dictionary.

The original VRD annotations dictionary was found to contain 223 entries
where an image name 'key' is associated with a 'value' that is an empty
list (meaning there are no vr annotations for that image). This script
removes these entries from the annotations dictionary so that all
images considered to be in the customised VRD training set have
at least one visual relationship annotation.
'''

#%%

import os
import vrd_utils3 as vrdu3

# Engage the correct configuration file depending on whether you are running
# this Step 6 script to perform TRAINING set or TEST set VR annotation
# customisations.

import vrd_anno_cust_config_train as vrdcfg
#import vrd_anno_cust_config_test as vrdcfg

#%% get the VRD data

# Set the path to the directory in which the source VRD annotations data resides.
anno_dir = os.path.join('..', *vrdcfg.anno_dir)

# get the VRD image annotations
vrd_anno_path = os.path.join(anno_dir, vrdcfg.annotations_file)
vrd_anno = vrdu3.load_VRD_image_annotations(vrd_anno_path)

# get a list of the VRD image names from the annotations dictionary
vrd_img_names = list(vrd_anno.keys())

#%%

print('Step 6: processing begins ...')
print()

#%% find and remove image name keys whose values are empty lists

# get the names of the images whose annotations are empty lists
images_with_empty_annos = []
for imname in vrd_img_names:
    imanno = vrd_anno[imname]
    if len(imanno) == 0:
        images_with_empty_annos.append(imname)

print(f'number of image names with zero annotations: {len(images_with_empty_annos)}')

# remove the entries for these images from the annotations dictionary
for imname in images_with_empty_annos:
    del vrd_anno[imname]

print(f'entries removed from annotations dictionary: {len(images_with_empty_annos)}')

#%% save customised annotations to file on disk

if len(images_with_empty_annos) > 0:
    vrdu3.write_customised_annotations_to_file(vrd_anno, vrd_anno_path)
    print(f'Customised annotations saved to file: {vrd_anno_path}')

print()
print('Step 6: processing complete')
