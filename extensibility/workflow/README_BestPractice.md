# NeSy4VRD: Workflow Best Practice

This document provides guidance as to best practice use of the **NeSy4VRD workflow**.


## Managing annotation customisation instruction dependencies

### Dependency scenarios

Specifying **NeSy4VRD protocol** annotation customisation instructions declaratively, in text files, gives you the most granular and surgical control over your annotation customisations.  But these instructions also create implicit dependencies of which one needs to stay mindful in order that one's customisation instructions can always be successfully processed by the protocol driver of the **NeSy4VRD workflow**.  To understand this point, let's consider an example where you are specifying annotation customisation instructions for image X across two instruction text files, A and B.  Let us also suppose that in your **NeSy4VRD workflow** configuration module you have arranged for text file A to be processed before text file B. 

Let's denote the starting state of image X's annotations by $S$. The annotation customisation instructions for image X in text file A need to be crafted with respect to image X's annotations as they exist in state $S$. But once instruction text file A has been processed by the NeSy4VRD protocol driver in a *run* of your configured instance of the **NeSy4VRD workflow**, the annotations of image X will be in state $S^\prime$.  Thus, to ensure that the annotation customisation instructions for image X specified in text file B can be successfully processed by the NeSy4VRD protocol driver, they need to have been crafted in a manner that is consistent with image X's annotations as they exist in state $S^\prime$, not state $S$. In such scenarios, if sufficient care has not been taken in this regard, the NeSy4VRD protocol driver may encounter discrepancies between the instructions in text file B for image X and the state $S^\prime$ of X's annotations. Upon encountering such discrepancies, the NeSy4VRD protocol driver will abort and report a problem.

Discrepancies will not always exist in such scenarios, but they may --- it depends on the particular annotation customisations you specify. And even if discrepancies are encountered by the NeSy4VRD protocol driver, no harm to the annotations will ever be done. But it can be a surprise and an inconvenience to find the NeSy4VRD protocol driver unexpectedly aborting and reporting a problem.

The very same type of implicit dependencies will arise in another scenario. Suppose now that you specify annotation customisation instructions for image X in multiple places within the same **NeSy4VRD protocol** instructions text file.  The NeSy4VRD protocol driver processes these instruction text files sequentially, from top to bottom.  The top-most entry for image X will be processed first and the state of image X's annotations will change from $S$ to $S^\prime$. So, for the customisation instructions in the next entry for image X (lower down in the text file) to be processed successfully, they must be consistent with state $S^\prime$.

### Managing dependencies

One way to manage such dependency issues is to try to aggregate all of one's annotation customisation instructions for a given image together, in one entry, in one NeSy4VRD protocol instructions text file.  This way, neither of the two scenarios described above will arise, and so discrepancies between annotation customisation instructions and annotation state will be avoided.

But it is not always convenient to organise your **NeSy4VRD protocol** annotation customisation instructions for a given image all in one place.  Sometimes it may be more convenient to create multiple entries for image X distributed across a single annotation customisation instruction text file, or across multiple instruction text files.

For example, suppose you specify annotation customisations for image X in text file A at time $t$. At time $t+k$ you run your configured instance of the **NeSy4VRD workflow** and your customisations to the annotations of image X are applied, shifting the annotations from state $S$ to state $S^\prime$, and your updated version of the NeSy4VRD visual relationship annotations is created. You then carry on with your research. Later (perhaps much later), at time $t+k+n$, suppose you encounter image X again (whilst using, say, the **NeSy4VRD analysis** code for some purpose) and you decide you wish to make further customisations to the annotations of image X. But now your judgements as to desirable customisations are conditional upon the annotations for image X being in state $S^\prime$. In this scenario, it may be much simpler and cleaner (and make good sense) to craft a separate entry for image X, because you wish to tailor state $S^\prime$ annotations this time, not state $S$ annotations.

Another way to manage these annotation customisation dependency issues is to run your configured instance of the **NeSy4VRD workflow** *regularly*, even if it is just to have the NeSy4VRD protocol driver validate that your annotation customisation instructions are executable, without yet saving the updated visual relationship annotations to disk.  If you let large amounts of time pass in which you accumulate large numbers of new annotation customisation instructions for large numbers of images, when you next attempt to run your configured instance of the **NeSy4VRD workflow**, you may find you are faced with a lengthy debugging exercise, as the NeSy4VRD protocol driver encounters discrepancy and discrepancy.




