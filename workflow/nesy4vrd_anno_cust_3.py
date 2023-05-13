#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script performs Step 3 of the NeSy4VRD workflow.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

Step 3 of the NeSy4VRD workflow:
* manages the process of changing object class A to object class B
  across all instances of VRs that refer to object class A for a 
  pre-specified set of named images

Step 3 of the NeSy4VRD workflow may or may not be required. It depends on
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

print('Step 3: processing begins ...')
print()

#%% process the customisation

if len(vrdcfg.step_3_from_class_to_class) != \
   len(vrdcfg.step_3_from_class_to_class_img_names):
    raise ValueError('problem with from/to class configuration parameters')

for idx, from_class_to_class in enumerate(vrdcfg.step_3_from_class_to_class):
    from_name, to_name = from_class_to_class
    if not from_name in vrd_objects:
        raise ValueError(f"Object class 'from name' not recognised: {from_name}")
    if not to_name in vrd_objects:
       raise ValueError(f"Object class 'to name' not recognised: {to_name}")
    img_names = vrdcfg.step_3_from_class_to_class_img_names[idx]
    if len(img_names) > 0:
        print(f"Switching object class '{from_name}' to '{to_name}' in named images begins ...")
        print()
    else:
        raise ValueError(f"no image names for from/to class pair: {from_name}, {to_name}")

    vrdu3.switch_object_classes_in_named_images(from_name, to_name, img_names,
                                                vrd_anno, vrd_objects, 
                                                vrd_predicates)  
    if len(img_names) > 0:
        print(f"Switching object class '{from_name}' to '{to_name}' in named images complete")
        print()

#%% save the customised annotations to file on disk 

if len(img_names) > 0:
    vrdu3.write_customised_annotations_to_file(vrd_anno, vrd_anno_path)
    print(f'Customised annotations saved to file: {vrd_anno_path}')

print()
print('Step 3: processing complete')


