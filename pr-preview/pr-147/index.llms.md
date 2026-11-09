# Information Theory for Data Science

Code

Published

Last modified: 2026-11-08 16:03:52 (PST)

## Welcome

Information theory quantifies uncertainty and information: how many [bits](entropy.llms.md#def-bit) a message needs, how much one [random variable](https://morrison-lab.github.io/pds/random-variables.html#def-random-variable) tells us about another, and how fast data can cross a noisy channel. Data science uses its quantities directly: [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) is the quantity that [logistic regression](https://morrison-lab.github.io/sds/logistic-inference.html#def-logistic-regression) and neural networks minimize, [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) links the fit of a model to the data it describes, and [mutual information](entropy.llms.md#def-mutual-information) drives the [information gain](entropy.llms.md#def-information-gain) of decision trees.

These notes gather the information theory that data science courses use. They are new. The pages written so far are:

- [Entropy and mutual information](entropy.llms.md): [surprisal](entropy.llms.md#def-surprisal), joint and [conditional entropy](entropy.llms.md#def-conditional-entropy), mutual information, and the [information gain](entropy.llms.md#def-information-gain) of decision trees
- [Source coding](source-coding.llms.md): the source coding [theorem](https://morrison-lab.github.io/mcs/proof-writing.html#def-theorem), and [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) as the cost of coding with a code built for the wrong source
- [Channel capacity](channel-capacity.llms.md): [discrete memoryless channels](channel-capacity.llms.md#def-channel), the [capacity](channel-capacity.llms.md#def-channel-capacity) of the [binary symmetric channel](channel-capacity.llms.md#def-binary-symmetric-channel) and the [binary erasure channel](channel-capacity.llms.md#def-binary-erasure-channel), and the noisy-channel coding theorem
- [Error-correcting codes](error-correcting-codes.llms.md): [Hamming distance](error-correcting-codes.llms.md#def-hamming-distance), the Hamming and [Reed–Solomon codes](error-correcting-codes.llms.md#def-reed-solomon-code), and how [locally decodable codes](error-correcting-codes.llms.md#def-locally-decodable) lead to hardness amplification and the PCP theorem

The planned topics still to come are:

- [KL divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) and its link to fitting models to data
- Huffman and arithmetic codes
- proofs of the [noisy-channel coding theorem](channel-capacity.llms.md#thm-channel-coding), and codes that approach [capacity](channel-capacity.llms.md#def-channel-capacity)

[Entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy), [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) and [KL divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) are defined in [*Probability for Data Science*](https://morrison-lab.github.io/pds/expectation.html#sec-entropy); pages here link to those definitions rather than repeating them. Computational complexity has its own library, [*Computational Complexity for Data Science*](https://morrison-lab.github.io/ccds/). [Kolmogorov complexity](https://morrison-lab.github.io/ccds/kolmogorov-complexity.html), which relates the shortest description of a single string to [Shannon entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy), is covered there.

## Where to read about the planned topics

Stanford’s information theory courses cover many of the planned topics above, and they publish their course pages:

- [EE 276, *Information Theory*](https://web.stanford.edu/class/ee276/) (Tsachy Weissman) covers [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) and [mutual information](entropy.llms.md#def-mutual-information), the asymptotic equipartition property, prefix codes and Huffman codes, [channel capacity](channel-capacity.llms.md#def-channel-capacity) and the [channel coding theorem](channel-capacity.llms.md#thm-channel-coding), and lossy compression. Its [reading page](https://web.stanford.edu/class/ee276/reading.html) lists books and the founding papers of the field.
- [EE 274, *Data Compression, Theory and Applications*](https://stanforddatacompressionclass.github.io/Fall22/) covers entropy coding and how tools such as gzip and bzip2 work, then lossy coding of pictures and video.

The courses’ own notes and slides carry no license, so these notes link to them and do not reuse their text.

## Using these notes in another site

Course sites link to these pages by URL; they do not include this repository as a git submodule. A host site that keeps a copy of this repository at its root, named `ids`, can still include fragments with paths that start with `ids/`. This site includes its own fragments the same way, through a `ids` symlink that points at the repository root.

Quarto resolves `@id` cross-references only within one rendered page, so a host site that links to a result here uses an explicit link to the page and anchor.

Back to top
