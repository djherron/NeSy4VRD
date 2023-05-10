NeSy4VRD ontology: VRD-World ontology files

This folder contains files for the NeSy4VRD OWL ontology called VRD-World.

The VRD-World OWL ontology is a well-aligned companion ontology for the NeSy4VRD dataset. The NeSy4VRD dataset consists of: 1) the VRD images, and 2) the NeSy4VRD visual relationship annotations.  The VRD-World OWL ontology describes the domain of the NeSy4VRD dataset, as reflected in the objects, object classes and predicates referenced in the NeSy4VRD visual relationship annotations of the VRD images.

It is conceivable that multiple versions of the VRD-World ontology can exist simultaneously whilst all of them are still perfectly aligned and compatible with a given version of the NeSy4VRD dataset.  Many ontology modelling decisions affecting the VRD-World class hierarchy and object property hierarchy can be taken without impacting alignment and compatibility in any way. Users of the NeSy4VRD dataset and the NeSy4VRD VRD-World OWL ontology should feel free to make copies of the VRD-World ontology and adapt it as they wish in order to explore their particular research ideas.

To maintain alignment and compatibility with the NeSy4VRD visual relationship annotations, the main considerations are as follows:

1) take care not to remove classes from the VRD-World class hierarchy that correspond directly to NeSy4VRD visual relationship object classes; altering other aspects of the class hierarchy should be feasible

2) take care not to remove object properties from the VRD-World property hierarchy; each object property corresponds to a NeSy4VRD visual relationship predicate or is otherwise needed to capture visual relationships in their entirety, including their relationships to the particular images with which they are associated; but altering other aspects of the object properties (such as their subPropertyOf and equivalence relationships, or their domain/range restrictions, or other characteristics) should be feasible without creating alignment problems

At some point NeSy4VRD may publish more than one version of the VRD-World ontology simultaneously. But, for now, we publish just one version at a time.

