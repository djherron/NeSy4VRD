# NeSy4VRD: Protocol - Specification

This folder contains assets relating to the **NeSy4VRD protocol** component of the NeSy4VRD infrastructure that supports extensibility of the NeSy4VRD visual relationship annotations and, thereby, of the NeSy4VRD OWL ontology, VRD-World. The **NeSy4VRD protocol** component of the NeSy4VRD infrastructure supporting extensibility is a custom-designed protocol that allows researchers to specify VRD / NeSy4VRD visual relationship annotation customisation instructions declaratively, in text files. Specifying annotation customisation instructions declaratively in text files enables researchers to define and apply large volumes of annotation customisations safely and responsibly, using the **NeSy4VRD workflow**. The **NeSy4VRD workflow** is the 3rd component of the NeSy4VRD infrastructure that supports extensibility of the annotations and VRD-World ontology. It is described in another folder of this GitHub repo.

## The NeSy4VRD protocol specification

Like most protocols, the **NeSy4VRD protocol** is conceptual in nature and is defined in a specification document. This README document is the specification document defining the **NeSy4VRD protocol**.  This  specification of the **NeSy4VRD protocol** is relatively informal and relies heavily on examples and explanations of the examples.

## NeSy4VRD protocol example listing

The following listing shows the **NeSy4VRD protocol** in action. The examples it contains illustrate all of the features of the **NeSy4VRD protocol**. We use the examples in this listing to explain what the **NeSy4VRD protocol** is and how it can be used to specify visual relationship annotation customisation instructions declaratively, in text files.

```
# This is a comment line

imname; 3223670633_7d3d72dfe8_b.jpg
cvrsoc; 4; ('person', 'on', 'shelf'); speaker
cvrsbb; 4; ('speaker', 'on', 'shelf'); [161,234,231,270]

imname; 8934043045_251b42d19a_b.jpg
cvrooc; 7; ('bus', 'beside', 'car'); truck
cvrobb; 7; ('bus', 'beside', 'truck'); [334,557,99,403]

imname; 1426904233_ee344879b6_b.jpg
cvrsoc; 5; ('bear', 'sit on', 'basket'); teddy bear
cvrpxx; 5; ('teddy bear', 'sit on', 'basket'); in

imname; 4929276486_ca06aedbb9_b.jpg
rvrxxx; 4; ('person', 'wear', 'jacket');
avrxxx; boat; [477,594,319,746]; has; dog; [478,529,587,618]
avrxxx; boat; [477,594,319,746]; carry; dog; [478,529,587,618]

imname; 7171463996_900cb4ce33_b.jpg; rimxxx
```

## Instruction types

The **NeSy4VRD protocol** recognises **9 instruction types** for declaring customisations of the NeSy4VRD visual relationship annotations of the VRD images:
* 2 instruction types relate to **images** as a whole:
  - the **image name**, `imname`, instruction announces a new image
  - the **remove image**, `rimxxx`, instruction declares the removal of an image's entry from the set of annotatations
* 7 instruction types relate to **visual relationship annotations** associated with an image:
  - the five **change visual relationship**, `cvr...`, instructions declare changes to one of the five components of an existing annotated visual relationship
  - the **remove visual relationship**, `rvrxxx`, instruction declares the removal of an existing annotated visual relationship
  - the **add visual relationship**, `avrxxx`, instruction declares the introduction of a *new* annotated visual relationship.

Instances of annotation customisation instructions for the various **types** consist of different numbers of **components**. The components of an instruction instance are always delimited with the `;` (**semicolon**) character. The number of instruction components per instruction **type** are as follows:
* the `imname` instruction type: usually 2, but optionally 3
* the `cvr...` instruction types: 4
* the `rvrxxx` instruction type: 3
* the `avrxxx` instruction type: 6

The sections that follow describe each of these 9 instruction types in detail.


### The `imname` instruction

The **image name**, `imname`, instruction announces a new image.

Instances of this instruction type always begin with the following two components:
```
imname; image_filename
```
where the `image_filename` component is the filename of a particular VRD image.  In the listing above, there are 5 instances of `imname` instructions, each one announcing customisations relating to a particular VRD image.

The `imname` instruction declares that the visual relationship annotation instructions which follow apply to the specified image. The `imname` instruction, therefore, establishes context. It establishes the context for the interpretation of all of the other **NeSy4VRD protocol** instruction types.

When a visual relationship annotation customisation instruction text file is processed by the protocol driver script of the **NeSy4VRD workflow**, if the image filename associated with an `imname` instruction is not found to have an entry in the NeSy4VRD annotations dictionary, the protocol driver script is said to *not recognise* the image and it will abort and report this problem. That is, VRD image filenames are *recognised* (or not) according to whether they have entries in the NeSy4VRD annotations dictionary, not according to whether they exist as physical files in the appropriate VRD image directory on disk. Further, this means that image filenames that fail to be recognised are NOT automatically granted new entries within the annotations dictionary, even if there are physical image files on disk with corresponding filenames.

Optionally (and very rarely), an instance of the `imname` instruction type can have a 3rd component, resulting in the following pattern:
```
imname; image_filename; rimxxx
```
where the 3rd component is the **remove image**, `rimxxx`, instruction type. This special case is described separately, below, under the heading of the `rimxxx` instruction type.



### The `cvr...` instruction types

The five **change visual relationship**, `cvr...`, instruction types consist of 4 components that conform to the following pattern:
```
cvr...; vr_index; vr_description; new_value
```

The particular `cvr...` instruction indicates which of the 5 components of the designated annotated visual relationship is to be changed by giving it a new value. The `vr_index` is the index position of the designated visual relationship within the Python list of annotated visual relationships for the image in question. As such, valid `vr_index` values for a given image range from 0 to `len(list) - 1`.  The `vr_description` is a 3-element, user-friendly description of the designated visual relationship at the index position specified by `vr_index`. The `vr_description` declared in an instruction must match the actual visual relationship that exists at the specified `vr_index`. If there is a mismatch, the protocol driver script of the **NeSy4VRD workflow** will abort and report the problem. The `new_value` specifies the new value to be assigned to the designated component of the designated visual relationship annotation (a new object class, a new bounding box, or a new predicate).

The convention of identifying the designated visual relationship that is to be customised using dual mechanisms --- the `vr_index` and the `vr_description` --- has several important benefits:
* it is an extremely useful **quality control mechanism** that allows the protocol driver script of the **NeSy4VRD workflow** to detect and prevent inadvertent errors in the formulation of annotation customisation instructions;
* it helps researchers to think clearly and precisely about the changes they wish to make;
* it ensures that the annotation customisation instructions are human-readable and can be readily interpreted in future, and refined if necessary.

### The `cvrsoc` and `cvrsbb` instructions

The `cvrsoc` instruction declares a change to the **'subject' object class**, `soc`, of an existing annotated visual relationship. The `cvrsbb` instruction declares a change to the **'subject' bounding box**, `sbb`, of an existing annotated visual relationship.  All bounding boxes are specified using the format: `[ymin, ymax, xmin, xmax]`.

*Example*: For the first image in the listing, an improvement to the visual relationship annotation at index position 4 (in the image's Python list of annotated visual relationships) is being specified.  The `cvrsoc` instruction declares an intention to change the object class of the 'subject' from **person** to **speaker** (as in 'stereo speaker'). The `cvrsbb` instruction declares an intention to change the existing bounding box specification of the 'subject' (which, at that point, will have acquired class **speaker**) to a more accurate bounding box specification that localises the 'subject' object more precisely within the image.

### The `cvrooc` and `cvrobb` instructions

The `cvrooc` instruction declares a change to the **'object' object class**, `ooc`, of an existing annotated visual relationship. The `cvrobb` instruction declares a change to the **'object' bounding box**, `obb`, of an existing annotated visual relationship. All bounding boxes are specified using the format: `[ymin, ymax, xmin, xmax]`.

*Example*: For the second image in the listing, an improvement to the visual relationship annotation at index position 7 (in the image's Python list of annotated visual relationships) is being specified.  The `cvrooc` instruction declares an intention to change the object class of the 'subject' from **car** to **truck**. The `cvrobb` instruction declares an intention to change the existing bounding box specification of the 'object' (which, at that point, will have acquired class **truck**) to a more accurate bounding box specification that localises the 'object' object more precisely within the image.

### The `cvrpxx` instruction

The `cvrpxx` instruction declares a change to the **predicate**, `pxx`, of an existing annotated visual relationship.

*Example*: For the third image in the listing, an improvement to the visual relationship at index position 5 (in the image's Python list of annotated visual relationships) is being specified. After a `cvrsoc` instruction specifying that the subject's object class be changed from **bear** to **teddy bear**, the `cvrpxx` instruction declares an intention to change the predicate from **sit on** to **in**.

### The `rvrxxx` instruction

The **remove visual relationship**, `rvrxxx`, instruction declares that an existing annotated visual relationship for a particular image be **removed**.

Instances of this instruction type consist of 3 components that conform to the following pattern:
```
rvrxxx; vr_index; vr_description
```

The `vr_index` is the index position of the designated visual relationship that is to be removed. The `vr_description` is a 3-element, user-friendly description of the designated visual relationship at the index position specified by `vr_index`.

The `vr_description` must match the actual visual relationship that exists at the specified `vr_index`. If there is a mismatch, the protocol driver script of the **NeSy4VRD workflow** will abort and report the problem.  This is a useful **quality control mechanism** that prevents the removal of a visual relationship other than the one intended.

*Example*: For the fourth image in the listing (above), the `rvrxxx` instruction declares an intention to remove the visual relationship at index position 4 within the image's Python list of annotated visual relationships.

### The `avrxxx` instruction

The **add visual relationship**, `avrxxx`, instruction declares that a **new** annotated visual relationship be **introduced** for a particular image.

Instances of this instruction type consist of 6 components that conform to the following pattern:
```
avrxxx; soc; sbb; pxx; ooc; obb
```
The `soc` component is the 'subject' object class, and `sbb` is its bounding box specification. The `pxx` component is the name of the predicate describing the relationship. The `ooc` component is the 'object' object class, and `obb` is its bounding box specification. 

New visual relationships introduced by the `avrxxx` instruction type are *always* **appended** to the end of the image's Python list of annotated visual relationships.  Any number of new visual relationships can be introduced for an image.

*Example*: For the fourth image in the listing (above), two new annotated visual relationships are being introduced.

### The `rimxxx` instruction

The **remove image**, `rimxxx`, instruction declares an intention to remove an image's entry from the NeSy4VRD visual relationship annotations dictionary altogether, including all of its annotated visual relationships (if any). This operation removes a *key:value* pair entry from a Python dictionary, where the *key* is the image's filename, and the *value* is its list of annotated visual relationships. 

The only valid location for the `rimxxx` (remove image) instruction to appear is immediately following the filename of a VRD image in an `imname` instruction. In effect, the `rimxxx` instruction is an optional, supplementary component of an `imname` instruction.

Removal of an image's entry from the annotations dictionary has no effect on the physical VRD image file itself. That stays intact on disk . Thus, the `rimxxx` instruction is equivalent to a form of *logical delete*.

*Example*: The fifth image in the listing above shows an example of the use of the `rimxxx` instruction. 

If and when a `rimxxx` instruction is used, it is invalid to have **NeSy4VRD protocol** instructions following the `imname` instruction in which the `rimxxx` instruction appears. If the protocol driver script processing the instructions file detects any, it will abort and point out the problem.

Researchers who are customising the NeSy4VRD visual relationship annotations with the **NeSy4VRD protocol** and **NeSy4VRD workflow** are free to dislike a particular VRD image for any reason and to choose to have its entry removed from the annotations dictionary using the `rimxxx` instruction. Reasons why a researcher may choose to do this can vary.

In our case, when applying our customisations and quality improvements to the original VRD visual relationship annotations in order to create the highly customised and quality-improved NeSy4VRD visual relationship annotations, we used the `rimxxx` instruction in scenarios such as the following:
* where the annotations of an image were found to be too broken and highly problematic to be recoverable with reasonable effort
* where the image in question contained too few candidate objects for viable visual relationships to be constructed, or
* where an image was found to be rotated by 90 degrees, meaning that its entire perspective was at odds with the rest of the images in the dataset, and retention of the image would amount to retaining unhelpful noise that could only compromise both object detection and relationship detection.

Most (if not all) of such scenarios, however, have already been detected and dealt with as part of the creation of the NeSy4VRD visual relationship annotations. So further use of the `rimxxx` instruction by researchers doing potential onward customisations and extensions of the NeSy4VRD visual relationship annotations is unlikely to be necessary.  However, the `rimxxx` instruction is part of the **NeSy4VRD protocol** and is available for use by any researcher for any reason.


## Further aspects of the NeSy4VRD protocol

The 9 instruction types defined above constitute the core elements of the **NeSy4VRD protocol** for specifying declarative customisations to NeSy4VRD visual relationship annotations.  This section describes supplementary aspects of the **NeSy4VRD protocol**.

### Comment lines and blank lines

The **NeSy4VRD protocol** also recognises **comment** lines and **blank** lines in instruction text files. A **comment** line begins with a `#` (hash) character.  Both **comment** lines and **blank** lines are ignored by the protocol driver script of the **NeSy4VRD workflow** that processes **NeSy4VRD protocol** annotation customisation instruction text files.  You can have as many of these types of lines in your instruction text files as you wish.

### Bounding box specifications

The reason that all bounding box specifications in the NeSy4VRD visual relationship annotations have the format `[ymin, ymax, xmin, xmax]` is historical. This is the format used in the original VRD visual relationship annotations of the VRD dataset and NeSy4VRD has retained this convention.  The protocol driver script of the **NeSy4VRD workflow** checks that this format is respected. It checks that all four elements are positive integers and that `ymax - ymin > 0` and `xmax - xmin > 0`. If these conditions are not met, a bounding box specification is regarded as degenerate and the protocol driver aborts and reports the problem. 

### Successive `cvr...` changes for one visual relationship

As described above, the 5 `cvr...` instruction types and the `rvrxxx` instruction type all require that the designated visual relationship be identified via dual mechanisms: 1) the `vr_index` index position of the visual relationship within the Python list of visual relationships for an image, and 2) the `vr_description` of the visual relationship, that reflects the researcher's understanding of the state of the visual relationship that exists at index position `vr_index`.  The benefits of this convention have been highlighted, above.

This convention has a subtle implication that needs to be recognised when multiple, successive `cvr...` instructions are specified for a single visual relationship for the same `vr_index`. This implication has already been pointed out, above. But, here, we highlight it again to help ensure it is fully taken onboard by readers, in order to avoid confusion.

The protocol driver script of the **NeSy4VRD workflow** processes annotation customisation instruction text files line-by-line, from top to bottom. Thus, if multiple `cvr...` changes are specified for a single visual relationship at a given `vr_index`, the incremental changes *may* need to be reflected in the `vr_description` components of the succedding `cvr...` instructions for that `vr_index`.  Otherwise, the protocol driver script of the **NeSy4VRD workflow** *may* detect a mismatch between the `vr_description` and the actual state of the visual relationship at index `vr_index` (at that moment in time) and have no option but to abort and report a problem.

For example, recall the following example from the listing (above):
```
imname; 8934043045_251b42d19a_b.jpg
cvrooc; 7; ('bus', 'beside', 'car'); truck
cvrobb; 7; ('bus', 'beside', 'truck'); [334,557,99,403]
```
The `cvrooc` instruction changes the 'object' object class from **car** to **truck**, and so the `vr_description` in the succeeding `cvrobb` instruction must refer to object class **truck**, because the `cvrooc` instruction will have already been executed and so (in memory) the visual relationship at index position 7 will already have been altered to refer to object class **truck**. 

Notice that we could have reversed the order of these two instructions and obviated the need to reflect the change in the state of the visual relationship. If we first change the bounding box and then change the object class, the `vr_description` in the two instructions need not change:
```
imname; 8934043045_251b42d19a_b.jpg
cvrobb; 7; ('bus', 'beside', 'car'); [334,557,99,403]
cvrooc; 7; ('bus', 'beside', 'car'); truck
```

### Training image vs test image annotation customisations

A given text file of **NeSy4VRD protocol** visual relationship annotation customisation instructions must always pertain only to customisations of either VRD training image annotations or VRD test image annotations. The two categories  cannot be mixed in the same text file. This is because the Python driver script that interprets the protocol and processes the instructions (as part of the **NeSy4VRD workflow**) operates on either training image annotations or test image annotations, not both.



