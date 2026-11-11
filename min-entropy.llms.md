# Min-entropy

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-11 11:19:07 (PST)

The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a [random variable](https://morrison-lab.github.io/pds/random-variables.html#def-random-variable) averages its [surprisal](entropy.llms.md#def-surprisal). Other summaries of its [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) answer other questions. This page adds the smallest of them, the [min-entropy](#def-min-entropy), to the [collision entropy](entropy.llms.md#def-renyi-entropy).

## 1 Min-entropy

> **NOTE:**
>
> **Definition 1 (Min-entropy)** The **min-entropy** of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of the reciprocal of the largest [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) that $X$ takes any one value:
>
> $${\mathbb{H}_{\infty}\mathopen{}\left(X\right)\mathclose{}} = -\log \max_x {\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}.$$
>
> It is the limiting case of the [Rényi entropy](entropy.llms.md#def-renyi-entropy) of order $\alpha$ ([Rényi 1961](#ref-renyi1961measures)), which approaches it as $\alpha \to \infty$.

> **NOTE:**
>
> **Example 1 (Min-entropy of a three-valued random variable)**  
>
> Let $X$ take three values with [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/2$, $1/4$ and $1/4$. The R chunk below finds the largest probability and the [min-entropy](#def-min-entropy), with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm).
>
> Show code
>
> ``` r
> p <- c(1 / 2, 1 / 4, 1 / 4)
> max_prob <- max(p)
> min_entropy <- -log2(max_prob)
> c(max_prob = max_prob, min_entropy = min_entropy)
> #>    max_prob min_entropy 
> #>         0.5         1.0
> ```
>
> The largest probability is $0.5$, so the min-entropy is ${\mathbb{H}_{\infty}\mathopen{}\left(X\right)\mathclose{}} = 1$ [bit](entropy.llms.md#def-bit).

> **NOTE:**
>
> **Theorem 1 (The min-entropy is at most the collision entropy)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv). Then the [min-entropy](#def-min-entropy) is at most the [collision entropy](entropy.llms.md#def-renyi-entropy):
>
> $${\mathbb{H}_{\infty}\mathopen{}\left(X\right)\mathclose{}} \le {\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Let $p_{\max} = \max_x {\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}$. Each [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) ${\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}$ is at most $p_{\max}$, so ${\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}^2 \le p_{\max} \, {\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}$. Sum over the values $x$:
>
> $$\sum_x {\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}^2 \le p_{\max} \sum_x {\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}.$$
>
> The probabilities sum to $1$, so the [collision probability](entropy.llms.md#def-collision-probability) is at most $p_{\max}$:
>
> $$\mathbb{P}(X = X') = \sum_x {\mathbb{P}\mathopen{}\left(X = x\right)\mathclose{}}^2 \le p_{\max}.$$
>
> The function $-\log$ is decreasing, so taking it of both sides flips the comparison:
>
> $$-\log \mathbb{P}(X = X') \ge -\log p_{\max}.$$
>
> The left side is ${\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}}$ and the right side is ${\mathbb{H}_{\infty}\mathopen{}\left(X\right)\mathclose{}}$.

> **NOTE:**
>
> **Example 2 (Three entropies of one random variable)**  
>
> The R chunk below computes the [min-entropy](#def-min-entropy), the [collision entropy](entropy.llms.md#def-renyi-entropy) and the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of the [random variable](https://morrison-lab.github.io/pds/random-variables.html#def-random-variable) of [Example 1](#exm-min-entropy).
>
> Show code
>
> ``` r
> p <- c(1 / 2, 1 / 4, 1 / 4)
> min_entropy <- -log2(max(p))
> collision_entropy <- -log2(sum(p^2))
> shannon_entropy <- -sum(p * log2(p))
> c(
>   min_entropy = min_entropy,
>   collision_entropy = collision_entropy,
>   shannon_entropy = shannon_entropy
> )
> #>       min_entropy collision_entropy   shannon_entropy 
> #>          1.000000          1.415037          1.500000
> ```
>
> The values rise from $1$ to $1.415$ to $1.5$ [bits](entropy.llms.md#def-bit), as [Theorem 1](#thm-min-entropy-at-most-collision-entropy) and the [collision entropy bound](entropy.llms.md#thm-collision-entropy-at-most-entropy) say.

> **NOTE:**
>
> *Remark 1* (Min-entropy measures the chance of a single guess). The best single guess at the value of $X$ is its most probable value, and that guess is right with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $2^{-{\mathbb{H}_{\infty}\mathopen{}\left(X\right)\mathclose{}}}$. So a [min-entropy](#def-min-entropy) of $k$ [bits](entropy.llms.md#def-bit) says that no guess succeeds with probability above $2^{-k}$. The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) gives no such guarantee, because it can be large while one value is very likely. That is why min-entropy is the measure of a secret’s unpredictability.

## References

Rényi, Alfréd. 1961. “On Measures of Entropy and Information.” In *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Contributions to the Theory of Statistics*, edited by Jerzy Neyman. University of California Press. <https://projecteuclid.org/euclid.bsmsp/1200512181>.

Back to top
