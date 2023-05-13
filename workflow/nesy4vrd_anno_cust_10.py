#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script performs Step 10 of the NeSy4VRD workflow.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

Step 10 of the NeSy4VRD workflow:
* finds duplicate visual relationships within the set of annotated visual
  relationships for an image and removes the duplicates. This is done on
  a global basis across all entries in the annotations dictionary.

Step 10 of the NeSy4VRD workflow may or may not be required. It depends on
the nature and extent of the annotation customisations you have made. It is
a quality control step only.

======

Note: The original VRD visual relationship annotations contained many
instances of duplicate visual relationships. These have all already been
removed as part of the creation of the NeSy4VRD visual relationship
annotations. Hence, it is unlikely that Step 10 will find instances of
duplicates unless, by chance, you have inadvertently introduced some, say
via use of the NeSy4VRD protocol to specify annotation customisation 
instructions in text files.  It may be worth keeping Step 10 in your
NeSy4VRD workflow and running it just in case, as a quality control measure.
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




