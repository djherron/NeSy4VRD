#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This script provides comprehensive support for deep analysis of the
VRD images and their associated NeSy4VRD visual relationship annotations.
'''

#%%

import os
import numpy as np
import matplotlib.pyplot as plt

import vrd_utils as vrdu


#%% get the NeSy4VRD visual relationships annotations data

# set path to directory in which the NeSy4VRD annotations files reside
anno_dir = os.path.join('..', 'data', 'annotations')

# get the NeSy4VRD object class names
path = os.path.join(anno_dir, 'nesy4vrd_objects.json')
vrd_objects = vrdu.load_VRD_object_class_names(path)

# get the NeSy4VRD predicate names
path = os.path.join(anno_dir, 'nesy4vrd_predicates.json')
vrd_predicates = vrdu.load_VRD_predicate_names(path)

# get the NeSy4VRD visual relationship annotations
path = os.path.join(anno_dir, 'nesy4vrd_annotations_train.json')
#path = os.path.join(anno_dir, 'nesy4vrd_annotations_test.json')
vrd_anno = vrdu.load_VRD_image_annotations(path)

# get the customised set of VRD (training or test) image names
vrd_img_names = list(vrd_anno.keys())


#%% set path to directory where the VRD images are located

# this is needed so that the functions that display images will know
# where to find them

# note: the image directory you specify here needs to correspond to the 
# type of VR annotations you are loading: training or test

imagedir = 'train_images'   # or 'test_images'
imagedir = os.path.join('..', 'data', imagedir)


#%% analysis X

# Number of image entries in the VR annotations dictionary loaded

#%% X.1

print(f'Number of image entries in annotations dictionary: {len(vrd_img_names)}')

# NeSy4VRD training set VR annotations: 3758
# NeSy4VRD     test set VR annotations:  962


#%%


###########################################################################
#
# Analyses devoted purely to displaying 'specified' images:
# * display image
# * print the visual relationships annotated for the image (either in
#   user-friendly format or raw format)
# * display selected combinations/permuations of bboxes for objects
#   annotated within the visual relationships for the image
#
###########################################################################



#%% analysis X

# Display a particular VRD image with no annotated objects.
# Optionally print all the visual relationship annotations for the image.

#%% X.1 select and display the image

# select the image by index within the list of image names, or
# specify the image name directly
idx = 1298
imname = vrd_img_names[idx]
#imname = '8130671821_5e96dc2bdb_b.jpg'

vrdu.display_image(imname, imagedir)

#%% X.2 print the visual relationships

imanno = vrd_anno[imname]

# print VRs in user-friendly format
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)



#%% analysis X

# Display a particular VRD image and the bounding boxes for the two
# objects involved in one particular annotated visual relationship.
# Optionally print all the annotated visual relationships as well.

#%% X.1 select image

# select the image by index within the list of image names, or
# specify the image name directly
idx = 1298
imname = vrd_img_names[idx]
#imname = '8130671821_5e96dc2bdb_b.jpg'
imanno = vrd_anno[imname]
print(f'image name: {imname}')

#%% X.2 print visual relationships (showing their index numbers)

# print VRs in user-friendly format
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 select VR by index number and display image 

# (note: bbox of subject is bright red; bbox of object is dark red)
vr_idx = 12
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.4 print visual relationships for image in raw format

# the raw visual relationships allow the bbox
for idx, vr in enumerate(imanno):
    print(idx, vr)



#%% analysis X

# Display an image along with the bboxes for all annotated objects
# appearing in any of its VRs.

#%% X.1 select image

# select the image by index within the list of image names, or
# specify the image name directly
idx = 1298
imname = vrd_img_names[idx]
#imname = '8130671821_5e96dc2bdb_b.jpg'
imanno = vrd_anno[imname]
print(f'image name: {imname}')

#%% X.2 display image with all annotated objects

vrdu.display_image_with_all_bboxes(imname, imanno, imagedir)

#%% X.3 show summary info about the annotated objects for the image

bboxes = vrdu.get_bboxes_and_object_classes(imname, imanno)

print(f'number of annotated objects: {len(bboxes)}')

# display the distinct bboxes and their object classes
bboxes2 = [(lab, bb) for bb, lab in bboxes.items()]
sorted_bboxes = sorted(bboxes2)
for lab, bb in sorted_bboxes:
    classname = vrd_objects[lab]
    print(bb, lab, classname) 

#%% X.4 print all VRs in user-friendly form

print('visual relationships:')
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.5 display the image again showing the bboxes for one VR

vr_idx = 5
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.6 print all VRs in raw form

for idx, vr in enumerate(imanno):
    print(idx, vr)



#%% analysis X

# Display an image along with the bboxes for selected VRs only

#%% X.1 select image

# select the image by index within the list of image names, or
# specify the image name directly
idx = 1298
imname = vrd_img_names[idx]
#imname = '8130671821_5e96dc2bdb_b.jpg'
imanno = vrd_anno[imname]
print(f'image name: {imname}')

#%% X.2 display image with bboxes for all objects

vrdu.display_image_with_all_bboxes(imname, imanno, imagedir)

#%% X.3 print all VRs in user-friendly format

vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.4 display image with bboxes for objects in selected VRs

vrs = [0,1,13]
vrdu.display_image_with_selected_vrs(imname, imanno, vrs, imagedir)



#%%


###########################################################################
#
# Analyses devoted to 'searching for' or 'finding' images that have
# annotated visual relationships that satisfy specified conditions or
# search criteria, or visual relationships that 
# 
# Having obtained the result set of images that satisfy the search criteria,
# analyse them by iterating through them at will, displaying the images,
# their visual relationships and the bboxes of the annotated objects.
#
###########################################################################



#%% analysis X

# Find and analyse images whose visual relationships reference a specified
# object class.

#%% X.1 set search criteria and find images that satisfy them

cls_name = 'helmet case' 

res_imgs, res_annos = vrdu.get_images_with_object_class(cls_name,
                                                        vrd_img_names, 
                                                        vrd_anno, 
                                                        vrd_objects, 
                                                        vrd_predicates)

print(f'Number of images found: {len(res_imgs)}')

#%% X.2 select an image by index per the result set

# select the image
idx = 5  
imname = res_imgs[idx]
imanno = res_annos[idx]

# print the visual relationships for the image
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

vr_idx = 9
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.4 print VRs in raw form

# print all of the raw visual relationships so we can see the
# bbox specifications
for idx, vr in enumerate(imanno):
    print(idx, vr)

#%% X.5 within the result set, get all the VRs for the target object class

# get all the visual relationships for a given object class
# (together with the name of the associated image)
vrs_for_cls = vrdu.get_all_relationships_for_object_class(cls_name,
                                                          res_imgs, res_annos,                                                     
                                                          vrd_objects, 
                                                          vrd_predicates)

print(f'number of relationship instances: {len(vrs_for_cls)}')

#%% X.6 print VRs referencing the target object class, and their image names

for i in range(0,24):
    print(vrs_for_cls[i])

#%% X.7 get all VRs for one of the images referencing the object class

imname = '6721496819_b7dd80e497_b.jpg'
imanno = vrd_anno[imname]

print(imname)
# print visual relationships
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)
    
#%% X.8 display the image with for a particular VR

vr_idx = 4
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.9 print VRs for that image in raw form

for idx, vr in enumerate(imanno):
    print(idx, vr)



#%% analysis X

# Find and analyse images whose visual relationships reference a specified
# 'set' of object class.

#%% X.1 find the images

cls_names = ['dog', 'surfboard']

res_imgs, res_annos = vrdu.get_images_with_object_classes(cls_names,
                                                          vrd_img_names, 
                                                          vrd_anno, 
                                                          vrd_objects)

print(f'Number of images found: {len(res_imgs)}')

#%% X.2 select an image by index per the result set

# select image 
idx = 2  
imname = res_imgs[idx]
imanno = res_annos[idx]

# print the visual relationships for the image
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

vr_idx = 9
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.4

# print the raw visual relationships
for idx2, vr in enumerate(imanno):
    print(idx2, vr)



#%% analysis X

# Find and analyse images that have a visual relationship that matches
# the pattern (subject, predicate, X).
# Get the distinct set of object classes used for X.

#%% X.1 find the images and values of X

sub_name = 'teddy bear'
prd_name = 'has'

res_imgs, res_annos, res_objects = vrdu.get_images_with_target_vr_A(sub_name, 
                                                                    prd_name, 
                                                                    vrd_img_names, 
                                                                    vrd_anno, 
                                                                    vrd_objects, 
                                                                    vrd_predicates)

print(f'Number of images with VRs matching the pattern: {len(res_imgs)}')

print(f'Number of distinct object classes for X: {len(res_objects)}')

for obj in res_objects:
    print(obj)

#%% X.2 select an image by index per the result set

idx = 1      
imname = res_imgs[idx]
imanno = res_annos[idx]

# print visual relationships
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

vr_idx = 2
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.4 print all VRs for the image in raw form

for idx2, vr in enumerate(imanno):
    print(idx2, vr)



#%% analysis X

# Find and analyse images that have a visual relationship that matches
# the pattern (X, predicate, object).
# Get the distinct set of object classes used for X.

#%% X.1 find the images and values of X

prd_name = 'on'
obj_name = 'hand'

res_imgs, res_annos, res_subjects = vrdu.get_images_with_target_vr_D(prd_name, 
                                                                     obj_name, 
                                                                     vrd_img_names, 
                                                                     vrd_anno, 
                                                                     vrd_objects, 
                                                                     vrd_predicates)

print(f'Number of images with VRs matching the pattern: {len(res_imgs)}')

print(f'Number of distinct object classes for X: {len(res_subjects)}')

for sub in res_subjects:
    print(sub)

#%% X.2 select an image by index per the result set

idx = 0
imname = res_imgs[idx]
imanno = res_annos[idx]

# print visual relationships
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

vr_idx = 3
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.4 print all VRs for the image in raw form

# print the visual relationships in raw format
for idx2, vr in enumerate(imanno):
    print(idx2, vr)



#%% analysis X

# Find and analyse images that have a visual relationship that matches
# the pattern (subject, X, object).
# Get the distinct set of object classes used for X.

#%% X.1 find the images matching the pattern and the values of X

sub_name = 'bike'
obj_name = 'person'

res_imgs, res_annos, res_pred = vrdu.get_images_with_target_vr_E(sub_name, 
                                                                 obj_name, 
                                                                 vrd_img_names, 
                                                                 vrd_anno, 
                                                                 vrd_objects, 
                                                                 vrd_predicates)

print(f'Number of images with VRs matching the pattern: {len(res_imgs)}')

print(f'Number of distinct predicates for X: {len(res_pred)}')

for prd in res_pred:
    print(prd)

#%% X.2 select an image by index per the result set

idx = 0      
imname = res_imgs[idx]
imanno = res_annos[idx]

# print visual relationships
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

vr_idx = 5
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)



#%% analysis X

# Analyse images associated with a given visual relationship
# (subject, predicate, object)

#%% X.1 

# Find and analyse images that have a visual relationship that matches
# the pattern (subject, predicate, object).

#%% X.1 find the images with VRs matching the pattern

sub_name = 'person'
prd_name = 'under'
obj_name = 'umbrella'

res_imgs, res_annos = vrdu.get_images_with_target_vr_B(sub_name,
                                                       prd_name,
                                                       obj_name,
                                                       vrd_img_names,
                                                       vrd_anno, 
                                                       vrd_objects,
                                                       vrd_predicates)

print(f'Number of images with VRs matching the pattern: {len(res_imgs)}')

#%% X.2 select an image by index per the result set

idx = 0      
imname = res_imgs[idx]
imanno = res_annos[idx]

# print visual relationships
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

vr_idx = 5
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)



#%% analysis X

# Analyse the images that have a visual relationship annotation that
# uses a given predicate

# Find and analyse images that have a visual relationship that matches
# the pattern (X, predicate, Y) --- ie that use a specified predicate.

#%% X.1 find the images with VRs matching the pattern

prd_name = 'inside'

prd_idx = vrd_predicates.index(prd_name)

images_to_review = []
annos_to_review = []
for idx, imname in enumerate(vrd_img_names):
    imanno = vrd_anno[imname]
    sub_classes, prd_classes, obj_classes = vrdu.get_object_classes_and_predicates(imanno)
    if prd_idx in prd_classes:
        images_to_review.append(imname)
        annos_to_review.append(imanno)

print(f'Number of images: {len(images_to_review)}')

#%% X.2 select an image by index per the result set

idx = 1
imname = images_to_review[idx]
imanno = annos_to_review[idx]

# print visual relationships
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

# display image with bboxes for a particular visual relationship
vr_idx = 7
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.4 get all VRs for the given predicate

vrs_for_prd = vrdu.get_all_relationships_for_predicate(prd_name,
                                                       images_to_review,
                                                       annos_to_review,
                                                       vrd_objects,
                                                       vrd_predicates)

print(f"Number of VR instances with predicate '{prd_name}': {len(vrs_for_prd)}")

#%% X.5 get the set of distinct VR types for the given predicate & count instances

vrs = []
vr_counts = []
for im_vr_pair in vrs_for_prd:
    vr = im_vr_pair[1]
    if vr in vrs:
        vr_idx = vrs.index(vr)
        vr_counts[vr_idx] += 1
    else:
        vrs.append(vr)
        vr_counts.append(1)

print(f"Number of distinct VR types with predicate '{prd_name}': {len(vrs)}")

#%% X.6 print the distinct VR types for the predicate and their instance counts

for idx, vr in enumerate(vrs):
    print(vr, vr_counts[idx])


# print each of the distinct vr instances for the given predicate
for idx, vr in enumerate(vrs):
    print(vr, vr_counts[idx])

#%% X.7 determine the distinct 'subject' and 'object' object classes

distinct_subjects = []
distinct_objects = []
for vr in vrs:
    if not vr[0] in distinct_subjects:
        distinct_subjects.append(vr[0])
    if not vr[2] in distinct_objects:
        distinct_objects.append(vr[2])

print(f'Number of distinct subjects: {len(distinct_subjects)}')
print()
print(f'Number of distinct objects: {len(distinct_objects)}')

#%% X.8 print the distinct 'subject' object classes

print(f'distinct subjects: {distinct_subjects}')

#%% X.9 print the distinct 'object' object classes

print(f'distinct objects: {distinct_objects}')



#%% analysis X

# Find and analyse images that have a visual relationship that uses a
# specified predicate but whose 'subject' is NOT of a particular object class
# (IE search for pattern (not subject, predicate, X))

#%% X.1 find the images with VRs matching the pattern

sub_name = 'person'
prd_name = 'carry'
res_imgs, res_annos = vrdu.get_images_with_target_vr_C(sub_name, prd_name,
                                                       vrd_img_names, 
                                                       vrd_anno,
                                                       vrd_objects, 
                                                       vrd_predicates)

print(f'Number of images: {len(res_imgs)}')

#%% X.2 select an image by index per the result set

idx = 1
imname = res_imgs[idx]
imanno = res_annos[idx]

# print visual relationships
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.3 display image for a particular VR

# display image with bboxes for a particular visual relationship
vr_idx = 6
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.4 get the distinct object classes appearing as the 'subject'

prd_idx = vrd_predicates.index(prd_name)

sub_cls_idxs = []
for imanno in res_annos:
    for vr in imanno:
        if vr['predicate'] == prd_idx:
            sub_cls_idxs.append(vr['subject']['category'])

sub_cls_idxs = list(set(sub_cls_idxs))

print(f"Subject object classes other than: '{sub_name}'")
for idx in sub_cls_idxs:
    sub_name2 = vrd_objects[idx]
    print(sub_name2)



#%%


###########################################################################
#
# Miscellaneous analyses
#
###########################################################################



#%% analysis X

# Analyse the predicates that are used with a given object class

#%% X.1 get all distinct predicates used with a specified object class

cls_name = 'face'

res_prd = vrdu.get_distinct_predicates_for_object_class(cls_name,
                                                        vrd_img_names, 
                                                        vrd_anno,
                                                        vrd_objects, 
                                                        vrd_predicates)

print(f'Number of distinct predicates: {len(res_prd)}')
print()

# print the distinct predicates
for prd in res_prd:
    print(prd)



#%% analysis X

# Get the distinct set of bboxes and their object classes for a given image

#%% X.1

imname = '8108277436_f0c3089030_b.jpg'
imanno = vrd_anno[imname]

bboxes = vrdu.get_bboxes_and_object_classes(imname, imanno)

print(imname)
print(f'Nr of unique objects (bboxes): {len(bboxes)}')

# print the unique objects (bboxes) and their assigned object class indices
print()
for k, v in bboxes.items():
    print(k, v)

#%% X.2 print the VRs of the image in raw format

for idx, vr in enumerate(imanno):
    print(idx, vr)



#%% analysis X

# Count the total number of visual relationships across all images

#%% X.1

cnt = 0
for idx, imname in enumerate(vrd_img_names):
    imanno = vrd_anno[imname]
    cnt += len(imanno)
    
print(f'Total number of visual relationships: {cnt}')



#%%


####################################################
#
# Distributional analyses
#
####################################################



#%% analysis X 

# Analyse the distribution of the number of visual relationship
# annotations per image

#%% X.1 calculate distribution data and show summary statistics

n_imgs = len(vrd_img_names)
n_vrs_per_img = np.zeros(n_imgs)

for idx, imname in enumerate(vrd_img_names):
    imanno = vrd_anno[imname]
    n_vrs_per_img[idx] = len(imanno)

max_vrs_per_img = int(np.max(n_vrs_per_img))

print(f'Max number of vrs per image: {max_vrs_per_img}')

print(f'Mean number of vrs per image: {np.mean(n_vrs_per_img)}')

print(f'Median number of vrs per image: {np.median(n_vrs_per_img)}')

print(f'Min number of vrs per image: {int(np.min(n_vrs_per_img))}')

#%% X.2 plot distribution histogram

bins = [idx for idx in range(max_vrs_per_img+1)]

plt.hist(n_vrs_per_img, bins)
plt.title('Distribution of number of vrs per image')

#%% X.3 find the images with a target number of VRs

target_num = 1

target_images = []
for imname in vrd_img_names:
    imanno = vrd_anno[imname]
    if len(imanno) == target_num:
        target_images.append(imname)

print(f'Nr images with {target_num} VRs: {len(target_images)}')

#%% X.4 select an image by index per the result set

idx = 0
imname = target_images[idx]
imanno = vrd_anno[imname]

# print the visual relationships for the image
print(imname)
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.5 display image for a particular VR

vr_idx = 0
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)



#%% analysis X

# Analyse the distribution of the number of distinct object classes
# referenced in the annotations of each image

#%% X.1 calculate distribution data and show summary statistics

n_imgs = len(vrd_img_names)
n_obj_cls_per_img = np.zeros(n_imgs)
for idx, imname in enumerate(vrd_img_names):
    imanno = vrd_anno[imname]
    sub_classes, prd_classes, obj_classes = vrdu.get_object_classes_and_predicates(imanno)
    all_classes = set(sub_classes + obj_classes)
    n_obj_cls_per_img[idx] = len(all_classes)

max_obj_cls_per_img = int(np.max(n_obj_cls_per_img))

print(f'Max number of object classes per image: {max_obj_cls_per_img}')

print(f'Mean number of object classes per image: {np.mean(n_obj_cls_per_img)}')

print(f'Median number of object classes per image: {np.median(n_obj_cls_per_img)}')

print(f'Min number of object classes per image: {int(np.min(n_obj_cls_per_img))}')

#%% X.2 plot distribution histogram

bins = [idx for idx in range(max_obj_cls_per_img+1)]

plt.hist(n_obj_cls_per_img, bins)
plt.title('Distribution of number of object classes per image')


#%% analysis X

# Analyse the distribution of the number of predicates referenced in the
# the annotations of each image

#%% X.1 calculate distribution data and show summary statistics

n_pred_per_img = []
for imname in vrd_img_names:
    imanno = vrd_anno[imname]
    sub_classes, prd_classes, obj_classes = vrdu.get_object_classes_and_predicates(imanno)
    n_pred_per_img.append(len(prd_classes))

max_pred_per_img = int(np.max(n_pred_per_img))

print(f'Max number of predicates per image: {max_pred_per_img}')

print(f'Mean number of predicates per image: {np.mean(n_pred_per_img)}')

print(f'Median number of predicates per image: {np.median(n_pred_per_img)}')

print(f'Min number of predicates per image: {int(np.min(n_pred_per_img))}')

#%% X.2 plot the distribution histogram

bins = [idx for idx in range(max_pred_per_img+1)]

plt.hist(n_pred_per_img, bins)
plt.title('Distribution of number of predicates per image')


#%% Analysis X

# Analyse the distribution of image sizes (W x H)

#%% X.1 gather the sizes of all the images

### CAUTION: this takes a few moments to run on the full training set annotations

img_sizes = []
for imname in vrd_img_names:
    size = vrdu.get_image_size(imname, imagedir)
    img_sizes.append(size)

#%% X.2 find the set of distinct image sizes

img_sizes_set = set(img_sizes)
print(f'Number of distinct image sizes: {len(img_sizes_set)}')

#%% X.3 find the min/max extremes of the image sizes

min_width = 5000
min_height = 5000
max_width = 0
max_height = 0
min_size = [5000,5000]
max_size = [0,0]
for size in img_sizes_set:
    if size[0] > max_width:
        max_width = size[0]
    if size[1] > max_height:
        max_height = size[1]
    if size[0] < min_width:
        min_width = size[0]
    if size[1] < min_height:
        min_height = size[1]
    if size[0] >= max_size[0] and size[1] >= max_size[1]:
        max_size[0] = size[0]
        max_size[1] = size[1]
    if size[0] <= min_size[0] and size[1] <= min_size[1]:
        min_size[0] = size[0]
        min_size[1] = size[1]

print(f'min width: {min_width}') 
print(f'min height: {min_height}') 
print(f'max width: {max_width}') 
print(f'max height: {max_height}') 
print(f'max size (W x H): {max_size}') 
print(f'min size (W x H): {min_size}') 



#%%


####################################################
#
# Quality verification analyses
#
####################################################



#%% analysis X

# Find images with zero annotated objects (which equates to zero VRs)

# NOTE: In the NeSy4VRD visual relationship annotations, the number of such
# images should be zero.

#%% X.1 find the images

images_with_no_objects = []
for imname in vrd_img_names:
    imanno = vrd_anno[imname]
    sub_classes, prd_classes, obj_classes = vrdu.get_object_classes_and_predicates(imanno)
    all_classes = set(sub_classes + obj_classes)
    if len(all_classes) == 0:
      images_with_no_objects.append(imname)

print(f'Number of images with 0 annotated objects: {len(images_with_no_objects)}')
# should be 0



#%% analysis X

# Find images whose annotations contain pairs of visual relationships
# that appear to be intended to be inverses of one another but where the
# inversion is flawed because the bounding boxes of the two respective
# objects ('subject' and 'object') are in the wrong positions and need to
# be swapped.
#
# example:
# (person, wear, hat)    (hat, on, person)
# (bbox1)     (bbox2)    (bbox1)   (bbox2)
#

#%% X.1 find the images

res_imgs, res_annos, res_indices = vrdu.get_images_with_target_vr_F(vrd_img_names,
                                                                    vrd_anno)

print(f'number of images: {len(res_imgs)}')
# should be 0



#%% analysis X

# Find images whose annotations contain exact duplicate visual relationships

#%% X.1 find the images

res_imgs, res_annos, res_indices = vrdu.get_images_with_duplicate_vrs(vrd_img_names,
                                                                      vrd_anno)

print(f'Number of images: {len(res_imgs)}')
# should be 0



#%% analysis X

# Find the images with a VR where the 'subject' and 'object' bboxes
# are identical

#%% X.1 find the images

res = vrdu.get_images_with_vrs_with_identical_bboxes(vrd_img_names,
                                                     vrd_anno)

res_imgs, res_annos, res_indices = res

print(f'Number of images: {len(res_imgs)}')
# should be 0

vr_cnt = 0
for vr_indices in res_indices:
    vr_cnt += len(vr_indices)

print(f"Number of VRs: {vr_cnt}")
# should be 0



#%% analysis X

# Find all images that have a bbox that has been assigned multiple
# different object classes.

#%% X.1 find the images

res3 = vrdu.get_images_with_bboxes_having_multiple_object_classes(vrd_img_names,
                                                                  vrd_anno) 
                                   
res_imgs, res_vr_indices_with_problem_bbox, res_problem_bboxes = res3

print(f'Number of images: {len(res_imgs)}')
# should be 0



#%% analysis X

# Find images with degenerate bounding boxes.

# All bboxes should have positive height and width.

# Bbox format is: [ymin, ymax, xmin, xmax]
# So we should have: ymin < ymax  and  xmin < xmax

#%% X.1 find the images

res = vrdu.get_images_with_degenerate_bboxes(vrd_img_names, vrd_anno)
res_imgs, res_vr_idxs = res

print(f'Number of images with degenerate bboxes: {len(res_imgs)}')
# should be 0



#%% analysis X

# Find images whose visual relationship annotations contain bbox
# specifications that are highly similar to one another (near duplicates).
# That is, find images with two object bboxes where their IoU 
# (intersection over union) is within a specified threshold bound.

#%% Special notes:

# Note re parameter 'obj_class_same':
#
# If obj_class_same=True, results are returned only if an image has two
# object bboxes where the IoU is between the two thresholds AND the
# object classes of the two bboxes are THE SAME.
#
# If obj_class_same=False, results are returned ONLY IF an image has two
# object bboxes where the IoU is between the two thresholds AND the
# object classes of the two bboxes are DIFFERENT.
#
# So the result sets returned in the two scenarios are mutually exclusive
# and represent subtly different potential quality shortcomings.
#
# If obj_class_same=True, images in the result set may contain near
# duplicate bboxes localising the same object and which are classified as
# belonging to the same object class.
#
# If obj_class_same=False, images in the result set may contain near
# duplicate bboxes localising the same object but which are classified as
# belonging to different object classes.

# Note: if the result set is non-empty, this isn't necessarily evidence of
# problems. One needs to display the images and analyse the objects and
# visual relationships to determine if there are indeed problems that need 
# fixing.  Everything may be fine.

# Note: the analysis and customisation performed in the preparation of the
# NeSy4VRD visual relationship annotations was very thorough with respect to
# this 'near duplicate' quality issue.  The NeSy4VRD visual relationship
# annotations are themselves very clean in this regard.  This functionality
# for finding cases of unintended 'near duplicate' bboxes is provided for
# the benefit of others who may choose to customise the NeSy4VRD visual
# relationship annotations further for themselves and may wish to have this
# quality checking functionality available for their use.

#%% X.1 find the images

lower_iou_thresh = 0.90
upper_iou_thresh = 1.00
res = vrdu.get_images_with_highly_similar_bboxes(vrd_img_names,
                                                 vrd_anno,
                                                 lower_iou_thresh,
                                                 upper_iou_thresh,
                                                 obj_class_same=False)

res_imgs, res_imgs_similar_bboxes, res_imgs_similar_bbox_ious = res

print(f'Number of images found: {len(res_imgs)}')

#%% X.2 select an image for analysis

idx = 5  
imname = res_imgs[idx]
imanno = vrd_anno[imname]

# display image with bboxes for all annotated objects
print(f'image name: {imname}')
vrdu.display_image_with_all_bboxes(imname, imanno, imagedir)

print()
print('similar bboxes and their IoUs:')
sim_bboxes = res_imgs_similar_bboxes[idx]
sim_bbox_ious = res_imgs_similar_bbox_ious[idx]
for sim_bbox, iou in zip(sim_bboxes, sim_bbox_ious):
    print(sim_bbox, iou)

# get the unique set of bboxes and their object classes for a given image
bboxes = vrdu.get_bboxes_and_object_classes(imname, imanno)
print()
print(f"the bboxes for the image's {len(bboxes)} objects ...")
for k, v in bboxes.items():
    className = vrd_objects[v]
    print(f'bbox: {k}, class: {v} {className}')

#%% X.3 select a pair of similar bboxes from the results for that image

# remember: bbox format is [ymin, ymax, xmin, xmax]

# for a given pair of similar bboxes, find the vrs that involve one
# or other of the two bboxes
idx2 = 0
b1 = list(sim_bboxes[idx2][0][0])
b2 = list(sim_bboxes[idx2][1][0])
vrs_with_b1 = []
vrs_with_b2 = []
for idx3, vr in enumerate(imanno):
    if (vr['subject']['bbox'] == b1 or vr['object']['bbox'] == b1):
        vrs_with_b1.append(idx3)
    if (vr['subject']['bbox'] == b2 or vr['object']['bbox'] == b2):
        vrs_with_b2.append(idx3)        

# get the visual relationships in user-friendly format
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)

# display the vrs with bbox b1
print()
print(f'VRs involving box {b1} ...\n')
for idx3, vr in enumerate(imanno):
    if idx3 in vrs_with_b1:
        print(idx3, vrs[idx3])
        print(idx3, vr)
        print()

# display the vrs with bbox b2
print()
print(f'VRs involving box {b2} ...\n')
for idx3, vr in enumerate(imanno):
    if idx3 in vrs_with_b2:
        print(idx3, vrs[idx3])
        print(idx3, vr)
        print()

#%% X.4 print the VRs for the image in user-friendly form

print('visual relationships:')
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx, vr in enumerate(vrs):
    print(idx, vr)

#%% X.5 display image for a particular VR

vr_idx = 0
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.6 print the VRs for the image in raw form

for idx, vr in enumerate(imanno):
    print(idx, vr)



#%% analysis X

# Find the images that have more than 1 object of a given object class.
#
# For some object classes, having more than 1 instance of that object class
# in an image may be suspicious and warrant investigation. This issue
# applies particularly to 'stuff' object classes, like 'sky', 'trees', 
# 'mountain', 'grass', 'street'

#%% X.1

obj_class_name = 'trees'

res = vrdu.get_images_with_multiple_objects_of_a_given_class(vrd_img_names,
                                                             vrd_anno,
                                                             vrd_objects,
                                                             obj_class_name)

res_imgs, res_bbox_class_tuples = res

print(f'Number of images: {len(res_imgs)}')

#%% X.2 select an image for analysis

idx = 2 
imname = res_imgs[idx]
imanno = vrd_anno[imname]

# display image with bboxes for all annotated objects
print(f'image name: {imname}')
vrdu.display_image_with_all_bboxes(imname, imanno, imagedir)

print()
print(f'bboxes for object class {obj_class_name}:')
bbox_class_tuples = res_bbox_class_tuples[idx]
for bb_cls_tuple in bbox_class_tuples:
    print(bb_cls_tuple)

#%% X.3 print VRs in friendly form

print('visual relationships')
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx2, vr in enumerate(vrs):
    print(idx2, vr)

#%% X.4 display image for a particular VR

# display image with the subject/object bboxes for a particular vr
vr_idx = 2
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.5 print VRs in raw format

for idx2, vr in enumerate(imanno):
    print(idx2, vr)



#%% analysis X

# Find images with annotations using a specific 'subject' object class
# and predicate.  Amongst the result set, find the images where the
# 'inclusion ratio' between the 'object' bbox and 'subject' bbox satisfies
# a specified condition.

# (person, wear, X) 
# (person, has, X)  
# (person, in, X)    
# (person, with, X) 
# (person, on, X) 
# or  
# (X, on, person)

# Note: This analysis can be used to catch scenarios such as the pattern
# (person, wear, X) or (X, on, person) but where the bbox for X is NOT 
# substantially within the bbox for the person. IE this analysis can be used 
# to identify cases where X is being worn by a different person. Cases like
# this are outright errors in visual relationship construction and will
# seriously hamper visual relationship detection.

#%% X.1a find the images with VRs that match the pattern

sub_name = 'person'
prd_name = 'on'

res_imgs, res_annos, res_objects = vrdu.get_images_with_target_vr_A(sub_name, 
                                                                    prd_name, 
                                                                    vrd_img_names, 
                                                                    vrd_anno, 
                                                                    vrd_objects, 
                                                                    vrd_predicates)

print(f'Number of images with target subject & predicate: {len(res_imgs)}')

print(f'Number of distinct objects involved: {len(res_objects)}')

for obj in res_objects:
    print(obj)

# NOTE: for these analyses, we typically want to use 
# parameter 'obb_within_sbb = True' below,
# so we can calculate the inclusion ratio of the object bbox (obb) within
# the subject bbox (sbb)

#%% X.1b

prd_name = 'on'
obj_name = 'person'

res_imgs, res_annos, res_subjects = vrdu.get_images_with_target_vr_D(prd_name, 
                                                                     obj_name, 
                                                                     vrd_img_names, 
                                                                     vrd_anno, 
                                                                     vrd_objects, 
                                                                     vrd_predicates)

print(f'Number of images with target predicate & object: {len(res_imgs)}')

print(f'Number of distinct subjects involved: {len(res_subjects)}')

for sub in res_subjects:
    print(sub)

# NOTE: for these analyses, we typically want to use 
# parameter 'obb_within_sbb = False' below,
# so we can calculate the inclusion ratio of the subject bbox (sbb) within
# the object bbox (obb)

#%% X.2 calculate the inclusion ratios and find images with problem VRs

# set these flags depending on the type of analysis being undertaken;
# they should always have opposite settings
sub_prd_analysis = True
prd_obj_analysis = False

# set to True if we want to calculate the inclusion ratio of the object
# bbox (obb) within the subject bbox (sbb); otherwise, if we want the
# inclusion ratio of the subject bbox (sbb) within the object bbox (obb),
# set to False
obb_within_sbb = True

# set inclusion ratio threshold
threshold = 0.005

images_with_target = []
image_vrs_with_problem = []
image_vrs_with_problem_incl_ratios = []

for idx, imanno in enumerate(res_annos):
    
    vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
    vrs_with_problem = []
    vrs_with_problem_incl_ratios = []
    
    for idx2, vr in enumerate(vrs):
        process_vr = False
        if sub_prd_analysis:
            if vr[0] == sub_name and vr[1] == prd_name:
                process_vr = True
        elif prd_obj_analysis:
            if vr[1] == prd_name and vr[2] == obj_name:
                process_vr = True
        else:
            raise ValueError('analysis type flags not set properly')
        if process_vr:
            sbb = imanno[idx2]['subject']['bbox']
            obb = imanno[idx2]['object']['bbox']
            if obb_within_sbb:
                bbpair = [sbb, obb]
            else:
                bbpair = [obb, sbb]
            incl_ratio = vrdu.calc_bbox_pair_inclusion_ratio(bbpair)
            incl_ratio = round(incl_ratio, 3)
            if incl_ratio < threshold:
                vrs_with_problem.append(idx2)
                vrs_with_problem_incl_ratios.append(incl_ratio)
    
    if len(vrs_with_problem) > 0:
        imname = res_imgs[idx]
        images_with_target.append(imname)
        image_vrs_with_problem.append(vrs_with_problem)
        image_vrs_with_problem_incl_ratios.append(vrs_with_problem_incl_ratios)

print(f'Number of images with problem VRs: {len(images_with_target)}')

#%% X.3 select an image for analysis

idx = 6
imname = images_with_target[idx]
imanno = vrd_anno[imname]

# display image with bboxes for all annotated objects
print(f'image name: {imname}')
print(f'indices of problem vrs: {image_vrs_with_problem[idx]}')
print(f'incl_ratios of problem vrs: {image_vrs_with_problem_incl_ratios[idx]}')
vrdu.display_image_with_all_bboxes(imname, imanno)

#%% X.4 print the VRs in friendly format

print('visual relationships:')
vrs = vrdu.get_visual_relationships(imanno, vrd_objects, vrd_predicates)
for idx2, vr in enumerate(vrs):
    print(idx2, vr)

#%% X.5 display the image for a particular VR

vr_idx = 1
vr = imanno[vr_idx]
vrdu.display_image_with_bboxes_for_vr(imname, vr, imagedir)

#%% X.6 print the VRs in raw format

for idx2, vr in enumerate(imanno):
    print(idx2, vr)



