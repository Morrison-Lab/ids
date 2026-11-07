# Source coding

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-07 15:08:34 (PST)

## 1 Codes

> **NOTE:**
>
> **Definition 1 (Binary code)** Let $X$ be a discrete random variable. A **binary code** for $X$ assigns each value $x$ a *codeword*, a finite string of binary digits, of length $\ell(x)$.

> **NOTE:**
>
> **Definition 2 (Uniquely decodable code)** A [binary code](#def-code) is **uniquely decodable** if every finite sequence of codewords, written one after another, can be split back into codewords in only one way.

> **NOTE:**
>
> **Definition 3 (Expected length)** The **expected length** of a [binary code](#def-code) for $X$, where $X$ has probability mass function $p(x) \stackrel{\text{def}}{=}\mathbb{P}(X=x)$, is
>
> $$L \stackrel{\text{def}}{=}{\mathbb{E}\mathopen{}\left[\ell(X)\right]\mathclose{}} = \sum_{x} p(x) \, \ell(x).$$

> **NOTE:**
>
> *Remark 1* (Short codewords for common values). A code with a small [expected length](#def-expected-length) gives frequent values short codewords and rare values long ones, since each value’s length counts in $L$ in proportion to its probability.

## 2 The source coding theorem

> **NOTE:**
>
> **Theorem 1 (Source coding theorem)** Let $X$ be a discrete random variable that takes finitely many values, at least two of them with positive probability, and let $H_2(X)$ be its [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) with base-2 logarithms.
>
> 1.  Every [uniquely decodable](#def-uniquely-decodable) binary code for $X$ has [expected length](#def-expected-length) $L \ge H_2(X)$.
>
> 2.  Some uniquely decodable binary code for $X$ has expected length $L < H_2(X) + 1$.
>
> 3.  Coding blocks of $n$ independent copies of $X$ at a time, some uniquely decodable binary code spends, on average, fewer than $H_2(X) + 1/n$ binary digits per copy.

> **NOTE:**
>
> *Remark 2* (Where the theorem comes from). Shannon ([1948](#ref-shannon1948mathematical)) proved that entropy is the limit on how far the output of a source can be compressed. Cover and Thomas ([2006, sec. 5.3](#ref-cover2006elements) to 5.5) prove each part of [Theorem 1](#thm-source-coding). For part 2, they give each value $x$ with $p(x) > 0$ the length $\ell(x) = \lceil -\log_2 p(x) \rceil$, its [surprisal](entropy.llms.md#def-surprisal) in [bits](entropy.llms.md#def-bit) rounded up; the Kraft inequality ([Cover and Thomas 2006, sec. 5.2](#ref-cover2006elements)) guarantees that a code with these lengths exists.

## 3 Coding with the wrong distribution

> **NOTE:**
>
> **Theorem 2 (The cost of coding with the wrong distribution)** Let $X$ take finitely many values, with probability mass function $p$, and let $q$ be a probability mass function, possibly different from $p$, with $q(x) > 0$ wherever $p(x) > 0$. Suppose a code gives each value $x$ with $p(x) > 0$ the length $\ell(x) = \lceil -\log_2 q(x) \rceil$. Then its [expected length](#def-expected-length) $L$ under $p$ satisfies
>
> $$H_2(p, q) \le L < H_2(p, q) + 1,$$
>
> where $H_2(p, q)$ is the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) of $q$ relative to $p$, with base-2 logarithms.

> **NOTE:**
>
> *Proof*. Every sum here runs over the values $x$ with $p(x) > 0$. Rounding up adds less than one binary digit, so for each such $x$
>
> $$-\log_2 q(x) \le \ell(x) < -\log_2 q(x) + 1.$$
>
> Multiply each part by $p(x) > 0$ and sum. Since $\sum_{x} p(x) = 1$,
>
> $$-\sum_{x} p(x) \log_2 q(x)
> \le \sum_{x} p(x) \, \ell(x)
> < -\sum_{x} p(x) \log_2 q(x) + 1.$$
>
> The middle sum is $L$, and the outer sums are $H_2(p, q)$.

> **NOTE:**
>
> **Theorem 3 (Cross-entropy is entropy plus divergence)** Let $p$ and $q$ be [probability mass functions](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) on the values $x_1, \ldots, x_n$, with $q(x) > 0$ wherever $p(x) > 0$. Write $H_2(p)$ for the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $p$, $H_2(p, q)$ for the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) of $q$ relative to $p$, and $D_2(p \,\|\, q)$ for the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of $q$ from $p$, all with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm). Then
>
> $$H_2(p, q) = H_2(p) + D_2(p \,\|\, q).$$

> **NOTE:**
>
> *Proof*. Every [sum](https://morrison-lab.github.io/mds/algebra-sums.html#def-summation) here runs over the values $x$ with $p(x) > 0$. For every such $x$,
>
> $$-\log_2 q(x)
> = -\log_2 p(x) + \log_2 \frac{p(x)}{q(x)}.$$
>
> Multiply by $p(x)$ and add over $x$:
>
> $$-\sum_x p(x) \log_2 q(x)
> = -\sum_x p(x) \log_2 p(x) + \sum_x p(x) \log_2 \frac{p(x)}{q(x)}.$$
>
> Reading left to right, these are $H_2(p, q)$, $H_2(p)$ and $D_2(p \,\|\, q)$.

> **NOTE:**
>
> **Example 1 (Cross-entropy, entropy and divergence for a uniform code)**  
>
> Let $p = (1/2, 1/4, 1/4)$ be the [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) of a three-valued [random variable](https://morrison-lab.github.io/pds/random-variables.html#def-random-variable), and let $q = (1/3, 1/3, 1/3)$ assign $1/3$ to each of the three values. The code below computes the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy), the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) and the divergence in [bits](entropy.llms.md#def-bit).
>
> Show code
>
> ``` r
> p <- c(1 / 2, 1 / 4, 1 / 4)
> q <- rep(1 / 3, 3)
> cross_entropy <- -sum(p * log2(q))
> shannon_entropy <- -sum(p * log2(p))
> divergence <- sum(p * log2(p / q))
> c(
>   cross_entropy = cross_entropy,
>   shannon_entropy = shannon_entropy,
>   divergence = divergence
> )
> #>   cross_entropy shannon_entropy      divergence 
> #>       1.5849625       1.5000000       0.0849625
> ```
>
> The cross-entropy is $H_2(p, q) = 1.585$ bits. The entropy is $H_2(p) = 1.5$ bits, and the divergence is $D_2(p \,\|\, q) = 0.085$ bits. They satisfy [Theorem 3](#thm-cross-entropy-decomposition): 1.5 + 0.085 = 1.585.

> **NOTE:**
>
> **Theorem 4 (The divergence is nonnegative)** Let $p$ and $q$ be [probability mass functions](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) on the values $x_1, \ldots, x_n$, with $q(x) > 0$ wherever $p(x) > 0$. Then the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) satisfies
>
> $$D_2(p \,\|\, q) \ge 0,$$
>
> with $D_2(p \,\|\, q) = 0$ exactly when $q = p$.

> **NOTE:**
>
> *Proof*. Every [sum](https://morrison-lab.github.io/mds/algebra-sums.html#def-summation) here runs over the values $x$ with $p(x) > 0$. For every $t > 0$, $\ln t \le t - 1$, with equality exactly when $t = 1$. Apply this with $t = q(x) / p(x)$, and multiply by $p(x) > 0$:
>
> $$p(x) \ln \frac{q(x)}{p(x)} \le q(x) - p(x),$$
>
> with equality exactly when $q(x) = p(x)$. Add over $x$. Since $\sum_x p(x) = 1$ and $\sum_x q(x) \le 1$,
>
> $$\sum_x p(x) \ln \frac{q(x)}{p(x)}
> \le \sum_x q(x) - 1
> \le 0.$$
>
> The left side is $-\ln 2 \cdot D_2(p \,\|\, q)$, so $D_2(p \,\|\, q) \ge 0$.
>
> If $D_2(p \,\|\, q) = 0$, both relations hold with equality. The first forces $q(x) = p(x)$ at every $x$ with $p(x) > 0$. The second then gives $\sum_x q(x) = 1$, so $q$ has no mass where $p$ has none, and $q = p$. Conversely, $q = p$ gives $\log_2 (p(x)/q(x)) = 0$ for every $x$.

> **NOTE:**
>
> **Example 2 (Divergence of a biased coin from a fair coin)**  
>
> Let $p = (0.9, 0.1)$ be the [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) of a biased coin, and let $q = (0.5, 0.5)$ be a fair coin. The code below computes the divergence both ways, in [bits](entropy.llms.md#def-bit).
>
> Show code
>
> ``` r
> p <- c(0.9, 0.1)
> q <- c(0.5, 0.5)
> c(
>   p_from_q = sum(p * log2(p / q)),
>   q_from_p = sum(q * log2(q / p)),
>   p_from_p = sum(p * log2(p / p))
> )
> #>  p_from_q  q_from_p  p_from_p 
> #> 0.5310044 0.7369656 0.0000000
> ```
>
> Both divergences between the two coins are positive, as [Theorem 4](#thm-kl-divergence-nonnegative) requires, and they differ, so swapping $p$ and $q$ changes the divergence. The divergence of $p$ from itself is $0$.

> **NOTE:**
>
> *Remark 3* (Cross-entropy is the cost of the wrong code). [Theorem 3](#thm-cross-entropy-decomposition) splits the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) into the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) and the divergence. By [Theorem 1](#thm-source-coding), no uniquely decodable code averages fewer than $H_2(p)$ bits. By [Theorem 2](#thm-wrong-code), a code built for $q$ costs about $D_2(p \,\|\, q)$ bits per value more than that. By [Theorem 4](#thm-kl-divergence-nonnegative), the excess vanishes only when the code was built for $p$ ([Cover and Thomas 2006, sec. 2.6](#ref-cover2006elements); [Yeung 2008, sec. 2.5](#ref-yeung2008information)). Cover and Thomas ([2006, sec. 5.4](#ref-cover2006elements)) state [Theorem 2](#thm-wrong-code) in this form, with $H_2(p) + D_2(p \,\|\, q)$ in place of $H_2(p, q)$.

> **NOTE:**
>
> *Remark 4* (Why models are fit by minimizing cross-entropy). Fitting a classifier by minimizing cross-entropy chooses the model’s distribution $q$ so that a code built for $q$ would spend as few bits as possible on the observed labels. By [Remark 3](#rem-cross-entropy-wrong-code), that pushes $q$ toward the distribution the labels came from.
>
> For a single labeled example, let $e$ be the distribution that puts all its mass on the observed label. Then $H_2(e) = 0$ ([as for a coin that always lands heads](https://morrison-lab.github.io/pds/expectation.html#exm-entropy-coin)), so the example’s cross-entropy loss $H_2(e, q)$ equals $D_2(e \,\|\, q)$: every bit the loss reports is a wasted one.

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

Shannon, C. E. 1948. “A Mathematical Theory of Communication.” *Bell System Technical Journal* 27 (3): 379–423. <https://doi.org/10.1002/j.1538-7305.1948.tb01338.x>.

Yeung, Raymond W. 2008. *Information Theory and Network Coding*. Springer. <https://doi.org/10.1007/978-0-387-79234-7>.

Back to top
