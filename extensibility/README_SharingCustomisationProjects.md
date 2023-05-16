# NeSy4VRD: Sharing Annotation Customisation Projects

This README discusses the recommended way of sharing NeSy4VRD visual relationship annotation customisation projects.

For researchers who are minded to share the results of their NeSy4VRD visual relationship annotation customisation projects (and their potential companion **NeSy4VRD ontology** customisation projects), here we describe recommended sharing practice.  To fully appreciate all of the details discussed here, readers may wish to first consult the **NeSy4VRD dataset package** entry on Zenodo, and read the README.md files associated with the **NeSy4VRD protocol** and **NeSy4VRD workflow** components of the **NeSy4VRD extensibility support infrastructure** here on GitHub.

## Customisation project package

To share the results of a NeSy4VRD visual relationship annotation customisation project, we recommend creating a `.zip` file with the following structure and content.

1. A copy of the `nesy4vrd_annotations` directory that was created by the annotation customisation project. Some or all of these files will be updated versions of the originals, depending on the nature and extent of the customisations applied in the project.
```
nesy4vrd_annotations
    nesy4vrd_annotations_test.json
    nesy4vrd_annotations_train.json
    nesy4vrd_objects.json
    nesy4vrd_predicates.json
    readme.txt
```

2. A copy of the `nesy4vrd_ontology` directory. The ontology file contained within this directory may or may not be an updated (customised) version of the original VRD-World ontology.  This will depend on the nature and extent of the customisation project. If NeSy4VRD object class or predicate names were changed or added as part of the NeSy4VRD annotations customisation project, and the VRD-World ontology file *was not* amended accordingly, then full alignment between the ontology and the visual relationship annotations will no longer exist. If the VRD-World ontology file *was* amended accordingly, then full alignment will still exist. If no changes were made to NeSy4VRD object class or predicate names were made, and the ontology was not touched, then full alignment will still exist. Either way, the state of the alignment between the **NeSy4VRD ontology** in the `.owl` file, and the NeSy4VRD visual relationship annotations in the `nesy4vrd_annotations` directory (as understood by the researcher doing the sharing) should be made clear to any potential users of the package being shared.
```
nesy4vrd_ontology
    readme.txt
    vrd_world_v1.owl
```

3. A directory containing copies of the **NeSy4VRD workflow** assets that capture the configuration details defining the annotation customisations that were specified for the **NeSy4VRD workflow** and applied by the **NeSy4VRD workflow**. These assets include: A) the two instances of the **NeSy4VRD workflow** Python configuration modules that were used to configure and drive the customisation project (one for the *training set* run of the workflow, one for the *test set* run of the workflow), and B) all NeSy4VRD annotation customisation instruction text files (in which annotation customisation instructions are specified declaratively, using the **NeSy4VRD protocol**). Depending on how these files may have been renamed (or not), and depending on the number of text files used for specifying annotation customisation instructions, such a directory may look as follows: 
```
nesy4vrd_customisation_project
    nesy4vrd_anno_cust_02_instructions_test.txt
    nesy4vrd_anno_cust_02_instructions_train.txt
    nesy4vrd_anno_cust_config_test.py
    nesy4vrd_anno_cust_config_train.py
```


