#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module contains utility functions that support the analysis of the
NeSy4VRD visual relationship annotations for the VRD images.

No function in this module modifies data files in any way.  
'''

#%%

import os
import json
from PIL import Image, ImageDraw
import itertools


#%%

def load_VRD_object_class_names(path):
    '''
    Load the VRD object class names.
    
    Parameters:
        path : string (path to object classes file in annotations directory)
    
    Returns:
        object_class_names : (ordered) tuple of strings
    
    Additional context:
    The returned tuple of object class names is 'ordered' and should NEVER
    be modified.  The position (index) of a name in the tuple determines
    that name's integer label.  The VRD image annotations, in their
    internal format, refer to object classes (and predicates) solely by 
    their integer labels.
    
    The tuple of object class names is used to convert, bi-directionally, 
    between object class names and object class integer labels.  
    '''

    with open(path, 'r') as fp:
        object_class_names = json.load(fp)
    
    return tuple(object_class_names)

#%%

def load_VRD_predicate_names(path):
    '''
    Load the VRD predicate names.
    
    Parameters:
        path : string (path to predicates file in annotations directory)
    
    Returns:
        predicate_names : (ordered) tuple of strings

    Additional context:
    The returned tuple of predicate names is 'ordered' and should NEVER
    be modified.  The position (index) of a name in the tuple determines
    that name's integer label.  The VRD image annotations, in their
    internal format, refer to predicates (and object classes) solely by 
    their integer labels.
    
    The tuple of predicate names is used to convert, bi-directionally, 
    between predicate names and predicate integer labels.    
    '''

    with open(path, 'r') as fp:
        predicate_names = json.load(fp)
    
    return tuple(predicate_names)

#%% 

def load_VRD_image_annotations(path):
    '''
    Load the VRD image visual relationship annotations.
       
    Parameters:
        path : string (path to annotations file in annotations directory)
    
    Returns:
        anno : dictionary
            - the keys are image names
            - the values are lists (of dictionaries)
    
    '''

    with open(path, 'r') as fp:
        annotations = json.load(fp)
    
    return annotations

#%%

def get_image_size(imname, imagedir):

    path = os.path.join(imagedir, imname)
    img = Image.open(path)  
         
    return img.size  # (W x H)

#%%

def display_image(imname, imagedir):
    
    path = os.path.join(imagedir, imname)
    img = Image.open(path)   

    # display the image
    # (on macOS, PIL launches Preview to display the image)
    img.show(title='VRD Image')
    
    print(f'image name: {imname}')
    print(f'image size: (W x H) {img.size}')
    
    return None

#%%

def display_image_with_bboxes_for_vr(imname, vr, imagedir):

    path = os.path.join(imagedir, imname)
    img = Image.open(path)   

    draw = ImageDraw.Draw(img)
    
    # draw bbox around vr subject
    bbox = vr['subject']['bbox']
    xy = [(bbox[2], bbox[0]), (bbox[3], bbox[1])]
    draw.rectangle(xy, outline=230, width=2)
    # nb: subject bbox outline is coloured bright red
    
    # draw bbox around vr object
    bbox = vr['object']['bbox']
    xy = [(bbox[2], bbox[0]), (bbox[3], bbox[1])]   
    draw.rectangle(xy, outline=128, width=2)
    # nb: object bbox outline is coloured dull red

    # display the image
    # (on macOS, PIL launches Apple's Preview to display the image)
    img.show(title='VRD Image')
    
    return None

#%%

def display_image_with_all_bboxes(imname, imanno, imagedir):

    path = os.path.join(imagedir, imname)
    img = Image.open(path)   
    
    draw = ImageDraw.Draw(img)
       
    bboxes = get_bboxes_and_object_classes(imname, imanno)
    
    for b in bboxes.keys():     
        # draw bbox 
        xy = [(b[2], b[0]), (b[3], b[1])]
        draw.rectangle(xy, outline=230, width=2)
    
    # display the image
    # (on macOS, PIL launches Apple's Preview to display the image)
    img.show(title='VRD Image')
    
    print(f'number of objects: {len(bboxes)}')
    
    return None


#%%

def display_image_with_selected_vrs(imname, imanno, vr_indices, imagedir):

    path = os.path.join(imagedir, imname)
    img = Image.open(path)   
    
    draw = ImageDraw.Draw(img)
    
    for vridx in vr_indices:
        
        if not (vridx >= 0 and vridx < len(imanno)):
            raise ValueError(f'VR index {vridx} out of range')
        
        vr = imanno[vridx]
        
        # draw bbox around vr subject
        bbox = vr['subject']['bbox']
        xy = [(bbox[2], bbox[0]), (bbox[3], bbox[1])] 
        draw.rectangle(xy, outline=230, width=4)  
            
        # draw bbox around vr object
        bbox = vr['object']['bbox']
        xy = [(bbox[2], bbox[0]), (bbox[3], bbox[1])]   
        draw.rectangle(xy, outline=230, width=4) 
        
    # display the image
    img.show(title='VRD Image')
       
    return None


#%%

def get_visual_relationships(imanno, vrd_objects, vrd_predicates):
    '''
    Get the visual relationship annotations for an image.
    
    More specifically, this function converts the internally formatted
    visual relationships for an image into readable form.
    
    Parameters:
        imanno : list of dictionaries
            - the visual relationship (vr) annotations for an image in
            their internal format which makes them hard to interpret
        vrd_objects : list of strings (object class names)
        vrd_predicates : list of strings (predicate names)
    
    Returns:
        vrs : list of tuples
            - readable vr 3-tuples of the form ('subject', 'predicate', 'object')
    
    Additional context:
    * when converting the visual relationships to a readable 3-tuple
      of the form ('subject', 'predicate', 'object') we ignore the
      bounding box specifications for the 'subject' and 'object' objects
    '''
    
    vrs = []
    for vr in imanno:
        sub_cls_idx = vr['subject']['category']
        prd_cls_idx = vr['predicate']
        obj_cls_idx = vr['object']['category']
        sub_name = vrd_objects[sub_cls_idx]
        prd_name = vrd_predicates[prd_cls_idx]
        obj_name = vrd_objects[obj_cls_idx]
        vrs.append((sub_name, prd_name, obj_name))

    return vrs

#%% 

class BboxError(Exception):
    '''
    Exception raised when the annotations for an image contain a bbox that
    has been assigned more than one object class.
    
    Attributes:
        message - explanation of problem
        
    '''
    def __init__(self, message, imgname, vridx, bbox):
        self.message = message
        self.imgname = imgname
        self.vridx = vridx
        self.bbox = bbox


def get_bboxes_and_object_classes(imgname, imganno):
    '''
    Parse the subject-predicate-object visual relationship annotations 
    associated with a given image. Extract 1) the unique set of
    bounding box specifications for the individual objects identified as
    being present in the image, and 2) the object class index assigned
    to each bbox.  If we encounter an image whose annotations contain
    a bbox that has been assigned more than one object class, raise an
    exception.

    Parameters:
        imgname : image file name (string)
        imganno : list of dictionaries
            - the subject-predicate-object visual relationship annotations 
            for a given image
   
    Returns:
        bboxes : dictionary containing bboxes as keys and object class
                 indices as values
    '''
    
    bboxes = {}
    
    for idx, vr in enumerate(imganno):
 
        sub_idx = vr['subject']['category']
        sub_bbox = vr['subject']['bbox']
        sub_bbox_tuple = tuple(sub_bbox)

        obj_idx = vr['object']['category']
        obj_bbox = vr['object']['bbox']
        obj_bbox_tuple = tuple(obj_bbox)
        
        if sub_bbox_tuple in bboxes:
            if sub_idx != bboxes[sub_bbox_tuple]:
                raise BboxError("Image has bbox with multiple classes", 
                                imgname, idx, sub_bbox_tuple)
        else:
            bboxes[sub_bbox_tuple] = sub_idx
        
        if obj_bbox_tuple in bboxes:
            if obj_idx != bboxes[obj_bbox_tuple]:
                raise BboxError("Image has bbox with multiple classes", 
                                imgname, idx, obj_bbox_tuple) 
        else:
            bboxes[obj_bbox_tuple] = obj_idx        

    return bboxes        
        

#%%

def get_object_classes_and_predicates(imganno):
    '''
    Parse the subject-predicate-object visual relationship annotations 
    associated with a given image of the VRD dataset. Extract 1) the set of  
    indices for the object classes mentioned within the annotations 
    (ie present in the image), and 2) the set of indices for the predicates
    mentioned within the annotations.
    
    Parameters:
        imganno : list of dictionaries
            - the subject-predicate-object visual relationship annotations 
            for a given image
    
    Returns
        sub_cls : a list of integers
            - the integers are the indices of the classes of object
            present in the associated image and occupying the role of
            'subject' in a visual relationship
        prd_cls : a list of integers
            - the integers are the indices of the predicate names
            present in the visual relationship annotations of the 
            associated image
        obj_cls : a list of integers
            - the integers are the indices of the classes of object
            present in the associated image and occupying the role of
            'object' in a visual relationship
    '''

    sub_classes = []
    prd_classes = []
    obj_classes = []
    for i in range(len(imganno)):
        rel = imganno[i]
        sub_cls = rel['subject']['category']
        obj_cls = rel['object']['category']
        if not sub_cls in sub_classes:
            sub_classes.append(sub_cls)
        if not obj_cls in obj_classes:
            obj_classes.append(obj_cls)
        prd_cls = rel['predicate']
        if not prd_cls in prd_classes:
            prd_classes.append(prd_cls)

    return sub_classes, prd_classes, obj_classes


#%% get all visual relationships for a given object class

def get_all_relationships_for_object_class(cls_name, imgs, img_annos,
                                           objects, predicates):
    '''
    '''
    res = []
    for idx, imanno in enumerate(img_annos):
        vrs = get_visual_relationships(imanno, objects, predicates)
        imname = imgs[idx]
        for vr in vrs:
            if cls_name in vr:
                res.append((imname, vr))

    return res

#%% get all visual relationships for a given predicate

def get_all_relationships_for_predicate(prd_name, imgs, img_annos,
                                        objects, predicates):
    '''
    '''
    res = []
    for idx, imanno in enumerate(img_annos):
        vrs = get_visual_relationships(imanno, objects, predicates)
        imname = imgs[idx]
        for vr in vrs:
            if prd_name in vr:
                res.append((imname, vr))

    return res

#%% get all images for a given object class

def get_images_with_object_class(cls_name, vrd_img_names, vrd_anno, 
                                 vrd_objects, vrd_predicates):
    '''
    '''
    
    cls_idx = vrd_objects.index(cls_name)
    
    images_with_target_cls = []
    annos_with_target_cls = []
    for idx, imname in enumerate(vrd_img_names):
        imanno = vrd_anno[imname].copy()
        sub_classes, prd_classes, obj_classes = get_object_classes_and_predicates(imanno)
        all_classes = set(sub_classes + obj_classes)    
        if cls_idx in all_classes:
            images_with_target_cls.append(imname)
            annos_with_target_cls.append(imanno)
    
    return images_with_target_cls, annos_with_target_cls


#%% get all images for a given set of object classes

def get_images_with_object_classes(cls_names, vrd_img_names, vrd_anno, 
                                   vrd_objects):
    '''
    Find the images whose VR annotations contain references to
    each of the object classes within a given set of object classes.
    '''
    
    cls_idxs = [vrd_objects.index(name) for name in cls_names]
    
    images_with_target_cls = []
    annos_with_target_cls = []
    for idx, imname in enumerate(vrd_img_names):
        imanno = vrd_anno[imname].copy()
        sub_classes, prd_classes, obj_classes = get_object_classes_and_predicates(imanno)
        all_classes = set(sub_classes + obj_classes)
        
        save_result = True
        for cls_idx in cls_idxs:            
            if cls_idx in all_classes:
                pass
            else:
                save_result = False
                break
        
        if save_result:
            images_with_target_cls.append(imname)
            annos_with_target_cls.append(imanno)
    
    return images_with_target_cls, annos_with_target_cls

#%% get all images for a given predicate

def get_images_with_predicate(prd_name, vrd_img_names, vrd_anno, 
                              vrd_objects, vrd_predicates):
    '''
    '''
    
    prd_idx = vrd_predicates.index(prd_name)
    
    images_with_target_prd = []
    annos_with_target_prd = []
    for idx, imname in enumerate(vrd_img_names):
        imanno = vrd_anno[imname].copy()
        sub_classes, prd_indices, obj_classes = get_object_classes_and_predicates(imanno)   
        if prd_idx in prd_indices:
            images_with_target_prd.append(imname)
            annos_with_target_prd.append(imanno)
    
    return images_with_target_prd, annos_with_target_prd


#%% get all distinct predicates used with a given object class

def get_distinct_predicates_for_object_class(cls_name, img_names, anno,
                                             objects, predicates):
    '''
    '''
    res_imgs, res_annos = get_images_with_object_class(cls_name, img_names,
                                                       anno, objects, 
                                                       predicates)

    vrs_with_img_names = get_all_relationships_for_object_class(cls_name, 
                                                                res_imgs,
                                                                res_annos, 
                                                                objects,
                                                                predicates)
    
    res_prd = []
    for item in vrs_with_img_names:
        vr = item[1]
        prd = vr[1]
        res_prd.append(prd)
    
    distinct_predicates = list(set(res_prd))
    
    return distinct_predicates

#%%

def get_images_with_target_vr_A(sub_name, prd_name, 
                                img_names, anno, objects, predicates):
    '''
    Find images with a visual relationship that uses a given target
    subject and predicate. Return the images/annos and the set of distinct
    object classes used in the 'object' of the visual relationship.
    '''
    sub_idx = objects.index(sub_name)
    prd_idx = predicates.index(prd_name)  

    images_with_target = []
    annos_with_target = []
    object_names = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname].copy()
        sub_classes, prd_classes, obj_classes = get_object_classes_and_predicates(imanno)
        #all_classes = set(sub_classes + obj_classes)
        keep_img = False
        if prd_idx in prd_classes:
            for vr in imanno:
                if vr['predicate'] == prd_idx:
                    if vr['subject']['category'] == sub_idx:
                        keep_img = True
                        obj_idx = vr['object']['category']
                        obj_name = objects[obj_idx]
                        object_names.append(obj_name)
                        #print(f'object: {obj_name}')
        if keep_img:
            images_with_target.append(imname)
            annos_with_target.append(imanno)

    distinct_object_names = list(set(object_names))
    
    return images_with_target, annos_with_target, distinct_object_names

#%%

def get_images_with_target_vr_B(sub_name, prd_name, obj_name, 
                                img_names, anno, objects, predicates):
    '''
    Find images with a visual relationship that uses a given target
    subject, predicate and object.
    '''
    sub_idx = objects.index(sub_name)
    prd_idx = predicates.index(prd_name)
    obj_idx = objects.index(obj_name)

    images_with_target = []
    annos_with_target = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname].copy()
        sub_classes, prd_classes, obj_classes = get_object_classes_and_predicates(imanno)
        keep_img = False
        if prd_idx in prd_classes:
            for vr in imanno:
                if vr['predicate'] == prd_idx:
                    if vr['subject']['category'] == sub_idx:
                        if vr['object']['category'] == obj_idx:
                            keep_img = True
        if keep_img:
            images_with_target.append(imname)
            annos_with_target.append(imanno)
 
    return images_with_target, annos_with_target

#%%

def get_images_with_target_vr_C(sub_name, prd_name, 
                                img_names, anno, objects, predicates):
    '''
    Find images with a visual relationship that uses a given predicate and
    whose subject is NOT a given object class.
    '''
    sub_idx = objects.index(sub_name)
    prd_idx = predicates.index(prd_name)
    #print(sub_name, sub_idx)
    #print(prd_name, prd_idx)

    images_with_target = []
    annos_with_target = []

    for idx, imname in enumerate(img_names):
        imanno = anno[imname].copy()
        sub_classes, prd_classes, obj_classes = get_object_classes_and_predicates(imanno)
        keep_img = False
        if prd_idx in prd_classes:
            for vr in imanno:
                if vr['predicate'] == prd_idx:
                    if vr['subject']['category'] != sub_idx:
                        keep_img = True
                        #print(vr['subject']['category'])
                        #obj_idx = vr['object']['category']
                        #obj_name = objects[obj_idx]
                        #print(f'object: {obj_name}')
             
            if keep_img:
                images_with_target.append(imname)
                annos_with_target.append(imanno)
        
    return images_with_target, annos_with_target

#%%

def get_images_with_target_vr_D(prd_name, obj_name, 
                                img_names, anno, objects, predicates):
    '''
    Find images with a visual relationship that uses a given target
    predicate and object. Return the images/annos and the set of distinct
    object classes used in the 'subject' of the visual relationship.
    '''

    prd_idx = predicates.index(prd_name)  
    obj_idx = objects.index(obj_name)

    images_with_target = []
    annos_with_target = []
    subject_names = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname].copy()
        sub_classes, prd_classes, obj_classes = get_object_classes_and_predicates(imanno)
        keep_img = False
        if prd_idx in prd_classes:
            for vr in imanno:
                if vr['predicate'] == prd_idx:
                    if vr['object']['category'] == obj_idx:
                        keep_img = True
                        sub_idx = vr['subject']['category']
                        sub_name = objects[sub_idx]
                        subject_names.append(sub_name)
        if keep_img:
            images_with_target.append(imname)
            annos_with_target.append(imanno)

    distinct_subject_names = list(set(subject_names))
    
    return images_with_target, annos_with_target, distinct_subject_names


#%%

def get_images_with_target_vr_E(sub_name, obj_name, 
                                img_names, anno, objects, predicates):
    '''
    Find images with a visual relationship that refers to a specific
    'subject' and 'object' object class. Return the images/annos and the 
    set of distinct predictes used in the result set of visual relationships.
    '''

    sub_idx = objects.index(sub_name)  
    obj_idx = objects.index(obj_name)

    images_with_target = []
    annos_with_target = []
    predicate_names = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname].copy()
        sub_classes, prd_classes, obj_classes = get_object_classes_and_predicates(imanno)
        keep_img = False
        if sub_idx in sub_classes:
            for vr in imanno:
                if vr['subject']['category'] == sub_idx:
                    if vr['object']['category'] == obj_idx:
                        keep_img = True
                        prd_idx = vr['predicate']
                        prd_name = predicates[prd_idx]
                        predicate_names.append(prd_name)
        if keep_img:
            images_with_target.append(imname)
            annos_with_target.append(imanno)

    distinct_predicate_names = list(set(predicate_names))
    
    return images_with_target, annos_with_target, distinct_predicate_names


#%%

def check_if_vrs_are_duplicates(vr1, vr2):
    '''
    Check whether two visual relationships (vrs) are identical (ie 
    duplicates of one another).
    '''
    
    duplicates = False
    
    if ((vr1['subject']['category'] == vr2['subject']['category'])
        and
        (vr1['subject']['bbox'] == vr2['subject']['bbox'])
        and
        (vr1['predicate'] == vr2['predicate'])
        and
        (vr1['object']['category'] == vr2['object']['category'])
        and
        (vr1['object']['bbox'] == vr2['object']['bbox'])):
        duplicates = True

    return duplicates


#%%

def get_images_with_target_vr_F(img_names, anno): 
                                
    '''
    Find images with two visual relationships whose 'subject' and 'object'
    bounding boxes likely need to be swapped.
    
    That is, find images whose annotations contain pairs of visual 
    relationships (vrs) that appear to be intended to be inverses of one 
    another, but where the inversion is flawed because the bounding boxes 
    of the two respective objects ('subject' and 'object'), on one of the two
    visual relationships in the pair, are in the wrong positions and need 
    to be swapped.

    example:
    (person, wear, hat)    (hat, on, person)
    (bb_p)       (bb_h)    (bb_p)     (bb_h)
    
    CAUTION: This function does NOT report on cases where the conditions above
    are met and where the 'subject' and 'object' object classes are themselves
    identical.  Such cases (a) MAY be flawed inverses of one another (and
    require fixing by swapping the bboxes), but they (b) MAY also be perfectly
    legitimate.
    
    The problem here is that we cannot distinguish between cases (a) and (b)
    because we do not have a reliable way to distinguish between pairs of
    predicates that are effective inverses for one another and which pairs
    of predicates are not.
    
    example: consider these 3 vrs ...
    2 ('giraffe', 'in the front of', 'giraffe')
    6 ('giraffe', 'taller than', 'giraffe')
    8 ('giraffe', 'behind', 'giraffe')
    
    If vrs (2) and (6) satisfy the conditions above they are NOT flawed
    inverses of one another because 'taller than' is not an inverse of
    'in the front of'; (6) is simply a vr using a different predicate than
    (2) to express a relationship between the same two objects
    
    However, if vrs (2) and (8) satisfy the conditions above they are 
    highly likely to be flawed inverses of one another because 'behind'
    is a likely predicate to choose if one wishes to express the inverse
    of 'in the front of'; in this case, the bboxes for the two objects in
    (8) should most likely be swapped.
    
    The upshot is that this function cannot identify *all possible cases*
    where the conditions above are satisfied.  If the conditions above
    are satisfied but the 'subject' and 'object' object classes are
    identical, we may have found a problem, but we may not have. Rather
    than report false positives, this function simply does not report, 
    meaning some problematic cases may 'slip through the cracks' and go
    unreported.
    '''

    images_with_target = []
    annos_with_target = []
    vr_pair_indices = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname].copy()
        keep_img = False
        for idx1, vr1 in enumerate(imanno):
            for idx2, vr2 in enumerate(imanno):
                if ((vr1['subject']['category'] == vr2['object']['category'])
                      and
                    (vr1['object']['category'] == vr2['subject']['category'])
                      and 
                    (vr1['subject']['category'] != vr1['object']['category'])
                      and
                    (vr1['subject']['bbox'] == vr2['subject']['bbox'])
                      and
                    (vr1['object']['bbox'] == vr2['object']['bbox'])
                      and
                    (idx1 != idx2)):
                    duplicates = check_if_vrs_are_duplicates(vr1, vr2)
                    if not duplicates:                       
                        keep_img = True
                        break
            if keep_img:
                break
    
        if keep_img:
            images_with_target.append(imname)
            annos_with_target.append(imanno)
            vr_pair_indices.append([idx1, idx2])

    return images_with_target, annos_with_target, vr_pair_indices


#%%

def get_images_with_duplicate_vrs(img_names, anno):                          
    '''
    Find images whose annotations contain at least one pair of duplicate
    visual relationships.

    example:
    (person, wear, hat)    (person, wear, hat)
    (bb_p)       (bb_h)    (bb_p)     (bb_h)
    '''

    images_with_target = []
    annos_with_target = []
    vr_pair_indices = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname]
        keep_img = False
        for idx1, vr1 in enumerate(imanno):
            for idx2, vr2 in enumerate(imanno):
                if idx1 != idx2:
                    duplicates = check_if_vrs_are_duplicates(vr1, vr2)
                    if duplicates:
                        keep_img = True
                        break
            
            if keep_img:
                break
    
        if keep_img:
            images_with_target.append(imname)
            annos_with_target.append(imanno)
            vr_pair_indices.append([idx1, idx2])

    return images_with_target, annos_with_target, vr_pair_indices


#%%

def get_images_with_vrs_with_identical_bboxes(img_names, anno):                          
    '''
    Find images whose annotations contain visual relationships (vrs)
    where the 'subject' and 'object' bboxes are identical.
    '''

    images_with_target = []
    annos_with_target = []
    vr_indices = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname]
        keep_img = False
        vr_idxs = []
        for idx2, vr in enumerate(imanno):
            if vr['subject']['bbox'] == vr['object']['bbox']:
                keep_img = True
                vr_idxs.append(idx2)
        
        if keep_img:
            images_with_target.append(imname)
            annos_with_target.append(imanno)
            vr_indices.append(vr_idxs)

    return images_with_target, annos_with_target, vr_indices

#%%

def get_images_with_bboxes_having_multiple_object_classes(img_names, anno):
    '''
    Find images whose annotations contain a bbox that has been assigned
    more than one object class.
    '''
    
    images_with_target = []
    vr_indices_with_problem_bbox = []
    bboxes_with_multiple_classes = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname]
        try:
            _ = get_bboxes_and_object_classes(imname, imanno)
        except BboxError as e:
            images_with_target.append(imname)
            vr_indices_with_problem_bbox.append(e.vridx)
            bboxes_with_multiple_classes.append(e.bbox)
    
    return images_with_target, vr_indices_with_problem_bbox, bboxes_with_multiple_classes
    
#%%

def get_images_with_degenerate_bboxes(img_names, anno):
    '''
    Find images that have degenerate bboxes.  A degenerate bbox is
    one where:
        NOT (ymin < ymax)
        or
        NOT (xmin < xmax)
    '''
    
    images_with_target = []
    vr_indices_with_bad_bbox = []
    
    for idx, imname in enumerate(img_names): 
        imanno = anno[imname]
        vr_idxs = []
        for idx2, vr in enumerate(imanno):
            vrok = True
            b = vr['subject']['bbox']
            if (not b[0] < b[1]) or (not b[2] < b[3]):
                vrok = False
            b = vr['object']['bbox']
            if (not b[0] < b[1]) or (not b[2] < b[3]):
                vrok = False
            if not vrok:
                vr_idxs.append(idx2)
        if len(vr_idxs) > 0:
            images_with_target.append(imname)
            vr_indices_with_bad_bbox.append(vr_idxs)
    
    return images_with_target, vr_indices_with_bad_bbox
    
    
#%% 

def calc_bbox_pair_iou(bb):
    '''
    Calculate the IoU (Intersection over Union) for a pair of bboxes.
    
    The bbox format is assumed to be the format used by the visual
    relationship annotations of the VRD dataset, which is
    [ymin, ymax, xmin, xmax].
    '''
    b1 = bb[0]
    b2 = bb[1]
    
    # calculate intersection area
    x1 = max(b1[2], b2[2])  # max xmin
    y1 = max(b1[0], b2[0])  # max ymin
    x2 = min(b1[3], b2[3])  # min xmax
    y2 = min(b1[1], b2[1])  # min ymax
    intersection_area = max(0, x2 - x1) * max(0, y2 - y1)
    
    # calculate union area
    b1_width = b1[3] - b1[2]
    b1_height = b1[1] - b1[0]
    b1_area = float(b1_width * b1_height)
    b2_width = b2[3] - b2[2]
    b2_height = b2[1] - b2[0]
    b2_area = float(b2_width * b2_height)    
    union_area = b1_area + b2_area - intersection_area
    
    # calculate IoU
    iou = intersection_area / union_area
    
    return iou


#%%

def get_images_with_highly_similar_bboxes(img_names, anno,
                                          lower_threshold,
                                          upper_threshold,
                                          obj_class_same=False):
    '''
    Find images whose visual relationship annotations contain bbox
    specifications that are highly similar to one another. Such cases
    are likely to represent multiple, slightly different bboxes for
    the same object.
    
    We want to identify such cases so we can eliminate them. We wish
    our annotations to utilise one single bbox for identifying each
    distinct object in an image.
    
    Parameters:
        obj_class_same : boolean flag; if True, results are returned
                         only if the pair of bboxes have the same 
                         object class. If False, results are returned
                         only if the pair of bboxes has different
                         object classes.
    '''
    
    images_with_target = []
    image_similar_bbox_pairs = []
    image_similar_bbox_ious = []
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname]
        bboxes_dict = get_bboxes_and_object_classes(imname, imanno)
        bboxes = list(bboxes_dict.keys())
        bbox_classes = list(bboxes_dict.values())
        bbox_class_tuples = list(zip(bboxes, bbox_classes))
        bbox_pairs = itertools.combinations(bbox_class_tuples, 2)
        keep_img = False
        bb_pairs = []
        bb_pair_ious = []
        for pair in bbox_pairs:
            bb1 = pair[0][0]
            bb2 = pair[1][0]
            bb1_cls = pair[0][1]
            bb2_cls = pair[1][1]
            bb_pair = [bb1, bb2]
            iou = calc_bbox_pair_iou(bb_pair)
            if iou > lower_threshold and iou <= upper_threshold:
                save_result = True
                if obj_class_same:
                    if bb1_cls == bb2_cls:
                        pass
                    else:
                        save_result = False
                else:
                    if bb1_cls == bb2_cls:
                        save_result = False
                    else:
                        pass                    
                if save_result:
                    keep_img = True
                    bb_pairs.append(pair)
                    bb_pair_ious.append(round(iou,3))
        if keep_img:
            images_with_target.append(imname)
            image_similar_bbox_pairs.append(bb_pairs)
            image_similar_bbox_ious.append(bb_pair_ious)
         
    return images_with_target, image_similar_bbox_pairs, image_similar_bbox_ious


#%%

def get_images_with_multiple_objects_of_a_given_class(img_names, anno,
                                                      objects,
                                                      obj_class_name):
    '''
    Find images whose visual relationship annotations contain more
    than one instance of an object of a given object class.
    '''
    
    images_with_target = []
    image_bbox_class_tuples = []
    
    obj_class_idx = objects.index(obj_class_name)
    
    for idx, imname in enumerate(img_names):
        imanno = anno[imname]
        bboxes_dict = get_bboxes_and_object_classes(imname, imanno)
        bboxes = list(bboxes_dict.keys())
        bbox_classes = list(bboxes_dict.values())
        bbox_class_tuples = list(zip(bboxes, bbox_classes))
        bb_cls_tuples = []
        for bb_cls_tuple in bbox_class_tuples:
            if bb_cls_tuple[1] == obj_class_idx:
                bb_cls_tuples.append(bb_cls_tuple)

        if len(bb_cls_tuples) > 1:
            images_with_target.append(imname)
            image_bbox_class_tuples.append(bb_cls_tuples)
         
    return images_with_target, image_bbox_class_tuples

#%%

def calc_bbox_pair_inclusion_ratio(bb):
    '''
    Calculate the Inclusion Ratio for a pair of bboxes.
    
    The bbox format is assumed to be the format used by the visual
    relationship annotations of the VRD dataset, which is
    [ymin, ymax, xmin, xmax].
    '''
    b1 = bb[0]  # subject object bbox
    b2 = bb[1]  # object object bbox
    
    # calculate bbox areas
    #b1_width = b1[3] - b1[2]
    #b1_height = b1[1] - b1[0]
    #b1_area = float(b1_width * b1_height)
    b2_width = b2[3] - b2[2]
    b2_height = b2[1] - b2[0]
    b2_area = float(b2_width * b2_height)   

    # calculate bbox intersection area
    x1 = max(b1[2], b2[2])  # max xmin
    y1 = max(b1[0], b2[0])  # max ymin
    x2 = min(b1[3], b2[3])  # min xmax
    y2 = min(b1[1], b2[1])  # min ymax
    intersection_area = max(0, x2 - x1) * max(0, y2 - y1)
      
    # calculate inclusion ratio of b2 within b1
    ir_b2b1 = intersection_area / b2_area
    
    return ir_b2b1


