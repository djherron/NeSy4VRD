# NeSy4VRD: Distributed Annotation Enhancement

The **NeSy4VRD extensibility support infrastructure** enables a **new model of collaboration** around dataset creation, sculpting and enhancement. The name we have adopted for this collaboration model is **Distributed Annotation Enhancement**, or **DAE**.

## Distributed Annotation Enhancement: overview

The key feature of the **NeSy4VRD extensibility support infrastructure** that enables the **DAE** model of collaboration is that it simultaneously supports all of the following activites:
1. **undertaking** NeSy4VRD annotation customisation projects
2. **sharing** NeSy4VRD annotation customisation projects
3. **reusing** other people's NeSy4VRD annotation customisation projects
4. **composing** diverse NeSy4VRD annotation customisation projects.

One might well initially **undertake** a NeSy4VRD annotation customisation project for personal and private reasons: e.g. to advance one's personal research vision. But having **undertaken** such a project, a researcher might come to feel that their project has value generally and opt to **share** the project. This gives other researchers the option to **reuse** the project for their own research and, potentially, to **compose** the project along with others to create a unique instance of the NeSy4VRD visual relationship annotations that combines the features and enhancements of diverse annotation customisation projects. 

The details around using the **NeSy4VRD extensibility support infrastructure** to **undertake** a NeSy4VRD annotation customisation project are documented extensively throughout the `extensibility` folder (and its subfolders) of the NeSy4VRD repository here on GitHub.

For details around **sharing**, **reusing** and **composing** NeSy4VRD annotation customisation projects, please see the following companion README files here in the `extensibility` folder:
* README_SharingCustomisationProjects.md
* README_UsingSharedCustomisationProjects.md


## DAE vs Crowdsourcing

one large project vs many small, independent projects
* CS is one project
* DAE is multiple, separate projects

organisation: distributed vs centralised
* in CS, there is some centralising authority that organises the project and consolidates the results into a final dataset
* in DAE, there is no centralising authority organising one overall project;

time: 
* CS for annotating a dataset can be regarded as a *point in time* project; the annotation work is distributed amongst participants, the work happens (roughly) concurrently, the contributions are assembled and consolidated, and the dataset is published
* DAE is more *longitudinal* in that it occurs *over time*; the distributed, uncoordinated contributions are created randomly and independently, *over time*, depending on the interests and motivations of individual researchers 


**Concept of central repository would facilitate sharing**
* sharing and reusing projects could be facilitated by having a central repository where projects could be posted and advertised; so there's one 'go to'  place to look for and review candidate projects, and common, curated information about the projects
* perhaps a rating scheme for contributors (sharers), so users can express satisfaction with their work

**the DAE model introduced by NeSy4VRD could be used for a crowdsourced project**
DAE offers another way of structuring a crowdsourced project
* with CS, the organisers partition the images into disjoint subsets, allocate a unique subset of images to each of the participating annotators, and have the annotators annotate each image in their entirety
* with DAE, each participant could be allocated the entire set of images and asked to annotate instances of just one or two object classes





**Guidelines for projects: reusing vs composing**

composing multiple projects can (in theory) result in 'conflicts' arising
* conflicts are akin to conflicts in software development, where multiple contributors to a code base make conflicting changes to one bit of code
* resolving the conflict requires analysis and a *merge* of the conflicting changes
* but these analysis and merge activities will always be local to a specific image; all the info to do the analysis and merge is available in the NeSy4VRD analysis code and the annotation customisation instruction text files

rvrxxx and avrxxx instructions are safest for 'composition'
* when composing multiple projects, conflicts between projects will never arise so long as those projects only use rvrxxx and avrxxx instructions
* cvr... can, in theory, lead to conflicts arising when composing multiple projects

any project can be reused, as is
* no restrictions on cvr, rvr, avr instructions

the projects that are most composable, without risk of conflicts, are ones that confine themselves to using rvrxxx and avrxxx instructions only

it's a trade-off each researcher needs to make
* the more cvr... instructions one uses, the more likely that conflicts might arise when used that project is composed with other projects
* but if one's personal research needs trump such composition considerations, so be it; you can still share your project, and researchers can still opt to reuse it, and even try to compose with it; 









