# NeSy4VRD: analysis

This folder contains assets relating to the **annotations analysis** component of the NeSy4VRD infrastructure that supports extensibility of the NeSy4VRD visual relationship annotations and, thereby, of the NeSy4VRD OWL ontology, VRD-World. The **annotations analysis** component of the NeSy4VRD infrastructure supporting extensibility provides comprehensive functionality for deep analysis of the NeSy4VRD dataset: the NeSy4VRD visual relationship annotations and the VRD images with which they are associated.

## nesy4vrd_annotations_analysis.py

This script contains extensive functionality for analysing the VRD images and their NeSy4VRD visual relationship annotations.

The analysis functionality in the script is organised into several large categories. Each category is clearly marked with prominent comment markings. These main categories of analysis functionality are:
* analyses devoted purely to displaying specified images with their annotated objects and printing their visual relationships
* analyses that require first 'searching for' or 'finding' images that have visual relationships that satisfy some specified condition or search criteria and then, having identified such images, analysing those images in the result set along with their visual relationships and annotated objects
* miscellaneous analyses (such as analysing the distinct predicates that are used with a given object class)
* distributional analyses (such as the number of visual relationships per image, the number of distinct object classes per image, the number of distinct predicates per image)
* quality verification analyses, such as checking that no images: have exact duplicate visual relationships; have visual relationships where the 'subject' and 'object' objects are the same; have a bounding box that has been assigned multiple different object classes; have degenerate bounding boxes).

The script is designed to be used interactively, within an IDE, where the analyst can adjust parameters and execute particular functionality cell by cell, and iteratively.

The functionality associated with each distinct analysis consists of some number of successive cells. The first cell of each distinct analysis begins with a new cell with a header **analysis X** and a description of the type of analysis to be undertaken. Successive cells associated with that unique type of analysis begin with cell headers **X.1**, **X.2**, **X.3**, etc..  In a typical analysis, cell **X.1** is used to select or find images for the analysis. Cell **X.2** is very often begins a sequence of cells designed to iterated over repeatedly, for different images. Cell **X.2** is used to select an image from the result set of images in cell **X.1** and begin a deeper analysis of that image and its visual relationships that might span over a sequence of successive cells. Once the analysis of that image is complete, the analyst would return to cell **X.2**, select another image from the result set discovered in cell **X.1** and conduct a similar analysis over the successive cells for that image.

The comments and documation into the script should make it clear how the script is meant to facilitate this particular style of iterative analysis.


