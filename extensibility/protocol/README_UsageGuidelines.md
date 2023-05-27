# NeSy4VRD: Protocol - Usage Guidelines

The main README file in this folder **specifies** the **NeSy4VRD protocol** itself. This README file defines the **guidelines** for **using** the **NeSy4VRD protocol** to specify NeSy4VRD visual relationship annotation customisation instructions declaratively, in text files.

Some of the **usage guidelines** are **mandatory**, some are **recommended**. Rather than complicate things by explaining the nuances of the distinctions between what is *mandatory* versus what is *recommended*, and the conditionality that exists surrounding these distinctions, the **usage guidelines** defined here have been written as if they are all **mandatory**. The protocol driver script of the **NeSy4VRD workflow** will detect any violations of the truly **mandatory** usage guidelines and abort and report the problem.

There are just 4 **usage guidelines**. Each image entry in a **NeSy4VRD protocol** annotation customisation instruction text file should be crafted so as to adhere to these 4 **usage guidelines**.

Before defining the 4 **usage guidelines**, we first clarify a couple of conventions that we use in their definitions:
* to reduce clutter, we use the acronym *VR* for *'visual relationship'*;
* in memory, the VRs for an image are held in a Python `List`, so when we refer to a VR's *index position*, we are refering to the integer index that identifies its position within that Python `List`.

## The NeSy4VRD Protocol Usage Guidelines

#### Usage guideline 1

If you have any *change VR* (`cvr...`) instructions to declare, specify all of these **first**, and do so in **ascending order by index** position of the VRs that your instructions target.  Here's an example:
```
imname; 4327585910_5c31ac88be_b.jpg
cvrsoc; 0; ('bear', 'on', 'skis'); teddy bear
cvrsoc; 1; ('bear', 'wear', 'skis'); teddy bear
```

#### Usage guideline 2

If you have any *remove VR* (`rvrxxx`) instructions to declare, specify all of these **after the `cvr...` instructions**, if any, and do so in **descending order by index** position of the VRs that your instructions target. Here's an example:
```
imname; 8626467744_d59654baf8_b.jpg
cvrobb; 7; ('sky', 'above', 'street'); [346, 676, 308, 1022]
cvrobb; 12; ('person', 'on', 'street'); [346, 676, 308, 1022]
rvrxxx; 18; ('bush', 'on', 'mountain')
rvrxxx; 5; ('street', 'on', 'mountain')
```

#### Usage guideline 3

If you have any *add VR* (`avrxxx`) instructions to declare, specify all of these **last**, after any `cvr...` or `rvrxxx` instructions (if any). Since `avrxxx` instructions do not reference index position numbers, you can order them in any manner.  Here's an example:
```
imname; 3330913880_0c57abe7c7_b.jpg
cvrsbb; 6; ('sky', 'above', 'mountain'); [1, 108, 416, 1022]
rvrxxx; 5; ('trees', 'on', 'mountain')
avrxxx; person; [214, 650, 62, 285]; wear; skis; [608, 730, 158, 355]
avrxxx; person; [214, 650, 62, 285]; on; skis; [608, 730, 158, 355]
```

#### Usage guideline 4

If you have multiple `cvr...` instructions that target the same VR at the same index position, you must ensure that the `vr_description` component of the instruction --- the `('subject', 'predicate', 'object')` component --- correctly reflects the actual VR as it will exist in memory as each successive instruction is executed by the protocol driver script of the **NeSy4VRD workflow**. Here's an example to clarify things:
```
imname; 5378594477_31245a0dc1_b.jpg
cvrsoc; 0; ('luggage', 'near', 'luggage'); suitcase
cvrooc; 0; ('suitcase', 'near', 'luggage'); suitcase
cvrpxx; 0; ('suitcase', 'near', 'suitcase'); next to
```

Adjusting the `vr_description` component in successive instructions ensures that the `vr_description` always matches the state of the actual VR at the designated index position. If the protocol driver script detects a mismatch between the `vr_description` component of an instruction and the actual VR (as it exists in memory at that moment), it will abort and report the mismatch.



