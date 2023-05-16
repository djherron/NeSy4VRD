# NeSy4VRD: Using Shared Annotation Customisation Projects

This README discusses methods for **using** NeSy4VRD visual relationship annotation customisation projects that have been undertaken and shared by other researchers.  In particular, it illustrates how the **NeSy4VRD workflow** and the corresponding Python configuration modules and **NeSy4VRD protocol** annotation customisation instruction text files used for NeSy4VRD annotation customisation projects can be used to **amalgamate multiple** NeSy4VRD annotation customisation projects conducted and shared by different researchers.

To properly understand this README, readers should first familiarise themselves with the rest of the **NeSy4VRD extensibility support infrastructure**, in particular the **NeSy4VRD workflow** and the `README_SharingCustomisationProjects.md` document that resides in this folder.

First, recall from `README_SharingCustomisationProjects.md`, that the `.zip` file created for sharing a NeSy4VRD visual relationship annotation customisation project is recommended to contain these three component directories:
1. a `nesy4vrd_annotations` directory
2. a `nesy4vrd_ontology` directory
3. a `nesy4vrd_customisation_project` directory.

We refer to these component directories in the sections which follow.


## Component 1: the nesy4vrd_annotations directory

Including component (1) in the package that shares a NeSy4VRD annotation customisation project makes sense because component (1) is the easiest way for a researcher to explore and use the results of another researcher's annotation customisation project. Some researchers may find this means of sharing sufficient. But while component (1) provides an **easy** way to use a shared NeSy4VRD annotation customisation project, it has inherent limitations. Specifically, it **does not facilitate amalgamation** of multiple different customisation projects undertaken by multiple different researchers.


## Component 3: the nesy4vrd_customisation_project directory

Also including component (3) in the package that shares a NeSy4VRD annotation customisation project makes sense for two key reasons. First, the configuration modules and text files of component (3) **fully document** precisely what NeSy4VRD visual relationship annotations were applied as part of the customisation project. In this sense, a NeSy4VRD customisation project undertaken using the **NeSy4VRD workflow** is **self-documenting**.  Second, component (3) **facilitates amalgamation** of multiple different customisation projects undertaken by multiple different researchers. 

Let us consider an example where researcher **Z** has acquired the NeSy4VRD customisation project package shared by researcher **X**. Suppose, for illustration purposes, that the project undertaken by researcher **X** was to introduce a new object class by annotating instances of *water* and by introducing new visual relationships that refer to these instances of *water*. Researcher **Z** can take the project files of component (3) from the project package shared by researcher **X** and, using the **NeSy4VRD workflow**, run these files against their own copies of the NeSy4VRD visual relationship annotation files. In doing so, researcher **Z** is applying the precise set of annotation customisations that were crafted by researcher **X** and now has an instance of the NeSy4VRD visual relationship annotations that include the object class *water*.

But now researcher **Z** can do the same thing with respect to a NeSy4VRD customisation project package shared by researcher **Y**. Suppose, for illustration purposes, that the project undertaken by researcher **Y** was to introduce a new object class by annotating instances of *snow* and by introducing new visual relationship annotations that refer to these instances of *snow*. Researcher **Z** can *apply* or *run in* the annotation customisations crafted by researcher **Y** *on top of* the annotation customisations crafted by researcher **X** with respect to *water*. Researcher **Z** will now have an instance of the NeSy4VRD visual relationship annotations that have been enriched by instances of both *water* and *snow*, and by relationships that refer to both *water* and *snow*.

The same concept can, in theory, be repeated an arbitrary number of times with respect to an arbitrary number of shared NeSy4VRD annotation customisation projects.



