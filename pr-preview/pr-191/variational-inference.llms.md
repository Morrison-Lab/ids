# Variational inference

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-12 00:51:44 (PST)

The [posterior](https://morrison-lab.github.io/sds/bayesian-inference.html#def-posterior) of an unobserved quantity is often too hard to compute. Variational inference replaces it with a simpler stand-in that is close to it, where closeness is measured by the [KL divergence](kl-divergence.llms.md).

## 1 The evidence lower bound

> **NOTE:**
>
> **Definition 1 (Evidence lower bound (ELBO))** Let $x$ be observed data, and let $z$ be an unobserved [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), with [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf) ${\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}$. Let $q$ be a [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) for $z$. Require that $q$ gives [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) zero to every value $z$ where the [posterior](https://morrison-lab.github.io/sds/bayesian-inference.html#def-posterior) ${\mathbb{p}\mathopen{}\left(z \mid x\right)\mathclose{}}$ is zero. The **evidence lower bound** (**ELBO**) of $q$ is the average, over $z$ drawn from $q$, of the difference between the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of ${\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}$ and the logarithm of $q(z)$:
>
> $$\mathrm{ELBO}(q) = {\mathbb{E}_{q}\mathopen{}\left[{\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}\right\}\mathclose{}} - {\operatorname{log}\mathopen{}\left\{q(z)\right\}\mathclose{}}\right]\mathclose{}}.$$
>
> Written as a sum over the values $z$ with $q(z) > 0$, the average is
>
> $$\mathrm{ELBO}(q) = \sum_z q(z) \mathopen{}\left({\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}\right\}\mathclose{}} - {\operatorname{log}\mathopen{}\left\{q(z)\right\}\mathclose{}}\right)\mathclose{}.$$

> **NOTE:**
>
> **Theorem 1 (The log evidence is the ELBO plus a divergence)** Let ${\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}$ and $q$ be as in [Definition 1](#def-evidence-lower-bound). Let ${\mathbb{p}\mathopen{}\left(x\right)\mathclose{}} = \sum_z {\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}$ be the [evidence](https://morrison-lab.github.io/sds/bayesian-inference.html#def-marginal-likelihood) of the data, also called its [marginal likelihood](https://morrison-lab.github.io/sds/bayesian-inference.html#def-marginal-likelihood). The evidence is nonzero, because a data value $x$ was observed. Then the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of the evidence is the [ELBO](#def-evidence-lower-bound) of $q$ plus the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of $q$ from the [posterior](https://morrison-lab.github.io/sds/bayesian-inference.html#def-posterior):
>
> $${\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}} = \mathrm{ELBO}(q) + {{D_{\mathrm{KL}}}\mathopen{}\left(q \,\Vert\, {\mathbb{p}\mathopen{}\left(\cdot \mid x\right)\mathclose{}}\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Let $z$ be a value with $q(z) > 0$. Then ${\mathbb{p}\mathopen{}\left(z \mid x\right)\mathclose{}} \ne 0$, and ${\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}} = {\mathbb{p}\mathopen{}\left(z \mid x\right)\mathclose{}} \, {\mathbb{p}\mathopen{}\left(x\right)\mathclose{}}$. Apply $\operatorname{log}$ to both sides and rearrange:
>
> $${\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}} = {\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}\right\}\mathclose{}} - {\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(z \mid x\right)\mathclose{}}\right\}\mathclose{}}.$$
>
> Add and subtract ${\operatorname{log}\mathopen{}\left\{q(z)\right\}\mathclose{}}$ on the right:
>
> $${\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}} = \mathopen{}\left({\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}\right\}\mathclose{}} - {\operatorname{log}\mathopen{}\left\{q(z)\right\}\mathclose{}}\right)\mathclose{} + \mathopen{}\left({\operatorname{log}\mathopen{}\left\{q(z)\right\}\mathclose{}} - {\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(z \mid x\right)\mathclose{}}\right\}\mathclose{}}\right)\mathclose{}.$$
>
> Multiply both sides by $q(z)$, then sum over the values $z$ with $q(z) > 0$. The left side sums to ${\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}}$, because $q$ sums to $1$:
>
> $${\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}} = \sum_z q(z) \mathopen{}\left({\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x, z\right)\mathclose{}}\right\}\mathclose{}} - {\operatorname{log}\mathopen{}\left\{q(z)\right\}\mathclose{}}\right)\mathclose{} + \sum_z q(z) \mathopen{}\left({\operatorname{log}\mathopen{}\left\{q(z)\right\}\mathclose{}} - {\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(z \mid x\right)\mathclose{}}\right\}\mathclose{}}\right)\mathclose{}.$$
>
> The first sum is $\mathrm{ELBO}(q)$ by its definition. The second sum is ${{D_{\mathrm{KL}}}\mathopen{}\left(q \,\Vert\, {\mathbb{p}\mathopen{}\left(\cdot \mid x\right)\mathclose{}}\right)\mathclose{}}$ by the definition of the divergence.

> **NOTE:**
>
> **Example 1 (The ELBO and the divergence for a three-valued latent variable)**  
>
> Let $z$ take the values $1, 2, 3$ with [prior](https://morrison-lab.github.io/sds/bayesian-inference.html#def-prior) [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.5, 0.3, 0.2$. A data value $x$ is observed, and its probabilities given $z$ are $0.1, 0.4, 0.8$. The R chunk below finds the [posterior](https://morrison-lab.github.io/sds/bayesian-inference.html#def-posterior), then computes the [ELBO](#def-evidence-lower-bound) and the divergence for three choices of $q$, with [natural logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-natural-log).
>
> Show code
>
> ``` r
> prior <- c(0.5, 0.3, 0.2)
> likelihood <- c(0.1, 0.4, 0.8)
> joint <- prior * likelihood
> evidence <- sum(joint)
> posterior <- joint / evidence
> log_evidence <- log(evidence)
>
> elbo_and_divergence <- function(q) {
>   log_ratio <- log(joint) - log(q)
>   elbo <- sum(q * log_ratio)
>   log_gap <- log(q) - log(posterior)
>   divergence <- sum(q * log_gap)
>   c(elbo = elbo, divergence = divergence, total = elbo + divergence)
> }
>
> uniform <- rep(1 / 3, 3)
> shifted <- c(0.2, 0.3, 0.5)
> rows <- rbind(
>   uniform = elbo_and_divergence(uniform),
>   shifted = elbo_and_divergence(shifted),
>   posterior = elbo_and_divergence(posterior)
> )
> round(rows, 4)
> #>              elbo divergence   total
> #> uniform   -1.2176     0.1089 -1.1087
> #> shifted   -1.1219     0.0132 -1.1087
> #> posterior -1.1087     0.0000 -1.1087
> ```
>
> The [evidence](https://morrison-lab.github.io/sds/bayesian-inference.html#def-marginal-likelihood) is $0.33$, so its [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) is $-1.1087$. In every row the ELBO plus the divergence equals this value, as [Theorem 1](#thm-evidence-lower-bound-decomposition) says. The ELBO is largest, and the divergence is $0$, for $q$ equal to the posterior.

> **NOTE:**
>
> *Remark 1* (Variational inference maximizes the ELBO). The [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of the [evidence](https://morrison-lab.github.io/sds/bayesian-inference.html#def-marginal-likelihood) ${\operatorname{log}\mathopen{}\left\{{\mathbb{p}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}}$ does not depend on $q$. By [Theorem 1](#thm-evidence-lower-bound-decomposition), choosing $q$ to maximize the [ELBO](#def-evidence-lower-bound) is therefore the same as choosing $q$ to minimize its [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) from the [posterior](https://morrison-lab.github.io/sds/bayesian-inference.html#def-posterior). The ELBO never exceeds the logarithm of the evidence, because the divergence is at least $0$. Variational inference searches a restricted family of choices for $q$ this way ([Blei et al. 2017](#ref-blei2017variational)).

## References

Blei, David M., Alp Kucukelbir, and Jon D. McAuliffe. 2017. “Variational Inference: A Review for Statisticians.” *Journal of the American Statistical Association* 112 (518): 859–77. <https://doi.org/10.1080/01621459.2017.1285773>.

Back to top
