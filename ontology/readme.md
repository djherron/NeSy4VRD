# The NeSy4VRD OWL ontology: VRD-World

This folder contains the **NeSy4VRD ontology**, an OWL ontology called VRD-World.

## The **NeSy4VRD ontology**, VRD-World

The **NeSy4VRD ontology**, VRD-World, is a well-aligned, common sense companion OWL ontology for the **NeSy4VRD dataset**.

The **NeSy4VRD dataset** consists of:
1. the VRD images of the original VRD (Visual Relationship Detection) dataset  (information about which is available [here](https://cs.stanford.edu/people/ranjaykrishna/vrd/))
2. the NeSy4VRD visual relationship annotations, a highly customised and quality-improved version of the original VRD visual relationship annotations of the VRD images.

The **NeSy4VRD ontology**, VRD-World, describes the domain of the **NeSy4VRD dataset**, as reflected in the object classes and predicates referenced in the NeSy4VRD visual relationship annotations of the VRD images.

The primary and *official* means of publicly distributing the **NeSy4VRD ontology**, VRD-World, is via the **NeSy4VRD dataset package** published on [Zenodo](https://doi.org/10.5281/zenodo.7916355).  The **NeSy4VRD dataset package** on Zenodo packages the **NeSy4VRD dataset** and the **NeSy4VRD ontology** together in one **NeSy4VRD.zip** zip file.

We also keep copies of successive versions of VRD-World here, in this folder, as part of the NeSy4VRD GitHub repository.


## Version history for OWL ontology VRD-World

v1.2 - This version extends version 1.1 and refines the domain and/or range restrictions defined for a few of the version 1.1 object properties. The extensions involve introducing additional classes into the class hierarchy, all of whose names are prefixed with NOT_.  These NOT_ classes are 'complement' classes for use in class disjointness axioms, such as: vrd:Person owl:disjointWith vrd:Not_Person. Many such class disjointness axioms have been introduced as well, further extending the ontology.  These extensions permit OWL reasoning to use VRD-World v1.2 to classify visual relationships as being either semantically valid or invalid. That is, they permit an OWL-based knowledge graph hosting VRD-World v1.2 to be used as a symbolic reasoning binary classifier of visual relationships.  Relationships that trigger logical inconsistencies can be regarded as being semantically invalid; relationships that do not can be regarded as semantically valid. For example, governed by VRD-World v1.2, OWL reasoning over visual relationship (:person :ride :horse) would not lead to a logical inconsistency. But OWL reasoning over visual relationship (:person :drive :horse) would lead to a logical inconsistency, because the ontology does not declare (or entail) that a horse is driveable.

v1.1 - This version is identical to version 1.0 except for the fact that object property 'attachedTo' is no longer declared to be 'symmetric'. Declaring it to be symmetric was a mistake, and v1.1 corrects this mistake. A separate ontology file for this small change has not been released. The change has been absorbed into successors of version 1.1.

v1.0 - The original VRD-World.


## Extensibility of VRD-World whilst maintaining alignment with the NeSy4VRD dataset

Researchers need not regard OWL ontology VRD-World as being frozen. There is huge scope for customising VRD-World to suit particular research needs whilst maintaining full alignment with the NeSy4VRD dataset.

Alignment with the NeSy4VRD annotated visual relationships depends primarily on two things: 1) a mapping between NeSy4VRD object classes and VRD-World classes, and 2) a mapping between NeSy4VRD predicates and VRD-World object properties.

Regarding the VRD-World class hierarchy: you can modify and extend the class hierarchy of VRD-World and maintain full alignment with the NeSy4VRD annotated visual relationships as long as you do not remove any of the 109 OWL classes that correspond directly to NeSy4VRD object classes. These 109 OWL classes are the 'leaf' classes of the VRD-World class hierarchy.

Regarding the VRD-World object properties: you should not remove any object properties from NeSy4VRD if you want to maintain full alignment with the NeSy4VRD dataset. However, there is still huge scope for modifying these properties. You can 1) modify the characteristics of these properties (e.g. symmetric, transitive, etc.), 2) modify  relationships declared for these properties (e.g. inverse relationships, subproperty relationships, equivalent property relationships), and 3) modify domain and/or range restrictions declared for these properties. The settings for these properties in VRD-World are our default, common sense choices --- but these choices are subjective. One can also introduce new, additional object properties into VRD-WORLD without affecting alignment with NeSy4VRD in any way.

## Extensibility of VRD-World with respect to visual relationship classification

As of v1.2, the object property domain/range restrictions, together with the NOT_ classes and class disjointness axioms, of VRD-World permit OWL reasoning to classify visual relationships as being either semantically valid or semantically invalid. Assertions of visual relationships that trigger logical inconsistencies can be interpreted as being semantically invalid.

Changes to these elements of VRD-World are likely to have knock-on effects as to which visual relationships are classified as semantically valid or invalid.

All NeSy4VRD annotated visual relationships (training and test) are semantically valid according to VRD-World v1.2. That is, they can all be inserted into an OWL-based knowledge graph hosting VRD-World v1.2 and OWL reasoning will not detect any logical inconsistencies. Changes to the elements of VRD-World mentioned here may result in some NeSy4VRD annotated visual relationships inadvertently becoming 'semantically invalid' with respect to the adjusted ontology. Hence, adjustments to these aspects of VRD-World should be undertaken carefully, and whilst recognising this risk.

