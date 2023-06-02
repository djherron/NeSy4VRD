# NeSy4VRD: Using Shared Annotation Customisation Projects

This README discusses methods for **using** NeSy4VRD visual relationship annotation customisation/enhancement projects that have been **undertaken** and **shared** by other AI researchers.  In particular, it describes how these projects can be **reused** in isolation and/or **composed** with multiple other shared NeSy4VRD annotation customisation/enhancement projects to create unique permutations and combinations of NeSy4VRD visual relationship annotations.  As explained elsewhere, by enabling the capability to **undertake**, **share**, **reuse** and **compose** NeSy4VRD annotation customisation/enhancement projects, the **NeSy4VRD extensibility support infrastructure** enables a new model of collaborative data annotation that we call **Distributed Annotation Enhancement** (**DAE**).  The capabilities for the **reuse** and, especially, the **composition** of **shared** NeSy4VRD annotation customisation/enhancement projects that are described here, in this README, are the capabilities that enable the most exciting characteristics of this new **DAE** model of collaborative data annotation.

## The NeSy4VRD customisation project package structure

Before getting into the details of NeSy4VRD annotation customisation/enhancement project **reuse** and **composition**, let us first recall the structure recommended for NeSy4VRD customisation project packages, as defined in `README_SharingCustomisationProjects.md`:
```
nesy4vrd_annotations
    nesy4vrd_annotations_test.json
    nesy4vrd_annotations_train.json
    nesy4vrd_objects.json
    nesy4vrd_predicates.json
    readme.txt
nesy4vrd_customisation_project
    nesy4vrd_anno_cust_02_instructions_test.txt
    nesy4vrd_anno_cust_02_instructions_train.txt
    nesy4vrd_anno_cust_config_test.py
    nesy4vrd_anno_cust_config_train.py
    readme.txt
nesy4vrd_ontology
    readme.txt
    vrd_world.owl
```

## Reusing individual NeSy4VRD customisation projects

There are two ways for AI researchers to **reuse** an individual NeSy4VRD customisation project that has been **undertaken** and **shared** by another researcher. The simplest and most direct method is to use the annotations files provided in the `nesy4vrd_annotations` component (folder) of the customisation project package. If the AI researcher who is **reusing** the shared project is doing NeSy research using OWL ontologies or OWL-based knowledge graphs, the `nesy4vrd_ontology` component of the project package also comes into play. The VRD-World OWL ontology provided in the `nesy4vrd_ontology` component may or may not be aligned with the annotations provided in the `nesy4vrd_annotations` component of the project package. Information about this should be provided in the `readme.txt` file of the `nesy4vrd_ontology` component. If the ontology is not aligned with the annotations, the AI researcher who is **reusing** the shared project will need to customise the ontology manually in order to re-establish full alignment. 

The second method of **reuse** is to use the customisation project files provided in the `nesy4vrd_customisation_project` component (folder) of the customisation project package. The `readme.txt` file for that component will (*should*) explicitly specify the **starting point** of the customisation/enhancement project. This **starting point** could be:
* *(i)* the default NeSy4VRD visual relationship annotations published on Zenodo;
* *(ii)* the NeSy4VRD annotations from some other shared project;
* *(iii)* the default NeSy4VRD annotations composed with the customisations/enhancements of specified shared projects;
* *(iv)* the NeSy4VRD annotations from some other shared project composed with the customisations/enhancements of specified shared projects.

The AI researcher who is **reusing** the shared project will need to establish a set of NeSy4VRD visual relationship annotations that conforms to the specified **starting point** and then use the **NeSy4VRD workflow** infrastructure to *run* the customisation project for themselves, driven by the customisation project files provided in the `nesy4vrd_customisation_project` component. This procedure will result in a set of NeSy4VRD annotations files identical to the ones provided in the `nesy4vrd_annotations` component (folder) of the customisation project package.

Again, if the AI researcher who is **reusing** the shared project is doing NeSy research using OWL ontologies or OWL-based knowledge graphs, the `nesy4vrd_ontology` component of project package comes into play, and the question of whether the VRD-World OWL ontology is aligned with the annotations will need to be investigated (as described above). 

If the intention is to simply **reuse** the shared NeSy4VRD annotation customisation/enhancement project **as is** and **in isolation**, the first method of **reuse** described above is simpler than the second method (especially if a complex project **starting point** pertains, as in scenarios *(iii)* and *(iv)*).

But, while simple, the first method of **reuse** has limitations, because the prepared annotations files provided in the `nesy4vrd_annotations` component of the project package can participate in shared project **composition** in only one, strictly limited manner: as the **starting point** of a project **composition** exercise.

## Composing multiple NeSy4VRD customisation projects

Being able to **reuse** a shared NeSy4VRD annotation customisation/enhancement project by freely **composing** it with other shared projects, in unrestricted and arbitrary ways, is the essence of the value of the **Distributed Annotation Enhancement** (**DAE**) model of collaborative data annotation enabled by the **NeSy4VRD extensibility support infrastructure**. This ability to **reuse** multiple shared projects by freely **composing** them into unique permutations and combinations requires that AI researchers embrace the second, more complex method of **reuse** described above. 

It is precisely for this reason that the recommended structure of NeSy4VRD customisation project packages includes the `nesy4vrd_customisation_project` component and its prescribed contents. The **NeSy4VRD workflow** configuration module files, and the **NeSy4VRD protocol** annotation customisation instruction text files, allow anyone to **replay** or **rerun** the NeSy4VRD annotation customisation/enhancement project that has been shared, and to do so by **layering** those annotation customisations/enhancements upon any set of NeSy4VRD annotations, however established, by having previously **composed** other shared projects. 

### The value of the `nesy4vrd_customisation_project` files

It is important to recognise that the project files provided in the `nesy4vrd_customisation_project` component of the shared project package provide value in several ways. First, as just described, they allow anyone to **rerun** the annotation customisation/enhancement project for themselves (using the **NeSy4VRD workflow** infrastructure) so as to freely **compose** that project with any others. Second, they comprehensively document precisely what annotation customisations/enhancements are applied as part of the project. Third, they allow AI researchers who are **reusing** the shared project to modify and adapt the declarative annotation customisations/enhancements in any way, for any reason, prior to **rerunning** the project for **composition** purposes.

### Example of shared project composition

Here we consider a concrete example of **composing** multiple shared NeSy4VRD annotation customisation/enhancement projects.

First, let us set the context for the example. Suppose AI researcher **X** has **undertaken** and **shared** a NeSy4VRD annotation enhancement project that introduces a new object class of **water**. Researcher **X** will have  used the **NeSy4VRD analysis** infrastructure to find images with instances of **water** and will have introduced new visual relationships for these images that refer to these instances of **water** (e.g. `<boat, on, water>`). The new visual relationships will have been specified declaratively in **NeSy4VRD protocol** annotation customisation instruction text files using the **NeSy4VRD protocol** `avrxxx` (*add visual relationship*) instruction type. For simplicity, let us suppose that the **starting point** of researchers **X's** project was the default NeSy4VRD visual relationship annotations published on Zenodo, and let us denote these default annotations as $N$. Finally, researcher **X** may or may be doing NeSy research using OWL ontologies or OWL-based knowledge graphs and, so, may or may not have enhanced the companion VRD-World OWL ontology to stay fully aligned with enhanced NeSy4VRD visual relationship annotations.

Further suppose that AI researcher **Y** has **undertaken** and **shared** a very similar NeSy4VRD annotation enhancement project, but this time one that introduces a new object class of **snow**.

Now suppose that AI researcher **Z** has acquired the shared NeSy4VRD customisation/enhancement projects of both researcher **X** and **Y** and wishes to **compose** them in order to utilise the annotation enhancements (and potential VRD-World OWL ontology enhancements) of both. In other words, researcher **Z** wishes to **compose** a set of NeSy4VRD visual relationship annotations that we can denote as $$N + X + Y$$ where $N$ denotes the default NeSy4VRD annotations, $X$ denotes the annotation enhancements in the shared project of researcher **X**, and $Y$ denotes the annotation enhancements in the shared project of researcher **Y**.

Researcher **Z** can choose one of several approaches for achieving the target **composition** $N+X+Y$:
* *Approach 1:* Begin with the default NeSy4VRD annotations, $N$. Using the `nesy4vrd_customisation_project` files from the shared project of researcher **X** and the **NeSy4VRD workflow** infrastructure, **compose** $X$ with $N$, giving $N + X$. Finally, using the `nesy4vrd_customisation_project` files from the shared project of researcher **Y** and the **NeSy4VRD workflow**, **compose** $Y$ with $N+X$, giving $N + X + Y$.
* *Approach 2:* Begin with the `nesy4vrd_annotations` from the shared project of researcher **X**, which already represent the annotations $N + X$. Then, using the `nesy4vrd_customisation_project` files from the shared project of researcher **Y** and the **NeSy4VRD workflow**, **compose** $Y$ with $N+X$, giving $N + X + Y$.
* *Approach 3:* Begin with the `nesy4vrd_annotations` from the shared project of researcher **Y**, which already represent the annotations $N + Y$. Then, using the `nesy4vrd_customisation_project` files from the shared project of researcher **X** and the **NeSy4VRD workflow**, **compose** $X$ with $N+Y$, giving $N + Y + X$.

Note that the two compositions $N+X+Y$ and $N+Y+X$ are functionally equivalent. Hence, using either of these 3 approaches, researcher **Z** can **compose** the two shared projects and have an enhanced set of NeSy4VRD visual relationship annotations that include instances of the object classes **water** and **snow**.

If we further suppose that researcher **Z** is doing NeSy AI research using OWL ontologies or OWL-based knowledge graphs, researcher **Z** will also need to manually create a companion VRD-World OWL ontology that reflects the two new object classes for **water** and **snow** in order to have a companion OWL ontology that is fully aligned with the set of NeSy4VRD annotations $N+X+Y$. Researcher **X** may or may not have adjusted the VRD-World ontology in their shared project package to incorporate an OWL class for **water**. Similarly with researcher **Y** with regard to an OWL class for **snow**. Researcher **Z** will need to investigate and decide on the best course of action.

The **composition** concepts illustrated in this simple example can, in theory, be repeated an arbitrary number of times with respect to an arbitrary number of shared NeSy4VRD annotation customisation/enhancement projects.  So the possibilities for easily constructing elaborately enhanced versions of the NeSy4VRD visual relationship annotations by **composing** multiple shared NeSy4VRD annotation enhancement projects are very real.  And hence the implications of the **Distributed Annotation Enhancement** (**DAE**) model of collaborative data annotation enabled by the **NeSy4VRD extensibility support infrastructure** are potentially profound.




