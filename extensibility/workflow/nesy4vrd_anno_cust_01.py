#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script performs Step 1 of the NeSy4VRD workflow.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

Step 1 of the NeSy4VRD workflow:
* modifies the master lists of NeSy4VRD object class names and predicate names

Step 1 of the NeSy4VRD workflow may or may not be required. It depends on
the nature of the annotation customisations you wish to make.

If the visual relationship annotation customisations you plan to make work
entirely with the existing set of NeSy4VRD object class names and NeSy4VRD
predicate names, then Step 1 is not required and can safely be bypassed.
Indeed, in this case there is no purpose to running Step 1 since there is
nothing for it to do.

If, however, you wish to do any of the following:
* change the names of existing object classes
* introduce new, additional object classes
* change the names of existing predicates
* introduce new, additional predicates
then Step 1 of the NeSy4VRD workflow is REQUIRED and must be executed as the
first step in a run of the workflow. Otherwise, object class names and/or
predicate names to which you make reference in annotation customisations 
processed in subsequent steps of the workflow will not be recognised as
valid names, and the workflow step that encounters them will abort and  
report the problem.

If you are running Step 1 (for one or more of the purposes just described),
you would normally do so as the first step of a 'training set' run of the
workflow: that is, a run of the workflow that targets customising the
annotations of VRD training set images.  This is default (expected) scenario.

Under this default (expected) scenario, running Step 1 as the first step of
a 'test set' run of the workflow (which targets customising the annotations
of VRD test set images) is REDUNDANT and not required.  Indeed, trying to
run Step 1 a second time, as the first step in a 'test set' run of the
workflow, would fail: this script would abort and report that it cannot
apply the changes you have requested (because they are already in place). 
'''

#%%

import os
import nesy4vrd_utils3 as vrdu3

# Import the appropriate NeSy4VRD workflow configuration module
import nesy4vrd_anno_cust_config_train as vrdcfg


#%% get the NeSy4VRD object class names and predicate names

# set the path to the directory in which the source NeSy4VRD annotations 
# data files reside
anno_dir = os.path.join('..', '..', *vrdcfg.anno_dir)

# get the NeSy4VRD object class names
vrd_objects_path = os.path.join(anno_dir, vrdcfg.object_classes_file)
vrd_objects = vrdu3.load_NeSy4VRD_object_class_names(vrd_objects_path)

# get NeSy4VRD predicate names
vrd_predicates_path = os.path.join(anno_dir, vrdcfg.predicates_file)
vrd_predicates = vrdu3.load_NeSy4VRD_predicate_names(vrd_predicates_path)

# NOTE: This script for Step 1 of the NeSy4VRD workflow does NOT load
# the NeSy4VRD visual relationship annotations file because it does 
# not need it.  The visual relationship annotations are loaded and
# updated only by subsequent steps of the NeSy4VRD workflow.


#%%

print('Step 1: processing begins ...')
print()

#%% introduce any new object class names

if len(vrdcfg.step_1_new_object_names) > 0:
    vrd_objects = list(vrd_objects) # make object class names mutable
    for name in vrdcfg.step_1_new_object_names:
        if name in vrd_objects:
            raise ValueError(f'new object class name already exists: {name}')
        vrd_objects.append(name)
    vrdu3.save_VRD_object_class_names(vrd_objects, vrd_objects_path)
    print(f'Extended object class names saved to file: {vrd_objects_path}')

#%% adjust/extend predicate names

predicates_adjusted = False
predicates_added = False

if len(vrdcfg.step_1_predicate_name_adjustments) > 0:
    vrd_predicates = list(vrd_predicates) # make predicate names mutable
    for adjustment in vrdcfg.step_1_predicate_name_adjustments:
        from_name, to_name = adjustment
        if not from_name in vrd_predicates:
            raise ValueError(f'predicate name not recognised: {from_name}')
        from_name_idx = vrd_predicates.index(from_name)
        vrd_predicates[from_name_idx] = to_name
        predicates_adjusted = True

if len(vrdcfg.step_1_new_predicate_names) > 0:
    if not predicates_adjusted:
        vrd_predicates = list(vrd_predicates) # convert tuple to list
    for name in vrdcfg.step_1_new_predicate_names:
        if name in vrd_predicates:
            raise ValueError(f'new predicate name already exists: {name}')
        vrd_predicates.append(name)
        predicates_added = True

if predicates_adjusted or predicates_added:
    vrdu3.save_VRD_predicate_names(vrd_predicates, vrd_predicates_path)
    print(f'Revised/extended predicate names saved to file: {vrd_predicates_path}')

#%%

print()
print('Step 1: processing complete')


