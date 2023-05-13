#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script performs Step 9 of the NeSy4VRD workflow.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

Step 9 of the NeSy4VRD workflow:
* manages transforming specified VR types to new, modified VR types on a
  global basis.

This is a 'from' --> 'to' operation.  Restrictions apply as to the type
of transformations that are possible to apply on a global basis. In 
particular, only transformations that change predicates or swap the 
positions of the 'subject' and 'object' objects are supported. See one of
the NeSy4VRD workflow configuration modules, in the section pertaining to
Step 9, for more specific details.

Step 9 of the NeSy4VRD workflow may or may not be required. It depends on
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
