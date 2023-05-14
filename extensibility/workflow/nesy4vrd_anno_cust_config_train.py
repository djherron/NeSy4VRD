#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: David Herron
"""

'''
This module is a NeSy4VRD workflow configuration module.

The NeSy4VRD workflow applies planned customisations to the NeSy4VRD 
visual relationship (VR) annotations of the images of the VRD image dataset
in a configurable, managed, automated and repeatable process.

This module is an example of a NeSy4VRD workflow configuration file
designed to manage a 'training set' run of the NeSy4VRD workflow.
A 'training set' run of the workflow is one that targets customising the
NeSy4VRD annotations of VRD training set images.

A NeSy4VRD workflow configuration file defines configuration parameters
(pre-named Python variables) that are used by the Python scripts that
perform the successive steps of the NeSy4VRD workflow. The Python script
for each step of the workflow will import a user-designated configuration 
module (file) such as this and access the variables it needs for its
execution from within the configuration module.
'''

#%% directory and file config parameters

# List the directory names which, when joined, form a relative
# path to the directory containing the NeSy4VRD annotations files.
anno_dir = ['data', 'annotations']

# Specify the name of the JSON file holding the NeSy4VRD object class names.
object_classes_file = 'nesy4vrd_objects.json'

# Specify the name of the JSON file holding the NeSy4VRD predicate names.
predicates_file = 'nesy4vrd_predicates.json'

# Specify the name of the JSON file holding the NeSy4VRD visual
# relationship annotations for the 'trainging set' VRD images.
annotations_file = 'nesy4vrd_annotations_train.json'


#%% Step 1 config parameters

# Here you can specify the names of any new object classes you wish to
# introduce into the NeSy4VRD visual relationship annotations.
# Any such new object class names are appended to the end of the
# existing master list of object class names. This leaves all of the
# existing object class names undisturbed in their original positions in
# the master list, which means they retain their original integer category
# IDs. This is CRITICAL, because within the visual relationship 
# annotations, all object classes are specified by category ID, not by
# name. The newly introduced object class names automatically acquire
# unique category IDs by virtue of being appended to the end of the
# master list.

step_1_new_object_names = [
                           'speaker',         # for subset of 'person' 
                           'drinking glass',  # for subset of 'glasses'
                           'license plate',   # for subset of 'plate'
                           'baseball plate',  # for subset of 'plate'
                           'stove top',       # for subset of 'stove'
                           'canopy',          # for subset of 'roof'
                           'cooking pot',     # for subset of 'pot'
                           'waste bin',       # for subset of 'trash can'
                           'teddy bear',      # for subset of 'bear'
                           'train engine',    # for subset of 'engine'
                           'boat motor',      # for subset of 'engine'
                           'helmet case'      # for subset of 'box'
                          ]


# Here you can specify adjustments to the names of existing predicates if,
# for any reason, you wish to do so.  Each adjustment is expressed with
# a 2-element list: ['current_name', 'adjusted_name'].
# Note that in any visual relationship annotation customisations specified
# in subsequent steps of the NeSy4VRD workflow, if you refer to one of these
# predicates you must do so by using the adjusted name, because the 
# original name will not be recognised as valid after Step 1 executes.

step_1_predicate_name_adjustments = [
                                     ['park next', 'park next to'],
                                     ['look', 'look at'],
                                     ['attach to', 'attached to'],
                                     ['walk past', 'walk on'],
                                     ['across', 'across from'],
                                     ['in the front of', 'in front of'],
                                     ['on the top of', 'on top of']
                                    ]

# Here you can specify the names of any new predicates you wish to
# introduce into the NeSy4VRD visual relationship annotations.
# Any such new predicate names are appended to the end of the
# existing master list of predicate names. This leaves all of the
# existing predicate names undisturbed in their original positions in
# the master list, which means they retain their original integer category
# IDs. This is CRITICAL, because within the visual relationship 
# annotations, all predicates are specified by category ID, not by
# name. The newly introduced predicate names automatically acquire
# unique category IDs by virtue of being appended to the end of the
# master list.

step_1_new_predicate_names = [
                              'fly in'      # for subset of 'fly'
                             ]


#%% Step 2 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_2_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_02_instructions_train.txt'


# Here you can specify whether or not you want the protocol driver script 
# to actually save the customised annotations to disk, thus over-writing
# the annotations file that was loaded at the start of Step 2.  You really
# should save the customised annotations to disk if you wish to advance to
# subsequent steps of the NeSy4VRD workflow, because there may be many
# dependencies amongst the subsequent annotation customisations that 
# were crafted assuming these Step 2 customisations are in place. But if you
# just want to quality-check your annotation customisation instructions by
# having the driver script process them, without running the risk of 
# inadvertently implementing your customisations by actually over-writing 
# the annotations file, you can set this variable to False. This way, if you
# inadvertently execute the final cell of the protocol driver script, it
# won't matter because the script will know not to save the updated
# annotations to disk. 

step_2_save_customised_annotations = True


#%% Step 3 config parameters

# Here you can specify lists of image filenames within whose annotations
# you wish to change all instances of object class A to object class B.
#
# You need to do thorough analysis of the images and their annotations 
# first in order to build up the lists of image names for which it is safe
# to use this Step 3 'batch' approach to changing object class A to B.

# Specify an individual change: ['from_class', 'to_class']
from_class_to_class_1 = ['glasses', 'drinking glass']

# Specify a list of image filenames to which the change applies
img_names_1 = [

'5772517433_38c7350190_b.jpg',
'4879501986_378a112275_b.jpg',
'5701950713_2e50fcc667_b.jpg',
'9425058051_d588dca90a_o.jpg',
'140906489_98f524bf33_b.jpg',
'10218327826_907c2b49df_o.jpg',
'2831772480_5b4970ea89_o.jpg',
'8560160806_11382bccda_o.jpg',
'5357403456_2d6bfe0268_b.jpg',
'3105242807_9cb9df7be4_b.jpg',
'2184834274_dd271aec9b_b.jpg',
'5233658278_73c5ff9a6a_b.jpg',
'10289721793_62b843e973_b.jpg',
'7420491946_4db56d7cf1_b.jpg',
'4768233995_7024ecacd3_b.jpg',
'6813865784_bfe15e3fbc_b.jpg',
'6332625685_92b4dd1f55_b.jpg',
'5421623873_15c55fdb06_b.jpg',
'3648786020_aa7babf611_b.jpg',
'3598192322_e3832fc68a_b.jpg',
'5924219545_54e9dbf92e_b.jpg',
'9045466497_e32f608110_b.jpg',
'3666682952_f86c6c0c2a_b.jpg',
'9981721826_063a0589b1_b.jpg',
'9413317849_59ee037005_b.jpg',
'8047703136_79100ac39e_b.jpg',
'2750909727_39d83825b3_b.jpg',
'3668798024_9f9b40cdb0_b.jpg',
'4384323461_920507913c_b.jpg',
'9165761570_ea097aba2b_b.jpg',
'4745633521_bda043e890_b.jpg',
'6875851714_4c87859b17_b.jpg',
'14104516_947fb0cfbb_o.jpg',
'8342372992_77550b4c0b_o.jpg',
'827372287_463db179f1_o.jpg',
'2086119608_672625bec8_b.jpg',
'5689121788_8e2a61239c_b.jpg',
'9489706788_6fc9a35bd4_b.jpg',
'7901520420_84e30e9933_b.jpg',
'5464460770_e2926cde29_o.jpg',
'4163729414_26c4467829_b.jpg',
'4347436774_5f447b1fc0_b.jpg',
'1164672210_4e513b9e8c_b.jpg',
'6054587784_5fbe53f082_b.jpg',
'3881283397_1d7fa59e2b_o.jpg',
'3227335672_e420c7fd21_b.jpg',
'334550573_cd6a394bbf_b.jpg',
'3053662468_f2f7514371_b.jpg',
'5816070088_9809f17540_b.jpg',
'2089240887_0b92223af3_b.jpg',
'141024523_bfe05f97de_b.jpg',
'8907780642_1d4876d498_b.jpg',
'6927980500_abeb501d27_b.jpg',
'4182606991_8bcce83e7a_b.jpg',
'8117128167_bb9ed223e7_b.jpg',
'369947624_fdda8f5c80_b.jpg',
'8087038174_a8365f0f97_b.jpg',
'9365439487_90405bc458_b.jpg',
'30701048_b197842f92_o.jpg',
'6093593_616559d353_o.jpg',
'8471766445_da895c6966_b.jpg',
'4179774753_b3dcfa443e_o.jpg',
'2599918811_42d19b91f0_b.jpg',
'2193305429_8bdf898329_b.jpg',
'4962884665_2d46628d09_b.jpg',
'5847433784_4744bb2e61_b.jpg',
'3682459597_455b827ae1_b.jpg',
'4581429768_971e7786b5_b.jpg',
'4637662561_1fd24b1cef_o.jpg',
'3091535294_37793e35d5_b.jpg',
'3967589068_4cdbd8d96f_b.jpg',
'4152569695_619dc315da_b.jpg',
'5795147272_ec6ea550fa_b.jpg',
'8168304300_dfe595eed0_o.jpg',
'290584551_7f219121ab_b.jpg',
'3916593894_9e2a2d0d5a_b.jpg',
'5517114538_91f825ecdf_b.jpg',
'390520381_1e4eff6648_b.jpg',
'9727996257_dd554865e4_o.jpg',
'8512544176_d81f778815_b.jpg',
'9657253006_b038a55ab7_b.jpg',
'9635094157_5274745b53_b.jpg',
'9272614085_8744b258ba_b.jpg',
'10010815684_efe23c9594_o.jpg'

]


# Aggregate your ['from_class', 'to_class'] pairs into a list

step_3_from_class_to_class = [
                              from_class_to_class_1
                             ]


# Aggregate your lists of image filenames into a list
#
# NOTE: take care to maintain the correct positional correspondence between 
# the entries in the two aggregate lists!!!

step_3_from_class_to_class_img_names = [
                                        img_names_1
                                       ]

#%% Step 4 config parameters

# Here you can specify pairs of object classes to be merged. The pairs to 
# be merged are expressed in 2-element lists. For example, 
# ['class_A', 'class_B'] is an instruction to merge all instances of 
# object class A into object class B.  What actually happens is that all
# instances of the integer category ID for object class A are changed to
# the integer category ID of object class B.

step_4_object_classes_to_merge = [
                                  ['plane', 'airplane'], # 'plane' into 'airplane'
                                  ['coat', 'jacket'],    # 'coat' into 'jacket'
                                  ['road', 'street']     # 'road' into 'street'
                                 ]

# Here you can specify pairs of predicates to be merged. The pairs to 
# be merged are expressed in 2-element lists. For example, 
# ['predicate_A', 'predicate_B'] is an instruction to merge all instances of 
# predicate A into predicate B.  What actually happens is that all
# instances of the integer category ID for predicate A are changed to
# the integer category ID of predicate B.
#
# We never merged any predicates when transforming the original VRD
# visual relationship annotations into the NeSy4VRD visual relationship
# annotations. But it is conceivable that someone may wish to do so. Many
# of the predicates have synonyms. For example: 'next to', 'beside'
# and 'adjacent to' can be interpreted as being synonyms.  In the NeSy4VRD
# OWL ontology, VRD-World, this 3-way synonym relationship is modeled by
# declaring each of the three OWL object properties that correspond to these
# three predicates as being owl:equivalentClass with one another.
#
# Note that the merging of predicates deemed to be synonyms is likely to
# have a powerful simplifying effect on relationship prediction. Such
# merging will significantly reduce the linguistic noise in the visual
# relationship annotations. Such simplification may or may not be 
# desired by the researcher.

step_4_predicates_to_merge = []



# NOTE: Whatever merges you specify here for Step 4 of a 'training set' run
# of your NeSy4VRD workflow should VERY LIKELY be replicated exactly for 
# Step 4 in the configuration module for the 'test set' run of your 
# NeSy4VRD workflow.  That is, if you decide to merge object classes,
# you very likely you want to do the same merging in the annotations of
# both the training set and test set images.


#%% Step 5 config parameters

# Here you can specify instances of visual relationship 'types' to be
# removed from the annotations of all images.
#
# When transforming the original VRD visual relationship annotations into 
# the NeSy4VRD visual relationship annotations, we used this functionality
# to remove several types of visual relationships that we found to be 
# nonsense. Most of these used the object class 'sky' as both the 'subject'
# and the 'object' of the visual relationship. Our analysis of these 
# visual relationships with their associated images revealed that for
# many such cases (but not all), either the 'subject' or 'object' bounding
# box was localising a cloud or a patch or region of sky containing clouds.
# We suspect that, at one time, these visual relationships would have
# referenced an object class such as 'cloud' or 'clouds', but that someone
# involved in constructing the VRD dataset (perhaps out of a desire
# to have the nice round number of 100 for the number of object classes) 
# made an executive decision to change all instances of object class 'cloud'
# to object class 'sky', thus introducing these nonsense visual 
# relationships.  One complication we detected was that very often there were 
# no clouds in the sky, and that annotators had simply drawn bounding boxes
# around arbitrary subregions of sky. In the end, we decided to remove all
# these nonsense visual relationships rather than spend the effort to 
# recover the ones that were recoverable by introducing a new object class
# of 'clouds'.

step_5_vrs_to_remove = [
                        ('sky', 'in', 'sky'),
                        ('sky', 'has', 'sky'),
                        ('sky', 'with', 'sky'),
                        ('sky', 'behind', 'sky'),
                        ('sky', 'contain', 'sky'),
                        ('wheel', 'on', 'wheel')
                       ]



# NOTE: Whatever VR types you specify here for Step 5 of a 'training set' run
# of your NeSy4VRD workflow should very likely be replicated exactly for 
# Step 5 in the configuration module for the 'test set' run of your 
# NeSy4VRD workflow. You will likely want such customisations to be applied 
# identically across the annotations of both the training set and test set 
# images.


#%% Step 6 config parameters

# Step 6 does a global trawl of the NeSy4VRD annotations dictionary looking 
# for image entries with empty lists of annotations (i.e. for images that
# have no annotations at all). The entries for such images are removed 
# from the annotations dictionary. 
#
# Removing image entries from the annotations dictionary is
# equivalent to a 'logical delete' of the image from the dataset. The
# physical image on disk is not affected in any way.

# No annotation customisation configuration parameters are required here in 
# the configuration module to tell Step 6 what to do when you run it.


#%% Step 7 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

# When transforming the original VRD visual relationship annotations into the
# NeSy4VRD visual relationship annotations, we used the annotation
# customisation instruction text file associated with Step 7 to remove
# the entries for specific images from the annotations dictionary. These
# images had annotations, but we found them to either be highly broken and
# problematic, and/or the images to weak in terms of available objects for
# the situation to be reasonably recoverable. Sometimes the images were
# rotated by 90 degrees as well. We opted to do a 'logical delete' of such
# images and remove their entries from the annotations dictionary so they
# would not be processed during training or inference or performance
# evaluation. We used the annotation customisation instruction text file 
# associated with Step 7 to gather all such removals of specific images
# into one place, for subsequent easy reference, if and when required. 

step_7_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_07_instructions_train.txt'


# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_7_save_customised_annotations = True


#%% Step 8 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_8_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_08_instructions_train.txt'


# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_8_save_customised_annotations = True


#%% Step 9 config parameters

# Here you can specify visual relationship types that you want to have
# transformed from type A to type B, on a global basis.  Each such
# instruction is expressed as a 2-element list: [(from_vr), (to_vr)].

# The transformations supported are limited to those that can be
# accomplished on a global basis. This means limiting the transformations
# to those that can be realised without bounding boxes having to be 
# specified (which are inherently individualistic, and hence incompatible 
# with a global customisation operation).
#
# The only transformation types supported are those that conform to one
# of the following patterns:
#
# 1) [(a, p1, b), ((a, p2, b)], where objects 'a' and 'b' keep their 
#    positions and predicate p1 is changed to p2. (Note: this is equivalent
#    to a 'cvrpxx' NeSy4VRD protocol instruction.)
#
# 2) [(a, p1, b), (b, p2, a)], where objects 'a' and 'b' swap positions and
#    predicate p1 is changed to p2.
#
# 3) [(a, p, b), (b, p, a)], where objects 'a' and 'b' swap positions and
#    predicate p remains unchanged.
#
# Note: for patterns (2) and (3), where the 'subject' and 'object' objects 
# swap positions, both the object bounding boxes and the object category
# IDs are swapped!

# When transforming the original VRD visual relationship annotations into the
# NeSy4VRD visual relationship annotations, we used this Step 9 functionality
# primarily to introduce greater use of the predicate 'attached to'. Within
# the predicates of the VRD visual relationship annotations, and the NeSy4VRD
# visual relationship annotations, predicate 'attached to' is the one that is
# closest to expressing the semantics of part-whole relationships. But in
# the VRD visual relationship annotations, predicate 'attached to' was 
# used only very scarcely when, in fact, it could have been used much more
# frequently.  We opted to increase its usage in order to enable distinct
# part-whole relationships to feature more prominently within the NeSy4VRD 
# visual relationship annotations. And we were also happy to reduce the 
# high frequency with which the predicate (very overloaded preposition) 
# 'on' was used.

step_9_from_vr_to_vr = [
                        
    [('wheel', 'on', 'motorcycle'), ('wheel', 'attached to', 'motorcycle')],
    [('wheel', 'on', 'car'), ('wheel', 'attached to', 'car')],
    [('wheel', 'on', 'truck'), ('wheel', 'attached to', 'truck')],
    [('wheel', 'on', 'bus'), ('wheel', 'attached to', 'bus')],    
    [('wheel', 'on', 'van'), ('wheel', 'attached to', 'van')],
    [('wheel', 'on', 'cart'), ('wheel', 'attached to', 'cart')],
    [('wheel', 'on', 'train'), ('wheel', 'attached to', 'train')],
    [('wheel', 'on', 'plane'), ('wheel', 'attached to', 'plane')],
    [('wheel', 'on', 'airplane'), ('wheel', 'attached to', 'airplane')],
    [('wheel', 'on', 'skateboard'), ('wheel', 'attached to', 'skateboard')],
    [('clock', 'on', 'building'), ('clock', 'attached to', 'building')],
    [('clock', 'on', 'tower'), ('clock', 'attached to', 'tower')],
    [('hand', 'on', 'person'), ('person', 'has', 'hand')]
                
                        ]


# NOTE: Whatever VR transformations you specify here for Step 9 of a 
# 'training set' run of your NeSy4VRD workflow should very likely be 
# replicated exactly for Step 9 in the configuration module for the 
# 'test set' run of your NeSy4VRD workflow. You will likely want such 
# customisations to be applied identically across the annotations of both 
# the training set and test set images.


#%% Step 10 config parameters

# Step 10 does a global trawl of the NeSy4VRD annotations looking for
# exact duplicate visual relationships (VRs) within the annotations of images.
# If duplicates are detected, the duplicates are removed, leaving a single
# instance of the VR.

# No annotation customisation configuration parameters are required here in 
# the configuration module to tell Step 10 what to do when you run it.


#%% Step 11 config parameters

# Here you can specify the filename of a text file containing NeSy4VRD
# annotation customisation instructions specified declaratively using the
# NeSy4VRD protocol.  The protocol driver script will parse, validate and
# process all the instructions in the file.

step_11_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_11_instructions_train.txt'


# Specify whether you want the driver script to save the customised 
# annotations to disk or not.

step_11_save_customised_annotations = True



