# The NeSy4VRD extensibility support infrastructure

This folder contains the NeSy4VRD extensibility support infrastructure. 

The NeSy4VRD extensibility support infrastructure consists of:
* open source Python **NeSy4VRD analysis** code for conducting deep and comprehensive analyses of the **NeSy4VRD dataset** (the VRD images and their associated NeSy4VRD visual relationship annotations)
* an open source, custom-designed **NeSy4VRD protocol** for specifying visual relationship annotation customisation instructions declaratively, in text files
* an open source, custom-designed **NeSy4VRD workflow**, implemented using Python scripts and modules, for applying small or large volumes of customisations or extensions to the NeSy4VRD visual relationship annotations in a configurable, managed, automated and repeatable process.

The purpose behind providing comprehensive infrastructure to support extensibility of the NeSy4VRD visual relationship annotations is to make it easy for researchers to take the **NeSy4VRD dataset** in new directions, by further enriching the annotations, or by tailoring them to introduce new or more data conditions that better suit their particular research needs and interests.

The NeSy4VRD extensibility support infrastructure is relevant for anyone who chooses to use the NeSy4VRD research resource. It may be of particular interest, however, to neurosymbolic AI researchers interested in using the **NeSy4VRD ontology**, VRD-World, in conjunction with the **NeSy4VRD dataset**. These researchers can of course tailor the VRD-World ontology if they wish without needing to modify or extend the NeSy4VRD visual relationship annotations in any way. But their degrees of freedom for doing so will be limited by the need to maintain alignment with the NeSy4VRD visual relationship annotations and the particular set of object classes and predicates to which they refer.  If neurosymbolic AI researchers want full freedom to tailor the VRD-World ontology, they may well need to tailor the NeSy4VRD visual relationship annotations first, in order that alignment be maintained.

To illustrate our point, and to illustrate our vision of how the NeSy4VRD extensibility support infrastructure can be used, let us consider a simple example. It is common in computer vision to distinguish between **thing** objects (that have well-defined shapes) and **stuff** objects (that are amorphous). Suppose a researcher wishes to have a greater number of **stuff** object classes with which to work.  *Water* is such a **stuff** object.  Many VRD images contain water but it is not currently one of the annotated object classes and hence is never referenced in any visual relationship annotations. So adding a *Water* class to the class hierarchy of the VRD-World ontology would be pointless because it would never acquire any instances (because an object detector would never classify a detected object as *water*). However, our hypothetical researcher could choose to do the following:
* use the analysis functionality of the NeSy4VRD extensibility infrastructure to find images containing water (by, say, searching for images whose visual relationships refer to object classes such as 'boat', 'surfboard', 'sand', 'umbrella', etc.);
* use free image analysis software (such as GIMP, at gimp.org) to get bounding boxes for instances of water in these images;
* use the NeSy4VRD protocol to specify new visual relationships for these images that refer to the new 'water' objects (e.g. <'boat', 'on', 'water'>);
* use the NeSy4VRD workflow to introduce the new object class 'water' and to apply the specified new visual relationships to the sets of annotations for the affected images;
* introduce class Water to the class hierarchy of the VRD-World ontology (using, say, the free Protege ontology editor);
* continue experimenting, now with the added benefit of the additional stuff object class 'water';
* contribute the enriched set of NeSy4VRD visual relationship annotations, and the enriched companion VRD-World ontology, to research communities.

Detailed information specifically about each of the three components of the **NeSy4VRD extensibility support infrastructure** is available in README files inside each of the respective folders:  **analysis**, **protocol** and **workflow**.

More detailed information about aspects of the **NeSy4VRD extensibility support infrastructure** in general, are available in this folder in supplementary README files.





