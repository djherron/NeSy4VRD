# NeSy4VRD: Annotation Customisation

This README discusses the topic of NeSy4VRD visual relationship annotation customisation in detail. It explains:
* the different categories of annotation customisation that are supported
* the different approaches to customising visual relationship annotations that are supported
* motivations for undertaking annotation customisation projects.


## Categories of customisation: modification vs. extension

The **NeSy4VRD extensibility support infrastructure** makes it easy to both *modify* and *extend* the NeSy4VRD visual relationship annotations. 

*Modification* refers to:
* *changing* existing visual relationships for VRD images in some way
* *removing* existing visual relationships for VRD images
* *removing* image entries from the NeSy4VRD annotations dictionary.

*Extension* refers to:
* *adding* (in the sense of introducing) new, supplementary visual relationships for VRD images.

Within the documentation for **NeSy4VRD**, for convenience we also often use the term *customisation* to refer to both *modification* and *extension* of the NeSy4VRD visual relationship annotations.

The **NeSy4VRD analysis** component of the **NeSy4VRD extensibility support infrastructure** makes it easy to find VRD images whose visual relationship annotations one may wish to customise in some way.

The **NeSy4VRD protocol** and **NeSy4VRD workflow** components of the **NeSy4VRD extensibility support infrastructure** make it easy to implement one's customisation wishes and choices.


## Approaches to annotation customisation

The **NeSy4VRD extensibility support infrastructure** provides *two* different *approaches* to customising the NeSy4VRD visual relationship annotations. One approach is designed for applying customisations to visual relationship annotations **individually**, and the other facilitates the application of customisations **collectively** (to groups of visual relationship annotations).

The **individual** approach to customisation supports both *modification* and  *extension* of the NeSy4VRD visual relationship annotations. The **collective** approach to customisation supports *modification* only.

### The individual approach

Under the **individual** approach to customising the NeSy4VRD visual relationship annotations, one hand-crafts declarative visual relationship annotation customisation instructions in text files. This **individual** approach to customisation provides the most low-level, granular and surgical control because it allows one to target: 1) *modifying* (i.e. changing or removing) specific visual relationships for specific VRD images, and 2) *extending* the annotations for specific VRD images by introducing new, additional visual relationships tailored specifically for them.

The **individual** approach to customising the NeSy4VRD visual relationship annotations is enabled by all three components of the **NeSy4VRD extensibility support infrastructure**: the **NeSy4VRD analysis** code, the **NeSy4VRD protocol**, and the **NeSy4VRD workflow**.

### The collective approach

Under the **collective** approach to customising the NeSy4VRD visual relationship annotations, one expresses desired *modifications* in terms of common *patterns* or *types* that are to be applied across groups of images (usually globally, across all VRD images, but sometimes also to specified subsets of VRD images). This **collective** approach to customisation provides convenience and efficiency: if a certain desired *modification* (change or removal) can be described as a pattern that applies to all instances of the pattern, then the *modification* can be applied *en masse*.

The **collective** approach to customising the NeSy4VRD visual relationship annotations is enabled by two of the three components of the **NeSy4VRD extensibility support infrastructure**: the **NeSy4VRD analysis** code, and the **NeSy4VRD workflow**.


## Motivations for customising annotations

Vision-based AI researchers (NeSy or not) may have diverse **motivations** for desiring to customise (modify and/or extend) the NeSy4VRD visual relationship annotations of the VRD images.  The **NeSy4VRD extensibility support infrastructure** makes it feasible and practical for researchers to *act* upon these **motivations**. Such **motivations** are likely to include the desire:
* [**$A$**] to further improve the overall quality of the annotations and/or to further enrich the annotations (e.g. by introducing more annotations that use the same set of object classes and predicates, by introducing additional object classes and associated new visual relationships, and/or by introducing additional predicates that express new categories of visual relationships);
* [**$B$**] to establish tailored data conditions that enable specialised experiments to be conducted and specialised hypotheses to be tested;
* [**$C$**] to increase the number of object classes and/or predicates so as to provide greater degrees of freedom to ontologists for customising and enriching the **NeSy4VRD ontology**, VRD-World, whilst maintaining its alignment with the NeSy4VRD visual relationship annotations.

These diverse **motivations** may each be pursued with an intention to **share** the fruits of the *annotation customisation project* by making them **public**, or to keep them **private**. Similarly, these **motivations** may each be pursued either with an attitude whereby the customisations are perceived as having enduring value and they are regarded as **permanent**, or with an attitude that perceives their value as being fleeting and they are regarded as **temporary**.

The table which follows places the three categories of **motivation** (**$A$**, **$B$** and **$C$**) in a grid formed by the intention as to **sharing** (**public** or **private**) and the attitude as to **longevity** (**permanent** or **temporary**) of the customisations made by hypothetical researchers. Hopefully this table will make it easier for the points we wish to make to be visualised and appreciated.

|             | permanent  | temporary    |
| ----------- | ---------- | ------------ |
| **public**  | $A$, $C$   | $B_2$, $C_2$ |
| **private** |            | $B_1$, $C_1$ |

Motivation **$A$** is most likely to be acted upon in scenarios where a researcher believes their customisations will have enduring value (**permanent**) and therefore should be shared and made **public**. 

Motivation **$B$** is most likely to be acted upon in scenarios where a researcher is primarily thinking about arranging optimal data conditions for particular specialised experiments (perhaps even just one). The mindset will likely be **private** and **temporary**, (**$B_1$**), because the specialised data conditions may only apply and only need to be instantiated long enough for that one specialised experiment to be conducted. But it is easy to share the results of an *annotation customisation project*, hence, a researcher's intention as to **sharing** can optionally and readily change such that motivation **$B$** later shifts from position **$B_1$** to **$B_2$**. This concept is consistent with the ethos of the *reproducability of research*.

Motivation **$C$** pertains best to NeSy researchers interested in using OWL ontologies and OWL-based knowledge graphs as symbolic components in NeSy systems and who are using the **NeSy4VRD ontology**, VRD-World, in that context. We anticipate that, in our conceptual landscape, motivation **$C$** for undertaking a NeSy4VRD annotation customisation project is equally likely to take the same position as motivation **$A$** or to follow the same trajectory as motivation **$B$**.

## Sharing NeSy4VRD annotation customisation projects

The idea of **sharing** NeSy4VRD annotation customisation projects is worth emphasising.  This is not a far-fetched concept.  The **NeSy4VRD extensibility support infrastructure** makes the idea of **sharing** a NeSy4VRD annotation customisation project that one undertakes **practical** and **useful**. It does so because the infrastructure simultaneously supports flexible ways for other researchers to **reuse** the NeSy4VRD annotation customisation projects that one undertakes and shares.  The infrastructure even supports the concept of a researcher **composing** multiple NeSy4VRD annotation customisation projects shared by diverse researchers in order to create a unique instance of the NeSy4VRD visual relationship annotations that combines the annotation enhancements of a particular set of customisation projects.

We call this concept of **sharing** and **reusing** and **composing** NeSy4VRD annotation customisation projects **Distributed Annotation Enhancement**. For more discussion and details concerning this concept and model of collaboration, please see the companion README files in this folder:
* README_DistributedAnnotationEnhancement.md
* README_SharingCustomisationProjects.md
* README_UsingSharedCustomisationProjects.md


