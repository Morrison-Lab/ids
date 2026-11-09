# KL divergence and maximum likelihood

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-09 03:02:09 (PST)

The [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of one model from another is the number of [bits](entropy.llms.md#def-bit) per value that a code built for the model wastes, by the [cross-entropy decomposition](source-coding.llms.md#thm-cross-entropy-decomposition). This page applies that to data, and shows that the model a [maximum likelihood estimate](https://morrison-lab.github.io/sds/intro-MLEs.html#def-mle) picks is the model with the least waste.

## 1 Maximum likelihood

> **NOTE:**
>
> **Theorem 1 (Maximum likelihood minimizes the divergence from the data)** Let $x_1, \ldots, x_n$ be data, and let $\mathop{\hat{\mathbb{p}}}\nolimits$ be their [empirical distribution](https://morrison-lab.github.io/sds/nonparametric-models.html#def-empirical-distribution). Let $q_\theta$ be [probability mass functions](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) with $q_\theta(v) > 0$ wherever $\mathop{\hat{\mathbb{p}}}\nolimits(v) > 0$, for parameter values $\theta$. Then $\theta$ maximizes the [likelihood](https://morrison-lab.github.io/sds/intro-MLEs.html#def-lik) $\prod_{i=1}^n q_\theta(x_i)$ exactly when it minimizes the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) ${{D_{\mathrm{KL}}}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits \,\Vert\, q_\theta\right)\mathclose{}}$.

> **NOTE:**
>
> *Proof*. Let $n_v$ be the number of data equal to $v$. Then $n_v = n \, \mathop{\hat{\mathbb{p}}}\nolimits(v)$.
>
> Group the terms of the [log-likelihood](https://morrison-lab.github.io/sds/intro-MLEs.html#def-loglik) by value:
>
> $$\sum_{i=1}^n \log_2 q_\theta(x_i) = \sum_v n \, \mathop{\hat{\mathbb{p}}}\nolimits(v) \log_2 q_\theta(v).$$
>
> Divide by $n$. The right side is minus the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) ${\mathbb{H}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits, q_\theta\right)\mathclose{}}$:
>
> $$\frac{1}{n} \sum_{i=1}^n \log_2 q_\theta(x_i) = -{\mathbb{H}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits, q_\theta\right)\mathclose{}}.$$
>
> By the [cross-entropy decomposition](source-coding.llms.md#thm-cross-entropy-decomposition), the cross-entropy is the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $\mathop{\hat{\mathbb{p}}}\nolimits$ plus the divergence:
>
> $$-{\mathbb{H}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits, q_\theta\right)\mathclose{}} = -{\mathbb{H}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits\right)\mathclose{}} - {{D_{\mathrm{KL}}}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits \,\Vert\, q_\theta\right)\mathclose{}}.$$
>
> The entropy ${\mathbb{H}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits\right)\mathclose{}}$ does not depend on $\theta$. So $\theta$ maximizes the average log-likelihood exactly when it minimizes ${{D_{\mathrm{KL}}}\mathopen{}\left(\mathop{\hat{\mathbb{p}}}\nolimits \,\Vert\, q_\theta\right)\mathclose{}}$. The [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) increases, and dividing by $n$ keeps the order, so $\theta$ maximizes the average log-likelihood exactly when it maximizes the [likelihood](https://morrison-lab.github.io/sds/intro-MLEs.html#def-lik).

> **NOTE:**
>
> **Example 1 (The divergence from the data for coin flips)**  
>
> A coin is flipped $100$ times, and it lands heads $70$ times. The chunk below follows [Theorem 1](#thm-maximum-likelihood-kl-divergence) for the [Bernoulli](https://morrison-lab.github.io/pds/random-variables.html#def-bernoulli) models with the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) of heads $0.1, 0.2, \ldots, 0.9$. It prints the divergence of each model from the [empirical distribution](https://morrison-lab.github.io/sds/nonparametric-models.html#def-empirical-distribution), the average [log-likelihood](https://morrison-lab.github.io/sds/intro-MLEs.html#def-loglik), and minus the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of the empirical distribution minus the divergence.
>
> Show code
>
> ``` r
> n_flips <- 100
> n_heads <- 70
> empirical <- c(tails = n_flips - n_heads, heads = n_heads) / n_flips
> success_prob <- seq(0.1, 0.9, by = 0.1)
> empirical_entropy <- -sum(empirical * log2(empirical))
> divergence <- numeric(length(success_prob))
> avg_loglik <- numeric(length(success_prob))
> for (j in seq_along(success_prob)) {
>   model <- c(1 - success_prob[j], success_prob[j])
>   divergence[j] <- sum(empirical * log2(empirical / model))
>   avg_loglik[j] <- sum(empirical * log2(model))
> }
> decomposition <- -empirical_entropy - divergence
> data.frame(
>   success_prob,
>   divergence = round(divergence, 4),
>   avg_loglik = round(avg_loglik, 4),
>   decomposition = round(decomposition, 4)
> )
> ```
>
> The last two columns agree, as the proof says. The divergence is smallest, at $0$ [bits](entropy.llms.md#def-bit), and the average log-likelihood is largest for the model with probability of heads $0.7$, which is the fraction of heads in the data, so that model is the empirical distribution.

> **NOTE:**
>
> *Remark 1* (One labeled example). For a single labeled example, $n = 1$, and the [empirical distribution](https://morrison-lab.github.io/sds/nonparametric-models.html#def-empirical-distribution) puts all its mass on the observed label. Then [Theorem 1](#thm-maximum-likelihood-kl-divergence) says that the model with the largest [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) for that label is the model with the smallest divergence from it. That is the case that [the cross-entropy loss remark](source-coding.llms.md#rem-cross-entropy-loss) describes.

## References

Back to top
