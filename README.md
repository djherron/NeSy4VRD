# NeSy4VRD: A Resource for Neurosymbolic AI Research using OWL-based Knowledge Graphs in Visual Relationship Detection

## NeSy4VRD

NeSy4VRD is a multifaceted, multipurpose resource designed to foster neurosymbolic AI (NeSy) research, particularly NeSy research using Semantic Web technologies such as OWL ontologies, OWL-based knowledge graphs and OWL-based reasoning as symbolic components.

The NeSy4VRD resource in its entirety is distributed across two locations: here on GitHub, and on Zenodo.

## NeSy4VRD on Zenodo

The NeSy4VRD dataset, together with the official version of the NeSy4VRD OWL ontology, called VRD-World, that is coupled with that version of the NeSy4VRD dataset, are hosted on Zenodo, at
https://doi.org/10.5281/zenodo.7916355

The NeSy4VRD dataset consists of an image dataset with associated visual relationship annotations. The images of the NeSy4VRD dataset are the same as those that were once publicly available as part of the VRD dataset. The NeSy4VRD visual relationship annotations of those images are a highly customised and quality-improved version of the original VRD visual relationship annotations.  The NeSy4VRD dataset is designed for computer vision-based research that involves detecting objects in images and predicting the relationships between ordered pairs of those objects that have been annotated for the images.  A visual relationship for an image of the NeSy4VRD dataset has the form <'subject', 'predicate', 'object'>, where the 'subject' and 'object' are two objects in the image, and the 'predicate' describes some relation between them.  Both the 'subject' and 'object' objects are specified in terms of bounding boxes and object classes.  For example, typical visual relationships are <'person', 'ride', 'horse'>, <'hat', 'on', 'teddy bear'> and <'cat', 'under', 'pillow'>.

Visual relationship detection is pursued as a computer vision application task in its own right, and as a building block capability for the broader application task of scene graph generation.  Scene graph generation, in turn, is commonly used as a precursor to a variety of enriched, downstream visual understanding and reasoning application tasks, such as image captioning, visual question answering, image retrieval, image generation and multimedia event processing.

The NeSy4VRD OWL ontology, called VRD-World, is a well-aligned, companion to the NeSy4VRD dataset. It directly describes the domain of the NeSy4VRD dataset, as reflected in the NeSy4VRD visual relationship annotations.  For example, all of the object classes featuring in the visual relationship annotations have corresponding classes within the VRD-World class hierarchy, and all of the predicates featuring in the visual relationship annotations have corresponding object properties within the VRD-World object property hierarchy.

## NeSy4VRD on GitHub

All of the components of the NeSy4VRD research resource other than the two components (the dataset and the ontology) hosted on Zenodo are available here, on GitHub.

The components of NeSy4VRD available here on GitHub include:
1. comprehensive infrastructure supporting the extensibility of the NeSy4VRD visual relationship annotations (and, thereby, of the VRD-World ontology as well)
2. open source Python sample code for both loading the NeSy4VRD visual relationship annotations into a knowledge graph hosting the VRD-World ontology, and for extracting the same and reconstituting the visual relationship annotations in their native format, without loss of information.

The infrastructure for extensibility of the NeSy4VRD visual relationships includes:
* open source NeSy4VRD Python code for deep and comprehensive analysis of the VRD images and their associated NeSy4VRD visual relationship annotations
* an open source, custom designed NeSy4VRD protocol for specifying visual relationship annotation customisation instructions declaratively, in text files
* an open source, custom designed NeSy4VRD workflow (implemented in Python scripts and modules) for applying visual relationship annotation customisations in a managed, automated and repeatable process.

## Information pertaining to the VRD dataset

More information about the VRD dataset is available here: https://cs.stanford.edu/people/ranjaykrishna/vrd/ . The original VRD visual relationship annotations for the VRD images are still publicly available from that URL, as they have always been.  Public availability of the VRD images themselves (via information accessible from that URL), however, ceased sometime in the latter part of 2021.  We thank Dr. Ranjay Krishna, one of the principals associated with the VRD dataset, for granting us permission to re-establish the public availability of the VRD images as part of NeSy4VRD.

People wishing to use the original VRD dataset can thus still do so. They can access the VRD images from within the NeSy4VRD dataset entry on Zenodo, and access the VRD visual relationship annotations from the URL just mentioned.

**A note of caution**: the NeSy4VRD OWL ontology, VRD-World, is not compatible with the original VRD visual relationship annotations and cannot be used in conjunction with them.  The VRD-World ontology has been engineered in relation to the highly customised and quality-improved NeSy4VRD visual relationship annotations. The customisations that were applied include ones that introduced many new object classes, merged some of the existing object classes, introduced one new predicate, and changed several predicate names.

However, users can, if they wish, use the NeSy4VRD visual relationship annotation customisation extensibility infrastructure (available here, on GitHub) to undertake their own customisation exercise on the original VRD visual relationship annotations. This is precisely how the highly customised NeSy4VRD visual relationship annotations were created in the first place. The primary intended use case of NeSy4VRD's extensibility support infrastructure, however, is for researchers to use the NeSy4VRD visual relationship annotations as their starting point, and to take these forward with onward customisations, whether to further enrich the annotations, or to create new or more data conditions of particular interest for their research, or to establish the necessary conditions for adapting or extending the VRD-World OWL ontology in various ways.



