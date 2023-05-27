# NeSy4VRD: Protocol - Usage Guidelines

The main README file in this folder **specifies** the **NeSy4VRD protocol** itself. This README file defines the **guidelines** for **using** the **NeSy4VRD protocol** to specify NeSy4VRD visual relationship annotation customisation instructions declaratively, in text files.

Some of the **usage guidelines** are **mandatory**, some are **recommended**. Rather than complicate things by explaining the nuances of the distinctions between what is *mandatory* versus what is *recommended*, and the conditionality that exists surrounding these distinctions, the **usage guidelines** defined here have been written as if they are all **mandatory**. The protocol driver script of the **NeSy4VRD workflow** will detect any violations of the truly **mandatory** usage guidelines and abort and report the problem.

There are just 4 **usage guidelines**. Each image entry in a **NeSy4VRD protocol** annotation customisation instruction text file should be crafted so as to adhere to these 4 **usage guidelines**.

Before defining the 4 **usage guidelines**, we first clarify a couple of conventions that we use in their definitions:
* to reduce clutter, we use the acronym *VR* for *'visual relationship'*;
* in memory, the VRs for an image are held in a Python `List`, so when we refer to a VR's *index position*, we are refering to the integer index that identifies its position within that Python `List`.

## The NeSy4VRD Protocol Usage Guidelines

#### Usage guideline 1

If you have any **change VR**, `cvr...`, instructions to declare for a given image, specify all of these **first**, and do so in **ascending order by index** position.  Here's an example:
```
imname; 4327585910_5c31ac88be_b.jpg
cvrsoc; 0; ('bear', 'on', 'skis'); teddy bear
cvrsoc; 1; ('bear', 'wear', 'skis'); teddy bear
```

#### Usage guideline 2

If you have any **remove VR**, `rvrxxx`, instructions to declare for a given image, specify all of these **after `cvr...` instructions**, if any, and do so in **descending order by index** position. Here's an example:
```
imname; 8626467744_d59654baf8_b.jpg
cvrobb; 7; ('sky', 'above', 'street'); [346, 676, 308, 1022]
cvrobb; 12; ('person', 'on', 'street'); [346, 676, 308, 1022]
rvrxxx; 18; ('bush', 'on', 'mountain')
rvrxxx; 5; ('street', 'on', 'mountain')
```

#### Usage guideline 3

If you have any **add VR**, `avrxxx`, instructions to declare for a given image, specify all of these **last**, after `cvr...` or `rvrxxx` instructions, if any. Since `avrxxx` instructions do not reference index positions, you can order them in any manner.  Here's an example:
```
imname; 3330913880_0c57abe7c7_b.jpg
cvrsbb; 6; ('sky', 'above', 'mountain'); [1, 108, 416, 1022]
rvrxxx; 5; ('trees', 'on', 'mountain')
avrxxx; person; [214, 650, 62, 285]; wear; skis; [608, 730, 158, 355]
avrxxx; person; [214, 650, 62, 285]; on; skis; [608, 730, 158, 355]
```

#### Usage guideline 4

If you have **multiple** **change VR**, `cvr...`, instructions for the same VR at the same index position, you must ensure that the `vr_description` component of the instruction --- the `('subject', 'predicate', 'object')` component --- correctly reflects the actual VR as it will exist in memory as each successive instruction is executed by the protocol driver script of the **NeSy4VRD workflow**. Here's an example to clarify things:
```
imname; 5378594477_31245a0dc1_b.jpg
cvrsoc; 0; ('luggage', 'near', 'luggage'); suitcase
cvrooc; 0; ('suitcase', 'near', 'luggage'); suitcase
cvrpxx; 0; ('suitcase', 'near', 'suitcase'); next to
```

Each instruction is executed by the protocol driver as it is encountered, from the top of the instruction file to the bottom. So once the `cvrsoc` instruction has been executed, the VR at index 0 will have changed internally: the object class of the 'subject' will now be 'suitcase', not 'luggage'. So the `vr_description` in the `cvrooc` instruction needs to reflect this fact.  Similarly, the `vr_description` in the `cvrpxx` instruction needs to reflect both of the two preceding changes.

If you sometimes forget to do keep the `vr_description` in sync with the internal state of the VR being customised, no harm will ever be done.  The only thing that happens is that the protocol driver script of the **NeSy4VRD workflow** will detect a mismatch and abort and report the problem so you can fix it.  This convention of requiring the `vr_description` to always match the internal VR referred to by the `vr_index` is a valuable **quality control mechanism** that prevents inadvertent errors being made when crafting annotation customisations. It is also a healthy discipline that encourages the analyst to think clearly and precisely about the changes they are crafting.

## Examples of the NeSy4VRD Protocol Usage Guidelines

Many more examples of these guidelines can be found in the several sample annotation customisation instruction text files in the **NeSy4VRD workflow** folder.



