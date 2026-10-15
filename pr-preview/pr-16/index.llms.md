# Information Theory for Data Science

Code

Published

Last modified: 2026-10-15 14:26:45 (PDT)

## Welcome

Information theory measures uncertainty and information: how many bits a message needs, how much one random variable tells us about another, and how fast data can cross a noisy channel. Data science uses its quantities directly: cross-entropy is the loss in logistic regression and neural networks, Kullback–Leibler divergence links maximum likelihood to model fit, and mutual information drives the information gain of decision trees.

These notes collect the information theory that data science courses use. They are new. The pages written so far are:

- [Entropy and mutual information](entropy.llms.md): surprisal, joint and conditional entropy, mutual information, and the information gain of decision trees
- [Source coding](source-coding.llms.md): the source coding theorem, and cross-entropy as the cost of coding with the wrong distribution
- [Channel capacity](channel-capacity.llms.md): discrete memoryless channels, the capacity of the binary symmetric and erasure channels, and the noisy-channel coding theorem
- [Error-correcting codes](error-correcting-codes.llms.md): Hamming distance, the Hamming and Reed–Solomon codes, and how locally decodable codes lead to hardness amplification and the PCP theorem

The planned topics still to come are:

- Kullback–Leibler divergence and its link to maximum likelihood
- Huffman and arithmetic codes
- proofs of the noisy-channel coding theorem, and codes that approach capacity

Entropy, cross-entropy and KL divergence are defined in [*Probability for Data Science*](https://morrison-lab.github.io/pds/expectation.html#sec-entropy); pages here link to those definitions rather than repeating them. Computational complexity has its own library, [*Computational Complexity for Data Science*](https://morrison-lab.github.io/cds/). [Kolmogorov complexity](https://morrison-lab.github.io/cds/kolmogorov-complexity.html), which relates the shortest description of a single string to Shannon entropy, is covered there.

## Where to read about the planned topics

Stanford’s information theory courses cover many of the planned topics above, and they publish their course pages:

- [EE 276, *Information Theory*](https://web.stanford.edu/class/ee276/) (Tsachy Weissman) covers entropy and mutual information, the asymptotic equipartition property, prefix codes and Huffman codes, channel capacity and the channel coding theorem, and rate distortion. Its [reading page](https://web.stanford.edu/class/ee276/reading.html) lists books and Shannon’s papers.
- [EE 274, *Data Compression, Theory and Applications*](https://stanforddatacompressionclass.github.io/Fall22/) covers entropy coding and how tools such as gzip and bzip2 work, then lossy image and video coding.

The courses’ own notes and slides carry no license, so these notes link to them and do not reuse their text.

## Using these notes in another site

Course sites link to these pages by URL; they do not include this repository as a git submodule. A host site that keeps a copy of this repository at its root, named `ids`, can still include fragments with paths that start with `ids/`. This site includes its own fragments the same way, through a `ids` symlink that points at the repository root.

Quarto resolves `@id` cross-references only within one rendered page, so a host site that links to a result here uses an explicit link to the page and anchor.

Back to top
