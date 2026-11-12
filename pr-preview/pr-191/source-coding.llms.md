# Source coding

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-12 00:51:44 (PST)

## 1 Codes

> **NOTE:**
>
> **Definition 1 (Binary code)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv). A **binary code** for $X$ assigns each value $x$ a *codeword*, a string of $\ell(x)$ [bits](entropy.llms.md#def-bit).

> **NOTE:**
>
> **Definition 2 (Uniquely decodable code)** A [binary code](#def-code) is **uniquely decodable** if every finite [sequence](https://morrison-lab.github.io/mcs/functions.html#def-sequence) of codewords, written one after another, can be split back into codewords in only one way.

> **NOTE:**
>
> **Definition 3 (Expected length)** The **expected length** of a [binary code](#def-code) for a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [codeword length](#def-code):
>
> $$L \stackrel{\text{def}}{=}{\mathbb{E}\mathopen{}\left[\ell(X)\right]\mathclose{}}.$$

> **NOTE:**
>
> **Theorem 1 (Expected length as a sum over values)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) $p(x) \stackrel{\text{def}}{=}\mathbb{P}(X=x)$. The [expected length](#def-expected-length) of a [binary code](#def-code) for $X$ is
>
> $$L = \sum_{x} p(x) \, \ell(x).$$

> **NOTE:**
>
> *Proof*. The [codeword length](#def-code) $\ell(X)$ is a [random variable](https://morrison-lab.github.io/pds/random-variables.html#def-random-variable) whose possible values are the [codeword lengths](#def-code) $\ell(x)$. By the [definition of expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation),
>
> $$L = \sum_{k} k \, \mathbb{P}(\ell(X) = k).$$
>
> The [event](https://morrison-lab.github.io/pds/probability-basics.html#def-event) $\ell(X) = k$ is the [union](https://morrison-lab.github.io/mcs/sets.html#def-union) of the [disjoint](https://morrison-lab.github.io/pds/probability-basics.html#def-mutually-exclusive) [events](https://morrison-lab.github.io/pds/probability-basics.html#def-event) $X = x$ over the values $x$ with $\ell(x) = k$. So $\mathbb{P}(\ell(X) = k) = \sum_{x : \ell(x) = k} p(x)$, and
>
> $$L = \sum_{k} \sum_{x : \ell(x) = k} k \, p(x).$$
>
> On the inner sum $k = \ell(x)$. Every value $x$ lies in exactly one inner sum, so the double sum runs once over each value:
>
> $$L = \sum_{x} \ell(x) \, p(x).$$

> **NOTE:**
>
> **Example 1 (Expected length of a code for a three-valued variable)**  
>
> Let $X$ have [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) $p = (1/2, 1/4, 1/4)$, and let a [binary code](#def-code) for $X$ have [codeword lengths](#def-code) $\ell = (1, 2, 2)$. The code below computes the [expected length](#def-expected-length) from its definition, as the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of $\ell(X)$, and as the sum in [Theorem 1](#thm-expected-length-sum).
>
> Show code
>
> ``` r
> p <- c(1 / 2, 1 / 4, 1 / 4)
> len <- c(1, 2, 2)
> lengths_seen <- sort(unique(len))
> prob_of_length <- vapply(
>   lengths_seen,
>   function(k) sum(p[len == k]),
>   numeric(1)
> )
> from_definition <- sum(lengths_seen * prob_of_length)
> from_sum <- sum(p * len)
> c(from_definition = from_definition, from_sum = from_sum)
> #> from_definition        from_sum 
> #>             1.5             1.5
> ```
>
> Both give $L = 1.5$ [bits](entropy.llms.md#def-bit), as [Theorem 1](#thm-expected-length-sum) states.

> **NOTE:**
>
> *Remark 1* (Short codewords for common values). A code with a small [expected length](#def-expected-length) gives frequent values short codewords and rare values long ones, since each value’s $\ell(x)$ counts in $L$ weighted by its [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability).

## 2 The source coding theorem

> **NOTE:**
>
> **Theorem 2 (Source coding theorem)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) that takes a finite number of values, at least two of them with nonzero [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability), and let ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ be its [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm).
>
> 1.  Every [uniquely decodable](#def-uniquely-decodable) [binary code](#def-code) for $X$ has [expected length](#def-expected-length) $L \ge {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$.
>
> 2.  Some uniquely decodable binary code for $X$ has expected length $L < {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + 1$.
>
> 3.  Coding $n$ [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt) copies of $X$ at a time, some uniquely decodable binary code spends, on average, fewer than ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + 1/n$ [bits](entropy.llms.md#def-bit) per copy.

> **NOTE:**
>
> *Remark 2* (Where the theorem comes from). Shannon ([1948](#ref-shannon1948mathematical)) proved that no compression of the output of a source can beat its [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy). Cover and Thomas ([2006, sec. 5.3](#ref-cover2006elements) to 5.5) prove each part of [Theorem 2](#thm-source-coding). For part 2, they give each value $x$ with $p(x) > 0$ the length $\ell(x) = \lceil -\log_2 p(x) \rceil$, its [surprisal](entropy.llms.md#def-surprisal) in [bits](entropy.llms.md#def-bit) rounded up; Kraft’s condition ([Cover and Thomas 2006, sec. 5.2](#ref-cover2006elements)) guarantees that there is a code with these lengths.

## 3 Coding with the wrong distribution

> **NOTE:**
>
> **Theorem 3 (The cost of coding with the wrong distribution)** Let $X$ take a finite number of values, with [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) $p$, and let $q$ be such a function, possibly different from $p$, with $q(x) > 0$ wherever $p(x) > 0$. Suppose a code gives each value $x$ with $p(x) > 0$ the length $\ell(x) = \lceil -\log_2 q(x) \rceil$. Then its [expected length](#def-expected-length) $L$ under $p$ satisfies
>
> $${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}} \le L < {\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}} + 1,$$
>
> where ${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}}$ is the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) of $q$ relative to $p$, with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm).

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
> The middle sum is $L$ by [Theorem 1](#thm-expected-length-sum), and the outer sums are ${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}}$.

> **NOTE:**
>
> **Theorem 4 (Cross-entropy is entropy plus divergence)** Let $p$ and $q$ be [probability mass functions](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) on the values $x_1, \ldots, x_n$, with $q(x) > 0$ wherever $p(x) > 0$. Write ${\mathbb{H}\mathopen{}\left(p\right)\mathclose{}}$ for the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $p$, ${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}}$ for the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) of $q$ relative to $p$, and ${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}}$ for the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of $q$ from $p$, all with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm). Then
>
> $${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(p\right)\mathclose{}} + {{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}}.$$

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
> Reading left to right, these are ${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}}$, ${\mathbb{H}\mathopen{}\left(p\right)\mathclose{}}$ and ${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}}$.

> **NOTE:**
>
> **Example 2 (Cross-entropy, entropy and divergence for a uniform code)**  
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
> The cross-entropy is ${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}} = 1.585$ bits. The entropy is ${\mathbb{H}\mathopen{}\left(p\right)\mathclose{}} = 1.5$ bits, and the divergence is ${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}} = 0.085$ bits. They satisfy [Theorem 4](#thm-cross-entropy-decomposition): 1.5 + 0.085 = 1.585.

> **NOTE:**
>
> *Remark 3* (Cross-entropy is the cost of the wrong code). [Theorem 4](#thm-cross-entropy-decomposition) splits the [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) into the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) and the divergence. By [Theorem 2](#thm-source-coding), no [uniquely decodable code](#def-uniquely-decodable) averages fewer than ${\mathbb{H}\mathopen{}\left(p\right)\mathclose{}}$ [bits](entropy.llms.md#def-bit). By [Theorem 3](#thm-wrong-code), a code built for $q$ costs about ${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}}$ bits per value more than that. By the [divergence theorem](entropy.llms.md#thm-kl-divergence-nonnegative), the excess vanishes only when the code was built for $p$ ([Cover and Thomas 2006, sec. 2.6](#ref-cover2006elements); [Yeung 2008, sec. 2.5](#ref-yeung2008information)). Cover and Thomas ([2006, sec. 5.4](#ref-cover2006elements)) state [Theorem 3](#thm-wrong-code) in this form, with ${\mathbb{H}\mathopen{}\left(p\right)\mathclose{}} + {{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}}$ in place of ${\mathbb{H}\mathopen{}\left(p, q\right)\mathclose{}}$.

> **NOTE:**
>
> *Remark 4* (Why models are fit by minimizing cross-entropy). Fitting a classifier by minimizing [cross-entropy](https://morrison-lab.github.io/pds/expectation.html#def-cross-entropy) chooses the [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $q$ the model assigns so that a code built for $q$ would spend as few [bits](entropy.llms.md#def-bit) as possible on the observed labels. By [Remark 3](#rem-cross-entropy-wrong-code), that pushes $q$ toward the probabilities the labels came from.
>
> For a single labeled example, let $e$ put all its mass on the observed label. Then ${\mathbb{H}\mathopen{}\left(e\right)\mathclose{}} = 0$ ([as for a coin that always lands heads](https://morrison-lab.github.io/pds/expectation.html#exm-entropy-coin)), so the example’s cross-entropy ${\mathbb{H}\mathopen{}\left(e, q\right)\mathclose{}}$ equals ${{D_{\mathrm{KL}}}\mathopen{}\left(e \,\Vert\, q\right)\mathclose{}}$: every [bit](entropy.llms.md#def-bit) it reports is a wasted one.

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

Shannon, C. E. 1948. “A Mathematical Theory of Communication.” *Bell System Technical Journal* 27 (3): 379–423. <https://doi.org/10.1002/j.1538-7305.1948.tb01338.x>.

Yeung, Raymond W. 2008. *Information Theory and Network Coding*. Springer. <https://doi.org/10.1007/978-0-387-79234-7>.

Back to top
