# NeSy4VRD: protocol

This folder contains assets relating to the **NeSy4VRD protocol** component of the NeSy4VRD infrastructure that supports extensibility of the NeSy4VRD visual relationship annotations and, thereby, of the NeSy4VRD OWL ontology, VRD-World. The **NeSy4VRD protocol** component of the NeSy4VRD infrastructure supporting extensibility is a custom-designed protocol that allows researchers to specify VRD / NeSy4VRD visual relationship annotation customisation instructions declaratively, in text files. Specifying annotation customisation instructions declaratively in text files enables researchers to define and apply large volumes of annotation customisations safely and responsibly, using the **NeSy4VRD workflow**. The **NeSy4VRD workflow** is the 3rd component of the NeSy4VRD infrastructure that supports extensibility of the annotations and VRD-World ontology. It is described in another folder of this GitHub repo.

## What is the NeSy4VRD protocol?

Like most protocols, the **NeSy4VRD protocol** is conceptual in nature. Rather than define it in a formal specification document, however, it is simpler to give examples of it and explain the examples.

Here is a representative sample of the **NeSy4VRD protocol** in action that illustates all of its features:
```
imname; 3223670633_7d3d72dfe8_b.jpg
cvrsoc; 4; (`person', `on', `shelf'); speaker
cvrsbb; 4; (`speaker', `on', `shelf'); [161,234,231,270]

imname; 8934043045_251b42d19a_b.jpg
cvrooc; 7; (`bus', `beside', `car'); truck
cvrobb; 7; (`bus', `beside', `truck'); [334,557,99,403]

imname; 1426904233_ee344879b6_b.jpg
cvrsoc; 5; (`bear', `sit on', `basket'); teddy bear
cvrpxx; 5; (`teddy bear', `sit on', `basket'); in

imname; 4929276486_ca06aedbb9_b.jpg
rvrxxx; 4; (`person', `wear', `jacket');
avrxxx; boat; [477,594,319,746]; has; dog; [478,529,587,618]
avrxxx; boat; [477,594,319,746]; carry; dog; [478,529,587,618]

imname; 7171463996_900cb4ce33_b.jpg; rimxxx
```
This listing shows various types of **NeSy4VRD protocol** annotation customisation instructions being specified with respect to five different VRD images.

A given text file of **NeSy4VRD protocol** annotation customisation instructions must always pertain only to the annotations of either VRD training images or VRD test images. Let us assume this listing pertains to the annotations of training set images.

The `imname;` instruction is always followed by the filename of a valid VRD image. In this case, it must be a valid VRD training image. 

For the first image in the listing, an improvement to the visual relationship annotation at index 4 (in the image's list of annotations) is being specified.  The \texttt{cvrsoc} instruction declares an intention to change the subject's object class (\texttt{soc}) from \texttt{person} to \texttt{speaker}, (as in `stereo speaker'). The \texttt{cvrsbb} instruction declares an intention to change the subject's bounding box (\texttt{sbb}) to a more accurate localisation of the object.

For the second image, similar types of changes are being specified, but this time for the visual relationship at index 7 and in relation to the object's object class and bounding box (\texttt{cvrooc} and \texttt{cvrobb}).

For the third image, an improvement to the visual relationship at index 5 is being specified. After a \texttt{cvrsoc} instruction specifying that the subject's object class be changed from \texttt{bear} to \texttt{teddy bear}, a \texttt{cvrpxx} instruction declares an intention to change the predicate (\texttt{pxx}) from \texttt{sit on} to \texttt{in}.

For the fourth image, the \texttt{rvrxxx} instruction declares an intention to remove the visual relationship at index 4 (because, say, it was found to be too badly broken or to be a near or exact duplicate of another annotation for the same image). The two \texttt{avrxxx} instructions declare intentions to \textit{add} two \textit{new} visual relationships to the set of annotations for the image.

Finally, the \texttt{rimxxx} instruction following the name of the fifth image in the listing declares an intention to have the entry for that image removed from the annotations dictionary (because the image and its annotations were found to be highly problematic and not recoverable).



