# The NeSy4VRD OWL ontology: VRD-World

This folder contains the **NeSy4VRD ontology**, an OWL ontology called VRD-World.

## The VRD-World OWL ontology

The **NeSy4VRD ontology**, VRD-World, is a well-aligned companion ontology for the **NeSy4VRD dataset**.

The **NeSy4VRD dataset** consists of:
1. the VRD images of the original VRD (Visual Relationship Detection) dataset  (information about which is available [here](https://cs.stanford.edu/people/ranjaykrishna/vrd/))
2. the NeSy4VRD visual relationship annotations, a highly customised and quality-improved version of the original VRD visual relationship annotations of the VRD images.

The **NeSy4VRD ontology**, VRD-World, describes the domain of the **NeSy4VRD dataset**, as reflected in the NeSy4VRD object classes and predicates referenced in the NeSy4VRD visual relationship annotations of the VRD images.

## NeSy4VRD versions of VRD-World

The primary and *official* means of publicly distributing the VRD-World OWL ontology is **NOT** via this folder on GitHub.  It is via the NeSy4VRD dataset package published on [Zenodo](https://doi.org/10.5281/zenodo.7916355).  That package will always contain both the NeSy4VRD dataset (VRD images and NeSy4VRD visual relationship annotations) and the NeSy4VRD VRD-World OWL ontology (the version of which is guaranteed to be perfectly aligned and compatible with the version of the NeSy4VRD dataset with which it is coupled in the package).

It is conceivable that, over time, multiple different *official* versions of the NeSy4VRD OWL ontology, VRD-World, may gradually evolve and accumulate. As and when this occurs, the files for these different versions of VRD-World will be hosted here.  We will maintain a record (on this README) of alignment relationships between the potential successive versions of the VRD-World ontology and any (potential) successive versions of the NeSy4VRD dataset.

## Researcher customised versions of VRD-World

It is entirely feasible for multiple, customised versions of the VRD-World ontology to exist which possess perfect alignment with the NeSy4VRD dataset (distributed via Zenodo). Many ontology modelling decisions affecting the VRD-World class hierarchy and object property hierarchy may be taken that do not impact that alignment or compatibility in any way.

Researchers using the NeSy4VRD dataset and VRD-World OWL ontology should therefore feel free to make their own copies of the VRD-World ontology and adapt them in order to create ontologies that better reflect their own personal modeling preferences and/or particular research needs or ideas.

## Considerations concerning maintaining alignment with the NeSy4VRD dataset

To maintain alignment and compatibility with the NeSy4VRD visual relationship annotations of the NeSy4VRD dataset, the main considerations are as follows:

1) Take care not to *remove* classes from the VRD-World class hierarchy that correspond directly to NeSy4VRD visual relationship object classes. Altering other aspects of the class hierarchy should be feasible without affecting dataset alignment. The association between NeSy4VRD visual relationship object class names and VRD-World class names is always clear and obvious: the latter is a capitalised version of the former. And, with just one exception, (VRD-World class vrd:Glasses), all VRD-World classes that correspond to NeSy4VRD visual relationship object classes are *leaf nodes* in the VRD-World class hierarchy.

2) Take care not to *remove* object properties from the VRD-World property hierarchy. Each object property corresponds to a NeSy4VRD visual relationship predicate or is otherwise needed to capture visual relationships in their entirety, such as the relationships between individual objects and the unique image with which they are associated. But altering aspects of the object property descriptions (such as their subproperty and equivalence relationships, or the class names used for their domain and range restrictions, or their individual property characteristics) should be feasible without affecting alignment. Such ontology modifications will of course impact the outcome of any OWL and/or Datalog reasoning that might be undertaken, in themselves they should be safe from a dataset alignment perspective.


