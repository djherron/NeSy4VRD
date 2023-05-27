#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script is the driver script for the NeSy4VRD protocol.

This protocol driver script performs all steps of the NeSy4VRD workflow 
that correspond to the processing of an annotation customisation instruction 
text file in which annotation customisation instructions have been 
specified declaratively using the NeSy4VRD protocol.  For such text files,
this protocol driver script reads, parses, validates and executes the 
annotation customisation instructions it finds specified there.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

To run this driver script for a particular step of the NeSy4VRD workflow,
the user MUST configure a particular variable that indicates the workflow
step number.  This driver script will then access the particular
annotation customisation instruction text file that has been configured
for that step number in the NeSy4VRD workflow configuration module imported
to manage the running of the workflow.

=======================================================================

More details of how this protocol driver script is meant to be used
within the context of the NeSy4VRD workflow ...

Two instances of the NeSy4VRD workflow were used to transform the
original VRD visual relationship annotations into the highly customised
and quality-improved NeSy4VRD visual relationship instructions:
* a 'training set' run of the workflow, which targeted customising the
  annotations of the training set VRD images, and
* a 'test set' run of the workflow, which targeted customising the
  annotations of the test set VRD images.

The 'training set' run of that workflow had annotation customisation 
instruction text files associated with steps 2, 7, 8 and 11 of the
NeSy4VRD workflow.

The 'test set' run of that workflow had annotation customisation 
instruction text files associated with steps 2, 7 and 11 of the
NeSy4VRD workflow.  The 'test set' run did not need or have an
annotation customisation instruction text file for step 8. Thus, in
the 'test set' run, Step 8 was skipped.
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
anno_dir = os.path.join('..', '..', *vrdcfg.anno_dir)

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

print('Annotations data loaded ...')
print(f'Number of image entries in VR annotations dictionary: {len(vrd_img_names)}')
print()

#%% CAUTION: configuration here is ESSENTIAL!!!!

# Set the NeSy4VRD workflow Step number you wish to run!

workflow_step_number = 11

print(f'Step {workflow_step_number}: processing begins ...')
print()

#%% get VRD annotation customisation instructions

# get the name of the annotation customisation instructions file to be processed
if workflow_step_number == 2:
    filename = vrdcfg.step_2_vrd_anno_cust_instructions_file
elif workflow_step_number == 7:
    filename = vrdcfg.step_7_vrd_anno_cust_instructions_file
elif workflow_step_number == 8:
    filename = vrdcfg.step_8_vrd_anno_cust_instructions_file
elif workflow_step_number == 11:
    filename = vrdcfg.step_11_vrd_anno_cust_instructions_file
else:
    raise ValueError('invalid annotation customisation step number specified')

# load the designated annotation customisation instructions text file
with open(filename) as fp:
    anno_cust_lines = fp.readlines()

print(f"Loaded annotation customisation instructions file '{filename}'")
print()

#%% define the annotation customisation instruction-set names

#
# the valid 'image' (image-level) instruction names
#

im_instruction_imname = 'imname'  # image name declaration
remove_image_instruction = 'rimxxx'  # remove image entry from anno dictionary

#
# the valid 'visual relationship' (vr-level) instruction names
#

vr_instruction_names_change = ['cvrsoc', # change vr 'subject' object class
                               'cvrsbb', # change vr 'subject' bbox
                               'cvrpxx', # change vr 'predicate'
                               'cvrooc', # change vr 'object' object class
                               'cvrobb'] # change vr 'object' bbox

vr_instruction_names_remove = ['rvrxxx'] # remove vr from image annos

vr_instruction_names_append = ['avrxxx'] # append (new) vr to image annos

vr_instruction_names = vr_instruction_names_change + \
                       vr_instruction_names_remove + \
                       vr_instruction_names_append

print('Annotation customisation instruction names loaded; ready to go ...')
print()

#%%

image_active = False
active_image_line_num = 0
vr_instructions_processed_for_image = False
remove_vr_instruction_processed_for_image = False
big_num = 1000
last_remove_vr_idx = big_num
image_cnt = 0

imname = ''
imanno = []

for line_num, line in enumerate(anno_cust_lines):

    line = line.strip()

    # determine the type of line we are about to process;
    # we recognise 4 types of line only

    linetype = ''
    if len(line) == 0 or line == '':  # blank line
        linetype = 'blank'
    elif line[0] == '#':  # comment line
        linetype = 'comment'
    elif line[0:6] == im_instruction_imname: # image instruction line
        linetype = 'image_name'
    elif line[0:6] in vr_instruction_names:  # vr instruction line
        linetype = 'vr_instruction'
    else:
        raise ValueError(f'Line type not recognised in source line {line_num+1}')

    # blank lines and comment lines require no processing; they are
    # allowed in the instruction file purely for the convenience of the
    # analyst creating/maintaining the text file of annotation 
    # customisation instructions
    if linetype == 'blank' or linetype == 'comment':
        continue
    
    # an image name line announces both 1) the 'end' of the customisation
    # instructions for the previous image, and 2) the 'start' of
    # customisation instructions for a new image
    if linetype == 'image_name':
        #
        # finalise the processing for the active (previous) image
        #
        
        if image_active:
            if vr_instructions_processed_for_image:
                # replace the original annotations for the active image
                # with the customised annotations for that image
                vrd_anno[imname] = imanno
            else:
                ln = active_image_line_num
                print(f"orphan image name '{imname}' has no instructions; line {ln}")
        
        #
        # begin processing a new image
        #
        
        imname, rim_instruction = vrdu3.parse_image_line(line_num+1, line)
        if not imname in vrd_img_names:
            raise ValueError(f"image name '{imname}' not recognised; line {line_num+1}")
        
        if rim_instruction == '':
            # no 'rimxxx' instruction present; keep the image
            image_cnt += 1
            image_active = True
        elif rim_instruction == remove_image_instruction:
            # 'rimxxx' instruction present; remove image
            vrdu3.remove_image(imname, vrd_anno) # updates vrd_anno 'in place'
            image_cnt += 1
            image_active = False  # processing for new image was just finalised
        else:
            raise ValueError(f'image instruction not recognised; line {line_num+1}')

        if image_active:
            # get vr annotations for new image as new object, not 'view' object
            imanno = vrd_anno[imname].copy()
            active_image_line_num = line_num + 1

        vr_instructions_processed_for_image = False  
        remove_vr_instruction_processed_for_image = False
        last_remove_vr_idx = big_num

        continue


    # if the processing of the current line reaches this point, then the line
    # must be a recognised customisation instruction; the type of the
    # instruction determines the type of processing

    # but first, catch any orphan instructions and disallow them;
    # every customisation instruction must be associated with a recognised
    # image name because otherwise we can't process it
    if not image_active:
        msg = f'orphan instruction encountered (no associated image); line {line_num+1}'
        raise ValueError(msg)

    # process the customisation instruction
    instruction = line[0:6]

     # chg vr 'subject' object class
    if instruction == 'cvrsoc':
        if remove_vr_instruction_processed_for_image:
            raise Exception(f"'cvr...' instruction  after 'rvrxxx' instruction not allowed, line {line_num+1}")
        vr_idx, target_vr, subj_idx = vrdu3.parse_change_soc_instruction(line_num+1, line, vrd_objects)
        imanno = vrdu3.change_vr_soc(imanno, vr_idx, target_vr, subj_idx,
                                     vrd_objects, vrd_predicates, line_num+1)
        vr_instructions_processed_for_image = True

    # chg vr 'subject' bbox
    elif instruction == 'cvrsbb':
        if remove_vr_instruction_processed_for_image:
            raise Exception(f"'cvr...' instruction  after 'rvrxxx' instruction not allowed, line {line_num+1}")        
        vr_idx, target_vr, subj_bbox = vrdu3.parse_change_sbb_instruction(line_num+1, line, vrd_objects)
        imanno = vrdu3.change_vr_sbb(imanno, vr_idx, target_vr, subj_bbox,
                                     vrd_objects, vrd_predicates, line_num+1)
        vr_instructions_processed_for_image = True

    # chg vr 'predicate'
    elif instruction == 'cvrpxx':
        if remove_vr_instruction_processed_for_image:
            raise Exception(f"'cvr...' instruction  after 'rvrxxx' instruction not allowed, line {line_num+1}")        
        vr_idx, target_vr, prd_idx = vrdu3.parse_change_predicate_instruction(line_num+1, line, vrd_predicates)
        imanno = vrdu3.change_vr_predicate(imanno, vr_idx, target_vr, prd_idx,
                                           vrd_objects, vrd_predicates, line_num+1)
        vr_instructions_processed_for_image = True

    # chg vr 'object' object class
    elif instruction == 'cvrooc':
        if remove_vr_instruction_processed_for_image:
            raise Exception(f"'cvr...' instruction  after 'rvrxxx' instruction not allowed, line {line_num+1}")        
        vr_idx, target_vr, obj_idx = vrdu3.parse_change_ooc_instruction(line_num+1, line, vrd_objects)
        imanno = vrdu3.change_vr_ooc(imanno, vr_idx, target_vr, obj_idx,
                                     vrd_objects, vrd_predicates, line_num+1)
        vr_instructions_processed_for_image = True

    # chg vr 'object' bbox
    elif instruction == 'cvrobb':
        if remove_vr_instruction_processed_for_image:
            raise Exception(f"'cvr...' instruction  after 'rvrxxx' instruction not allowed, line {line_num+1}")        
        vr_idx, target_vr, obj_bbox = vrdu3.parse_change_obb_instruction(line_num+1, line, vrd_objects)
        imanno = vrdu3.change_vr_obb(imanno, vr_idx, target_vr, obj_bbox,
                                     vrd_objects, vrd_predicates, line_num+1)
        vr_instructions_processed_for_image = True

    # append new vr to annotations
    elif instruction == 'avrxxx':
        if not image_active:
            raise Exception('append vr instruction not associated with image')
        new_vr = vrdu3.parse_append_vr_instruction(line_num+1, line, vrd_objects, vrd_predicates)
        imanno.append(new_vr)
        vr_instructions_processed_for_image = True

    # remove vr
    elif instruction == 'rvrxxx':
        vr_idx, target_vr = vrdu3.parse_remove_vr_instruction(line_num+1, line, vrd_objects)
        if remove_vr_instruction_processed_for_image:
            if not vr_idx < last_remove_vr_idx:
                raise Exception(f"'rvrxxx' instructions not in descending order by index, line {line_num+1}")
        imanno = vrdu3.remove_vr(imanno, vr_idx, target_vr,
                                 vrd_objects, vrd_predicates, line_num+1)
        vr_instructions_processed_for_image = True
        remove_vr_instruction_processed_for_image = True
        last_remove_vr_idx = vr_idx

    else:
        raise ValueError(f'instruction not recognised; line {line_num+1}')

# if necessary, finalise the processing for the last image name entry in the
# annotations customisation instruction file
if image_active:
    if vr_instructions_processed_for_image:
        vrd_anno[imname] = imanno
    else:
        ln = active_image_line_num
        print(f'image {imname} has no instructions; line {ln}')

print()
print('all annotation customisation instructions were interpreted and executed!')
print()
print(f'number of images processed: {image_cnt}')
print()
print('processing complete but changes not (yet) saved to disk')


#%%

save_modifications_to_file = False

if workflow_step_number == 2:
    if vrdcfg.step_2_save_customised_annotations:
        save_modifications_to_file = True
elif workflow_step_number == 7:
    if vrdcfg.step_7_save_customised_annotations:
        save_modifications_to_file = True   
elif workflow_step_number == 8:
    if vrdcfg.step_8_save_customised_annotations:
        save_modifications_to_file = True    
elif workflow_step_number == 11:
    if vrdcfg.step_11_save_customised_annotations:
        save_modifications_to_file = True    
else:
    raise ValueError('invalid annotation customisation step number')

if save_modifications_to_file:
    vrdu3.write_customised_annotations_to_file(vrd_anno, vrd_anno_path)
    print()
    print(f'customised annotations saved to file: {vrd_anno_path}')

print()
print(f'Step {workflow_step_number}: processing complete')

