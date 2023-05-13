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
annotations of VRD training set images.

A NeSy4VRD workflow configuration file defines configuration parameters
(pre-named Python variables) that are used by the Python scripts that
perform the successive steps of the NeSy4VRD workflow. The Python script
for each step of the workflow will import a user-designated configuration 
module (file) such as this and access the variables it needs for its
execution from within the configuration module.

For any given run of the NeSy4VRD workflow, each successive step (script) 
of the workflow must be adapted (by the user) to import the same 
configuration module. In this way, a configuration module such as this
can define and determine every aspect of the visual relationship 
annotation customisations that a given run of the NeSy4VRD workflow
performs.  By saving the configuration module one used for a given run of
the NeSy4VRD workflow one can, in effect, retain an historical record of the 
annotation customisations that were applied by a given run of the NeSy4VRD
workflow.  Saving the configuration modules one uses for the 'training set'
and 'test set' runs of the NeSy4VRD workflow is good practice because it 
allows one to iteratively refine and extend the customisations and
extensions one applies to the NeSy4VRD visual relationship annotations over
time.  By keeping a clean version of the default NeSy4VRD visual 
relationship annotations to use as one's starting point, one can, over time,
repeatedly re-run the NeSy4VRD workflow to re-apply one's ever-growing
set of annotations customisations.  The benefit of this repeatability of
the process for applying one's customisations and extensions to the NeSy4VRD
annotations, and the ability to iteratively refine and extend the set
of one's customisations and extensions, will become more and more apparent
the more one uses the workflow in this manner.
 
The NeSy4VRD workflow requires that configured and specified annotation
customisations be organised for two separate runs of the workflow: a
'training set' run that targets customising the annotations of VRD training
set images, and a 'test set' run that targets customising the annotations
of VRD test set images. A separate instance of a NeSy4VRD configuration 
module file such as this one is required to configure and manage these two
separate but related runs of the NeSy4VRD workflow.

You can name your two NeSy4VRD configuration module files however you wish.

To perform a 'training set' run, you do the following:
* establish your 'training set' configuration module by defining the content
  of the pre-named variables in the manner you wish
* adapt the scripts for the various steps of the workflow to import your 
  'training set' configuration module
* run the successive steps of the workflow.

To perform a 'test set' run, you do the following:
* define your 'test set' configuration module 
* adapt the scripts for the various steps of the workflow to import your 
  'test set' configuration module
* run the successive steps of the workflow.

Each succesive step of the workflow will:
* import the configuration module file you tell it to import
* load the visual relationship annotation files you designate in your 
  configuration module file
* access the pre-named variables it needs from your configuration module
* apply the category of annotation customisations the script is designed to 
  perform, according to the content you have defined in your configuration
  module for the pre-named variables used by the script that performs that
  step of the workflow
* abort and report, should any issues or problems be detected
* save the updated visual relationship annotations to a file on disk, 
  using the same filename as the one from which the annotations were loaded
  in the first place; (note: saving or not saving to disk is controllable
  within your configuration module file; not saving to disk can facilitate 
  testing, to allow you to verify that all your planned customisations that
  are processed by a given step of the workflow are clean and executable,
  without making a mistake and the updated annotations to disk before you
  are ready to do so)

It is because each step of the workflow 1) loads the annotations, 2) applies
customisations, and 3) saves the updated annotations to disk that the 
steps of the workflow should always be run, one after the other, in a fixed
sequence. Many forms of dependency can arise within your cumulative set
of annotation customisations across the different steps of the workflow.
So, to ensure that these dependencies are always satisfied and prevent 
workflow steps aborting unexpectedly, always run your workflow steps in the
same fixed sequence.

One scenario where dependencies can arise is if you have created multiple
annotation customisation instruction text files in which you specify 
annotation customiation instructions using the NeSy4VRD protocol. It can
sometimes occur that you specify some customisations to the annotations of
image X in instructions text file A, and then specify some more customisations
to the annotations of image X in instructions text file B. For the
customisation instructions in text file B to be interpreted as being valid,
it may well be that customisations specified in text files A must already be
in place.  For this reason, it can be advantageous to try to ensure that
all customisation instructions affecting a given image are gathered together
in one place, in one customisation instructions text file.
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

# List the names of new object classes to be introduced into the VRD dataset.
# New object class names are strictly 'appended' to the existing list of 
# object class names so as not to disturb their positions in the ordered list,
# which is what defines the integer label for each object class.

# NOTE: Several of the original VRD object classes refer to objects of 
# very different type. We introduce new object class names so that in Step 2
# references to the old object class in specific visual relationships for
# specific, named images can be changed (re-classified) to the 'correct'
# new object class. The objective is to enhance the quality and precision
# of the VRD class labelling so that neural networks can better learn to
# detect objects of a given class.

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

# list the adjustments you wish made to existing predicate names; each
# adjustment is expressed with a 2-element list ['current_name', 'adjusted_name'];
# the 2-element lists are themselves elements of a list

step_1_predicate_name_adjustments = [
                                     ['park next', 'park next to'],
                                     ['look', 'look at'],
                                     ['attach to', 'attached to'],
                                     ['walk past', 'walk on'],
                                     ['across', 'across from'],
                                     ['in the front of', 'in front of'],
                                     ['on the top of', 'on top of']
                                    ]

# list the names of new predicates to be introduced into the VRD dataset;
# new predicates are strictly 'appended' to the existing list of predicate
# names so as not to disturb their positions in the ordered list, which
# is what defines the integer label for each predicate

step_1_new_predicate_names = [
                              'fly in'      # for subset of 'fly'
                             ]


#%% Step 2 config parameters

# The text file containing the VRD annotation customisation instructions
# for Step 2 of the annotation customisation process. This file must be
# in the current working directory, not the annotations directory.
step_2_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_2_instructions_train.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk (over-writing the current state of the annotations
# file defined above) or not. If you set this to False, you can safely run
# the driver script on the instructions file just to validate that all of
# your customisation instructions are interpretable and executable (given
# the current state of the VRD annotations).  Once you are happy with your
# instructions file, set this variable to True and the driver script will
# save the customised annotations to disk.
step_2_save_customised_annotations = True


#%% Step 3 config parameters

# The annotations for the images named in the following list use object
# class 'glasses' to refer exclusively to 'drinking glass' glasses.
# Use of object class 'glasses' is being standardised to refer exclusively to
# eyeglasses. So, in the annotations for images named in the list we want
# to change all references to object class 'glasses' to (the newly 
# introduced) object class 'drinking glass'.

from_class_to_class_1 = ['glasses', 'drinking glass']

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

# Build a list of ['from class', 'to class'] pairs
step_3_from_class_to_class = [
                              from_class_to_class_1
                             ]

# Build a list of image name lists
# (NOTE: the positions of the variables named in this list must match
# the positions of the corresponding ['from_class', 'to_class'] pairs)
step_3_from_class_to_class_img_names = [
                                        img_names_1
                                       ]

#%% Step 4 config parameters

# Specify pairs of object classes and pairs of predicates to be merged, globally,
# across the VR annotations for all images within the training set of the 
# VRD dataset.

# The objects of classes 'plane' and 'airplane' are clearly drawn from the
# same distribution. There is no basis for distinguishing the objects of
# the one class from those of the other.  The only sensible course of action
# is to merge the two classes. We chose to merge objects of class 'plane'
# into class 'airplane' (rather than the other way round) simply because
# 'airplane' is a more explicit name and we prefer it for that reason.
# The original VRD training set contains 61 images whose annotations refer
# to object class 'plane' and 48 images whose annotations refer to object
# class 'airplane'.  After merging class 'plane' into class 'airplane'
# there will be 0 training images that refer to object class 'plane' and
# 48 + 61 = 109 images whose annotations refer to object class 'airplane'.

# The objects of classes 'coat' and 'jacket' are cleary drawn from the
# same distribution. There is no basis for distinguishing the objects of
# the one class from those of the other. The only sensible course of action
# is to merge the two classes. We chose to merge object of class 'coat'
# into class 'jacket' because of the numbers of images involved.
# The original VRD training set contains 161 images whose annotations refer
# to object class 'coat' and 505 images whose annotations refer to object
# class 'jacket'.  So we chose to merge the class with fewer images into
# the class with the greater number of images.

# A similar rationale applies for merging instances of object class 'road'
# into object class 'street'.

step_4_object_classes_to_merge = [
                                  ['plane', 'airplane'], # 'plane' into 'airplane'
                                  ['coat', 'jacket'],    # 'coat' into 'jacket'
                                  ['road', 'street']     # 'road' into 'street'
                                 ]

# Define from/to pairs of predicates to merge

step_4_predicates_to_merge = []


#%% Step 5 config parameters

# Step 5: remove instances of specific visual relationships globally

# list the ('subject', 'predicate', 'object') vr instances you wish to
# remove on a global basis (ie across the annotations for all images)

step_5_vrs_to_remove = [
                        ('sky', 'in', 'sky'),
                        ('sky', 'has', 'sky'),
                        ('sky', 'with', 'sky'),
                        ('sky', 'behind', 'sky'),
                        ('sky', 'contain', 'sky'),
                        ('wheel', 'on', 'wheel')
                       ]

#%% Step 6 config parameters

# Step 6 does a global trawl of the VRD annotations dictionary looking for 
# keys (image names) with empty lists as values (ie zero annotations). 
# Images with zero visual relationship annotations are removed from the
# annotations dictionary because we cannot train on images that have no
# targets.  Removing image entries from the annotations dictionary is
# equivalent to a 'logical delete' of the image from the dataset. The
# physical image is not removed from the images directory.

# No annotation customisation configuration parameters are required for
# this step.

#%% Step 7 config parameters

# Step 7 removes unwanted/problematic images from the annotations dictionary. 
# The images are not physically removed from the image directory. But by
# removing their entries from the annotations dictionary, we logically remove
# them from the dataset.  They will never participate in training.

# Specify the text file containing the VRD annotation customisation 
# 'remove image' instructions for Step 7 of the annotation customisation 
# process.  The instructions file must be in the current working directory, 
# not the annotations data directory.
step_7_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_7_instructions_train.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk (over-writing the current state of the annotations
# file defined above) or not. If you set this to False, you can safely run
# the driver script on the instructions file just to validate that all of
# your customisation instructions are interpretable and executable (given
# the current state of the VRD annotations).  Once you are happy with your
# instructions file, set this variable to True and the driver script will
# save the customised annotations to disk.
step_7_save_customised_annotations = True


#%% Step 8 config parameters

# Step 8 augments the annotations for designated images with new, additional
# ('subject', 'predicate', 'object') visual relationships specified by the
# analyst. The motivation is usually to reference additional objects that 
# are present in the image but which are not yet mentioned by any of the 
# currently existing visual relationships.  It's impossible to annotate 
# every instance of a VRD object class in every VRD image, so the annotations
# for most images will be a subset of what could be annotated. But sometimes
# the omission of certain objects from a VRD image's annotations feels like
# an injustice one can't resist correcting. Or one may wish to increase the
# frequency with which certain object classes, predicates and/or complete 
# visual relationships are referenced in the annotations data. 

# Specify the text file containing the VRD annotation customisation instructions
# for Step 8 of the annotation customisation process. This file must be
# in the current working directory, not the annotations directory.
step_8_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_8_instructions_train.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk (over-writing the current state of the annotations
# file defined above) or not. If you set this to False, you can safely run
# the driver script on the instructions file just to validate that all of
# your customisation instructions are interpretable and executable (given
# the current state of the VRD annotations).  Once you are happy with your
# instructions file, set this variable to True and the driver script will
# save the customised annotations to disk.
step_8_save_customised_annotations = True


#%% Step 9 config parameters

# Step 9 transforms visual relationships on a global basis.

# Specify pairs of visual relationships, [from_vr, to_vr], where from_vr
# is to be transformed into to_vr.  Each vr transformation instruction is
# applied globally, across the annotations for all images.

# The number of supported transformations is limited to those that can be
# accomplished on a global basis, which means those transformations that
# can be realised without bounding boxes having to be specified (which are 
# inherently individualistic, and hence incompatible with a global 
# customisation approach).
#
# A global vr transformation instruction has a format consistent with one
# of the following patterns:
#
# 1) [(a, p1, b), ((a, p2, b)], where objects 'a' and 'b' keep their 
#    positions and predicate p1 is changed to p2; (nb: this is equivalent
#    to a 'cvrpxx' vr annotation customisation instruction)
#
# 2) [(a, p1, b), (b, p2, a)], where objects 'a' and 'b' swap positions and
#    predicate p1 is changed to p2
#
# 3) [(a, p, b), (b, p, a)], where objects 'a' and 'b' swap positions and
#    predicate p is unchanged
#
# note: in cases (2) and (3), where the 'subject' and 'object' objects 
# swap positions, both the integer object class labels and bboxes are 
# swapped!


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

#%% Step 10 config parameters

# Step 10 does a global trawl of the VRD annotations looking for
# duplicate visual relationships (VRs) within the set of annotations
# for each image. It removes any such duplicate vrs.

# No annotation customisation configuration parameters are required for
# this step.

#%% Step 11 config parameters

# Specify the text file containing the VRD annotation customisation instructions
# for Step 11 of the annotation customisation process. This file must be
# in the current working directory, not the annotations directory.
step_11_vrd_anno_cust_instructions_file = 'nesy4vrd_anno_cust_11_instructions_train.txt'

# Specify whether you want the driver script to save the customised 
# annotations to disk (over-writing the current state of the annotations
# file defined above) or not. If you set this to False, you can safely run
# the driver script on the instructions file just to validate that all of
# your customisation instructions are interpretable and executable (given
# the current state of the VRD annotations).  Once you are happy with your
# instructions file, set this variable to True and the driver script will
# save the customised annotations to disk.
step_11_save_customised_annotations = True



