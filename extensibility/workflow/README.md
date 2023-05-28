# NeSy4VRD: workflow

This folder contains assets relating to the **NeSy4VRD workflow** component of the **NeSy4VRD extensibility support infrastructure**.

The **NeSy4VRD workflow** is a set of Python scripts and modules that together represent and implement a configurable, managed, automated and repeatable process for safely defining and applying small or large volumes of customisations and extensions to the NeSy4VRD visual relationship annotations for the VRD images, which together constitute the **NeSy4VRD dataset**.

This README describes the **NeSy4VRD workflow** and how to use it, in detail.

## The NeSy4VRD workflow: overview

The **NeSy4VRD workflow** is a flexible, multi-step sequential process for applying planned and pre-specified visual relationship annotation customisations in a configurable, automated and repeatable manner. Each step of the workflow is performed by a dedicated Python script that has been designed to perform a particular category (type) of annotation customisation task. All of the data describing the precise nature of the actual annotation customisations to be applied with respect to a particular category of customisation task are specified in a Python configuration module, using predetermined variable names and data formats. Each script (step) of the workflow imports this common configuration module to access its step-specific variables that tell it precisely what to do.

## The NeSy4VRD workflow configuration module

An instance of a **NeSy4VRD workflow** configuration module effectively represents a unique **instance** of the workflow. It determines which steps (categories of annotation customisation task) participate (or not) in that particular instance of the workflow, and for the participating steps it specifies the particulars of the precise customisations that are applied to the NeSy4VRD visual relationship annotations.  

The concept of the **NeSy4VRD workflow** configuration module provides a surprising number of real, practical benefits:
* It allows one to work iteratively and incrementally, gradually accumulating and refining one's annotation customisation decisions, over time, as one makes continued use of the **NeSy4VRD analysis** support code to learn and discover more about the details and nuances of the VRD images and the NeSy4VRD visual relationship annotations;
* The configuration module enables repeatability of the entire customisation process. Starting from a fresh copy of the default NeSy4VRD visual relationship annotations each time, you can rerun the **NeSy4VRD workflow** under management of your configuration module, and re-apply your ever growing and ever more refined set of annotation customisations so as to incorporate all of your  customisation decisions that have accumulated since you last did a run of the workflow;
* By saving the instance of the configuration module used for running the **NeSy4VRD workflow**, you effectively retain a complete historical record of all of the annotation customisations that were applied under the management of that configuration module;
* Finally, the concept of the **NeSy4VRD workflow** configuration module also enables **sharing of annotation customisation projects** amongst researchers who use the **NeSy4VRD research resource**.  Suppose researcher A uses the **NeSy4VRD extensibility support infrastructure** to undertake an annotation customisation project that extends and enriches the NeSy4VRD visual relationship annotations for a particular purpose and thinks the results might be of general interest. If researcher A shares the **NeSy4VRD workflow** configuration module developed for this project (along with any annotation customisation instruction text files developed using the **NeSy4VRD protocol** and referenced in the configuration module), then researcher B (who also uses **NeSy4VRD**) can run the **NeSy4VRD workflow** under the management of researcher A's configuration module (along with its associated annotation customisation instruction text files), and apply researcher A's enriching annotation customisations to their own copy of the NeSy4VRD visual relationship annotations. 

## 'Training set' and 'test set' runs of the NeSy4VRD workflow

A particular execution or *run* of the **NeSy4VRD workflow** targets customising the NeSy4VRD visual relationship annotations of either the VRD training set images or the VRD test set images, but not both.  Thus, all configured and protocol-specified annotation customisations must be organised for two distinct *runs* of the workflow: a **training set** run and a **test set** run.  A separate instance of a **NeSy4VRD workflow** configuration module is required to manage each of these two distinct, but strongly related, *runs* of the workflow. Thus, instances of **NeSy4VRD workflow** configuration module files should always come in pairs: one tailored for managing a **training set** run, and one tailored for managing the corresponding **test set** run of the workflow.

The set of **NeSy4VRD workflow** steps (scripts) that participate in the two related runs of the workflow need not be identical in all respects. For some steps (scripts) of the workflow, if they participate in the **training set** run they should also participate in the **test set** run (because you will always want to apply certain categories of customisation to the annotions of both the training set and test set images). But for other steps (scripts), this tight coupling does not apply. The details of these matters are thoroughly documented inside the sample **training set** and **test set** **NeSy4VRD workflow** configuration modules that reside in this folder.

To perform your **training set** *run* of the **NeSy4VRD workflow** (under the management of your **training set** configuration module) you do the following:
* adapt all of the workflow scripts that are to participate in your **training set** *run* so that they all import the same **training set** configuration module;
* execute the scripts for the successive participating steps of the workflow in your favourite IDE; (the scripts are designed for cell-by-cell execution, but this is not strictly necessary).

To perform your **test set** *run*, do the same, but using your **test set** configuration module.

## The common pattern of the NeSy4VRD workflow steps (scripts)

Each step (script) of the **NeSy4VRD workflow** follows this common pattern:
* import the specified **NeSy4VRD workflow** configuration module; 
* load the NeSy4VRD visual relationship annotation files (as specified in the configuration module);
* access the step-specific variables from the configuration module that tell the script what to do;
* apply the category of annotation customisations that the script is designed to perform, as governed by the data content specified in its step-specific variables;
* if any problems are encountered, abort and report;
* save the updated NeSy4VRD visual relationship annotations to disk using the same filename from which they were loaded.

## Workflow functionality

The following listing does two things: 1) it summarises the functionality of the various steps (scripts) of the **NeSy4VRD workflow**, and 2) it shows the particular configured instance of the **training set** *run* of the **NeSy4VRD workflow** that was used to transform the original VRD visual relationship annotations into the NeSy4VRD visual relationship annotations.  (The corresponding **test set** *run* used the same steps except for 1 and 8.) The sample workflow configuration module files that reside in this folder reflect this original 11-step workflow instance.

```
step | functionality
 01  - maintain the object class name and predicate name master lists
 02  - process NeSy4VRD protocol annotation customisation instruction file A
 03  - change object class A to B, for a specified set of images       
 04  - change object class (or predicate) C to D, globally   
 05  - remove specified visual relationship 'types', globally
 06  - remove entries from the annotations dictionary for images with zero annotations, globally   
 07  - process NeSy4VRD protocol annotation customisation instruction file B
 08  - process NeSy4VRD protocol annotation customisation instruction file C
 09  - transform visual relationship 'type' A to 'type' B, globally
 10  - check for and remove duplicate visual relationships, globally
 11  - process NeSy4VRD protocol annotation customisation instruction file D
```

Now that the highly customised and quality-improved NeSy4VRD visual relationship annotations already exist, researchers using the **NeSy4VRD workflow** to manage their own annotation customisation projects are highly unlikely to need anything nearly so elaborate.

We anticipate that most researchers who undertake NeSy4VRD visual relationship annotation customisation projects of their own will need only simple configured **NeSy4VRD workflow** instances, such as the ones which follow.

If no new object class names or predicate names are being introduced, a workflow instance might only need one step:
```
step | functionality
 02  - process NeSy4VRD protocol annotation customisation instruction file A
```

Even if new object class names and/or predicate names are being introduced to the visual relationship annotations, a workflow instance as simple as this might well suffice:
```
step | functionality
 01  - maintain the object class name and predicate name master lists
 02  - process NeSy4VRD protocol annotation customisation instruction file A
```

This workflow instance reflects a more substantial project:
```
step | functionality
 01  - maintain the object class name and predicate name master lists
 02  - process NeSy4VRD protocol annotation customisation instruction file A
 07  - process NeSy4VRD protocol annotation customisation instruction file B
 10  - check for and remove duplicate visual relationships, globally
```



