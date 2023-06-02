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


## Shared project composition and potential incompatibilities

Shared NeSy4VRD annotation customisation/enhancement project **composition** makes the **Distributed Annotation Enhancement** (**DAE**) model of collaborative data annotation particularly attractive. But project **composition** may not always be pure **clear sailing**. This is because it is possible that minor **incompatibilities** may exist within the **NeSy4VRD protocol** annotation customisation instructions declared for different NeSy4VRD projects with respect to common VRD images. If any such **incompatibilities** do exist between shared NeSy4VRD projects, they will be detected by the protocol driver of the **NeSy4VRD workflow** when it is processing a **NeSy4VRD protocol** annotation customisation instruction text file.

**Incompatibilities** between the NeSy4VRD annotation customisations of different shared NeSy4VRD projects are analogous to **conflicts** that can emerge in software development projects when multiple developers contribute to a common code base.  Sometimes two changes proposed for the same bit of code **conflict** with one another. The version control software (`git`, say) may detect and report a **conflict** during a `git merge` or `git pull` operation, for example. If so, the developer investigates and resolves the **conflict** manually.  The same applies to **incompatibilities** between shared NeSy4VRD projects detected by the protocol driver of the **NeSy4VRD workflow** during NeSy4VRD project **composition** exercises. If the protocol driver aborts and reports an **incompatibility**, the AI researcher needs to investigate and resolve the **incompatibility** manually (by amending the annotation customisation instruction involved in the **incompatibility** appropriately) before proceeding by re-running the protocol driver.

There are several bits of **good news** in relation to potential **incompatiblities**:
* First, like **conflicts** in collaborative software development, **incompatibilities** in **DAE** collaborative data annotation are **highly localised**. In the case of NeSy4VRD annotation customisation/enhancement projects, an **incompatibility** will **always** be local to a particular VRD image and **usually** be local to a specific annotated visual relationship for that VRD image.
* Second, with 4000 training images and 1000 test images, the likelihood of two shared NeSy4VRD annotation customisation/enhancement projects containing **incompatible** changes to the same visual relationship for the same image is low. So even if **incompatibilities** do sometimes arise, their **overall volume is highly likely to be very small**.
* Third, if and when **incompatibilities** do arise, they are **easy to investigate and resolve**. The **NeSy4VRD analysis** component of the **NeSy4VRD extensibility support infrastructure** provides comprehensive means for displaying and analysing the visual relationship annotations of any VRD image. The AI researcher need only review these and compare them with the **NeSy4VRD protocol** annotation customisation instruction reported as being incompatible by the protocol driver script. The researcher will  quickly come to a decision how best to amend the customisation instruction in question in order to resolve the incompatibility.
* Finally, only some of the **NeSy4VRD protocol** instruction types carry an associated risk of leading to a potential **incompatibility** between shared NeSy4VRD projects. Hence, it is possible for AI researchers to **undertake** and **share** meaningful and valuable NeSy4VRD annotation enhancement projects, and thereby contribute to demonstrating the value of **DAE** collaborative data annotation, with **zero risk** of their shared project ever being involved in an incompatibility with another shared NeSy4VRD project.


## NeSy4VRD protocol instructions and risk of incompatibilities

Here we review the **NeSy4VRD protocol** instruction types from the perspective of the relative risk they carry of being involved in potential **incompatibilities** when multiple shared NeSy4VRD projects are **composed** with one another. The full **NeSy4VRD protocol** specification, containing full details of all of the instruction types, is in the main `README.md` file in the `extensibility/protocol` folder of this GitHub repo. 

### The `cvr...` instruction types and incompatibility risk

The **NeSy4VRD protocol** specification defines five **change visual relationship**, `cvr...`, instruction types that consist of 4 components conforming to the following pattern:
```
cvr...; vr_index; vr_description; new_value
```
These five instruction types relate to the five components of every NeSy4VRD annotated visual relationship:
* `cvrsoc`: change visual relationship *'subject' object class*
* `cvrsbb`: change visual relationship *'subject' bounding box*
* `cvrpxx`: change visual relationship *predicate*
* `cvrooc`: change visual relationship *'object' object class*
* `cvrobb`: change visual relationship *'object' bounding box*

For example, two sample instances of `cvr...` instruction types are:
```
imname; 3223670633_7d3d72dfe8_b.jpg
cvrsoc; 4; ('person', 'on', 'shelf'); speaker
cvrsbb; 4; ('speaker', 'on', 'shelf'); [161,234,231,270]
```
where the *4* is a `vr_index` and *('person', 'on', 'shelf')* is a `vr_description`. As explained in the **NeSy4VRD protocol** specification, the `vr_description` in an annotation customisation instruction must **match** the actual visual relationship held internally, in memory, at the index position corresponding to the specified `vr_index`. This is an important **quality control mechanism** and discipline that prevents inadvertent errors being made in annotation customisation instructions.

If an **incompatibility** involving a `cvr...` instruction arises between shared NeSy4VRD projects that are being **composed** with one another, it will arise because of a mismatch between the `vr_description` in an instruction and the internal, in memory, visual relationship at the specified `vr_index`.  Suppose an AI researcher has acquired two shared projects, $X$ and $Y$, and first **composes** project $X$. Suppose project $X$ contains the annotation customisation instruction
``` 
imname; 3223670633_7d3d72dfe8_b.jpg
cvrsoc; 4; ('person', 'on', 'shelf'); speaker
```
If project $Y$ also contains a `cvr...` instruction for the same image and the same visual relationship, at `vr_index` 4, if that instruction also uses the `vr_description` *('person', 'on', 'shelf')*, a mismatch will be detected by the protocol driver of the **NeSy4VRD workflow** because when project $X$ was **composed**, the visual relationship for that image at `vr_index` 4 was changed and is now *('speaker', 'on', 'shelf')*, not *('person', 'on', 'shelf')*.

Notice also that the `vr_description` components of `cvr...` instructions refer only to *object class* names and *predicate* names, not to *bounding box specifications*.  This means that use of two of the five `cvr...` instruction types, `cvrsbb` and `cvrobb`, can **never** lead to **incompatibilities** between shared NeSy4VRD projects during **composition** exercises.

### The `rvrxxx` instruction type and incompatibility risk

The **NeSy4VRD protocol** specification defines one **remove visual relationship**, `rvrxxx`, instruction type that consists of 3 components conforming to the following pattern:
```
rvrxxx; vr_index; vr_description
```
For example, a sample instance of an `rvrxxx` instruction type is:
```
imname; 4929276486_ca06aedbb9_b.jpg
rvrxxx; 4; ('person', 'wear', 'jacket');
```
Suppose an AI researcher has acquired two shared projects, $X$ and $Y$, and first **composes** project $X$. Suppose that project $X$ contains the sample annotation customisation instruction just given. In memory, the visual relationships for an image are maintained in a Python `List`, so once the visual relationship at `vr_index` 4 is removed, the positions of all subsequent visual relationships in that list change --- they are decremented by 1. So if project $Y$ contains an annotation customisation instruction for this image (either a `cvr...` instruction, or and `rvrxxx` instruction) that references a `vr_index` greater than 3, it is most likely that a mismatch will be detected between the `vr_description` specified in that instruction and the actual, in memory, visual relationship that exists at that specified `vr_index`.  Thus, in terms of **relative risk of incompatibilities arising** between shared NeSy4VRD projects during **composition** exercises, the *remove visual relationship*, or `rvrxxx`, instruction ranks fairly high.

### The `avrxxx` instruction type and incompatibility risk

The **NeSy4VRD protocol** specification defines one **add visual relationship**, `avrxxx`, instruction type that consists of 6 components conforming to the following pattern:
```
avrxxx; soc; sbb; pxx; ooc; obb
```
For example, sample instances of `avrxxx` instruction types are:
```
imname; 4929276486_ca06aedbb9_b.jpg
avrxxx; boat; [477,594,319,746]; has; dog; [478,529,587,618]
avrxxx; boat; [477,594,319,746]; carry; dog; [478,529,587,618]
```
Notice that `avrxxx` instructions are not constructed using either `vr_index` or `vr_description` components.  New visual relationships introduced by the `avrxxx` instruction type are always simply **appended** to the end of the Python `List` holding the visual relationships for an image. This means that mismatches between a `vr_description` and the actual visual relationship that exists, in memory, at a specified `vr_index` position can never arise in relation to an `avrxxx` instruction. Thus, in terms of **relative risk of incompatibilities arising**, the `avrxxx` instruction type is the **safest** of all because its use can never lead to an **incompatibility** arising between shared NeSy4VRD annotation customisation/enhancement projects during project **composition**.

### The `rimxxx` instruction type and incompatibility risk

The **NeSy4VRD protocol** specification defines one **remove image**, `rimxxx`, instruction type is an optional component of an **image name**, `imname`, instruction type. An example instance of the `rimxxx` instruction is given here:
```
imname; 7171463996_900cb4ce33_b.jpg; rimxxx
```
The presence of the `rimxxx` component of the `imname` instruction declares that the `key:value` entry for the specified image is to be removed from the NeSy4VRD annotations dictionary altogether. Suppose once again that an AI researcher has acquired two shared NeSy4VRD projects, $X$ and $Y$, and first **composes** project $X$. And suppose that project $X$ contains the `imname` instruction given above, containing the optional `rimxxx` component. If project $Y$ contains an `imname` instruction specifying the same image name, the protocol driver of the **NeSy4VRD workflow** will abort and report that the specified image is **not recognised**, because it no longer exists in the NeSy4VRD annotations dictionary. So **none** of the annotation customisation instructions that project $Y$ may have declared in relation to that particular image will be able to be processed. Thus, in terms of **relative risk of incompatibilities arising** between shared NeSy4VRD projects during **composition** exercises, use of the `rimxxx` instruction type is the **riskiest** instruction of all!

### Summary ranking of instructions by risk of incompatibilities

For reader convenience, here we rank the various **NeSy4VRD protocol** instruction types mentioned above in terms of **relative risk of incompatibilities arising** between shared NeSy4VRD annotation customisation/enhancement projects during **composition** exercises. The ranking is in **descending** order by level of relative risk of **incompatibilities** arising:
1. `rimxxx` - *remove image*
2. `rvrxxx` - *remove visual relationship*
3. `cvrsoc`, `cvspxx`, `cvrooc` - *change visual relationship*

The instruction types `cvrsbb`, `cvrobb` and `avrxxx` carry **zero risk** of **incompatibilities** arising between shared NeSy4VRD projects during **composition**, so, for clarity, we exclude these from the above relative risk ranking altogether.

Finally, to re-emphasise what has already been highlighted above, it is important to remember that the **incidence rate** of **incompatibilities** between shared NeSy4VRD projects during **composition** exercises is expected to be **very low**, regardless of which **NeSy4VRD protocol** instruction types AI researchers choose to use in their shared projects. And if and when **incompatibilities** do arise during **composition** they are **easy to resolve**.  

