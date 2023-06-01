# NeSy4VRD: Sharing Annotation Customisation Projects

This README discusses recommended best practice for **sharing** NeSy4VRD visual relationship annotation customisation projects **undertaken** by AI researchers. These recommendations for **sharing** are designed to facilitate and promote the other elements of the **Distributed Annotation Enhancement** (**DAE**) model of collaborative data annotation: **reusing** shared projects and **composing** multiple shared projects.

We introduce the concept of a **customisation project package**. We define the structure and content of this package and recommend it as the optimal and standard way to archive and distribute the results of any NeSy4VRD visual relationship annotation customisation project undertaken by an AI researcher.

We also propose the concept of a **central repository** for sharing NeSy4VRD **customisation project packages**. We discuss the utility of such a mechanism for advertising the existence of  shared NeSy4VRD **customisation project packages**, and we argue that this mechanism will best facilitate the **sharing**, **reusing** and **composing** of NeSy4VRD **customisation project packages** and, hence, serve to maximise the overall utility of NeSy4VRD as an AI research resource.


## NeSy4VRD customisation project packages

To share the results of a NeSy4VRD visual relationship annotation customisation project, we recommend creating a `.zip` file with the following folder structure and content. The three **components** (folders) of this archive are described in turn, below. It may well prove helpful if these shared archive files are named in a standard way, such as `nesy4vrd_<projectName>.zip`, where `<projectName>` is chosen by the AI researcher sharing the project.

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


### The `nesy4vrd_annotations` component

The `nesy4vrd_annotations` component of a NeSy4VRD customisation project package is a directory identical in structure and content to the similarly named directory present in the **NeSy4VRD dataset package** published on [Zenodo](https://doi.org/10.5281/zenodo.7916355). The only difference is that the files in this component of a shared NeSy4VRD customisation project package will be **updated versions** of the corresponding original NeSy4VRD files. These **updated versions** are the concrete results (the deliverable) of the NeSy4VRD customisation project.

If the customisation project introduced no new object classes, the `nesy4vrd_objects.json` file will be the original NeSy4VRD file. Similarly, if the customisation project introduced no new predicates and did not alter the names of any of the existing predicates, the `nesy4vrd_predicates.json` file will be the original NeSy4VRD file.

In all conceivable cases, both the `nesy4vrd_annotations_train.json` and `nesy4vrd_annotations_test.json` files will be updated versions of the corresponding NeSy4VRD originals, otherwise no annotation customisations or enhancements will have been applied.

Whether the `readme.txt` file is a copy of the original or an updated version will depend on the nature of the customisation project and the judgement of the AI researcher. It may well be helpful to highlight relevant information pertaining to the customisation project, particularly if the changes were applied to the lists of object classes and/or predicates.


### The `nesy4vrd_customisation_project` component

The `nesy4vrd_customisation_project` component of a NeSy4VRD customisation project package is a directory containing copies of all of the **NeSy4VRD workflow** assets that were configured and crafted in order to conduct the annotation customisation project.

These assets must always include the pair of **NeSy4VRD workflow** Python configuration modules crafted to drive the customisation project, one for the *training set* run and one for the *test set* run of the workflow. The two such module files mentioned above, `nesy4vrd_anno_cust_config_train.py` and `nesy4vrd_anno_cust_config_test.py`, are provided for illustration purposes. The actual names of these two configuration module files may vary.

The **NeSy4VRD workflow** assets in this directory must also include all of the **NeSy4VRD protocol** annotation customisation instruction text files crafted for the project. The number of such text files (and their names) will vary. (Zero such text files is a possibility, but such a customisation project would be an extreme edge case.) The two instruction text files mentioned above, `nesy4vrd_anno_cust_02_instructions_train.txt` and `nesy4vrd_anno_cust_02_instructions_test.txt`, are representative and are provided for illustration purposes.

#### The `readme.txt` file

Including a `readme.txt` file in the `nesy4vrd_customisation_project` directory is also highly recommended.  This file provides a logical place to explain the nature, motivation, objectives, and scope of the NeSy4VRD annotation customisation project. While the pair of **NeSy4VRD workflow** configuration module files, together with the **NeSy4VRD protocol** annotation customisation instruction text files, do, in fact, provide complete documentation of any NeSy4VRD annotation customisation project, the information they contain is low-level. A high-level project summary in a supplementary `readme.txt` file is likely to best facilitate and promote project **reuse** and **composition**. Such a summary will make it easier for AI researchers who may be considering whether to **reuse** the shared project to come to a decision. And it will have particular value to AI researchers whose reuse considerations extend to potentially **composing** the shared project with other projects (either their own projects and/or with other shared projects).

#### The `readme.txt` file and project *starting points*

Another important role for the recommended `readme.txt` file is to be the place where the AI researcher who is sharing the project specifies precisely the **starting point** for the annotation customisation/enhancement project.  The **default starting point** will be the NeSy4VRD visual relationship annotations distributed in the **NeSy4VRD dataset package** published on Zenodo. But even here the possibility exists for multiple versions of the NeSy4VRD visual relationship annotations to emerge over time and be published on Zenodo under different version numbers. So if the starting point for a NeSy4VRD annotation customisation/enhancement project is the annotations in a **NeSy4VRD dataset package** published on Zenodo, it would be good practice to always specify the **version number** that dataset package **explicitly**.

Interestingly, however, the project **reuse** and **composition** capabilities of the **Distributed Annotation Enhancement** model of collaborative data annotation enabled by NeSy4VRD means that the **starting point** for an annotation customisation/enhancement project need not necessarily be the default NeSy4VRD visual relationship annotations distributed on Zenodo. It is quite feasible for AI researchers to start their annotation customisation/enhancement projects by building upon a **shared** project that they are **reusing**. It is equally feasible for AI researchers to start their annotation customisation/enhancement projects by first **composing** an arbitrary set of **shared** projects and then building upon that cumulative base. In such cases, **explicitly specifying the starting point** of the annotation customisation/enhancement project that is being shared is **essential**. Otherwise, although **reuse** of the shared project would always be feasible (via the annotation files packaged in the `nesy4vrd_annotations` directory), use of the project's **NeSy4VRD workflow** configuration module files, together with its **NeSy4VRD protocol** annotation customisation instruction text files for **composition** purposes could be infeasible.  Composition could be infeasible if these project files contain dependencies upon the shared projects that were originally used to establish the project's **starting point**.

For example, suppose we use $N$ to denote the default NeSy4VRD visual relationship annotations published on Zenodo. And suppose we use $A$ and $B$ to denote two **shared** projects that have been **composed** (in that order) with $N$ to establish the **starting point** for a new annotation customisation/enhancement project that we denote by $C$. In this case, the **starting point** for project $C$ can be described as
$$N + A + B.$$ The project files packaged in directory `nesy4vrd_customisation_project` for shared project $C$ need be only the files specific to project $C$, because the files for projects $A$ and $B$, if needed, can be obtained online from their NeSy4VRD customisation project packages. But if the project files for project $C$ have dependencies upon projects $A$ and $B$, it may not be feasible to run them cleanly without first having **composed** projects $A$ and $B$. So researchers considering whether to **reuse** or **compose** project $C$ need to know this information --- that is, they need to be told explicitly that the **starting point** of project $C$ was $N + A + B$.


### The `nesy4vrd_ontology` component

The `nesy4vrd_ontology` component of a NeSy4VRD customisation project package is a directory containing one or more versions of the NeSy4VRD VRD-World OWL ontology that is a companion of the customised and/or enhanced NeSy4VRD visual relationship annotations in the `nesy4vrd_annotations` directory.

#### Researchers doing NeSy AI using OWL-based knowledge graphs

If the AI researcher who conducted the annotation customisation project that is being shared **is pursuing NeSy research using OWL ontologies or OWL-based knowledge graphs**, we ask that such researchers recognise an obligation to ensure that the version (or versions) of the VRD-World OWL ontology packaged in this `nesy4vrd_ontology` directory be **fully aligned and compatible** with the customised/enhanced annotations in the `nesy4vrd_annotations` directory.  In short: researchers with the Semantic Web knowledge and skills to keep the VRD-World OWL ontology aligned with their customised/enhanced annotations should please do so. If the original VRD-World OWL ontology is still fully aligned and compatible, it should be included in this directory. If a customised/enhanced version of the VRD-World OWL ontology was developed by the AI researcher, it should be included in this directory (as a contribution to the **NeSy AI using OWL-based knowledge graphs** research community).

This last point is important because it illustrates that the vision behind the concept of the **Distributed Annotation Enhancement** model of collaborative data annotation extends beyond the annotations themselves to the companion OWL ontology as well.  Researchers pursuing NeSy AI using OWL-based knowledge graphs can **undertake**, **share** and **reuse** OWL ontology customisations and enhancements in tandem with annotation customisations/enhancements.  **Composing** multiple shared OWL ontology enhancement projects is also a possibility, but currently NeSy4VRD does not provide an automated mechanism for achieving such composition.  In other words, NeSy4VRD does not currently provide infrastructure akin to the **NeSy4VRD protocol** and **NeSy4VRD workflow** which, together, enable automated **composition** of annotation customisation/enhancement projects. Currently, **composing** multiple VRD-World OWL ontology customisations/enhancements would need to be performed manually using (presumably) an ontology editor such as Protege.

We recommend that a `readme.txt` file be included in the `nesy4vrd_ontology` directory. This file can be used to communicate all pertinent information concerning the version (or versions) of the VRD-World OWL ontology files included in this directory.

#### Other researchers

If the AI researcher who conducted the annotation customisation project that is being shared **is NOT pursuing NeSy research using OWL ontologies or OWL-based knowledge graphs**, we recommend that the version of the VRD-World OWL ontology packaged in the `nesy4vrd_ontology` directory **should always be the original** VRD-World OWL ontology distributed in the **NeSy4VRD dataset package** on Zenodo.

We recommend that a `readme.txt` file be included in the `nesy4vrd_ontology` directory. In this case, the AI researcher who is sharing the annotation customisation project can use this `readme.txt` file to make it clear that their project did not touch the VRD-World OWL ontology and that, therefore, it may or may not be fully aligned with their annotation customisations/enhancements.  In other words, the AI researcher sharing the project can warn prospective **reusers** of their project that they must evaluate the nature of the annotation customisations/enhancements that were applied (as documented in the `nesy4vrd_customisation_project` directory) and come to their own assessment as to whether the companion VRD-World OWL ontology is still fully aligned with the project's annotations or not.

The original VRD-World OWL ontology may still be aligned with the annotations: it depends on the nature of the customisations/enhancements that were applied. If no changes or additions were made to the NeSy4VRD object class names and predicate names, then full alignment will still exist. But otherwise, not.

## Rationale for the customisation project package structure

The reason for recommending that both the `nesy4vrd_annotations` and `nesy4vrd_customisation_project` components are included in a NeSy4VRD customisation project package is that **sharing** both of these components best facilitates and promotes the **reusing** and **composing** aspects of the **Distributed Annotation Enhancement** model for collaborative data annotation. The former component permits project **reuse** most readily; but the latter component offers the greatest flexibility, by permitting both project **reuse** and project **composition** to be realised. More information on these topics is provided in the file `README_UsingSharedCustomisationProjects.md`.


## Central repository to facilitate project sharing

For the **Distributed Annotation Enhancement** (**DAE**) model of collaborative data annotation to function optimally, it needs to be **easy to share** NeSy4VRD annotation customisation/enhancement projects (including their associated, and potentially enhanced, VRD-World OWL ontologies). It also needs to be **easy to find** shared projects, so that they can most readily be **reused** and **composed** with one another. This points to the **utility** of having a **central repository** for **sharing** all NeSy4VRD annotation customisation/enhancement  projects.

A **central repository** would provide one single **go to** place for **sharing** projects and project information, for **reviewing** shared projects, and for **accessing** shared projects for **reuse** and **composition**.  For a **central repository** to have **utility**, it need not necessarily physically host the **NeSy4VRD customisation project package** archive (`.zip`) files of each shared project.  It would be sufficient for the **central repository** to have some basic summary information about a shared project and a *hyperlink* to where the project's physical **NeSy4VRD customisation project package** archive (`.zip`) file can be accessed.  AI researchers would be free to choose which approach they prefer: to have the central repository host their project's archive (`.zip`) file or to simply advertise a *hyperlink* to their project's archive (`.zip`) file. 

One **logical candidate** for such a **central repository** is this NeSy4VRD repository here on GitHub. The `shared_projects` folder of this NeSy4VRD GitHub repo has been created with this purpose in mind.  It is available now to be used for advertising, publishing and sharing information about NeSy4VRD annotation customisation/enhancement projects. The **README** file in the `shared_projects` folder is envisaged as becoming the primary place to advertise the existence of  shared projects. For researchers who opt to have their project's `nesy4vrd_<projectName>.zip` file hosted in the NeSy4VRD `shared_projects` folder, a dedicated subfolder can be created in which to store it. Otherwise, the README can be used to *hyperlink* to the location from which the project's `nesy4vrd_<projectName>.zip` file can be accessed.

The size of a **NeSy4VRD customisation project package**, as described above, has been estimated to be under 6.5 MB uncompressed, and under 1 MB compressed. So a large number of physical `nesy4vrd_<projectName>.zip` project files can be hosted in the NeSy4VRD `shared_projects` folder before space considerations become an issue.  GitHub's established **pull request** functionality can be used to manage the process by which AI researchers publish their shared projects in the NeSy4VRD `shared_projects` folder.  For more information on this topic, see the NeSy4VRD `shared_projects` folder.




