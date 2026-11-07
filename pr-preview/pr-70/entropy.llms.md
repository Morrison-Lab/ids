# Entropy and mutual information

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-07 13:01:22 (PST)

This page builds on the definitions of [entropy, cross-entropy and Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#sec-entropy) in *Probability for Data Science*.

## 1 Surprisal

> **NOTE:**
>
> **Definition 1 (Surprisal)** The **surprisal** of an outcome $x$ of a discrete random variable $X$ with $\mathbb{P}(X=x) > 0$ is
>
> $$s(x) \stackrel{\text{def}}{=}-\log \mathbb{P}(X=x).$$
>
> With base-2 logarithms, surprisal is also called the **Shannon information content** of the outcome $x$ ([MacKay 2003, sec. 2.4](#ref-mackay2003information)).

> **NOTE:**
>
> **Definition 2 (Bit (shannon))** A **bit**, also called a **shannon** (symbol Sh) ([International Electrotechnical Commission 2008](#ref-iec80000132008)), is the unit of information when the logarithm in [surprisal](#def-surprisal), and in every quantity built from it, has base $2$.
>
> One bit is the surprisal of an outcome with probability $1/2$: for an outcome $x$ of a discrete random variable $X$,
>
> $$\begin{aligned}
> s(x) = 1 \text{ bit}
> &\iff -\log_2 \mathbb{P}(X=x) = 1\\
> &\iff \mathbb{P}(X=x) = 2^{-1} = \tfrac{1}{2}.
> \end{aligned}$$
>
> In words, a bit is the surprisal of the outcome of one binary trial whose two outcomes are equally likely, such as one toss of a fair coin.

> **NOTE:**
>
> **Example 1 (Counting bits with fair coins)** One toss of a fair coin has $2$ equally likely outcomes, and one binary digit is enough to record which one happened. Two tosses have $4$ outcomes, and two binary digits record them. In general, $k$ tosses have $n = 2^k$ equally likely outcomes, and $k = \log_2 n$ binary digits record them.
>
> Each of those $n$ outcomes has probability $p = 1/n$, so
>
> $$\begin{aligned}
> k
> &= \log_2 n \\
> &= \log_2 \frac{1}{p} \\
> &= -\log_2 p,
> \end{aligned}$$
>
> which is the [surprisal](#def-surprisal) of the outcome, in [bits](#def-bit).
>
> Ten tosses that all land heads have probability $2^{-10}$, so
>
> $$\begin{aligned}
> s(\text{ten heads})
> &= -\log_2 2^{-10} \\
> &= 10 \text{ bits}.
> \end{aligned}$$

> **NOTE:**
>
> **Definition 3 (Nat)** A **nat** is the unit of information when the logarithm in [surprisal](#def-surprisal), and in every quantity built from it, is the natural logarithm.
>
> One nat is the surprisal of an outcome with probability $1/\text{e}$: for an outcome $x$ of a discrete random variable $X$,
>
> $$\begin{aligned}
> s(x) = 1 \text{ nat}
> &\iff -\ln \mathbb{P}(X=x) = 1\\
> &\iff \mathbb{P}(X=x) = \text{e}^{-1} = 1/\text{e}\approx 0.368.
> \end{aligned}$$

> **NOTE:**
>
> **Example 2 (One fair coin toss in nats)** By [Example 1](#exm-surprisal-coins) with $k = 1$, one toss of a fair coin landing heads has a [surprisal](#def-surprisal) of $1$ [bit](#def-bit). In [nats](#def-nat), the same outcome has a surprisal of
>
> $$\begin{aligned}
> s(\text{heads})
> &= -\ln \tfrac{1}{2} \\
> &= \ln 2 \\
> &\approx 0.693 \text{ nats}.
> \end{aligned}$$

> **NOTE:**
>
> *Remark 1* (Converting between bits and nats). For any probability $p \in (0, 1]$, the change-of-base rule for logarithms gives
>
> $$\begin{aligned}
> -\log_2 p
> &= \frac{-\ln p}{\ln 2}\\
> &\approx 1.443 \times (-\ln p).
> \end{aligned}$$
>
> So an outcome with a [surprisal](#def-surprisal) of $1$ [nat](#def-nat) has a surprisal of $1 / \ln 2 \approx 1.443$ [bits](#def-bit), and the $\ln 2 \approx 0.693$ [nats](#def-nat) of [Example 2](#exm-coin-nats) are exactly $\ln 2 / \ln 2 = 1$ [bit](#def-bit).
>
> A bit as a unit of information is not the same thing as a bit as a binary digit. The name [shannon](#def-bit) refers only to the unit of information, so it avoids this ambiguity. A binary digit whose two values are equally likely has a surprisal of exactly $1$ bit, whichever value it takes. A binary digit that is $0$ nine times in ten does not: the value $0$ has a surprisal of $-\log_2 0.9 \approx 0.152$ bits, and the value $1$ has a surprisal of $-\log_2 0.1 \approx 3.322$ bits.

> **NOTE:**
>
> *Remark 2* (Unlikely outcomes carry more information). Surprisal is large when an outcome was unlikely, and it falls to $0$ as the outcome becomes certain. Correctly predicting heads on one toss of a fair coin is worth $1$ bit; correctly predicting ten heads in a row is worth $10$ bits.

> **NOTE:**
>
> *Remark 3* (Entropy is expected surprisal). The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a discrete random variable $X$ is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [surprisal](#def-surprisal):
>
> $$\begin{aligned}
> H(X)
> &= {\mathbb{E}\mathopen{}\left[-\log \mathbb{P}(X)\right]\mathclose{}} \\
> &= {\mathbb{E}\mathopen{}\left[s(X)\right]\mathclose{}}.
> \end{aligned}$$
>
> So $H(X)$ is the average number of bits (with base-2 logarithms) needed to record an outcome of $X$ when each outcome $x$ costs $s(x)$ bits. The [source coding theorem](source-coding.llms.md#thm-source-coding), on a later page of these notes, makes that average precise: no uniquely decodable code does better.

> **NOTE:**
>
> **Definition 4 (Rarity)** The **rarity** of an [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) $x$ of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the reciprocal of its [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) mass:
>
> $${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} \stackrel{\text{def}}{=}\frac{1}{\mathbb{P}(X=x)}.$$
>
> For a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) $X$ with [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) $\mathbb{p}$, the rarity of a value $x$ is the reciprocal of the density:
>
> $${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} \stackrel{\text{def}}{=}\frac{1}{\mathbb{p}(x)}.$$
>
> When the mass or the density is $0$, the rarity is $\infty$.

> **NOTE:**
>
> **Example 3 (Rarity of the outcomes of a die)**  
>
> Let $X$ be the roll of a fair six-sided die. Each [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) has [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/6$.
>
> Show code
>
> ``` r
> rarity <- function(p) 1 / p
> p_fair <- 1 / 6
> p_loaded_six <- 1 / 2
> p_loaded_other <- (1 - p_loaded_six) / 5
> rarity_fair <- rarity(p_fair)
> rarity_loaded_six <- rarity(p_loaded_six)
> rarity_loaded_other <- rarity(p_loaded_other)
> rarities <- c(
>   fair = rarity_fair,
>   loaded_six = rarity_loaded_six,
>   loaded_other = rarity_loaded_other
> )
> rarities
> #>         fair   loaded_six loaded_other 
> #>            6            2           10
> ```
>
> So each face of the fair die has [rarity](#def-rarity) ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} = 6$: one roll in six.
>
> Suppose the die is loaded so that a six has probability $1/2$. Then ${\mathbb{r}\mathopen{}\left(6\right)\mathclose{}} = 2$. If the other five faces share the rest equally, each has ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} = 10$. The more probable an outcome, the lower its rarity.

> **NOTE:**
>
> *Remark 4* (Source of the name). Leinster writes that, for a community whose $i$th species has relative abundance $p_i$, “$1/p_i$ is a measure of its rarity or specialness” ([Leinster 2021, sec. 2.4](#ref-leinster2021entropy), p. 52). The name “rarity” for the reciprocal of a [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) is borrowed from there.

> **NOTE:**
>
> **Theorem 1 (Surprisal is the logarithm of the rarity)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), and let $x$ be an [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) with $\mathbb{P}(X=x) > 0$. Then the [surprisal](#def-surprisal) of $x$ is the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of its [rarity](#def-rarity):
>
> $${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} = {\operatorname{log}\mathopen{}\left\{{\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. $$\begin{aligned}
> {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}
> &= -{\operatorname{log}\mathopen{}\left\{\mathbb{P}(X=x)\right\}\mathclose{}} && \text{(definition of surprisal)} \\
> &= {\operatorname{log}\mathopen{}\left\{\frac{1}{\mathbb{P}(X=x)}\right\}\mathclose{}} && \text{(logarithm of a reciprocal)} \\
> &= {\operatorname{log}\mathopen{}\left\{{\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}}. && \text{(definition of rarity)}
> \end{aligned}$$

> **NOTE:**
>
> **Theorem 2 (Surprisal of a continuous value is the logarithm of the rarity)** Let $X$ be a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) with [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) $\mathbb{p}$, and let $x$ be a value with $\mathbb{p}(x) > 0$. Then the [surprisal](#def-surprisal) of $x$ is the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of its [rarity](#def-rarity):
>
> $${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} = {\operatorname{log}\mathopen{}\left\{{\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. $$\begin{aligned}
> {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}
> &= -{\operatorname{log}\mathopen{}\left\{\mathbb{p}(x)\right\}\mathclose{}} && \text{(definition of surprisal)} \\
> &= {\operatorname{log}\mathopen{}\left\{\frac{1}{\mathbb{p}(x)}\right\}\mathclose{}} && \text{(logarithm of a reciprocal)} \\
> &= {\operatorname{log}\mathopen{}\left\{{\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}}. && \text{(definition of rarity)}
> \end{aligned}$$

> **NOTE:**
>
> **Corollary 1 (Surprisal of a discrete outcome is nonnegative)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), and let $x$ be an [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) with $\mathbb{P}(X=x) > 0$. Then the [rarity](#def-rarity) of $x$ is at least $1$, with equality exactly when $\mathbb{P}(X=x) = 1$, and the [surprisal](#def-surprisal) satisfies
>
> $${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} \ge 0.$$

> **NOTE:**
>
> *Proof*. Since $0 < \mathbb{P}(X=x) \le 1$, the [rarity](#def-rarity) ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} = 1 / \mathbb{P}(X=x)$ is at least $1$, with equality exactly when $\mathbb{P}(X=x) = 1$. The [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) is increasing, and ${\operatorname{log}\mathopen{}\left\{1\right\}\mathclose{}} = 0$, so by [Theorem 1](#thm-surprisal-log-rarity), ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} = {\operatorname{log}\mathopen{}\left\{{\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}} \ge 0$.

> **NOTE:**
>
> **Example 4 (Surprisal and rarity of an outcome with probability one quarter)** Take an [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/4$:
>
> Show code
>
> ``` r
> p_four <- 1 / 4
> rarity_four <- 1 / p_four
> surprisal_four <- log2(rarity_four)
> surprisal_four
> #> [1] 2
> ```
>
> It has [rarity](#def-rarity) $4$ by definition. By [Theorem 1](#thm-surprisal-log-rarity), its [surprisal](#def-surprisal) is the base-2 [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of that rarity, $2$ [bits](#def-bit).

> **NOTE:**
>
> *Remark 5* (Reading the rarity of an outcome). A [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) can exceed $1$, so for a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) the [rarity](#def-rarity) can be below $1$, and then the [surprisal](#def-surprisal) is negative ([Theorem 2](#thm-surprisal-log-rarity-continuous)). For a mass, a rarity of $r$ reads “one in $r$”, and the surprisal is the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of $r$ ([Theorem 1](#thm-surprisal-log-rarity)).

> **NOTE:**
>
> *Remark 6* (Values of the probability, the rarity and the surprisal). For a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), the mass $\mathbb{P}(X=x)$ of an [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) with a mass above $0$, its [rarity](#def-rarity) ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}$ and its [surprisal](#def-surprisal) ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ take the values in the middle column. For a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv), the [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) $\mathbb{p}(x)$ takes the place of the mass. At a value $x$ with a density above $0$, the rarity ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}$ is the reciprocal of $\mathbb{p}(x)$, and the surprisal ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ is the [surprisal of a continuous value](https://morrison-lab.github.io/pds/expectation.html#def-surprisal-continuous). Their values are in the right column.
>
> |  | Mass $\mathbb{P}(X=x)$ | Density $\mathbb{p}(x)$ |
> |----|----|----|
> | Mass or density | $(0, 1]$ | $(0, \infty)$ |
> | Rarity ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}$ | $[1, \infty)$ | $(0, \infty)$ |
> | Surprisal ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ | $[0, \infty)$ | $(-\infty, \infty)$ |
>
> - **Mass.** A mass of $1$ gives the smallest rarity, $1$, and the smallest surprisal, $0$. No mass exceeds $1$, the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) of a certain outcome. So no mass gives a rarity below $1$ or a surprisal below $0$.
> - **Density.** A density can be arbitrarily large, as in the [uniform example](https://morrison-lab.github.io/pds/expectation.html#exm-entropy-uniform), so the rarity can fall below $1$ and the surprisal can fall below $0$.
> - **Zero.** A mass or density of $0$ gives a rarity and a surprisal of $\infty$.
> - **Units.** A mass has no units. A density has the units of $1/x$, so its rarity has the units of $x$. Rescaling $x$ by a nonzero $c$ shifts its surprisal by ${\operatorname{log}\mathopen{}\left\{\mathopen{}\left|c\right|\mathclose{}\right\}\mathclose{}}$.

> **NOTE:**
>
> *Remark 7* (Differential entropy differs from entropy). A [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) value is not a probability, so the [surprisal](https://morrison-lab.github.io/pds/expectation.html#def-surprisal-continuous) of a continuous value and the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a continuous random variable (the differential entropy) behave differently from their discrete counterparts:
>
> - **Sign.** A density can exceed $1$, so the surprisal ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ and the differential entropy can be negative, as in the [uniform example](https://morrison-lab.github.io/pds/expectation.html#exm-entropy-uniform) ([Cover and Thomas 2006, sec. 8.1](#ref-cover2006elements)). The entropy of a discrete random variable is never negative.
> - **Units.** Rescaling changes the differential entropy: ${\mathbb{H}\mathopen{}\left(aX\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + \log |a|$ for a constant $a \ne 0$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.4). Measuring the same quantity in metres rather than centimetres therefore changes it. Adding a constant does not: ${\mathbb{H}\mathopen{}\left(X + c\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.3).
> - **Not a limit of entropy.** Round a continuous $X$ to bins of width $\Delta$, which gives a discrete random variable $X^\Delta$. Then ${\mathbb{H}\mathopen{}\left(X^\Delta\right)\mathclose{}} + \log \Delta \to {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ as $\Delta \to 0$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.3.1). The entropy ${\mathbb{H}\mathopen{}\left(X^\Delta\right)\mathclose{}}$ itself grows without bound as $\Delta \to 0$, so the differential entropy is not its limit.

> **NOTE:**
>
> **Definition 5 (Collision probability)** The **collision probability** of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the chance that two [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt) copies $X$ and $X'$ of $X$ take the same value:
>
> $$\mathbb{P}(X = X') = \sum_x \mathbb{P}(X=x)^2.$$

> **NOTE:**
>
> **Definition 6 (Rényi entropy of order 2 (collision entropy))** The **Rényi entropy of order 2**, also called the **collision entropy** ([Wikipedia contributors 2026](#ref-wikipedia_renyi_entropy)), of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the negative [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability), where $\mathbb{P}(X)$ is the [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) evaluated at the [random variable](https://morrison-lab.github.io/pds/random-variables.html#def-random-variable) $X$ itself:
>
> $$H_2(X) = -\log {\mathbb{E}\mathopen{}\left[\mathbb{P}(X)\right]\mathclose{}}.$$

> **NOTE:**
>
> **Theorem 3 (The expected probability is the collision probability)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), and let $X'$ be an [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt) copy of $X$. Then
>
> $${\mathbb{E}\mathopen{}\left[\mathbb{P}(X)\right]\mathclose{}} = \sum_x \mathbb{P}(X=x)^2 = \mathbb{P}(X = X').$$

> **NOTE:**
>
> *Proof*. The [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of $\mathbb{P}(X)$ adds, over the values $x$, the value $\mathbb{P}(X=x)$ times its [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $\mathbb{P}(X=x)$:
>
> $$\begin{aligned}
> {\mathbb{E}\mathopen{}\left[\mathbb{P}(X)\right]\mathclose{}}
> &= \sum_x \mathbb{P}(X=x) \, \mathbb{P}(X=x) \\
> &= \sum_x \mathbb{P}(X=x)^2.
> \end{aligned}$$
>
> By the definition of the [collision probability](#def-collision-probability), the last [sum](https://morrison-lab.github.io/mds/algebra-sums.html#def-summation) is $\mathbb{P}(X = X')$.

> **NOTE:**
>
> **Theorem 4 (The collision entropy is at most the Shannon entropy)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with values $x_1, \ldots, x_n$. Then the [collision entropy](#def-renyi-entropy) is at most the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy):
>
> $$H_2(X) \le {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}.$$
>
> The two coincide exactly when each value that $X$ takes with positive [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) has the same probability.

> **NOTE:**
>
> *Proof*. Write $\mathbb{P}(X)$ for the [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) evaluated at $X$. The function $-\log$ is [strictly convex](https://morrison-lab.github.io/mds/algebra-sums.html#def-convex-function), so Jensen’s inequality gives
>
> $${\mathbb{E}\mathopen{}\left[-\log \mathbb{P}(X)\right]\mathclose{}} \ge -\log {\mathbb{E}\mathopen{}\left[\mathbb{P}(X)\right]\mathclose{}},$$
>
> with equality exactly when $\mathbb{P}(X)$ is constant. The left side is ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$. The right side is $H_2(X)$ by its definition. The function $\mathbb{P}(X)$ is constant exactly when every value that $X$ takes with positive [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) has that same probability.

> **NOTE:**
>
> **Example 5 (Collision entropy and entropy of a three-valued random variable)**  
>
> Let $X$ take three values with probabilities $1/2$, $1/4$ and $1/4$. The code below computes the expected [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability), the [collision entropy](#def-renyi-entropy) and the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy), with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm).
>
> Show code
>
> ``` r
> p <- c(1 / 2, 1 / 4, 1 / 4)
> expected_prob <- sum(p^2)
> collision_entropy <- -log2(expected_prob)
> shannon_entropy <- -sum(p * log2(p))
> c(
>   expected_prob = expected_prob,
>   collision_entropy = collision_entropy,
>   shannon_entropy = shannon_entropy
> )
> #>     expected_prob collision_entropy   shannon_entropy 
> #>          0.375000          1.415037          1.500000
> ```
>
> By [Theorem 3](#thm-expected-probability-collision), the expected probability ${\mathbb{E}\mathopen{}\left[\mathbb{P}(X)\right]\mathclose{}} = 0.375$ is the [collision probability](#def-collision-probability). The collision entropy is $H_2(X) = 1.415$ [bits](#def-bit). The entropy is ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} = 1.5$ bits. As [Theorem 4](#thm-collision-entropy-at-most-entropy) states, $H_2(X) \le {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$, and the two differ because the three values are not equally likely.

> **NOTE:**
>
> *Remark 8* (Two ways to summarize a random variable by its probabilities). [Entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of the [surprisal](#def-surprisal) $-\log \mathbb{P}(X)$. Taking the expectation of the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $\mathbb{P}(X)$ itself summarizes $X$ differently. For a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), [Theorem 3](#thm-expected-probability-collision) identifies that expectation with the [collision probability](#def-collision-probability), so the [collision entropy](#def-renyi-entropy) is $H_2(X) = -\log \mathbb{P}(X = X')$.
>
> For a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) with [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) $\mathbb{p}$, the analogue is ${\mathbb{E}\mathopen{}\left[\mathbb{p}(X)\right]\mathclose{}} = \int \mathbb{p}(x)^2\,dx$. The [expected-density exercises](https://morrison-lab.github.io/pds/expectation.html#exr-expected-density) derive this quantity, then compute it in the [uniform case](https://morrison-lab.github.io/pds/expectation.html#exr-expected-density-uniform) and the [normal case](https://morrison-lab.github.io/pds/expectation.html#exr-expected-density-normal).
>
> [Theorem 4](#thm-collision-entropy-at-most-entropy) compares the collision entropy with the [Shannon entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy).

> **NOTE:**
>
> *Remark 9* (Surprisal and the Fisher information). When the probabilities depend on a parameter $\theta$, the [surprisal](#def-surprisal) of an outcome $x$ is $-\log \mathbb{p}(x \mid \theta)$, which is minus the log-likelihood:
>
> $$\mathbb{s}_{\theta}(x) = -\log \mathbb{p}(x \mid \theta) = -\ell(\theta).$$
>
> Its derivative with respect to $\theta$ is minus the [score](https://morrison-lab.github.io/sds/intro-MLEs.html#def-score):
>
> $$\frac{\partial}{\partial \theta} \mathbb{s}_{\theta}(x) = -{\ell'\mathopen{}\left(\theta\right)\mathclose{}}.$$
>
> The expected squared score is the [expected information](https://morrison-lab.github.io/sds/intro-MLEs.html#def-einf), also called the Fisher information. It is also the expected [second derivative](https://morrison-lab.github.io/mds/calculus-derivatives.html#def-second-derivative) of the surprisal, when the outcome $X$ is drawn from the model at the true parameter value $\theta_0$, and the score is evaluated at that same outcome $X$:
>
> $$\mathcal{I}(\theta_0)
> = \mathbb{E}_{\theta_0}\mathopen{}\left[{\ell'\mathopen{}\left(\theta_0\right)\mathclose{}}^2\right]\mathclose{}
> = \mathbb{E}_{\theta_0}\mathopen{}\left[\left.{\frac{\partial^2}{\partial \theta^2} \mathbb{s}_{\theta}(X)}\right|_{\theta= \theta_0}\right]\mathclose{}.$$
>
> It is also the second derivative, at the true parameter value, of the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) between the model at that value and the model at the varying value ([proved in the sds notes](https://morrison-lab.github.io/sds/intro-MLEs.html#thm-fisher-kl-curvature)):
>
> $$\left.{\frac{\partial^2}{\partial \theta^2} {{D_{\mathrm{KL}}}\mathopen{}\left(\theta_0 \,\Vert\, \theta\right)\mathclose{}}}\right|_{\theta= \theta_0} = \mathcal{I}(\theta_0).$$

## 2 Joint and conditional entropy

> **NOTE:**
>
> **Definition 7 (Joint entropy)** Let $X$ and $Y$ be discrete random variables with joint probability mass function $p(x, y) \stackrel{\text{def}}{=}\mathbb{P}(X=x, Y=y)$. Their **joint entropy** is the entropy of the pair $(X, Y)$:
>
> $$H(X, Y) \stackrel{\text{def}}{=}-\sum_{x, y} p(x, y) \log p(x, y),$$
>
> where the sum runs over the pairs with $p(x, y) > 0$.

> **NOTE:**
>
> **Definition 8 (Entropy given one value)** For $X$ and $Y$ as in [Definition 7](#def-joint-entropy), write $p(y \mid x) \stackrel{\text{def}}{=}\mathbb{P}(Y=y \mid X=x)$. The **entropy of** $Y$ given $X=x$, for a value $x$ with $\mathbb{P}(X=x) > 0$, is
>
> $$H(Y \mid X=x) \stackrel{\text{def}}{=}-\sum_{y} p(y \mid x) \log p(y \mid x),$$
>
> where the sum runs over the values $y$ with $p(y \mid x) > 0$.

> **NOTE:**
>
> **Definition 9 (Conditional entropy)** For $X$ and $Y$ as in [Definition 7](#def-joint-entropy), write $p(x) \stackrel{\text{def}}{=}\mathbb{P}(X=x)$. The **conditional entropy** of $Y$ given $X$ averages the [entropy of](#def-entropy-given-value) $Y$ given each value of $X$ over the distribution of $X$:
>
> $$H(Y \mid X) \stackrel{\text{def}}{=}\sum_{x} p(x) \, H(Y \mid X=x),$$
>
> where the sum runs over the values $x$ with $p(x) > 0$.

> **NOTE:**
>
> **Theorem 5 (Chain rule for entropy)** For discrete random variables $X$ and $Y$,
>
> $$H(X, Y) = H(X) + H(Y \mid X).$$

> **NOTE:**
>
> *Proof*. Use the notation of [Definition 8](#def-entropy-given-value) and [Definition 9](#def-conditional-entropy), with every sum over the pairs with $p(x, y) > 0$. Since $p(x, y) = p(x) \, p(y \mid x)$,
>
> $$\begin{aligned}
> H(X, Y)
> &= -\sum_{x, y} p(x, y) \log p(x, y) \\
> &= -\sum_{x, y} p(x, y) \log \mathopen{}\left[p(x) \, p(y \mid x)\right]\mathclose{} \\
> &= -\sum_{x, y} p(x, y) \log p(x)
>    - \sum_{x, y} p(x, y) \log p(y \mid x) \\
> &= -\sum_{x} \log p(x) \sum_{y} p(x, y)
>    - \sum_{x} p(x) \sum_{y} p(y \mid x) \log p(y \mid x) \\
> &= -\sum_{x} p(x) \log p(x)
>    + \sum_{x} p(x) \, H(Y \mid X=x) \\
> &= H(X) + H(Y \mid X).
> \end{aligned}$$
>
> The fourth line groups the terms by $x$ and uses $p(x, y) = p(x) \, p(y \mid x)$ in the second sum; the fifth uses $\sum_{y} p(x, y) = p(x)$ and the definition of $H(Y \mid X=x)$.

## 3 Mutual information

> **NOTE:**
>
> **Definition 10 (Mutual information)** The **mutual information** between discrete random variables $X$ and $Y$ with finite entropies is the reduction in the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $Y$ from learning $X$:
>
> $$I(X; Y) \stackrel{\text{def}}{=}H(Y) - H(Y \mid X),$$
>
> where $H(Y \mid X)$ is the [conditional entropy](#def-conditional-entropy).

> **NOTE:**
>
> **Theorem 6 (Mutual information is symmetric)** For discrete random variables $X$ and $Y$ with finite entropies,
>
> $$I(X; Y) = H(X) - H(X \mid Y) = I(Y; X).$$

> **NOTE:**
>
> *Proof*. The [chain rule](#thm-entropy-chain-rule) expands $H(X, Y)$ in either order:
>
> $$H(X) + H(Y \mid X) = H(X, Y) = H(Y) + H(X \mid Y).$$
>
> Subtracting $H(X \mid Y) + H(Y \mid X)$ from the outer two expressions gives
>
> $$H(X) - H(X \mid Y) = H(Y) - H(Y \mid X).$$
>
> The right side is $I(X; Y)$ by [Definition 10](#def-mutual-information), and the left side is $I(Y; X)$ by the same definition.

> **NOTE:**
>
> *Remark 10* (Mutual information as a divergence). Cover and Thomas ([2006, sec. 2.3](#ref-cover2006elements)) define mutual information as the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of the joint distribution of $(X, Y)$ from the product of its marginals, and show that this equals $H(Y) - H(Y \mid X)$ ([Cover and Thomas 2006, sec. 2.4](#ref-cover2006elements)). Since a Kullback–Leibler divergence is never negative, and is $0$ only when the two distributions are equal ([Cover and Thomas 2006, sec. 2.6](#ref-cover2006elements)), $I(X; Y) \ge 0$, with equality exactly when $X$ and $Y$ are independent. Learning $X$ never raises the entropy of $Y$ on average.

> **NOTE:**
>
> **Definition 11 (Information gain)** A decision tree splits the points at a node into branches. The **information gain** of the split is the entropy of the class labels at the node, minus the entropy of the labels in each branch, weighted by the share of the node’s points that branch holds ([Quinlan 1986](#ref-quinlan1986induction)).

> **NOTE:**
>
> *Remark 11* (Information gain is mutual information). Draw one point uniformly at random from the node of [Definition 11](#def-information-gain), and let $Y$ be its class and $X$ the branch it falls into. Then the entropy at the node is $H(Y)$, the weighted entropy left in the branches is $H(Y \mid X)$, and the information gain is the [mutual information](#def-mutual-information) $I(X; Y)$.

> **NOTE:**
>
> **Exercise 1 (Choosing between two splits)** A node holds $20$ points, $10$ red and $10$ green. Two candidate splits each send the points into two branches:
>
> | split | branch | red | green |
> |-------|--------|-----|-------|
> | A     | yes    | $4$ | $0$   |
> |       | no     | $6$ | $10$  |
> | B     | yes    | $5$ | $10$  |
> |       | no     | $5$ | $0$   |
>
> Draw one point uniformly at random from the node, let $Y$ be its color, and let $X$ be the branch it falls into ([Remark 11](#rem-information-gain)). The information gain of each split ([Definition 11](#def-information-gain)) is then $I(X; Y)$. Use base-2 logarithms throughout.
>
> 1.  Compute $H(Y)$.
>
> 2.  For each split, compute $H(Y \mid X = x)$ for both branches, and then $H(Y \mid X)$.
>
> 3.  Compute the information gain $I(X; Y)$ for each split. Which split has the larger gain?

> **NOTE:**
>
> *Solution 1*.
>
> 1.  Half the points are red, so
>
>     $$\begin{aligned}
>     H(Y)
>     &= -\tfrac{1}{2} \log_2 \tfrac{1}{2} - \tfrac{1}{2} \log_2 \tfrac{1}{2} \\
>     &= 1 \text{ bit}.
>     \end{aligned}$$
>
> 2.  A branch holding one color only has entropy $0$. For split A, the “no” branch holds $6$ red and $10$ green points of $16$:
>
>     $$\begin{aligned}
>     H(Y \mid X = \text{no})
>     &= -\tfrac{6}{16} \log_2 \tfrac{6}{16} - \tfrac{10}{16} \log_2 \tfrac{10}{16} \\
>     &\approx 0.531 + 0.424 \\
>     &\approx 0.954 \text{ bits}.
>     \end{aligned}$$
>
>     The “yes” branch holds $4$ of the $20$ points and the “no” branch $16$, so
>
>     $$\begin{aligned}
>     H(Y \mid X)
>     &= \tfrac{4}{20} \cdot 0 + \tfrac{16}{20} \cdot 0.954 \\
>     &\approx 0.764 \text{ bits}.
>     \end{aligned}$$
>
>     For split B, the “yes” branch holds $5$ red and $10$ green points of $15$:
>
>     $$\begin{aligned}
>     H(Y \mid X = \text{yes})
>     &= -\tfrac{1}{3} \log_2 \tfrac{1}{3} - \tfrac{2}{3} \log_2 \tfrac{2}{3} \\
>     &\approx 0.528 + 0.390 \\
>     &\approx 0.918 \text{ bits}.
>     \end{aligned}$$
>
>     The “yes” branch holds $15$ of the $20$ points and the “no” branch $5$, so
>
>     $$\begin{aligned}
>     H(Y \mid X)
>     &= \tfrac{15}{20} \cdot 0.918 + \tfrac{5}{20} \cdot 0 \\
>     &\approx 0.689 \text{ bits}.
>     \end{aligned}$$
>
> 3.  By [Definition 10](#def-mutual-information), the gain is $H(Y) - H(Y \mid X)$:
>
>     - split A: $1 - 0.764 = 0.236$ bits
>     - split B: $1 - 0.689 = 0.311$ bits
>
>     Split B has the larger gain. Both splits isolate a branch of one color, so the gain depends on the other, mixed branch. B’s mixed branch, $5$ red against $10$ green, is more lopsided than A’s $6$ against $10$, so it has less entropy, and it also holds fewer of the points, $15$ against $16$, so its entropy gets less weight.

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

International Electrotechnical Commission. 2008. *Quantities and Units — Part 13: Information Science and Technology*. IEC 80000-13:2008. International Electrotechnical Commission.

Leinster, Tom. 2021. *Entropy and Diversity: The Axiomatic Approach*. Cambridge University Press. <https://doi.org/10.1017/9781108963558>.

MacKay, David J. C. 2003. *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.

Quinlan, J. R. 1986. “Induction of Decision Trees.” *Machine Learning* 1 (1): 81–106. <https://doi.org/10.1007/BF00116251>.

Wikipedia contributors. 2026. *Rényi Entropy — Wikipedia, the Free Encyclopedia*. <https://en.wikipedia.org/wiki/R%C3%A9nyi_entropy>.

Back to top
