# Minimum description length

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-09 03:17:28 (PST)

A model that fits the data well gives the data a short [code](source-coding.llms.md#def-code), but a model that is itself long to describe costs [bits](entropy.llms.md#def-bit) of its own. This page counts both costs in bits, and chooses the model that makes the sum shortest.

## 1 Description length

> **NOTE:**
>
> **Definition 1 (Two-part description length)** Let $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ be data, and let $p_1, \ldots, p_m$ be models, each of which gives $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ a [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $p_j(\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}})$. Let a [prefix code](huffman-codes.llms.md#def-prefix-code) on the models give each model $p_j$ a codeword of ${\ell\mathopen{}\left(p_j\right)\mathclose{}}$ [bits](entropy.llms.md#def-bit).
>
> The **two-part description length** of $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ under a model $p_j$ is
>
> $${\ell\mathopen{}\left(p_j\right)\mathclose{}} + {\mathbb{s}_{p_j}\mathopen{}\left(\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}\right)\mathclose{}}.$$
>
> The first part is the length of the codeword that names the model. The second part is the [surprisal](entropy.llms.md#def-surprisal) $\log_2 \frac{1}{p_j(\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}})}$ of $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ under the model, which is the length in bits of a [code](source-coding.llms.md#def-code) for $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ built from the model.

> **NOTE:**
>
> **Example 1 (The two-part description lengths of coin flips)**  
>
> A coin is flipped $100$ times, and it lands heads $70$ times. The chunk below follows [Definition 1](#def-two-part-description-length) with nine models, the [Bernoulli](https://morrison-lab.github.io/pds/random-variables.html#def-bernoulli) models with the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) of heads $0.1, 0.2, \ldots, 0.9$. It gives each model a codeword of the same length, and it prints the two parts and their sum for each model.
>
> Show code
>
> ``` r
> n_flips <- 100
> n_heads <- 70
> success_prob <- seq(0.1, 0.9, by = 0.1)
> model_bits <- log2(length(success_prob))
> heads_bits <- n_heads * log2(success_prob)
> tails_bits <- (n_flips - n_heads) * log2(1 - success_prob)
> data_bits <- -(heads_bits + tails_bits)
> total_bits <- model_bits + data_bits
> data.frame(success_prob, model_bits, data_bits, total_bits)
> ```
>
> Each model takes $3.17$ [bits](entropy.llms.md#def-bit) to name, because nine equally long codewords need $\log_2 9$ bits. The data part is smallest, at $88.1$ bits, for the model with probability of heads $0.7$.

> **NOTE:**
>
> **Definition 2 (Minimum description length principle)** Given data $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ and models $p_1, \ldots, p_m$, the **minimum description length principle** chooses the model with the smallest [two-part description length](#def-two-part-description-length) of $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$. The models may have codewords of different lengths.

> **NOTE:**
>
> **Example 2 (The minimum description length model for coin flips)**  
>
> The chunk below applies [Definition 2](#def-minimum-description-length) to the [two-part description lengths](#def-two-part-description-length) of [Example 1](#exm-two-part-description-length). It prints the model with the smallest two-part description length, and it prints the length of writing the $100$ flips, with $70$ heads, out as plain heads and tails.
>
> Show code
>
> ``` r
> chosen <- which.min(total_bits)
> success_prob[chosen]
> #> [1] 0.7
> total_bits[chosen]
> #> [1] 91.29901
> n_flips
> #> [1] 100
> ```
>
> The principle chooses the model with the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) of heads $0.7$, with a two-part length of $91.3$ [bits](entropy.llms.md#def-bit). That is shorter than the $100$ bits of the flips themselves, because the flips are far from fair.

> **NOTE:**
>
> **Theorem 1 (Minimum description length and maximum likelihood)** Let $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ be data, and let $p_1, \ldots, p_m$ be models that give $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ the [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $p_j(\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}) > 0$, with the same [codeword length](source-coding.llms.md#def-code) ${\ell\mathopen{}\left(p_j\right)\mathclose{}} = \ell_0$ for every model. Then a model has the smallest [two-part description length](#def-two-part-description-length) of $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$ exactly when it is a [maximum likelihood estimate](https://morrison-lab.github.io/sds/intro-MLEs.html#def-mle) of the model given $\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}$.

> **NOTE:**
>
> *Proof*. Every model has the first part $\ell_0$, so the models differ only in the second part ${\mathbb{s}_{p_j}\mathopen{}\left(\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}}\right)\mathclose{}}$. The [surprisal](entropy.llms.md#def-surprisal) $\log_2 \frac{1}{u}$ decreases as the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $u$ increases. So the second part is smallest for the model with the largest $p_j(\mathord{\smash[b]{\underset{\raise.3ex\hbox{$\scriptstyle\sim$}}{x}}\vphantom{x}})$, which is a [maximum likelihood estimate](https://morrison-lab.github.io/sds/intro-MLEs.html#def-mle).

> **NOTE:**
>
> **Example 3 (Equal codeword lengths for the coin flips)**  
>
> The $9$ models of [Example 1](#exm-two-part-description-length) have codewords of equal length, so [Theorem 1](#thm-minimum-description-length-maximum-likelihood) applies to the data of $70$ heads in $100$ flips. The chunk below compares the model with the shortest [two-part description length](#def-two-part-description-length) to the model that gives the flips the highest [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability).
>
> Show code
>
> ``` r
> likelihood <- success_prob^n_heads * (1 - success_prob)^(n_flips - n_heads)
> success_prob[which.max(likelihood)]
> #> [1] 0.7
> success_prob[which.min(total_bits)]
> #> [1] 0.7
> ```
>
> Both models have the probability of heads $0.7$, as the [theorem](https://morrison-lab.github.io/mcs/proof-writing.html#def-theorem) says.

> **NOTE:**
>
> *Remark 1* (Where the minimum description length principle comes from). Cover and Thomas ([2006, sec. 14.13](#ref-cover2006elements)) state the principle as the choice of the model such that the model’s length plus the length of the data given the model is as short as possible. They give the model’s length as its Kolmogorov complexity, not as the length of a codeword from a [prefix code](huffman-codes.llms.md#def-prefix-code).

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

Back to top
