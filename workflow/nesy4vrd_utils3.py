#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module defines utility functions used by the NeSy4VRD workflow.
'''

#%%

import json
import sys
sys.path.insert(0, '../analysis')
import vrd_utils as vrdu

#%%

def load_VRD_object_class_names(path):

    return vrdu.load_VRD_object_class_names(path)                  

#%%

def load_VRD_predicate_names(path):

    return vrdu.load_VRD_predicate_names(path)
 
#%% 

def load_VRD_image_annotations(path):

    return vrdu.load_VRD_image_annotations(path)

#%%

def get_tokens(line):
    '''
    Split an image annotation customisation instruction line into its 
    constituent tokens.
    
    Parameters:
        line : string (a line from a text file)
    
    Returns:
        tokens : list of strings
    '''
    
    tokens = line.split(';')
    for idx, token in enumerate(tokens):
        tokens[idx] = token.strip()
    
    return tokens


#%%

def format_bbox(bbox_spec, line_num):
    '''
    Convert a string bbox specification into a list of integers.
    
    Parameters:
        bbox_spec : string
    
    Returns:
        bbox : list (of 4 non-negative integers)
    '''
    
    min_length_of_bbox_spec = 10
    if len(bbox_spec) < min_length_of_bbox_spec:
        raise ValueError(f'invalid bbox specification, line {line_num}')
    
    if bbox_spec[0] == '[' and bbox_spec[-1] == ']':
        bbox_spec = bbox_spec.lstrip('[')
        bbox_spec = bbox_spec.rstrip(']')
    else:
        raise ValueError(f'invalid bbox specification, line {line_num}')
    
    bbox_elem = bbox_spec.split(',')
    
    if len(bbox_elem) != 4:
        raise ValueError(f'invalid bbox specification, line {line_num}')   
        
    for idx, elem in enumerate(bbox_elem):
        bbox_elem[idx] = elem.strip()
 
    for elem in bbox_elem:
        if not elem.isnumeric():
            raise ValueError(f'invalid bbox specification, line {line_num}')    
    
    bbox = [int(bbox_elem[0]), int(bbox_elem[1]), 
            int(bbox_elem[2]), int(bbox_elem[3])]
    
    return bbox


#%%

def parse_image_line(line_num, line):
    '''
    Extract the image name from an image line ('imname')
    '''
    tokens = get_tokens(line)

    if tokens[0] != 'imname':
        raise ValueError(f"expected image line indicated by 'imname', line {line_num}")
    
    if len(tokens) < 2:
        raise ValueError(f'missing image name, line {line_num}')
    
    imname = tokens[1]
    if not (imname.endswith('.jpg') or imname.endswith('.png')):
        raise ValueError(f'bad image name, line {line_num}')
    
    # check the image name starts with digits (as all VRD image names do)
    if not imname[0:5].isnumeric(): 
        raise ValueError(f'bad image name, line {line_num}')
    
    # if there are more than 2 tokens on the image name line, assume the 3rd
    # token is an 'image removal'
    im_instruction = ''
    if len(tokens) > 2:
        im_instruction = tokens[2]
    
    return imname, im_instruction

#%%

def parse_change_soc_instruction(line_num, line, vrd_objects):
    '''
    Parse a 'change subject object class' instruction line.
    
    Return:
        vr_idx : integer (the position index of a vr targetted for customisation)
        prd_idx : integer (the index value (integer label) for a predicate name)
    '''
    
    tokens = get_tokens(line)

    if tokens[0] != 'cvrsoc':
        raise ValueError(f"expected instruction type 'cvrsoc', line {line_num}")
    
    if len(tokens) < 4:
        raise ValueError(f"'cvrsoc' instruction is malformed, line {line_num}")
    
    if tokens[1].isnumeric():
        vr_idx = int(tokens[1])
    else:
        raise ValueError(f"vr index for 'cvrsoc' instruction not obtained, line {line_num}")
    
    target_vr = tokens[2]  # "('subject', 'predicate', 'object')"
    
    subj_name = tokens[3]
    if subj_name in vrd_objects:
        subj_idx = vrd_objects.index(subj_name)
    else:
        raise ValueError(f"invalid object class name '{subj_name}', line {line_num}")
      
    return vr_idx, target_vr, subj_idx

#%%

def parse_change_sbb_instruction(line_num, line, vrd_objects):
    '''
    Parse a 'change subject bounding box' instruction line.
    
    Return:
        vr_idx : integer (the position index of a vr targetted for customisation)
        prd_idx : integer (the index value (integer label) for a predicate name)
    '''
    
    tokens = get_tokens(line)

    if tokens[0] != 'cvrsbb':
        raise ValueError(f"expected instruction type 'cvrsbb', line {line_num}")
    
    if len(tokens) < 4:
        raise ValueError(f"'cvrsbb' instruction is malformed, line {line_num}")
    
    if tokens[1].isnumeric():
        vr_idx = int(tokens[1])
    else:
        raise ValueError(f"vr index for 'cvrsbb' instruction not obtained, line {line_num}")
    
    target_vr = tokens[2]  # "('subject', 'predicate', 'object')"

    subj_bbox = tokens[3]
    subj_bbox = format_bbox(subj_bbox, line_num)
    
    return vr_idx, target_vr, subj_bbox

#%% 

def parse_change_predicate_instruction(line_num, line, vrd_predicates):
    '''
    Parse a 'change predicate' instruction line.
    
    Return:
        vr_idx : integer (the position index of a vr targetted for customisation)
        prd_idx : integer (the index value (integer label) for a predicate name)
    '''
    
    tokens = get_tokens(line)

    if tokens[0] != 'cvrpxx':
        raise ValueError(f"expected instruction type 'cvrpxx', line {line_num}")
    
    if len(tokens) < 4:
        raise ValueError(f"'cvrpxx' instruction is malformed, line {line_num}")
    
    if tokens[1].isnumeric():
        vr_idx = int(tokens[1])
    else:
        raise ValueError(f"vr index for 'cvrpxx' instruction not obtained, line {line_num}")
    
    target_vr = tokens[2]  # ('subject', 'predicate', 'object')
    
    prd_name = tokens[3]
    if prd_name in vrd_predicates:
        prd_idx = vrd_predicates.index(prd_name)
    else:
        raise ValueError(f"invalid predicate name '{prd_name}' specified, line {line_num}")
      
    return vr_idx, target_vr, prd_idx


#%%

def parse_change_ooc_instruction(line_num, line, vrd_objects):
    '''
    Parse a 'change object object class' instruction line.
    
    Return:
        vr_idx : integer (the position index of a vr targetted for customisation)
        target_vr : string ( "('subject', 'predicate', 'object')" )
        obj_idx : integer (the index value (integer label) for an object class name)
    '''
    
    tokens = get_tokens(line)

    if tokens[0] != 'cvrooc':
        raise ValueError(f"expected instruction type 'cvrooc', line {line_num}")
    
    if len(tokens) < 4:
        raise ValueError(f"'cvrooc' instruction is malformed, line {line_num}")
    
    if tokens[1].isnumeric():
        vr_idx = int(tokens[1])
    else:
        raise ValueError(f"vr index for 'cvrooc' instruction not obtained, line {line_num}")
    
    target_vr = tokens[2]  # "('subject', 'predicate', 'object')"
    
    obj_name = tokens[3]
    if obj_name in vrd_objects:
        obj_idx = vrd_objects.index(obj_name)
    else:
        raise ValueError(f"invalid object class name '{obj_name}', line {line_num}")
      
    return vr_idx, target_vr, obj_idx


#%%

def parse_change_obb_instruction(line_num, line, vrd_objects):
    '''
    Parse a "change 'object' bounding box" instruction line.
    
    Return:
        vr_idx : integer (the position index of a vr targetted for customisation)
        prd_idx : integer (the index value (integer label) for a predicate name)
    '''
    
    tokens = get_tokens(line)

    if tokens[0] != 'cvrobb':
        raise ValueError(f"expected instruction type 'cvrobb', line {line_num}")
    
    if len(tokens) < 4:
        raise ValueError(f"'cvrobb' instruction is malformed, line {line_num}")
    
    if tokens[1].isnumeric():
        vr_idx = int(tokens[1])
    else:
        raise ValueError(f"vr index for 'cvrobb' instruction not obtained, line {line_num}")
    
    target_vr = tokens[2]  # "('subject', 'predicate', 'object')"

    obj_bbox = tokens[3]
    obj_bbox = format_bbox(obj_bbox, line_num)
    
    return vr_idx, target_vr, obj_bbox


#%%

def parse_remove_vr_instruction(line_num, line, vrd_objects):
    '''
    Parse a "remove visual relationship" instruction line.
    
    Return:
        vr_idx : integer (the position index of a vr targetted for customisation)
        prd_idx : integer (the index value (integer label) for a predicate name)
    '''
    
    tokens = get_tokens(line)

    if tokens[0] != 'rvrxxx':
        raise ValueError(f"expected instruction type 'rvrxxx', line {line_num}")
    
    if len(tokens) < 3:
        raise ValueError(f"'rvrxxx' instruction is malformed, line {line_num}")
    
    if tokens[1].isnumeric():
        vr_idx = int(tokens[1])
    else:
        raise ValueError(f"vr index for 'rvrxxx' instruction not obtained,  line {line_num}")
    
    target_vr = tokens[2]  # "('subject', 'predicate', 'object')"
    
    return vr_idx, target_vr


#%%

def parse_append_vr_instruction(line_num, line, vrd_objects, vrd_predicates):
    '''
    Parse an append vr instruction line. Build a properly formatted
    vr dictionary for the new vr to be appended.
    
    Returns:
        new_vr : dictionary (a new vr to be appended to the annotions
                             of an image)
    '''
    
    tokens = get_tokens(line)

    #for token in tokens:
    #    print(token)

    if tokens[0] != 'avrxxx':
        raise ValueError(f"expected instruction type 'avrxxx', line {line_num}")
    
    if len(tokens) < 6:
        raise ValueError(f"'avrxxx' instruction is malformed, line {line_num}")
    
    subj_name = tokens[1]
    if subj_name in vrd_objects:
        subj_idx = vrd_objects.index(subj_name)
    else:
        raise ValueError(f"invalid 'subject' object class name '{subj_name}', line {line_num}")
    
    subj_bbox = tokens[2]
    subj_bbox = format_bbox(subj_bbox, line_num)
    
    prd_name = tokens[3]
    if prd_name in vrd_predicates:
        prd_idx = vrd_predicates.index(prd_name)
    else:
        raise ValueError(f"invalid 'predicate' name '{prd_name}', line {line_num}")
 
    obj_name = tokens[4]
    if obj_name in vrd_objects:
        obj_idx = vrd_objects.index(obj_name)
    else:
        raise ValueError(f"invalid 'object' object class name '{obj_name}', line {line_num}")

    obj_bbox = tokens[5]
    obj_bbox = format_bbox(obj_bbox, line_num)

    new_vr = {'predicate': prd_idx,
              'object': {'category': obj_idx, 'bbox': obj_bbox},
              'subject': {'category': subj_idx, 'bbox': subj_bbox}}
    
    return  new_vr


#%%

def change_vr_soc(imanno, vr_idx, target_vr, new_subj_idx,
                  vrd_objects, vrd_predicates, line_num):
    '''
    For a given image and a particular visual relationship, replace the
    current subject object class with a new one.
    
    Parameters:
        imanno : list of dictionaries (vr annotations for an image)
        vr_idx : integer  (index of visual relationship to be modified)
        new_prd_idx : integer (id of the new predicate)
    
    Returns
        imanno : list of dictionaries
            - the visual relationship annotations for an image after
            having applied a specified customisation
    '''

    # safety check; ensure the target vr we plan to change actually
    # matches the actual current vr indicated by vr_idx
    vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
    if not vr_idx in range(0, len(vrs)):
        raise Exception(f"invalid vr index in 'cvrsoc' instruction, line {line_num}")
    current_vr = str(vrs[vr_idx])
    if not current_vr == target_vr:
        raise Exception(f"cvrsoc instruction failed; target vr mismatches actual vr, line {line_num}")
    
    # change the predicate in the target relationship
    imanno[vr_idx]['subject']['category'] = new_subj_idx
    
    return imanno


#%%

def change_vr_sbb(imanno, vr_idx, target_vr, new_subj_bbox,
                  vrd_objects, vrd_predicates, line_num):
    '''
    For a given image and a particular visual relationship, replace the
    current subject bounding box with a new one.
    
    Parameters:
        imanno : list of dictionaries (vr annotations for an image)
        vr_idx : integer  (index of visual relationship to be modified)
        new_prd_idx : integer (id of the new predicate)
    
    Returns
        imanno : list of dictionaries
            - the visual relationship annotations for an image after
            having applied a specified customisation
    '''

    # safety check; ensure the target vr we plan to change actually
    # matches the actual current vr indicated by vr_idx
    vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
    if not vr_idx in range(0, len(vrs)):
        raise Exception(f"invalid vr index in 'cvrsbb' instruction, line {line_num}")
    current_vr = str(vrs[vr_idx])
    if not current_vr == target_vr:
        raise Exception(f"cvrsbb instruction failed; target vr mismatches actual vr, line {line_num}")
    
    # change the predicate in the target relationship
    imanno[vr_idx]['subject']['bbox'] = new_subj_bbox
    
    return imanno

#%%

def change_vr_predicate(imanno, vr_idx, target_vr, new_prd_idx,
                        vrd_objects, vrd_predicates, line_num):
    '''
    For a given image and a particular visual relationship, replace the
    current predicate with a new one.
    
    Parameters:
        imanno : list of dictionaries (vr annotations for an image)
        vr_idx : integer  (index of visual relationship to be modified)
        new_prd_idx : integer (id of the new predicate)
    
    Returns
        imanno : list of dictionaries
            - the visual relationship annotations for an image after
            having applied a specified customisation
    '''

    # safety check; ensure the target vr we plan to change actually
    # matches the actual current vr indicated by vr_idx
    vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
    if not vr_idx in range(0, len(vrs)):
        raise Exception(f"invalid vr index in 'cvrpxx' instruction, line {line_num}")
    current_vr = str(vrs[vr_idx])
    if not current_vr == target_vr:
        raise Exception(f"cvrpxx instruction failed; expected vr mismatches actual vr; line {line_num}")
    
    # change the predicate in the target relationship
    imanno[vr_idx]['predicate'] = new_prd_idx
    
    return imanno

#%%

def change_vr_ooc(imanno, vr_idx, target_vr, new_obj_idx,
                  vrd_objects, vrd_predicates, line_num):
    '''
    For a given image and a particular visual relationship, replace the
    current 'object' object class with a new one.
    
    Parameters:
        imanno : list of dictionaries (vr annotations for an image)
        vr_idx : integer  (index of visual relationship to be modified)
        new_prd_idx : integer (id of the new predicate)
    
    Returns
        imanno : list of dictionaries
            - the visual relationship annotations for an image after
            having applied a specified customisation
    '''

    # safety check; ensure the target vr we plan to change actually
    # matches the actual current vr indicated by vr_idx
    vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
    if not vr_idx in range(0, len(vrs)):
        raise Exception(f"invalid vr index in 'cvrooc' instruction, line {line_num}")
    current_vr = str(vrs[vr_idx])
    if not current_vr == target_vr:
        raise Exception(f"'cvrooc' instruction failed; expected vr mismatches actual vr, line {line_num}")
    
    # change the predicate in the target relationship
    imanno[vr_idx]['object']['category'] = new_obj_idx
    
    return imanno


#%%

def change_vr_obb(imanno, vr_idx, target_vr, new_obj_bbox,
                  vrd_objects, vrd_predicates, line_num):
    '''
    For a given image and a particular visual relationship, replace the
    current 'object' bounding box with a new one.
    
    Parameters:
        imanno : list of dictionaries (vr annotations for an image)
        vr_idx : integer  (index of visual relationship to be modified)
        new_prd_idx : integer (id of the new predicate)
    
    Returns
        imanno : list of dictionaries
            - the visual relationship annotations for an image after
            having applied a specified customisation
    '''

    # safety check; ensure the target vr we plan to change actually
    # matches the actual current vr indicated by vr_idx
    vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
    if not vr_idx in range(0, len(vrs)):
        raise Exception(f"invalid vr index in 'cvrobb' instruction, line {line_num}")
    current_vr = str(vrs[vr_idx])
    if not current_vr == target_vr:
        raise Exception(f"'cvrobb' instruction failed; expected vr mismatches actual vr, line {line_num}")
    
    # change the predicate in the target relationship
    imanno[vr_idx]['object']['bbox'] = new_obj_bbox
    
    return imanno


#%%

def remove_vr(imanno, vr_idx, target_vr,
              vrd_objects, vrd_predicates, line_num):
    '''
    For a given image and a particular visual relationship, remove the
    visual relationship from the annotations.
    
    Parameters:
        imanno : list of dictionaries (vr annotations for an image)
        vr_idx : integer  (index of visual relationship to be modified)
        target_vr : string 
    
    Returns
        imanno : list of dictionaries
            - the visual relationship annotations for an image after
            having applied a specified customisation
    '''

    # safety check; ensure the target vr we plan to change actually
    # matches the actual current vr indicated by vr_idx
    vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
    if not vr_idx in range(0, len(vrs)):
        raise Exception(f"invalid vr index in 'rvrxxx' instruction, line {line_num}")
    current_vr = str(vrs[vr_idx])
    if not current_vr == target_vr:
        raise Exception(f"'rvrxxx' instruction failed; expected vr mismatches actual vr, line {line_num}")

    del imanno[vr_idx]
    
    return imanno


#%%

def remove_image(imname, vrd_anno):
    '''
    Remove the (key, value) pair consisting of an image name and its
    corresponding visual relationship annotations from the VRD annotations
    dictionary. This effectively simulates the removal of the named image
    from the dataset.
    
    The physical image file (.jpg) is NOT deleted.
    
    Handling image removals in this way means that to build a list of the
    image file names one must do this using the annotations dictionary via,
    say, `vrd_img_names = vrd_anno.keys()` and NOT via, say,
    `vrd_img_names = os.listdir(path)`.  In PyTorch, this issue is most
    relevant when instantiating one's subclass of 'Dataset'.  This way, the
    PyTorch 'DataLoader' will retrieve only those physical images that have
    entries in the annotations dictionary.
    
    Parameters:
        imname : string
            - the name of an image file that is a key in the annotations
              dictionary
        vrd_anno : dictionary (the annotations dictionary)
    
    Returns:
        None
    '''
    
    # the 'del' statement updates the annotations dictionary 'in place',
    # so there's no need to return the dictionary as a return value
    del vrd_anno[imname]
    
    return None


#%%

def write_customised_annotations_to_file(vrd_anno, path):
    '''
    Write visual relationship annotations dictionary to file in json format.
    
    Parameters:
        vrd_anno : dictionary (VRD annotations)
        path : string (path and filename to which to write)
    
    Returns:
        None
            - the new .json file appearing on disk is the side effect of
            calling this function; no return value required
    '''

    with open(path, 'w') as fp:
        json.dump(vrd_anno, fp)

#    try:
#        fp = open(path, mode='w')
#        json.dump(vrd_anno, fp)
#    except:
#        raise Exception(f"problem saving annotations file: {path}")
#    else:
#        fp.close()
    
    return None

#%%

def save_VRD_object_class_names(object_names, path):
    '''
    Write object names to file in json format.
    '''

    with open(path, 'w') as fp:
        json.dump(object_names, fp)
    
#    try:
#        fp = open(path, mode='w')
#        json.dump(object_names, fp)
#    except:
#        raise Exception(f"problem saving object classes file: {path}")
#    else:
#        fp.close()
    
    return None

#%%

def save_VRD_predicate_names(predicate_names, path):
    '''
    Write predicate names to file in json format.
    '''

    with open(path, 'w') as fp:
        json.dump(predicate_names, fp)

#    try:
#        fp = open(path, mode='w')
#        json.dump(predicate_names, fp)
#    except:
#        raise Exception(f"problem saving predicates file: {path}")
#    else:
#        fp.close()
    
    return None

#%%

def merge_object_classes(from_name, to_name, vrd_img_names,
                         vrd_anno, vrd_objects, vrd_predicates):
    '''
    Perform a global merge of one object class into another across the
    image annotations for a designated VRD dataset (train/test).
    
    The annotations dictionary 'vrd_anno' is updated 'in place', so there
    is no need for a return value.
    
    Returns:
        None
    '''
    
    # find the names of all image files (and their corresponding 
    # vr annotations) for which the corresponding annotations refer
    # to the object class named in 'from_name'
    res_imgs, res_annos = vrdu.get_images_with_object_class(from_name,
                                                            vrd_img_names, 
                                                            vrd_anno, 
                                                            vrd_objects, 
                                                            vrd_predicates)

    print(f'Number of images referring to object class {from_name}: {len(res_imgs)}')
    
    from_name_int_label = vrd_objects.index(from_name)
    to_name_int_label = vrd_objects.index(to_name)
    
    for idx, imanno in enumerate(res_annos):
        imname = res_imgs[idx]
        merge_applied = False
        for vr_idx, vr in enumerate(imanno):
            if vr['subject']['category'] == from_name_int_label:
                imanno[vr_idx]['subject']['category'] = to_name_int_label
                merge_applied = True
            if vr['object']['category'] == from_name_int_label:
                imanno[vr_idx]['object']['category'] = to_name_int_label
                merge_applied = True
        
        if merge_applied:
            # replace the image's annotations with the customised annotations
            vrd_anno[imname] = imanno
        else:
            raise Exception('Unexpected condition encountered merging object classes')                               
    
    return None

#%%

def merge_predicates(from_name, to_name, vrd_img_names,
                     vrd_anno, vrd_objects, vrd_predicates):
    '''
    Perform a global merge of one predicate into another across the
    image annotations for a designated VRD dataset (train/test).
    
    The annotations dictionary 'vrd_anno' is updated 'in place', so there
    is no need for a return value.
    
    Returns:
        None
    '''
    
    # find the names of all image files (and their corresponding 
    # vr annotations) for which the corresponding annotations refer
    # to the predicate named in 'from_name'
    res_imgs, res_annos = vrdu.get_images_with_predicate(from_name,
                                                         vrd_img_names, 
                                                         vrd_anno, 
                                                         vrd_objects, 
                                                         vrd_predicates)

    print(f'Number of images referring to predicate {from_name}: {len(res_imgs)}')
    
    from_name_int_label = vrd_predicates.index(from_name)
    to_name_int_label = vrd_predicates.index(to_name)
    
    for idx, imanno in enumerate(res_annos):
        imname = res_imgs[idx]
        merge_applied = False
        for vr_idx, vr in enumerate(imanno):
            if vr['predicate'] == from_name_int_label:
                imanno[vr_idx]['predicate'] = to_name_int_label
                merge_applied = True
        
        if merge_applied:
            # replace the image's annotations with the customised annotations
            vrd_anno[imname] = imanno
        else:
            raise Exception('Unexpected condition encountered merging predicates')                               
    
    return None


#%%

def remove_vr_globally(vr, vrd_img_names, vrd_anno, vrd_objects, vrd_predicates):
    '''
    Remove a target visual relationship from the VRD annotations on a
    global basis (ie across all image annotations).
    
    Parameters:
        vr : tuple of strings
            - the target vr to remove, form ('subject', 'predicate', 'object')
        vrd_anno : dictionary
            - the VRD annotations dictionary for the dataset
    
    Returns:
        instance_cnt : integer
            - the number of instances of the target vr removed
            
        NOTE: - the annotations dictionary parameter is updated 'in place'
                and represents the real 'return value' of this function;
                returning the instance count is sugar
    '''
    
    sub_name, prd_name, obj_name = vr
    
    img_names, img_annos = vrdu.get_images_with_target_vr_B(sub_name, 
                                                            prd_name,
                                                            obj_name,
                                                            vrd_img_names,
                                                            vrd_anno, 
                                                            vrd_objects,
                                                            vrd_predicates)

    sub_int_label = vrd_objects.index(sub_name)
    prd_int_label = vrd_predicates.index(prd_name)
    obj_int_label = vrd_objects.index(obj_name)
    
    instance_cnt = 0
        
    for idx, imanno in enumerate(img_annos):

        # find the vrs that match the target vr and save their index values
        vrs_to_remove = []
        for vr_idx, vr in enumerate(imanno):
            if vr['subject']['category'] == sub_int_label and \
               vr['predicate'] == prd_int_label and \
               vr['object']['category'] == obj_int_label:
                 vrs_to_remove.append(vr_idx)
        
        # remove the vrs identified for removal (carefully)
        if len(vrs_to_remove) > 0:
            # We MUST process the vr removals in DESCENDING order of
            # index because most removals will cause the index
            # of some number of the remaining vrs in the list to shift, which
            # would invalidate some index identifiers we just
            # collected in the preceding code block. An invalidated
            # index will result in either 1) an 'index out of range'
            # exception or 2) the wrong vr being silently removed.
            for vr_idx in reversed(vrs_to_remove):
                del imanno[vr_idx]
                instance_cnt += 1
            
            # replace the original annotations for the image with the
            # now customisted annotations
            imname = img_names[idx]
            vrd_anno[imname] = imanno
    
    return instance_cnt  
    

#%%

def change_vr_globally(from_vr, to_vr, objects_swap_positions, predicate_changes,
                       vrd_img_names, vrd_anno, vrd_objects, vrd_predicates):
    '''
    Change a target visual relationship in the VRD annotations on a
    global basis (ie across all image annotations).
    
    Parameters:
        from_vr : tuple of strings
            - the target vr to change, form ('subject', 'predicate', 'object')
        to_vr : tuple of strings
            - the new vr to be established
        objects_swap_positions : Boolean
            - boolean flag indicating whether the 'subject' and 'object'
              object classes (and their corresponding bboxes) keep their 
              positions or swap positions
        predicate_changes : Boolean
            - boolean flag indicating whether the predicate changes or
              stays the same
        vrd_anno : dictionary
            - the VRD annotations dictionary for the dataset
    
    Returns:
        instance_cnt : integer
            - the number of instances of the target vr found and changed
            
        NOTE: - the annotations dictionary parameter is updated 'in place'
                and represents the real 'return value' of this function;
                returning the instance count is sugar
    '''
    
    from_sub_name, from_prd_name, from_obj_name = from_vr
    to_sub_name, to_prd_name, to_obj_name = to_vr
     
    img_names, img_annos = vrdu.get_images_with_target_vr_B(from_sub_name, 
                                                            from_prd_name,
                                                            from_obj_name,
                                                            vrd_img_names,
                                                            vrd_anno, 
                                                            vrd_objects,
                                                            vrd_predicates)

    from_sub_int_label = vrd_objects.index(from_sub_name)
    from_prd_int_label = vrd_predicates.index(from_prd_name)
    from_obj_int_label = vrd_objects.index(from_obj_name)
    
    to_prd_int_label = vrd_predicates.index(to_prd_name)    
    
    instance_cnt = 0
        
    for idx, imanno in enumerate(img_annos):

        # find the vrs that match the target vr and save their index values
        vrs_to_change = []
        for vr_idx, vr in enumerate(imanno):
            if vr['subject']['category'] == from_sub_int_label and \
               vr['predicate'] == from_prd_int_label and \
               vr['object']['category'] == from_obj_int_label:
                 vrs_to_change.append(vr_idx)
        
        # change the vr instances identified for transformation
        # (nb: there will normally be one only per image, but multiple
        # instances per image are possible)
        if len(vrs_to_change) > 0:
            imname = img_names[idx]
            for vr_idx in vrs_to_change:
                vr = imanno[vr_idx]
                if predicate_changes:
                    vr['predicate'] = to_prd_int_label
                if objects_swap_positions:
                    save_subj_category = vr['subject']['category']
                    save_subj_bbox = vr['subject']['bbox']
                    vr['subject']['category'] = vr['object']['category']
                    vr['subject']['bbox'] = vr['object']['bbox']
                    vr['object']['category'] = save_subj_category
                    vr['object']['bbox'] = save_subj_bbox
                imanno[vr_idx] = vr
                instance_cnt += 1
            vrd_anno[imname] = imanno
    
    return instance_cnt
    

#%%

def switch_object_classes_in_named_images(from_name, to_name, img_names,
                                          vrd_anno, vrd_objects, vrd_predicates):
    '''
    Switch all references to object class A to object class B in the
    annotations for a set of named images.
    
    Returns:
        None
    
        NOTE: the annotations dictionary parameter is updated 'in place'
              and represents the real 'return value' of this function
    '''
  
    from_name_int_label = vrd_objects.index(from_name)
    to_name_int_label = vrd_objects.index(to_name)
    
    for idx, imname in enumerate(img_names):
        imanno = vrd_anno[imname].copy()
        switch_applied = False
        for vr_idx, vr in enumerate(imanno):
            if vr['subject']['category'] == from_name_int_label:
                imanno[vr_idx]['subject']['category'] = to_name_int_label
                switch_applied = True
            if vr['object']['category'] == from_name_int_label:
                imanno[vr_idx]['object']['category'] = to_name_int_label
                switch_applied = True
        
        if switch_applied:
            # replace the image's annotations with the customised annotations
            vrd_anno[imname] = imanno
        else:
            raise Exception('Unexpected condition encountered switching object classes')                               
    
    return None

#%%

def check_if_vrs_are_duplicates(vr1, vr2):
    
    return vrdu.check_if_vrs_are_duplicates(vr1, vr2)

#%%



