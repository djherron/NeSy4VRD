# NeSy4VRD: protocol

This folder contains assets relating to the **NeSy4VRD protocol** component of the NeSy4VRD infrastructure that supports extensibility of the NeSy4VRD visual relationship annotations and, thereby, of the NeSy4VRD OWL ontology, VRD-World. The **NeSy4VRD protocol** component of the NeSy4VRD infrastructure supporting extensibility is a custom-designed protocol that allows researchers to specify VRD / NeSy4VRD visual relationship annotation customisation instructions declaratively, in text files. Specifying annotation customisation instructions declaratively in text files enables researchers to define and apply large volumes of annotation customisations safely and responsibly, using the **NeSy4VRD workflow**. The **NeSy4VRD workflow** is the 3rd component of the NeSy4VRD infrastructure that supports extensibility of the annotations and VRD-World ontology. It is described in another folder of this GitHub repo.

## The NeSy4VRD protocol specification

Like most protocols, the **NeSy4VRD protocol** is conceptual in nature and is defined in a specification document. This README document is the specification document defining the **NeSy4VRD protocol**.  For simplicity, it is an informal specification that relies on examples and explanations of the examples.

The following listing shows the **NeSy4VRD protocol** in action. The examples it contains illustrate all of the features of the **NeSy4VRD protocol**. We use the examples in this listing to explain what the **NeSy4VRD protocol** is and how it can be used to specify visual relationship annotation customisation instructions declaratively, in text files.

```
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

### Training image vs test image annotation customisations

A given text file of **NeSy4VRD protocol** visual relationship annotation customisation instructions must always pertain only to customisations of either VRD training image annotations or VRD test image annotations. The two categories  cannot be mixed in the same text file. This is because the Python driver script that interprets the protocol and processes the instructions (as part of the **NeSy4VRD workflow**) operates on either training image annotations or test image annotations, not both.

#### The `imname` instruction

The `imname` instruction announces a new image.  It is always followed by the filename of a valid VRD image. The `imname` instruction declares that the visual relationship annotation instructions which follow apply to the specified image. The `imname` instruction, therefore, establishes context. It establishes the context for the interpretation of all of the other **NeSy4VRD protocol** instruction types.

When a **NeSy4VRD protocol** annotation customisation instruction file is processed (as part of the **NeSy4VRD workflow**), if the image filename associated with an `imname` instruction is not recognised (i.e. is found to not have an entry in the NeSy4VRD annotations dictionary), the driver script will abort and point to the problem.  That is, VRD image filenames are *recognised* or not according to whether or not they have entries in the NeSy4VRD annotations dictionary, not according to whether they exist as physical files in the appropriate VRD image directory on disk. Further, this means that image filenames that fail to be so recognised are NOT interpreted as 'new images' to be automatically given new entries within the annotations dictionary.

#### The `cvrsoc` and `cvrsbb` instructions

For the first image in the listing, an improvement to the visual relationship annotation at index position 4 (in the image's Python list of annotated visual relationships) is being specified.  The `cvrsoc` instruction declares an intention to change the subject's object class (`soc`) from **person** to **speaker**, (as in 'stereo speaker'). The `cvrsbb` instruction declares an intention to change the subject's bounding box (`sbb`) to a more accurate localisation of the object.

#### The `cvrooc` and `cvrobb` instructions

For the second image, similar types of changes are being specified, but this time for the visual relationship at index position 7 and in relation to the object's object class and bounding box (via instructions `cvrooc` and `cvrobb`, respectively).

#### The `cvrpxx` instruction

For the third image, an improvement to the visual relationship at index position 5 is being specified. After a `cvrsoc` instruction specifying that the subject's object class be changed from **bear** to **teddy bear**, a `cvrpxx` instruction declares an intention to change the predicate (`pxx`) from **sit on** to **in**.

#### The `rvrxxx` instruction

For the fourth image, the `rvrxxx` instruction declares an intention to remove the visual relationship at index position 4 within the image's Python list of annotated visual relationships.

#### The `avrxxx` instruction

The fourth image in the listing also has two instances of the `avrxxx` instruction associated with it. These declare intentions to **add** two *new* visual relationships to the set of annotations for the image.  These will be **appended** to the end the image's Python list of annotated visual relationships.

#### The `rimxxx` instruction

The fifth image in the listing above shows an example of the use of the only other **NeSy4VRD protocol** instruction not already mentioned: the `rimxxx` instruction (for 'remove image'). The only valid location for the `rimxxx` instruction to appear is immediately following the filename of a VRD image, as a supplementary component of an `imname` instruction.

The `rimxxx` instruction is an instruction to remove the entry for the specified VRD image from the NeSy4VRD visual relationship annotations dictionary. Removal of an image's entry from the annotations dictionary has no effect on the physical VRD image file itself. That stays intact on disk . Thus, the `rimxxx` instruction is equivalent to a form of 'logical delete'.

If and when a `rimxxx` instruction is used, it is invalid to have *NeSy4VRD protocol** instructions following the `imname` instruction in which the `rimxxx` instruction appears. If the driver script processing the instructions file detects any, it will abort and point out the problem.

Researchers who are customising the NeSy4VRD visual relationship annotations with the **NeSy4VRD protocol** and **NeSy4VRD workflow** are free to dislike a particular VRD image for any reason and to choose to have its entry removed from the annotations dictionary using the `rimxxx` instruction. Reasons why a researcher may choose to do this can vary.

In our case, when applying our customisations and quality improvements to the original VRD visual relationship annotations in order to create the highly customised and quality-improved NeSy4VRD visual relationship annotations, we used the `rimxxx` instruction in scenarios such as the following:
* where the annotations of an image were found to be too broken and highly problematic to be recoverable with reasonable effort
* where the image in question contained too few candidate objects for viable visual relationships to be constructed, or
* where an image was found to be rotated by 90 degrees, meaning that its entire perspective was at odds with the rest of the images in the dataset, and retention of the image would amount to retaining unhelpful noise that could only compromise both object detection and relationship detection.

Most (if not all) of such scenarios, however, have already been detected and dealt with as part of the creation of the NeSy4VRD visual relationship annotations. So further use of the `rimxxx` instruction, by researchers doing potential onward customisations and extensions of the NeSy4VRD visual relationship annotations, is unlikely to be necessary.  However, the `rimxxx` instruction is part of the **NeSy4VRD protocol** and is available for use by any researcher for any reason.


