#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script performs Step 6 of the NeSy4VRD workflow.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

Step 6 of the NeSy4VRD workflow:
* manages the removal of entries for images in the NeSy4VRD visual 
  relationship annotations dictionary that have zero annotated visual
  relationships

Step 6 of the NeSy4VRD workflow may or may not be required. It depends on
the nature of the annotation customisations you wish to make.

======

Note: The original VRD visual relationship annotations dictionaries, for
both the VRD training set and test set images, were found to have many
entries with zero annotated visual relationships.  The VRD annotations
dictionary for the VRD training set images was found to have well over
200 entries with zero annotations.  Given that images with zero annotations
would be unable to participate effectively in either the training of
neural networks (because they have no supervisory target annotations) or
the evaluation of visual relationship detection predictive performance
(since they have no target annotations to be matched and counted as hits),
NeSy4VRD took the decision to remove the 'empty' entries for these images
from the respective training and test annotations dictionaries. The physical
image files themselves were unaffected by this decision and still exist in
the respective 'train_images' and 'test_images' zip files and directories.

Given that the NeSy4VRD training and test annotations files (dictionaries)
only contain entries for images that have at least 1 annotated visual
relationship, Step 6 of the NeSy4VRD workflow is unlikely to be needed.
It has been retained as part of the NeSy4VRD workflow in order to keep a
full historical record of how the original VRD visual relationship
annotations were transformed into the NeSy4VRD visual relationship
annotations.
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

# get NeSy4VRD visual relationship annotations
vrd_anno_path = os.path.join(anno_dir, vrdcfg.annotations_file)
vrd_anno = vrdu3.load_NeSy4VRD_image_annotations(vrd_anno_path)

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
