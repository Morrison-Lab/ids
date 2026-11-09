# Entropy and mutual information

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-09 11:50:51 (PST)

This page builds on the definitions of [entropy, cross-entropy and Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#sec-entropy) in *[Probability for Data Science](https://morrison-lab.github.io/pds/)*.

## 1 Surprisal

> **NOTE:**
>
> **Definition 1 (Surprisal)** The **surprisal** of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) $x$ of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ with $\mathbb{P}(X=x) > 0$ is
>
> $$s(x) \stackrel{\text{def}}{=}-\log \mathbb{P}(X=x).$$
>
> With base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm), surprisal is also called the **Shannon information content** of the value $x$ ([MacKay 2003, sec. 2.4](#ref-mackay2003information)).

> **NOTE:**
>
> **Definition 2 (Bit (shannon))** A **bit**, also called a **shannon** (symbol Sh) ([International Electrotechnical Commission 2008](#ref-iec80000132008)), is the unit of information when the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) in [surprisal](#def-surprisal), and in every quantity built from it, has base $2$.
>
> One bit is the surprisal of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/2$: for a value $x$ of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$,
>
> $$\begin{aligned}
> s(x) = 1 \text{ bit}
> &\iff -\log_2 \mathbb{P}(X=x) = 1\\
> &\iff \mathbb{P}(X=x) = 2^{-1} = \tfrac{1}{2}.
> \end{aligned}$$
>
> In words, a bit is the surprisal of the [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) of one trial whose two [outcomes](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) are equally likely, such as one toss of a fair coin.

> **NOTE:**
>
> **Example 1 (Counting bits with fair coins)** One toss of a fair coin has $2$ equally likely [outcomes](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome), and one binary digit is enough to record which one happened. Two tosses have $4$ outcomes, and two binary digits record them. In general, $k$ tosses have $n = 2^k$ equally likely outcomes, and $k = \log_2 n$ binary digits record them.
>
> Each of those $n$ outcomes has [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $p = 1/n$, so
>
> $$\begin{aligned}
> k
> &= \log_2 n \\
> &= \log_2 \frac{1}{p} \\
> &= -\log_2 p,
> \end{aligned}$$
>
> which is the [surprisal](#def-surprisal) of any one of them, in [bits](#def-bit).
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
> **Theorem 1 (Surprisal as a logarithm to base one half)** For a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) $x$ of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ with $\mathbb{P}(X=x) > 0$, the [surprisal](#def-surprisal) in [bits](#def-bit) is
>
> $$s(x) = \log_{1/2} \mathbb{P}(X=x).$$

> **NOTE:**
>
> *Proof*. Write $p = \mathbb{P}(X=x)$. The [change of base formula](https://morrison-lab.github.io/mds/algebra-exponentials.html#rem-logarithm-formula) gives
>
> $$\log_b y = \frac{{\operatorname{log}\mathopen{}\left\{y\right\}\mathclose{}}}{{\operatorname{log}\mathopen{}\left\{b\right\}\mathclose{}}}$$
>
> for $y > 0$ and $b > 0$ with $b \ne 1$. With $b = 1/2$ and $y = p$,
>
> $$\begin{aligned}
> \log_{1/2} p
> &= \frac{{\operatorname{log}\mathopen{}\left\{p\right\}\mathclose{}}}{{\operatorname{log}\mathopen{}\left\{1/2\right\}\mathclose{}}} \\
> &= \frac{{\operatorname{log}\mathopen{}\left\{p\right\}\mathclose{}}}{-{\operatorname{log}\mathopen{}\left\{2\right\}\mathclose{}}} \\
> &= -\frac{{\operatorname{log}\mathopen{}\left\{p\right\}\mathclose{}}}{{\operatorname{log}\mathopen{}\left\{2\right\}\mathclose{}}} \\
> &= -\log_2 p \\
> &= s(x).
> \end{aligned}$$
>
> The step from the third to the fourth line is the change of base formula with $b = 2$.

> **NOTE:**
>
> **Example 2 (Halvings of certainty for a loaded coin)**  
>
> A coin lands heads with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.2$. The chunk computes the [surprisal](#def-surprisal) of heads in two ways: as $-\log_2 0.2$, and as $\log_{1/2} 0.2$.
>
> Show code
>
> ``` r
> p_heads <- 0.2
> from_base_two <- -log(x = p_heads, base = 2)
> from_base_half <- log(x = p_heads, base = 0.5)
> c(from_base_two, from_base_half)
> #> [1] 2.321928 2.321928
> ```
>
> Both give $2.322$ [bits](#def-bit) ([Theorem 1](#thm-surprisal-log-half)). Halving $1$ that many times gives $0.5^{2.322} = 0.2$, the probability of heads.

> **NOTE:**
>
> *Remark 1* (Surprisal as halvings of certainty). Start from certainty, [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1$. Each halving multiplies the probability by $1/2$. After $s$ halvings the probability is $(1/2)^s$, and solving $(1/2)^s = p$ for $s$ gives $s = \log_{1/2} p$. This count is only motivation. [Theorem 1](#thm-surprisal-log-half) proves that this $s$ is the [surprisal](#def-surprisal) in [bits](#def-bit). So the surprisal of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) is the number of times certainty must be halved to reach the probability of that value. When $p$ is not $(1/2)^k$ for a whole number $k$, the number of halvings is not a whole number.

> **NOTE:**
>
> **Definition 3 (Nat)** A **nat** is the unit of information when the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) in [surprisal](#def-surprisal), and in every quantity built from it, is the [natural logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-natural-log).
>
> One nat is the surprisal of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/\text{e}$: for a value $x$ of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$,
>
> $$\begin{aligned}
> s(x) = 1 \text{ nat}
> &\iff -\ln \mathbb{P}(X=x) = 1\\
> &\iff \mathbb{P}(X=x) = \text{e}^{-1} = 1/\text{e}\approx 0.368.
> \end{aligned}$$

> **NOTE:**
>
> **Example 3 (One fair coin toss in nats)** By [Example 1](#exm-surprisal-coins) with $k = 1$, one toss of a fair coin landing heads has a [surprisal](#def-surprisal) of $1$ [bit](#def-bit). In [nats](#def-nat), the same [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) has a surprisal of
>
> $$\begin{aligned}
> s(\text{heads})
> &= -\ln \tfrac{1}{2} \\
> &= \ln 2 \\
> &\approx 0.693 \text{ nats}.
> \end{aligned}$$

> **NOTE:**
>
> *Remark 2* (Converting between bits and nats). For any [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $p \in (0, 1]$, the change-of-base rule for [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) gives
>
> $$\begin{aligned}
> -\log_2 p
> &= \frac{-\ln p}{\ln 2}\\
> &\approx 1.443 \times (-\ln p).
> \end{aligned}$$
>
> So a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) with a [surprisal](#def-surprisal) of $1$ [nat](#def-nat) has a surprisal of $1 / \ln 2 \approx 1.443$ [bits](#def-bit), and the $\ln 2 \approx 0.693$ [nats](#def-nat) of [Example 3](#exm-coin-nats) are exactly $\ln 2 / \ln 2 = 1$ [bit](#def-bit).
>
> A bit as a unit of information is not the same thing as a bit as a binary digit. The name [shannon](#def-bit) refers only to the unit of information, so it avoids this ambiguity. A binary digit whose two values are equally likely has a surprisal of exactly $1$ bit, whichever value it takes. A binary digit that is $0$ nine times in ten does not: the value $0$ has a surprisal of $-\log_2 0.9 \approx 0.152$ bits, and the value $1$ has a surprisal of $-\log_2 0.1 \approx 3.322$ bits.

> **NOTE:**
>
> *Remark 3* (Unlikely outcomes carry more information). The [surprisal](#def-surprisal) of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) is large when the value was unlikely, and it falls to $0$ as the value becomes certain. Correctly guessing heads on one toss of a fair coin is worth $1$ [bit](#def-bit); correctly guessing ten heads in a row is worth $10$ [bits](#def-bit).

> **NOTE:**
>
> *Remark 4* (Entropy is expected surprisal). The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [surprisal](#def-surprisal):
>
> $$\begin{aligned}
> H(X)
> &= {\mathbb{E}\mathopen{}\left[-\log \mathbb{P}(X)\right]\mathclose{}} \\
> &= {\mathbb{E}\mathopen{}\left[s(X)\right]\mathclose{}}.
> \end{aligned}$$
>
> So $H(X)$ is the average number of [bits](entropy.llms.md#def-bit) (with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm)) needed to record a value of $X$ when each value $x$ costs $s(x)$ bits. The [source coding theorem](source-coding.llms.md#thm-source-coding), on a later page of these notes, makes that average precise: no [uniquely decodable code](source-coding.llms.md#def-uniquely-decodable) does better.

> **NOTE:**
>
> **Definition 4 (Rarity)** The **rarity** of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) $x$ of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the reciprocal of its [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) mass:
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
> **Example 4 (Rarity of the outcomes of a die)**  
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
> *Remark 5* (Source of the name). Leinster writes that, for a community whose $i$th species has relative abundance $p_i$, “$1/p_i$ is a measure of its rarity or specialness” ([Leinster 2021, sec. 2.4](#ref-leinster2021entropy), p. 52). The name “rarity” for the reciprocal of a [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) is borrowed from there.

> **NOTE:**
>
> **Theorem 2 (Surprisal is the logarithm of the rarity)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), and let $x$ be a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) of $X$ with $\mathbb{P}(X=x) > 0$. Then the [surprisal](#def-surprisal) of $x$ is the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of its [rarity](#def-rarity):
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
> **Theorem 3 (Surprisal of a continuous value is the logarithm of the rarity)** Let $X$ be a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) with [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) $\mathbb{p}$, and let $x$ be a value with $\mathbb{p}(x) > 0$. Then the [surprisal](#def-surprisal) of $x$ is the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of its [rarity](#def-rarity):
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
> **Corollary 1 (Surprisal of a discrete value is nonnegative)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), and let $x$ be a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) of $X$ with $\mathbb{P}(X=x) > 0$. Then the [rarity](#def-rarity) of $x$ is at least $1$, with equality exactly when $\mathbb{P}(X=x) = 1$, and the [surprisal](#def-surprisal) satisfies
>
> $${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} \ge 0.$$

> **NOTE:**
>
> *Proof*. Since $0 < \mathbb{P}(X=x) \le 1$, the [rarity](#def-rarity) ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} = 1 / \mathbb{P}(X=x)$ is at least $1$, with equality exactly when $\mathbb{P}(X=x) = 1$. The [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) is increasing, and ${\operatorname{log}\mathopen{}\left\{1\right\}\mathclose{}} = 0$, so by [Theorem 2](#thm-surprisal-log-rarity), ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} = {\operatorname{log}\mathopen{}\left\{{\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}\right\}\mathclose{}} \ge 0$.

> **NOTE:**
>
> **Example 5 (Surprisal and rarity of a value with probability one quarter)** Take a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/4$:
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
> It has [rarity](#def-rarity) $4$ by definition. By [Theorem 2](#thm-surprisal-log-rarity), its [surprisal](#def-surprisal) is the base-2 [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of that rarity, $2$ [bits](#def-bit).

> **NOTE:**
>
> *Remark 6* (Reading the rarity of a value). A [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) can exceed $1$, so for a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) the [rarity](#def-rarity) can be below $1$, and then the [surprisal](#def-surprisal) is negative ([Theorem 3](#thm-surprisal-log-rarity-continuous)). For a mass, a rarity of $r$ reads “one in $r$”, and the surprisal is the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of $r$ ([Theorem 2](#thm-surprisal-log-rarity)).

> **NOTE:**
>
> *Remark 7* (Values of the probability, the rarity and the surprisal). For a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), the mass $\mathbb{P}(X=x)$ of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) with a mass above $0$, its [rarity](#def-rarity) ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}$ and its [surprisal](#def-surprisal) ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ take the values in the middle column. For a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv), the [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) $\mathbb{p}(x)$ takes the place of the mass. At a value $x$ with a density above $0$, the rarity ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}$ is the reciprocal of $\mathbb{p}(x)$, and the surprisal ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ is the [surprisal of a continuous value](https://morrison-lab.github.io/pds/expectation.html#def-surprisal-continuous). Their values are in the right column.
>
> |  | Mass $\mathbb{P}(X=x)$ | Density $\mathbb{p}(x)$ |
> |----|----|----|
> | Mass or density | $(0, 1]$ | $(0, \infty)$ |
> | Rarity ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}$ | $[1, \infty)$ | $(0, \infty)$ |
> | Surprisal ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ | $[0, \infty)$ | $(-\infty, \infty)$ |
>
> - **Mass.** A mass of $1$ gives the smallest rarity, $1$, and the smallest surprisal, $0$. No mass exceeds $1$, the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) of a value that is certain. So no mass gives a rarity below $1$ or a surprisal below $0$.
> - **Density.** A density can be arbitrarily large, as in the [uniform example](https://morrison-lab.github.io/pds/expectation.html#exm-entropy-uniform), so the rarity can fall below $1$ and the surprisal can fall below $0$.
> - **Zero.** A mass or density of $0$ gives a rarity and a surprisal of $\infty$.
> - **Units.** A mass has no units. A density has the units of $1/x$, so its rarity has the units of $x$. Rescaling $x$ by a nonzero $c$ shifts its surprisal by ${\operatorname{log}\mathopen{}\left\{\mathopen{}\left|c\right|\mathclose{}\right\}\mathclose{}}$.

> **NOTE:**
>
> *Remark 8* (Rarity and odds). Let $x$ be a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$, and let $A$ be the [event](https://morrison-lab.github.io/pds/probability-basics.html#def-event) $X = x$ with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $p = \mathbb{P}(X=x)$. The [odds](https://morrison-lab.github.io/pds/probability-basics.html#def-odds) in favour of $A$ are $p / (1 - p)$, and the odds against $A$ are $(1 - p) / p$ ([Grinstead and Snell 1997](#ref-grinstead1997introduction), Definition 1.4). The [rarity](#def-rarity) of $x$ is ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} = 1/p$, so the odds against $A$ are ${\mathbb{r}\mathopen{}\left(x\right)\mathclose{}} - 1$.
>
> Show code
>
> ``` r
> p_value <- c(1 / 4, 1 / 100, 1)
> rarity_value <- 1 / p_value
> odds_against <- (1 - p_value) / p_value
> rarity_value - odds_against
> #> [1] 1 1 1
> rarity_value
> #> [1]   4 100   1
> odds_against
> #> [1]  3 99  0
> ```
>
> The first printed line shows that, for each $p$, the rarity of the value exceeds the odds against its event by exactly $1$. A value with probability $1/4$ has rarity $4$, and its event has odds of $3$ to $1$ against. The two differ by exactly $1$, so they are relatively close when the rarity is large. At $p = 1$ the rarity is $1$ and the odds against are $0$, but the odds in favour divide by zero.
>
> The odds compare an event with its [complement](https://morrison-lab.github.io/pds/probability-basics.html#def-complement), and the odds against take values in $[0, \infty)$ when $p$ is above $0$. At $p = 0$, the odds against and the rarity divide by zero, and both tend to $\infty$ as $p$ decreases to $0$. For a value of a discrete random variable with $p$ above $0$, the rarity takes values in $[1, \infty)$. For a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv), the event $X = x$ for a single value has probability $0$, so its odds against and $1/\mathbb{P}(X=x)$ are not defined, but the rarity of the value is defined from the [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf). An event such as $X \le c$ can have a probability above $0$, so it can have odds.

> **NOTE:**
>
> **Definition 5 (Perplexity)** The **perplexity** of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the [exponential](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-exponential-function) of its [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy), with the same base as the [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) in the entropy:
>
> $${\mathrm{PP}\mathopen{}\left(X\right)\mathclose{}} \stackrel{\text{def}}{=}b^{{\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}}.$$
>
> With base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm), ${\mathrm{PP}\mathopen{}\left(X\right)\mathclose{}} = 2^{{\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}}$ with ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ in [bits](#def-bit). With [natural logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-natural-log), ${\mathrm{PP}\mathopen{}\left(X\right)\mathclose{}} = \text{e}^{{\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}}$ with ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ in [nats](#def-nat). The two give the same value.

> **NOTE:**
>
> **Theorem 4 (Perplexity is the probability-weighted geometric mean of the rarities)** For a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$, the [perplexity](#def-perplexity) is a weighted geometric mean of the [rarities](#def-rarity), each raised to its [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability). Take $x$ over the values with $\mathbb{P}(X=x) > 0$. Then
>
> $${\mathrm{PP}\mathopen{}\left(X\right)\mathclose{}} = \prod_x {\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}^{\mathbb{P}(X=x)}.$$

> **NOTE:**
>
> *Proof*. $$\begin{aligned}
> {\mathrm{PP}\mathopen{}\left(X\right)\mathclose{}}
> &= b^{{\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}}
> && \text{(definition of perplexity)} \\
> &= b^{{\mathbb{E}\mathopen{}\left[{\mathbb{s}\mathopen{}\left(X\right)\mathclose{}}\right]\mathclose{}}}
> && \text{(entropy is expected surprisal)} \\
> &= b^{\sum_x \mathbb{P}(X=x) \log_b {\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}}
> && \text{(surprisal is the logarithm of the rarity)} \\
> &= \prod_x b^{\mathbb{P}(X=x) \log_b {\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}}
> && \text{(a sum in the exponent is a product)} \\
> &= \prod_x {\mathbb{r}\mathopen{}\left(x\right)\mathclose{}}^{\mathbb{P}(X=x)}
> && \text{(} b^{\log_b y} = y \text{)}
> \end{aligned}$$

> **NOTE:**
>
> **Example 6 (Perplexity of a uniform distribution)**  
>
> If $X$ is uniform on $k$ [values](https://morrison-lab.github.io/pds/random-variables.html#def-realization), then every value has [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/k$ and [rarity](#def-rarity) $k$, so by [Theorem 4](#thm-perplexity-geometric-mean) the [perplexity](#def-perplexity) of $X$ is $k$. In general, the perplexity is the count of equally likely values that would give the same [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) as $X$.

> **NOTE:**
>
> **Example 7 (Perplexity of a loaded die)**  
>
> Let $X$ be the roll of the loaded die from [Example 4](#exm-rarity-die), where a six has [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/2$ and each other face has probability $1/10$. The code computes the [perplexity](#def-perplexity) from the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) in [bits](#def-bit), and then from the [rarities](#def-rarity) by [Theorem 4](#thm-perplexity-geometric-mean).
>
> Show code
>
> ``` r
> p_other_faces <- rep(1 / 10, 5)
> p <- c(1 / 2, p_other_faces)
> surprisal <- -log2(p)
> entropy <- sum(p * surprisal)
> perplexity_from_entropy <- 2^entropy
> rarity <- 1 / p
> perplexity_from_rarities <- prod(rarity^p)
> c(perplexity_from_entropy, perplexity_from_rarities)
> #> [1] 4.472136 4.472136
> ```
>
> Both routes give a perplexity of about $4.47$. The loaded die has the same entropy as a fair die with about that many faces, fewer than the $6$ faces it has.

> **NOTE:**
>
> *Remark 9* (Source of the name). The name comes from speech recognition ([Jelinek et al. 1977](#ref-jelinek1977perplexity)). Leinster defines the “diversity of order 1” as the [exponential](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-exponential-function) of the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) ([Leinster 2021](#ref-leinster2021entropy), Definition 2.4.1). He calls a diversity index an “effective number” when it is $k$ for $k$ species with the same abundance ([Leinster 2021](#ref-leinster2021entropy), Definition 2.4.5).

> **NOTE:**
>
> *Remark 10* (Differential entropy differs from entropy). A [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) value is not a [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability), so the [surprisal of a continuous value](https://morrison-lab.github.io/pds/expectation.html#def-surprisal-continuous) and the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) (the [differential entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy)) behave differently from their counterparts for a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv):
>
> - **Sign.** A density can exceed $1$, so the [surprisal](#def-surprisal) ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ and the differential entropy can fall below $0$, as in the [uniform example](https://morrison-lab.github.io/pds/expectation.html#exm-entropy-uniform) ([Cover and Thomas 2006, sec. 8.1](#ref-cover2006elements)). The entropy of a discrete random variable is never negative.
> - **Units.** Rescaling changes the differential entropy: ${\mathbb{H}\mathopen{}\left(aX\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + \log |a|$ for a constant $a \ne 0$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.4). Measuring the same quantity in metres rather than centimetres therefore changes it. Adding a constant does not: ${\mathbb{H}\mathopen{}\left(X + c\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.3).
> - **Not what the entropy approaches.** Round $X$ down to a multiple of $\Delta$, which gives a discrete random variable $X^\Delta$. Then ${\mathbb{H}\mathopen{}\left(X^\Delta\right)\mathclose{}} + \log \Delta \to {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ as $\Delta \to 0$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.3.1). The entropy ${\mathbb{H}\mathopen{}\left(X^\Delta\right)\mathclose{}}$ itself grows indefinitely as $\Delta \to 0$, so the differential entropy is not what it approaches.

> **NOTE:**
>
> **Definition 6 (Collision probability)** The **collision probability** of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the chance that $X$ and a second variable $X'$ take the same value, where $X$ and $X'$ are [IID](https://morrison-lab.github.io/pds/independence.html#def-iid):
>
> $$\mathbb{P}(X = X').$$

> **NOTE:**
>
> **Definition 7 (Rényi entropy of order 2 (collision entropy))** The **Rényi entropy of order 2**, also called the **collision entropy** ([Wikipedia contributors 2026](#ref-wikipedia_renyi_entropy)), of a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ is the negative [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) of the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability), where ${\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}$ is the [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) evaluated at the [random variable](https://morrison-lab.github.io/pds/random-variables.html#def-random-variable) $X$ itself:
>
> $${\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}} = -\log {\mathbb{E}\mathopen{}\left[{\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}\right]\mathclose{}}.$$
>
> Rényi introduced this case of a family of [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) ([Rényi 1961](#ref-renyi1961measures)).

> **NOTE:**
>
> **Theorem 5 (The expected probability is the collision probability)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), and let $X'$ be a variable such that $X$ and $X'$ are [IID](https://morrison-lab.github.io/pds/independence.html#def-iid). Then
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
> The variables $X$ and $X'$ take the same value exactly when both equal some value $x$. Because $X$ and $X'$ are [IID](https://morrison-lab.github.io/pds/independence.html#def-iid), the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) that both equal $x$ is $\mathbb{P}(X=x) \, \mathbb{P}(X'=x) = \mathbb{P}(X=x)^2$. Adding over the values $x$ gives
>
> $$\begin{aligned}
> \mathbb{P}(X = X')
> &= \sum_x \mathbb{P}(X=x, X'=x) \\
> &= \sum_x \mathbb{P}(X=x)^2.
> \end{aligned}$$
>
> The expectation ${\mathbb{E}\mathopen{}\left[\mathbb{P}(X)\right]\mathclose{}}$ and the [collision probability](#def-collision-probability) $\mathbb{P}(X = X')$ both equal $\sum_x \mathbb{P}(X=x)^2$, so they are equal.

> **NOTE:**
>
> **Theorem 6 (The collision entropy is at most the Shannon entropy)** Let $X$ be a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with values $x_1, \ldots, x_n$. Then the [collision entropy](#def-renyi-entropy) is at most the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy):
>
> $${\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}.$$
>
> The two coincide exactly when each value that $X$ takes with positive [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) has the same probability.

> **NOTE:**
>
> *Proof*. Write ${\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}$ for the [probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) evaluated at $X$. The function $-\log$ is [strictly convex](https://morrison-lab.github.io/mds/algebra-sums.html#def-convex-function), so [Jensen’s inequality](https://morrison-lab.github.io/mds/algebra-sums.html#thm-jensen) gives
>
> $${\mathbb{E}\mathopen{}\left[-\log {\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}\right]\mathclose{}} \ge -\log {\mathbb{E}\mathopen{}\left[{\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}\right]\mathclose{}},$$
>
> with equality exactly when ${\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}$ is constant. The left side is ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$. The right side is ${\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}}$ by its definition. The function ${\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}$ is constant exactly when every value that $X$ takes with positive [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) has that same probability.

> **NOTE:**
>
> **Example 8 (Collision entropy and entropy of a three-valued random variable)**  
>
> Let $X$ take three values with [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1/2$, $1/4$ and $1/4$. The code below computes the expected [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability), the [collision entropy](#def-renyi-entropy) and the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy), with base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm).
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
> By [Theorem 5](#thm-expected-probability-collision), the expected probability ${\mathbb{E}\mathopen{}\left[{\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}\right]\mathclose{}} = 0.375$ is the [collision probability](#def-collision-probability). The collision entropy is ${\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}} = 1.415$ [bits](#def-bit). The entropy is ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} = 1.5$ bits. As [Theorem 6](#thm-collision-entropy-at-most-entropy) states, ${\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$, and the two differ because the three values are not equally likely.

> **NOTE:**
>
> *Remark 11* (Two ways to summarize a random variable by its probabilities). [Entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of the [surprisal](#def-surprisal) $-\log {\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}$. Taking the expectation of the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) ${\mathbb{P}\mathopen{}\left(X\right)\mathclose{}}$ itself summarizes $X$ differently. For a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv), [Theorem 5](#thm-expected-probability-collision) identifies that expectation with the [collision probability](#def-collision-probability), so the [collision entropy](#def-renyi-entropy) is ${\mathbb{H}_{2}\mathopen{}\left(X\right)\mathclose{}} = -\log {\mathbb{P}\mathopen{}\left(X = X'\right)\mathclose{}}$.
>
> For a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) with [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) $\mathbb{p}$, the analogue is ${\mathbb{E}\mathopen{}\left[\mathbb{p}(X)\right]\mathclose{}} = \int \mathbb{p}(x)^2\,dx$. The [expected-density exercises](https://morrison-lab.github.io/pds/expectation.html#exr-expected-density) derive this quantity, then compute it in the [uniform case](https://morrison-lab.github.io/pds/expectation.html#exr-expected-density-uniform) and the [normal case](https://morrison-lab.github.io/pds/expectation.html#exr-expected-density-normal).
>
> [Theorem 6](#thm-collision-entropy-at-most-entropy) compares the collision entropy with the [Shannon entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy).

> **NOTE:**
>
> *Remark 12* (Surprisal and the Fisher information). When the [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) depend on a parameter $\theta$, the [surprisal](#def-surprisal) of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) $x$ is $-\log \mathbb{p}(x \mid \theta)$, which is minus the log-likelihood:
>
> $$\mathbb{s}_{\theta}(x) = -\log \mathbb{p}(x \mid \theta) = -\ell(\theta).$$
>
> Its [derivative with respect to](https://morrison-lab.github.io/mds/calculus-derivatives.html#def-derivative) $\theta$ is minus the [score](https://morrison-lab.github.io/sds/intro-MLEs.html#def-score):
>
> $$\frac{\partial}{\partial \theta} \mathbb{s}_{\theta}(x) = -{\ell'\mathopen{}\left(\theta\right)\mathclose{}}.$$
>
> The expected squared score is the [expected information](https://morrison-lab.github.io/sds/intro-MLEs.html#def-einf), also called the Fisher information. It is also the expected [second derivative](https://morrison-lab.github.io/mds/calculus-derivatives.html#def-second-derivative) of the surprisal, when $X$ is drawn from the model at the true parameter value $\theta_0$, and the score is evaluated at that same $X$:
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
> **Definition 8 (Joint entropy)** Let $X$ and $Y$ be [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf) $p(x, y) \stackrel{\text{def}}{=}\mathbb{P}(X=x, Y=y)$. Their **joint entropy** is the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of the pair $(X, Y)$:
>
> $$H(X, Y) \stackrel{\text{def}}{=}{\mathbb{E}\mathopen{}\left[-\log p(X, Y)\right]\mathclose{}}.$$

> **NOTE:**
>
> **Definition 9 (Entropy given one value)** For $X$ and $Y$ as in [Definition 8](#def-joint-entropy), write $p(y \mid x) \stackrel{\text{def}}{=}\mathbb{P}(Y=y \mid X=x)$. The **entropy of** $Y$ given $X=x$, for a value $x$ with $\mathbb{P}(X=x) > 0$, is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of $-\log p(Y \mid x)$ given $X=x$:
>
> $$H(Y \mid X=x) \stackrel{\text{def}}{=}{{\mathbb{E}\mathopen{}\left[-\log p(Y \mid x) \mid X=x\right]\mathclose{}}}.$$

> **NOTE:**
>
> **Definition 10 (Conditional entropy)** For $X$ and $Y$ as in [Definition 8](#def-joint-entropy) and $p(y \mid x)$ as in [Definition 9](#def-entropy-given-value), the **conditional entropy** of $Y$ given $X$ is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of $-\log p(Y \mid X)$:
>
> $$H(Y \mid X) \stackrel{\text{def}}{=}{\mathbb{E}\mathopen{}\left[-\log p(Y \mid X)\right]\mathclose{}}.$$

> **NOTE:**
>
> **Theorem 7 (Conditional entropy as an average of entropies given a value)** For $X$ and $Y$ as in [Definition 8](#def-joint-entropy),
>
> $$H(Y \mid X) = \sum_{x} p(x) \, H(Y \mid X=x),$$
>
> where $p(x) \stackrel{\text{def}}{=}\mathbb{P}(X=x)$, and the sum runs over the values $x$ with $p(x) > 0$.

> **NOTE:**
>
> *Proof*. The [law of iterated expectations](https://morrison-lab.github.io/pds/expectation.html#thm-lie) conditions on $X$:
>
> $$\begin{aligned}
> H(Y \mid X)
> &= {\mathbb{E}\mathopen{}\left[-\log p(Y \mid X)\right]\mathclose{}} \\
> &= {\mathbb{E}\mathopen{}\left[{{\mathbb{E}\mathopen{}\left[-\log p(Y \mid X) \mid X\right]\mathclose{}}}\right]\mathclose{}} \\
> &= \sum_{x} p(x) \, {{\mathbb{E}\mathopen{}\left[-\log p(Y \mid x) \mid X=x\right]\mathclose{}}} \\
> &= \sum_{x} p(x) \, H(Y \mid X=x).
> \end{aligned}$$
>
> The third line is the [definition of expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) over the values $x$ of $X$, and the last line is [Definition 9](#def-entropy-given-value).

> **NOTE:**
>
> **Theorem 8 (Chain rule for entropy)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$,
>
> $$H(X, Y) = H(X) + H(Y \mid X).$$

> **NOTE:**
>
> *Proof*. Use the notation of [Definition 8](#def-joint-entropy) and [Definition 9](#def-entropy-given-value). With [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1$, $p(X, Y) = p(X) \, p(Y \mid X)$ and $p(X, Y) > 0$, so
>
> $$-\log p(X, Y) = -\log p(X) - \log p(Y \mid X).$$
>
> Both terms on the right are nonnegative, so the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of the sum is the sum of the expectation of each term:
>
> $$\begin{aligned}
> H(X, Y)
> &= {\mathbb{E}\mathopen{}\left[-\log p(X, Y)\right]\mathclose{}} \\
> &= {\mathbb{E}\mathopen{}\left[-\log p(X)\right]\mathclose{}} + {\mathbb{E}\mathopen{}\left[-\log p(Y \mid X)\right]\mathclose{}} \\
> &= H(X) + H(Y \mid X).
> \end{aligned}$$

> **NOTE:**
>
> **Corollary 2 (Chain rule for entropy, other order)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$,
>
> $${\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. The pair $(Y, X)$ takes each value $(y, x)$ with the same [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) that $(X, Y)$ takes $(x, y)$, so
>
> $${\mathbb{H}\mathopen{}\left(Y, X\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}}.$$
>
> The [chain rule](#thm-entropy-chain-rule), applied with the roles of $X$ and $Y$ exchanged, gives
>
> $${\mathbb{H}\mathopen{}\left(Y, X\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}.$$
>
> Combining the two displays gives the claim.

> **NOTE:**
>
> **Corollary 3 (Conditional entropy as a difference)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Subtract ${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}$ from both sides of [Corollary 2](#cor-entropy-chain-rule-reversed):
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} \\
> &= {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Example 9 (Chain rule for entropy with a noisy copy)**  
>
> Let $X$ be a fair coin toss, coded $0$ or $1$. Let $Y$ be a noisy copy of $X$: it equals $X$ with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.8$ and the other value with probability $0.2$. The [joint distribution](https://morrison-lab.github.io/pds/random-variables.html#def-joint-distribution) gives probability $0.4$ to $(0, 0)$ and $(1, 1)$, and $0.1$ to $(0, 1)$ and $(1, 0)$. The chunk computes each [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) from its definition, in [bits](#def-bit).
>
> Show code
>
> ``` r
> entropy <- function(p) -sum(p * log2(p))
> joint <- matrix(
>   data = c(0.4, 0.1, 0.1, 0.4),
>   nrow = 2,
>   dimnames = list(x = 0:1, y = 0:1)
> )
> p_y <- colSums(joint)
> cond_x_given_y <- sweep(x = joint, MARGIN = 2, STATS = p_y, FUN = "/")
> h_x_given_y_values <- apply(X = cond_x_given_y, MARGIN = 2, FUN = entropy)
> h_x_given_y <- sum(p_y * h_x_given_y_values)
> h_xy <- entropy(joint)
> h_y <- entropy(p_y)
> c(h_xy = h_xy, h_x_given_y = h_x_given_y, h_y = h_y)
> #>        h_xy h_x_given_y         h_y 
> #>   1.7219281   0.7219281   1.0000000
> ```
>
> The chunk computes ${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}$ as the average of the [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) given each value of $Y$, as in [Theorem 7](#thm-conditional-entropy-average) with $X$ and $Y$ exchanged. Here ${\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} = 1.722$ bits, ${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} = 0.722$ bits and ${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} = 1$ bits. So ${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} = 1.722$ bits agrees with ${\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}}$ ([Corollary 2](#cor-entropy-chain-rule-reversed)), and ${\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} = 0.722$ bits agrees with ${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}$ ([Corollary 3](#cor-conditional-entropy-difference)).

> **NOTE:**
>
> **Definition 11 (Joint surprisal)** Let $X$ and $Y$ be [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf) $p(x, y) \stackrel{\text{def}}{=}\mathbb{P}(X=x, Y=y)$. The **joint surprisal** of a pair of [values](https://morrison-lab.github.io/pds/random-variables.html#def-realization) $(x, y)$ with $p(x, y) > 0$ is the [surprisal](#def-surprisal) of that pair:
>
> $${\mathbb{s}\mathopen{}\left(x, y\right)\mathclose{}} \stackrel{\text{def}}{=}-\log p(x, y).$$

> **NOTE:**
>
> **Definition 12 (Conditional surprisal)** For $X$ and $Y$ as in [Definition 11](#def-joint-surprisal), the **conditional surprisal** of a [value](https://morrison-lab.github.io/pds/random-variables.html#def-realization) $y$ given a value $x$ with $\mathbb{P}(X=x) > 0$ and $\mathbb{P}(Y=y \mid X=x) > 0$ is
>
> $${\mathbb{s}\mathopen{}\left(y \mid x\right)\mathclose{}} \stackrel{\text{def}}{=}-\log \mathbb{P}(Y=y \mid X=x).$$

> **NOTE:**
>
> **Example 10 (Joint and conditional surprisal of a noisy copy)**  
>
> Let $X$ be a fair coin toss, coded $0$ or $1$. Let $Y$ be a noisy copy of $X$: it equals $X$ with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.8$ and the other value with probability $0.2$. Take the pair of values $x = 0$ and $y = 1$. The joint [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) is $\mathbb{P}(X=0, Y=1) = 0.1$, the probability of $X=0$ is $0.5$, and the [conditional probability](https://morrison-lab.github.io/pds/probability-basics.html#def-conditional-prob) is $\mathbb{P}(Y=1 \mid X=0) = 0.2$. The chunk computes the three [surprisals](#def-surprisal), in [bits](#def-bit).
>
> Show code
>
> ``` r
> s_xy <- -log2(0.1)
> s_x <- -log2(0.5)
> s_y_given_x <- -log2(0.2)
> c(s_xy = s_xy, s_x = s_x, s_y_given_x = s_y_given_x)
> #>        s_xy         s_x s_y_given_x 
> #>    3.321928    1.000000    2.321928
> ```
>
> The [joint surprisal](#def-joint-surprisal) is ${\mathbb{s}\mathopen{}\left(0, 1\right)\mathclose{}} = 3.322$ bits, the [surprisal](#def-surprisal) of $x = 0$ alone is ${\mathbb{s}\mathopen{}\left(0\right)\mathclose{}} = 1$ [bit](#def-bit), and the [conditional surprisal](#def-conditional-surprisal) is ${\mathbb{s}\mathopen{}\left(1 \mid 0\right)\mathclose{}} = 2.322$ bits.

> **NOTE:**
>
> **Theorem 9 (Chain rule for surprisal)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ and [values](https://morrison-lab.github.io/pds/random-variables.html#def-realization) $x$ and $y$ with $\mathbb{P}(X=x, Y=y) > 0$,
>
> $${\mathbb{s}\mathopen{}\left(x, y\right)\mathclose{}} = {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} + {\mathbb{s}\mathopen{}\left(y \mid x\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Since $\mathbb{P}(X=x, Y=y) = \mathbb{P}(X=x) \, \mathbb{P}(Y=y \mid X=x)$,
>
> $$\begin{aligned}
> {\mathbb{s}\mathopen{}\left(x, y\right)\mathclose{}}
> &= -\log \mathbb{P}(X=x, Y=y) \\
> &= -\log \mathopen{}\left[\mathbb{P}(X=x) \, \mathbb{P}(Y=y \mid X=x)\right]\mathclose{} \\
> &= -\log \mathbb{P}(X=x) - \log \mathbb{P}(Y=y \mid X=x) \\
> &= {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} + {\mathbb{s}\mathopen{}\left(y \mid x\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Corollary 4 (Conditional surprisal as a difference)** For $X$, $Y$, $x$ and $y$ as in [Theorem 9](#thm-surprisal-chain-rule),
>
> $${\mathbb{s}\mathopen{}\left(y \mid x\right)\mathclose{}} = {\mathbb{s}\mathopen{}\left(x, y\right)\mathclose{}} - {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Subtract ${\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}$ from both sides of [Theorem 9](#thm-surprisal-chain-rule):
>
> $$\begin{aligned}
> {\mathbb{s}\mathopen{}\left(x, y\right)\mathclose{}} - {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}}
> &= {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} + {\mathbb{s}\mathopen{}\left(y \mid x\right)\mathclose{}} - {\mathbb{s}\mathopen{}\left(x\right)\mathclose{}} \\
> &= {\mathbb{s}\mathopen{}\left(y \mid x\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Example 11 (Chain rule for surprisal with a noisy copy)**  
>
> For the pair of values in [Example 10](#exm-joint-conditional-surprisal), the chunk recomputes the three [surprisals](#def-surprisal) in [bits](#def-bit).
>
> Show code
>
> ``` r
> s_xy <- -log2(0.1)
> s_x <- -log2(0.5)
> s_y_given_x <- -log2(0.2)
> c(sum = s_x + s_y_given_x, joint = s_xy)
> #>      sum    joint 
> #> 3.321928 3.321928
> ```
>
> The [surprisal](#def-surprisal) of $x = 0$ plus the [conditional surprisal](#def-conditional-surprisal) of $y = 1$ given $x = 0$ is $3.322$ [bits](#def-bit). This sum is the [joint surprisal](#def-joint-surprisal) ${\mathbb{s}\mathopen{}\left(0, 1\right)\mathclose{}} = 3.322$ bits ([Theorem 9](#thm-surprisal-chain-rule)). Subtracting ${\mathbb{s}\mathopen{}\left(0\right)\mathclose{}} = 1$ [bit](#def-bit) from the joint surprisal recovers ${\mathbb{s}\mathopen{}\left(1 \mid 0\right)\mathclose{}} = 2.322$ bits ([Corollary 4](#cor-conditional-surprisal-difference)).

> **NOTE:**
>
> **Lemma 1 (Chain rule for surprisal with the conditioning reversed)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ and [outcomes](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) $x$ and $y$ with $\mathbb{P}(X=x, Y=y) > 0$,
>
> $${\mathbb{s}\mathopen{}\left(x, y\right)\mathclose{}} = {\mathbb{s}\mathopen{}\left(x \mid y\right)\mathclose{}} + {\mathbb{s}\mathopen{}\left(y\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Applying [Theorem 9](#thm-surprisal-chain-rule) with the roles of $X$ and $Y$ swapped gives
>
> $${\mathbb{s}\mathopen{}\left(y, x\right)\mathclose{}} = {\mathbb{s}\mathopen{}\left(y\right)\mathclose{}} + {\mathbb{s}\mathopen{}\left(x \mid y\right)\mathclose{}}.$$
>
> Both $\mathbb{P}(Y=y, X=x)$ and $\mathbb{P}(X=x, Y=y)$ are the [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) of the same pair of values, so ${\mathbb{s}\mathopen{}\left(y, x\right)\mathclose{}} = {\mathbb{s}\mathopen{}\left(x, y\right)\mathclose{}}$. Substituting this into the display above, and swapping the two summands, gives the claim.

> **NOTE:**
>
> **Example 12 (Chain rule for surprisal with the conditioning reversed, for a noisy copy)**  
>
> For the pair of values in [Example 10](#exm-joint-conditional-surprisal), $\mathbb{P}(X=0, Y=1) = 0.1$, $\mathbb{P}(Y=1) = 0.5$ and $\mathbb{P}(X=0 \mid Y=1) = 0.2$. The chunk computes the three [surprisals](#def-surprisal) in [bits](#def-bit).
>
> Show code
>
> ``` r
> s_xy <- -log2(0.1)
> s_y <- -log2(0.5)
> s_x_given_y <- -log2(0.2)
> c(sum = s_x_given_y + s_y, joint = s_xy)
> #>      sum    joint 
> #> 3.321928 3.321928
> ```
>
> The [conditional surprisal](#def-conditional-surprisal) of $x = 0$ given $y = 1$ plus the [surprisal](#def-surprisal) of $y = 1$ is $3.322$ bits. This sum is the [joint surprisal](#def-joint-surprisal) ${\mathbb{s}\mathopen{}\left(0, 1\right)\mathclose{}} = 3.322$ bits ([Lemma 1](#lem-surprisal-chain-rule-reversed)).

> **NOTE:**
>
> *Remark 13* (The chain rule for entropy is the chain rule for surprisal on average). The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a pair is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [joint surprisal](#def-joint-surprisal), and the [conditional entropy](#def-conditional-entropy) is the expectation of the [conditional surprisal](#def-conditional-surprisal):
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} &= {\mathbb{E}\mathopen{}\left[{\mathbb{s}\mathopen{}\left(X, Y\right)\mathclose{}}\right]\mathclose{}} \\
> {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} &= {\mathbb{E}\mathopen{}\left[{\mathbb{s}\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{}}.
> \end{aligned}$$
>
> Taking the expectation of both sides of [Theorem 9](#thm-surprisal-chain-rule) therefore gives [Theorem 8](#thm-entropy-chain-rule).

## 3 Mutual information

> **NOTE:**
>
> **Definition 13 (Mutual information)** The **mutual information** between [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) is the sum of their entropies minus their [joint entropy](#def-joint-entropy):
>
> $${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} \stackrel{\text{def}}{=}{\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}}.$$

> **NOTE:**
>
> **Theorem 10 (Mutual information is symmetric)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(Y ; X\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. The [joint entropy](#def-joint-entropy) of the pair $(X, Y)$ equals that of $(Y, X)$, because both are the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of the same two values, listed in either order. So [Definition 13](#def-mutual-information) gives
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} \\
> &= {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y, X\right)\mathclose{}} \\
> &= {\mathbb{I}\mathopen{}\left(Y ; X\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Theorem 11 (Mutual information as a reduction in entropy)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy), the [mutual information](#def-mutual-information) is the reduction in the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of either variable from learning the other:
>
> $${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Subtract ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ from both sides of the [chain rule](#thm-entropy-chain-rule):
>
> $${\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}.$$
>
> Substituting into [Definition 13](#def-mutual-information) gives
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - \mathopen{}\left[{\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}\right]\mathclose{} \\
> &= {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} \\
> &= {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}.
> \end{aligned}$$
>
> The [chain rule](#thm-entropy-chain-rule) also gives ${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}$, so exchanging $X$ and $Y$ in the aligned display above gives ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$.

> **NOTE:**
>
> **Theorem 12 (Mutual information from the conditional entropies)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - \mathopen{}\left[{\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{}.$$

> **NOTE:**
>
> *Proof*. By [Corollary 3](#cor-conditional-entropy-difference) and the [chain rule](#thm-entropy-chain-rule), the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of each variable is the [joint entropy](#def-joint-entropy) minus a [conditional entropy](#def-conditional-entropy):
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} &= {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} \\
> {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} &= {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}.
> \end{aligned}$$
>
> Substituting both into [Definition 13](#def-mutual-information) gives
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} \\
> &= \mathopen{}\left[{\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{} + \mathopen{}\left[{\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}\right]\mathclose{} - {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} \\
> &= {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} - \mathopen{}\left[{\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{}.
> \end{aligned}$$

> **NOTE:**
>
> **Theorem 13 (Decomposition of the sum of entropies)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + 2 \, {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Rearranging [Theorem 12](#thm-mutual-information-joint-minus-conditionals) gives
>
> $${\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}.$$
>
> Rearranging [Definition 13](#def-mutual-information) gives
>
> $${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}}.$$
>
> Substituting the first display into the second gives
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}
> &= {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + \mathopen{}\left[{\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{} \\
> &= {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + 2 \, {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Theorem 14 (Twice the mutual information)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $$2 \, {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = \mathopen{}\left[{\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}\right]\mathclose{} + \mathopen{}\left[{\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{}.$$

> **NOTE:**
>
> *Proof*. By [Theorem 11](#thm-mutual-information-reduction),
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} &= {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} \\
> {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} &= {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}.
> \end{aligned}$$
>
> Adding the two displays gives
>
> $$\begin{aligned}
> \mathopen{}\left[{\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}\right]\mathclose{} + \mathopen{}\left[{\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{}
> &= {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} \\
> &= 2 \, {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Example 13 (Mutual information identities with a noisy copy)**  
>
> Take the fair coin $X$ and its noisy copy $Y$ from [Example 9](#exm-entropy-chain-rule-noisy-copy). The chunk computes the [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) from the joint [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) in [bits](#def-bit), then the [mutual information](#def-mutual-information) in four ways.
>
> Show code
>
> ``` r
> entropy <- function(p) -sum(p * log2(p))
> joint <- matrix(
>   data = c(0.4, 0.1, 0.1, 0.4),
>   nrow = 2
> )
> h_xy <- entropy(joint)
> h_x <- entropy(rowSums(joint))
> h_y <- entropy(colSums(joint))
> h_x_given_y <- h_xy - h_y
> h_y_given_x <- h_xy - h_x
> mi_definition <- h_x + h_y - h_xy
> mi_reduction <- h_y - h_y_given_x
> mi_conditionals <- h_xy - (h_x_given_y + h_y_given_x)
> mi_twice <- ((h_x - h_x_given_y) + (h_y - h_y_given_x)) / 2
> c(mi_definition, mi_reduction, mi_conditionals, mi_twice)
> #> [1] 0.2780719 0.2780719 0.2780719 0.2780719
> ```
>
> All four agree: ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = 0.278$ bits ([Definition 13](#def-mutual-information), [Theorem 11](#thm-mutual-information-reduction), [Theorem 12](#thm-mutual-information-joint-minus-conditionals) and [Theorem 14](#thm-twice-mutual-information)). Also ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} = 2$ bits matches ${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} + 2 \, {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} = 2$ bits ([Theorem 13](#thm-entropy-sum-decomposition)).

> **NOTE:**
>
> *Remark 14* (Entropies as areas). The identities above match a picture of two overlapping regions, with the area of one region standing for ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$ and the area of the other for ${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}$. The overlap has area ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$ ([Definition 13](#def-mutual-information)). The part of the first region outside the overlap has area ${\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}$, and the part of the second region outside the overlap has area ${\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}$. The two regions together have area ${\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}}$ ([Theorem 12](#thm-mutual-information-joint-minus-conditionals)). The picture is a mnemonic for two variables only.

> **NOTE:**
>
> **Theorem 15 (Mutual information as a divergence)** Let $X$ and $Y$ be [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf) $p(x, y)$ and [marginal](https://morrison-lab.github.io/pds/random-variables.html#def-marginal) [probability mass functions](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) $p(x)$ and $p(y)$. If their [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) are finite, then their [mutual information](#def-mutual-information) is the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of the product of the [marginals](https://morrison-lab.github.io/pds/random-variables.html#def-marginal) from the [joint distribution](https://morrison-lab.github.io/pds/random-variables.html#def-joint-distribution):
>
> $${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = \sum_{x, y} p(x, y) \log \frac{p(x, y)}{p(x) \, p(y)},$$
>
> where the sum runs over the pairs with $p(x, y) > 0$.

> **NOTE:**
>
> *Proof*. The [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) are finite, so the [expectations](https://morrison-lab.github.io/pds/expectation.html#def-expectation) below are finite and can be split and regrouped. With [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1$, $p(X, Y) > 0$, $p(X) > 0$ and $p(Y) > 0$. By [Definition 13](#def-mutual-information) and the definitions of [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) and [joint entropy](#def-joint-entropy),
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X, Y\right)\mathclose{}} \\
> &= {\mathbb{E}\mathopen{}\left[-\log p(X)\right]\mathclose{}} + {\mathbb{E}\mathopen{}\left[-\log p(Y)\right]\mathclose{}} - {\mathbb{E}\mathopen{}\left[-\log p(X, Y)\right]\mathclose{}} \\
> &= {\mathbb{E}\mathopen{}\left[\log p(X, Y) - \log p(X) - \log p(Y)\right]\mathclose{}} \\
> &= {\mathbb{E}\mathopen{}\left[\log \frac{p(X, Y)}{p(X) \, p(Y)}\right]\mathclose{}} \\
> &= \sum_{x, y} p(x, y) \log \frac{p(x, y)}{p(x) \, p(y)}.
> \end{aligned}$$
>
> The last line is the [definition of expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) over the pairs with $p(x, y) > 0$. It is the divergence of $p(x) \, p(y)$ from $p(x, y)$ by the [discrete formula](https://morrison-lab.github.io/pds/expectation.html#thm-kl-divergence-discrete).

> **NOTE:**
>
> **Example 14 (Mutual information of a noisy copy)**  
>
> Let $X$ be a fair coin toss, coded $0$ or $1$. Let $Y$ equal $X$ with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.8$ and the other value with probability $0.2$. The [joint distribution](https://morrison-lab.github.io/pds/random-variables.html#def-joint-distribution) gives probability $0.4$ to $(0, 0)$ and $(1, 1)$ and $0.1$ to $(0, 1)$ and $(1, 0)$. The chunk computes the [mutual information](#def-mutual-information) in [bits](#def-bit) from the divergence formula in [Theorem 15](#thm-mutual-information-kl).
>
> Show code
>
> ``` r
> joint <- matrix(
>   data = c(0.4, 0.1, 0.1, 0.4),
>   nrow = 2,
>   dimnames = list(x = 0:1, y = 0:1)
> )
> p_x <- rowSums(joint)
> p_y <- colSums(joint)
> product <- outer(X = p_x, Y = p_y)
> terms <- joint * log2(joint / product)
> mutual_information <- sum(terms)
> mutual_information
> #> [1] 0.2780719
> ```
>
> So ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = 0.278$ bits. This matches ${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}$, which is $1$ [bit](#def-bit) minus the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a coin with [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.8$ and $0.2$. That is $1 - 0.722$ bits.

> **NOTE:**
>
> **Theorem 16 (The divergence is nonnegative)** Let $p$ and $q$ be [probability mass functions](https://morrison-lab.github.io/pds/random-variables.html#def-pmf) on the values $x_1, x_2, \ldots$, with $q(x) > 0$ wherever $p(x) > 0$, and suppose that
>
> $$\sum_x p(x) \, \bigl\lvert \log_2 \bigl( p(x) / q(x) \bigr) \bigr\rvert < \infty.$$
>
> Then the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) satisfies
>
> $${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}} \ge 0,$$
>
> with ${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}} = 0$ exactly when $q = p$.

> **NOTE:**
>
> *Proof*. Every [sum](https://morrison-lab.github.io/mds/algebra-sums.html#def-summation) here runs over the values $x$ with $p(x) > 0$. For every $t > 0$, [the logarithm lies below its tangent line](https://morrison-lab.github.io/mds/optimization-convexity.html#cor-log-below-tangent): $\ln t \le t - 1$, with equality exactly when $t = 1$. Apply this with $t = q(x) / p(x)$, and multiply by $p(x) > 0$, as in the proof of [Gibbs’ inequality](https://morrison-lab.github.io/pds/expectation.html#thm-kl-divergence-nonnegative) for [finitely many](https://morrison-lab.github.io/mcs/functions.html#def-finite-set) values:
>
> $$p(x) \ln \frac{q(x)}{p(x)} \le q(x) - p(x),$$
>
> with equality exactly when $q(x) = p(x)$. Both sides are summable over $x$. The left side does by the assumption in the statement, and the right side does because $\sum_x p(x) = 1$ and $\sum_x q(x) \le 1$. So the relation holds for the totals over $x$:
>
> $$\sum_x p(x) \ln \frac{q(x)}{p(x)}
> \le \sum_x q(x) - 1
> \le 0.$$
>
> The left side is $-\ln 2 \cdot {{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}}$, so ${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}} \ge 0$.
>
> If ${{D_{\mathrm{KL}}}\mathopen{}\left(p \,\Vert\, q\right)\mathclose{}} = 0$, both relations hold with equality. The first forces $q(x) = p(x)$ at every $x$ with $p(x) > 0$. The second then gives $\sum_x q(x) = 1$, so $q$ has no mass where $p$ has none, and $q = p$. Conversely, $q = p$ gives $\log_2 (p(x)/q(x)) = 0$ for every $x$.

> **NOTE:**
>
> **Example 15 (Divergence of a biased coin from a fair coin)**  
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
> Both divergences between the two coins are positive, as [Theorem 16](#thm-kl-divergence-nonnegative) requires, and they differ, so swapping $p$ and $q$ changes the divergence. The divergence of $p$ from itself is $0$.

> **NOTE:**
>
> **Theorem 17 (Mutual information is nonnegative)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} \ge 0.$$
>
> Equality holds exactly when $X$ and $Y$ are [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt).

> **NOTE:**
>
> *Proof*. Let $p(x, y)$ be the [joint mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf), with [marginals](https://morrison-lab.github.io/pds/random-variables.html#def-marginal) $p(x)$ and $p(y)$. By [Theorem 15](#thm-mutual-information-kl), ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$ is the divergence of $p(x) \, p(y)$ from $p(x, y)$, and the [sum](https://morrison-lab.github.io/mds/algebra-sums.html#def-summation) defining it is absolutely summable, as the proof of that result shows. The product $p(x) \, p(y)$ is nonzero wherever $p(x, y)$ is nonzero, because each of $p(x)$ and $p(y)$ is at least $p(x, y)$ there. By [Theorem 16](#thm-kl-divergence-nonnegative), the divergence is nonnegative, with equality exactly when $p(x) \, p(y)$ and $p(x, y)$ agree. The [logarithm](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) satisfies $\log_b t = \ln t / \ln b$, so the divergence with $\log_b$ is the divergence with $\log_2$ times $\ln 2 / \ln b$, which has the same sign and the same zero. Hence ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} \ge 0$, and ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = 0$ exactly when $p(x, y) = p(x) \, p(y)$ for every pair, which is independence.

> **NOTE:**
>
> **Example 16 (Mutual information of dependent and independent coins)**  
>
> For the noisy copy in [Example 14](#exm-mutual-information-noisy-copy), the [mutual information](#def-mutual-information) is positive, because $Y$ depends on $X$. For two [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt) fair coins, every joint [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) is $0.25$. The chunk computes the mutual information of both pairs.
>
> Show code
>
> ``` r
> joint_dependent <- matrix(data = c(0.4, 0.1, 0.1, 0.4), nrow = 2)
> ratio_dependent <- joint_dependent / outer(
>   X = rowSums(joint_dependent),
>   Y = colSums(joint_dependent)
> )
> mi_dependent <- sum(joint_dependent * log2(ratio_dependent))
> joint_independent <- matrix(data = 0.25, nrow = 2, ncol = 2)
> product_independent <- outer(
>   X = rowSums(joint_independent),
>   Y = colSums(joint_independent)
> )
> ratio_independent <- joint_independent / product_independent
> terms_independent <- joint_independent * log2(ratio_independent)
> mi_independent <- sum(terms_independent)
> c(mi_dependent = mi_dependent, mi_independent = mi_independent)
> #>   mi_dependent mi_independent 
> #>      0.2780719      0.0000000
> ```
>
> So the mutual information of the independent coins is $0$ [bits](#def-bit), and that of the dependent pair is $0.278$ bits ([Theorem 17](#thm-mutual-information-nonnegative)).

> **NOTE:**
>
> **Corollary 5 (Conditioning reduces entropy)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}.$$
>
> Equality holds exactly when $X$ and $Y$ are [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt).

> **NOTE:**
>
> *Proof*. By [Theorem 11](#thm-mutual-information-reduction),
>
> $${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}.$$
>
> By [Theorem 17](#thm-mutual-information-nonnegative), the right side is nonnegative, and it is $0$ exactly when $X$ and $Y$ are [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt).

> **NOTE:**
>
> **Example 17 (Learning a noisy copy lowers the entropy)**  
>
> For the coin $X$ and noisy copy $Y$ in [Example 14](#exm-mutual-information-noisy-copy), the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $Y$ is $1$ [bit](#def-bit). Given $X$, the variable $Y$ is a coin with [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.8$ and $0.2$. The chunk computes the [conditional entropy](#def-conditional-entropy) from that coin.
>
> Show code
>
> ``` r
> h_y <- 1
> h_y_given_x <- -0.8 * log2(0.8) - 0.2 * log2(0.2)
> c(h_y = h_y, h_y_given_x = h_y_given_x)
> #>         h_y h_y_given_x 
> #>   1.0000000   0.7219281
> ```
>
> Here ${\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}} = 0.722$ [bits](#def-bit), which is below ${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} = 1$ bit ([Corollary 5](#cor-conditioning-reduces-entropy)).

> **NOTE:**
>
> *Remark 15* (Mutual information as a divergence). Cover and Thomas ([2006, sec. 2.3](#ref-cover2006elements)) define [mutual information](#def-mutual-information) as the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of the product of the [marginals](https://morrison-lab.github.io/pds/random-variables.html#def-marginal) of $(X, Y)$ from their [joint distribution](https://morrison-lab.github.io/pds/random-variables.html#def-joint-distribution). [Theorem 15](#thm-mutual-information-kl) proves that this divergence equals ${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X\right)\mathclose{}}$ ([Cover and Thomas 2006, sec. 2.4](#ref-cover2006elements)), and [Theorem 17](#thm-mutual-information-nonnegative) proves that ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} \ge 0$ ([Cover and Thomas 2006, sec. 2.6](#ref-cover2006elements)). Learning $X$ never raises the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $Y$ on average ([Corollary 5](#cor-conditioning-reduces-entropy)).

> **NOTE:**
>
> **Theorem 18 (Mutual information of a variable with itself)** For a [discrete random variable](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ with finite [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{I}\mathopen{}\left(X ; X\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Given $X=x$, the variable $X$ equals $x$ with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $1$, so $p(x \mid x) = 1$. Hence $-\log p(X \mid x) = -\log 1 = 0$ given $X=x$, and the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of this constant is $0$:
>
> $${\mathbb{H}\mathopen{}\left(X \mid X=x\right)\mathclose{}} = 0.$$
>
> By [Theorem 7](#thm-conditional-entropy-average),
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(X \mid X\right)\mathclose{}}
> &= \sum_{x} p(x) \, {\mathbb{H}\mathopen{}\left(X \mid X=x\right)\mathclose{}} \\
> &= 0.
> \end{aligned}$$
>
> By [Theorem 11](#thm-mutual-information-reduction) with $Y = X$,
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(X ; X\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid X\right)\mathclose{}} \\
> &= {\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Example 18 (A fair coin is fully informative about itself)**  
>
> Let $X$ be a fair coin toss. Its [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) is $1$ [bit](#def-bit). Given $X$ itself, there is no uncertainty left, so ${\mathbb{H}\mathopen{}\left(X \mid X\right)\mathclose{}} = 0$. Hence ${\mathbb{I}\mathopen{}\left(X ; X\right)\mathclose{}} = 1 - 0 = 1$ bit ([Theorem 18](#thm-mutual-information-self)), the same as ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$.

> **NOTE:**
>
> **Definition 14 (Information gain)** A decision tree splits the points at a node into branches. The **information gain** of the split is the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of the labels at the node, minus the entropy of the labels in each branch, weighted by the share of the node’s points that branch holds ([Quinlan 1986](#ref-quinlan1986induction)).

> **NOTE:**
>
> *Remark 16* (Information gain is mutual information). Draw one point from the node of [Definition 14](#def-information-gain), and let $Y$ be its class and $X$ the branch it falls into. Then the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) at the node is $H(Y)$, the weighted entropy left in the branches is $H(Y \mid X)$, and the [information gain](#def-information-gain) is the [mutual information](#def-mutual-information) ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$.

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
> Draw one point from the node, each equally likely, let $Y$ be its color, and let $X$ be the branch it falls into ([Remark 16](#rem-information-gain)). The [information gain](#def-information-gain) of each split is then ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$. Use base-2 [logarithms](https://morrison-lab.github.io/mds/algebra-exponentials.html#def-logarithm) throughout.
>
> 1.  Compute $H(Y)$.
>
> 2.  For each split, compute $H(Y \mid X = x)$ for both branches, and then $H(Y \mid X)$.
>
> 3.  Compute the information gain ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$ for each split. Which split has the larger gain?

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
> 2.  A branch holding one color only has [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) $0$. For split A, the “no” branch holds $6$ red and $10$ green points of $16$:
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
> 3.  By [Theorem 11](#thm-mutual-information-reduction), the gain is $H(Y) - H(Y \mid X)$:
>
>     - split A: $1 - 0.764 = 0.236$ [bits](entropy.llms.md#def-bit)
>     - split B: $1 - 0.689 = 0.311$ bits
>
>     Split B has the larger gain. Both splits isolate a branch of one color, so the gain depends on the other, mixed branch. B’s mixed branch, $5$ red against $10$ green, is more lopsided than A’s $6$ against $10$, so it has less entropy, and it also holds fewer of the points, $15$ against $16$, so its entropy counts for less.

## 4 Chain rules

> **NOTE:**
>
> **Theorem 19 (Chain rule for entropy, many variables)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X_1, \ldots, X_n$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{H}\mathopen{}\left(X_1, \ldots, X_n\right)\mathclose{}} = \sum_{i=1}^{n} {\mathbb{H}\mathopen{}\left(X_i \mid X_1, \ldots, X_{i-1}\right)\mathclose{}},$$
>
> where the term for $i = 1$ is ${\mathbb{H}\mathopen{}\left(X_1\right)\mathclose{}}$.

> **NOTE:**
>
> *Proof*. The proof is by [induction](https://morrison-lab.github.io/mcs/induction.html#def-proof-by-induction) on $n$. The claim for $n = 1$ is ${\mathbb{H}\mathopen{}\left(X_1\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X_1\right)\mathclose{}}$.
>
> Let $n \ge 2$, and suppose the claim holds for $n - 1$ variables. Treat $(X_1, \ldots, X_{n-1})$ as a single variable. The chain rule for two variables ([Theorem 8](#thm-entropy-chain-rule)) gives
>
> $${\mathbb{H}\mathopen{}\left(X_1, \ldots, X_n\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X_1, \ldots, X_{n-1}\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(X_n \mid X_1, \ldots, X_{n-1}\right)\mathclose{}}.$$
>
> The induction hypothesis expands the first summand on the right:
>
> $$\begin{aligned}
> {\mathbb{H}\mathopen{}\left(X_1, \ldots, X_n\right)\mathclose{}}
> &= \sum_{i=1}^{n-1} {\mathbb{H}\mathopen{}\left(X_i \mid X_1, \ldots, X_{i-1}\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(X_n \mid X_1, \ldots, X_{n-1}\right)\mathclose{}} \\
> &= \sum_{i=1}^{n} {\mathbb{H}\mathopen{}\left(X_i \mid X_1, \ldots, X_{i-1}\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Example 19 (Chain rule for entropy along a chain of noisy copies)**  
>
> Let $X_1$ be a fair coin toss, coded $0$ or $1$. Let $X_2$ be a noisy copy of $X_1$ that flips it with [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.2$, and let $X_3$ be a noisy copy of $X_2$ that flips it with probability $0.2$, independently of $X_1$ given $X_2$. The chunk builds the [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf) of $(X_1, X_2, X_3)$ and compares their [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy), in [bits](#def-bit), with the sum in [Theorem 19](#thm-entropy-chain-rule-n).
>
> Show code
>
> ``` r
> flip <- 0.2
> channel <- matrix(
>   data = c(1 - flip, flip, flip, 1 - flip),
>   nrow = 2,
>   byrow = TRUE
> )
> joint <- array(data = 0, dim = c(2, 2, 2))
> for (x1 in 1:2) {
>   for (x2 in 1:2) {
>     for (x3 in 1:2) {
>       joint[x1, x2, x3] <- 0.5 * channel[x1, x2] * channel[x2, x3]
>     }
>   }
> }
> h_joint <- -sum(joint * log2(joint))
> h_coin <- -flip * log2(flip) - (1 - flip) * log2(1 - flip)
> h_sum <- 1 + h_coin + h_coin
> c(h_joint = h_joint, h_sum = h_sum)
> #>  h_joint    h_sum 
> #> 2.443856 2.443856
> ```
>
> The first term of the sum is ${\mathbb{H}\mathopen{}\left(X_1\right)\mathclose{}} = 1$ [bit](#def-bit). Given $X_1$, the variable $X_2$ is a coin with flip probability $0.2$, and given $(X_1, X_2)$ the variable $X_3$ is the same kind of coin, so each of the other two terms is $0.722$ bits. The sum is $2.444$ bits, which equals ${\mathbb{H}\mathopen{}\left(X_1, X_2, X_3\right)\mathclose{}} = 2.444$ bits.

> **NOTE:**
>
> **Definition 15 (Conditional mutual information)** The **conditional mutual information** of [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ given a third one, $Z$, with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy), is the reduction in the [conditional entropy](#def-conditional-entropy) of $Y$ given $Z$ from also learning $X$:
>
> $${\mathbb{I}\mathopen{}\left(X ; Y \mid Z\right)\mathclose{}} \stackrel{\text{def}}{=}{\mathbb{H}\mathopen{}\left(Y \mid Z\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X, Z\right)\mathclose{}}.$$

> **NOTE:**
>
> **Example 20 (Conditional mutual information along a chain of noisy copies)**  
>
> Take the chain of noisy copies $X_1$, $X_2$, $X_3$ from [Example 19](#exm-entropy-chain-rule-n-copies). Once $X_2$ is known, $X_1$ adds nothing to the [prediction](https://morrison-lab.github.io/pds/expectation.html#def-prediction) of $X_3$, so ${\mathbb{H}\mathopen{}\left(X_3 \mid X_1, X_2\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X_3 \mid X_2\right)\mathclose{}}$, and both equal the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) $h$ of a coin with flip [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.2$. The chunk computes the [conditional mutual information](#def-conditional-mutual-information).
>
> Show code
>
> ``` r
> flip <- 0.2
> h_coin <- -flip * log2(flip) - (1 - flip) * log2(1 - flip)
> h_x3_given_x2 <- h_coin
> h_x3_given_x1_x2 <- h_coin
> h_x3_given_x2 - h_x3_given_x1_x2
> #> [1] 0
> ```
>
> So ${\mathbb{I}\mathopen{}\left(X_1 ; X_3 \mid X_2\right)\mathclose{}} = 0$ [bits](#def-bit).

> **NOTE:**
>
> **Theorem 20 (Chain rule for mutual information)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$, $Y$ and $Z$ whose [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) ${\mathbb{H}\mathopen{}\left(X\right)\mathclose{}}$, ${\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}}$ and ${\mathbb{H}\mathopen{}\left(Z\right)\mathclose{}}$ are finite,
>
> $${\mathbb{I}\mathopen{}\left(X, Z ; Y\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(Z ; Y\right)\mathclose{}} + {\mathbb{I}\mathopen{}\left(X ; Y \mid Z\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. By [Theorem 11](#thm-mutual-information-reduction), applied to the pair $(X, Z)$ and to $Z$,
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(X, Z ; Y\right)\mathclose{}} &= {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X, Z\right)\mathclose{}} \\
> {\mathbb{I}\mathopen{}\left(Z ; Y\right)\mathclose{}} &= {\mathbb{H}\mathopen{}\left(Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid Z\right)\mathclose{}}.
> \end{aligned}$$
>
> Subtracting the second display from the first gives
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(X, Z ; Y\right)\mathclose{}} - {\mathbb{I}\mathopen{}\left(Z ; Y\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(Y \mid Z\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X, Z\right)\mathclose{}} \\
> &= {\mathbb{I}\mathopen{}\left(X ; Y \mid Z\right)\mathclose{}},
> \end{aligned}$$
>
> where the last line is [Definition 15](#def-conditional-mutual-information).

> **NOTE:**
>
> **Example 21 (Chain rule for mutual information along a chain of noisy copies)**  
>
> For the chain in [Example 19](#exm-entropy-chain-rule-n-copies), the [marginal distribution](https://morrison-lab.github.io/pds/random-variables.html#def-marginal) of $X_3$ is a fair coin, so ${\mathbb{H}\mathopen{}\left(X_3\right)\mathclose{}} = 1$ [bit](#def-bit). The chunk computes the [mutual information](#def-mutual-information) of $X_3$ with $X_2$, and with the pair $(X_1, X_2)$.
>
> Show code
>
> ``` r
> flip <- 0.2
> h_coin <- -flip * log2(flip) - (1 - flip) * log2(1 - flip)
> h_x3_given_x1_x2 <- h_coin
> i_x2_x3 <- 1 - h_coin
> i_pair_x3 <- 1 - h_x3_given_x1_x2
> c(i_x2_x3 = i_x2_x3, i_pair_x3 = i_pair_x3)
> #>   i_x2_x3 i_pair_x3 
> #> 0.2780719 0.2780719
> ```
>
> Here ${\mathbb{I}\mathopen{}\left(X_2 ; X_3\right)\mathclose{}} = 0.278$ [bits](#def-bit) and ${\mathbb{I}\mathopen{}\left(X_1, X_2 ; X_3\right)\mathclose{}} = 0.278$ bits. The difference is ${\mathbb{I}\mathopen{}\left(X_1 ; X_3 \mid X_2\right)\mathclose{}} = 0$ ([Theorem 20](#thm-mutual-information-chain-rule)), as in [Example 20](#exm-conditional-mutual-information).

> **NOTE:**
>
> **Theorem 21 (Conditional mutual information is nonnegative)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$, $Y$ and $Z$ with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy),
>
> $${\mathbb{I}\mathopen{}\left(X ; Y \mid Z\right)\mathclose{}} \ge 0.$$

> **NOTE:**
>
> *Proof*. For each value $z$ with $\mathbb{P}(Z=z) > 0$, let ${\mathbb{I}_{z}\mathopen{}\left(X ; Y\right)\mathclose{}}$ be the [mutual information](#def-mutual-information) of $X$ and $Y$ computed from their joint [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) given $Z=z$, so that ${\mathbb{I}_{z}\mathopen{}\left(X ; Y\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(Y \mid Z=z\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X, Z=z\right)\mathclose{}}$. Applying [Definition 10](#def-conditional-entropy) to ${\mathbb{H}\mathopen{}\left(Y \mid Z\right)\mathclose{}}$ and to ${\mathbb{H}\mathopen{}\left(Y \mid X, Z\right)\mathclose{}}$ expands each over the values $z$ of $Z$:
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(X ; Y \mid Z\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(Y \mid Z\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X, Z\right)\mathclose{}} \\
> &= \sum_z \mathbb{P}(Z=z) \mathopen{}\left[{\mathbb{H}\mathopen{}\left(Y \mid Z=z\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(Y \mid X, Z=z\right)\mathclose{}}\right]\mathclose{} \\
> &= \sum_z \mathbb{P}(Z=z) \, {\mathbb{I}_{z}\mathopen{}\left(X ; Y\right)\mathclose{}}.
> \end{aligned}$$
>
> Each ${\mathbb{I}_{z}\mathopen{}\left(X ; Y\right)\mathclose{}}$ is nonnegative by [Theorem 17](#thm-mutual-information-nonnegative). Since $\mathbb{P}(Z=z) \ge 0$ as well, every summand $\mathbb{P}(Z=z) \, {\mathbb{I}_{z}\mathopen{}\left(X ; Y\right)\mathclose{}}$ is nonnegative, so ${\mathbb{I}\mathopen{}\left(X ; Y \mid Z\right)\mathclose{}} \ge 0$.

> **NOTE:**
>
> **Example 22 (Learning a third variable can create information)**  
>
> Let $X$ and $Y$ be [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt) fair coins, coded $0$ or $1$, and let $Z = X + Y \bmod 2$ record whether they differ. The two coins are independent, so ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = 0$ ([Theorem 17](#thm-mutual-information-nonnegative)). Given $Z$, each of $X$ and $Y$ determines the other. The chunk computes the [conditional mutual information](#def-conditional-mutual-information) from the [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf), in [bits](#def-bit).
>
> Show code
>
> ``` r
> entropy <- function(p) -sum(p[p > 0] * log2(p[p > 0]))
> joint <- array(data = 0, dim = c(2, 2, 2))
> for (x in 0:1) {
>   for (y in 0:1) {
>     z <- (x + y) %% 2
>     joint[x + 1, y + 1, z + 1] <- 0.25
>   }
> }
> h_xyz <- entropy(joint)
> h_xz <- entropy(apply(X = joint, MARGIN = c(1, 3), FUN = sum))
> h_yz <- entropy(apply(X = joint, MARGIN = c(2, 3), FUN = sum))
> h_z <- entropy(apply(X = joint, MARGIN = 3, FUN = sum))
> h_y_given_z <- h_yz - h_z
> h_y_given_xz <- h_xyz - h_xz
> h_y_given_z - h_y_given_xz
> #> [1] 1
> ```
>
> So ${\mathbb{I}\mathopen{}\left(X ; Y \mid Z\right)\mathclose{}} = 1$ [bit](#def-bit), which is nonnegative ([Theorem 21](#thm-conditional-mutual-information-nonnegative)), although ${\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}} = 0$.

> **NOTE:**
>
> **Definition 16 (Markov chain of three random variables)** [Discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$, $Y$ and $Z$ form a **Markov chain** $X \to Y \to Z$ ([Cover and Thomas 2006, sec. 2.8](#ref-cover2006elements)) if $X$ and $Z$ are [conditionally independent](https://morrison-lab.github.io/pds/independence.html#def-cind) given $Y$: for every value $y$ with $\mathbb{P}(Y=y) > 0$ and all values $x$ and $z$,
>
> $$\mathbb{P}(X=x, Z=z \mid Y=y) = \mathbb{P}(X=x \mid Y=y) \, \mathbb{P}(Z=z \mid Y=y).$$

> **NOTE:**
>
> **Example 23 (A chain of noisy copies is a Markov chain)**  
>
> In [Example 19](#exm-entropy-chain-rule-n-copies), each of $X_2$ and $X_3$ is a noisy copy of the variable before it. So $X_3$ depends on $X_1$ only through $X_2$. The chunk builds the [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf) of $(X_1, X_2, X_3)$ and checks the defining equation of the chain $X_1 \to X_2 \to X_3$ for each value of $X_2$.
>
> Show code
>
> ``` r
> flip <- 0.2
> copy <- matrix(
>   data = c(1 - flip, flip, flip, 1 - flip),
>   nrow = 2
> )
> joint <- array(data = 0, dim = c(2, 2, 2))
> for (x1 in 1:2) {
>   for (x2 in 1:2) {
>     for (x3 in 1:2) {
>       joint[x1, x2, x3] <- 0.5 * copy[x1, x2] * copy[x2, x3]
>     }
>   }
> }
> gaps <- numeric(2)
> for (x2 in 1:2) {
>   slice <- joint[, x2, ]
>   given_x2 <- slice / sum(slice)
>   product <- outer(rowSums(given_x2), colSums(given_x2))
>   gaps[x2] <- max(abs(given_x2 - product))
> }
> gaps
> #> [1] 1.110223e-16 1.110223e-16
> ```
>
> Both gaps are zero up to rounding, so $X_1$ and $X_3$ are [conditionally independent](https://morrison-lab.github.io/pds/independence.html#def-cind) given $X_2$.

> **NOTE:**
>
> **Lemma 2 (Conditional mutual information along a Markov chain)** If $X \to Y \to Z$ is a [Markov chain](#def-markov-chain) and the [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $X$, $Y$ and $Z$ are finite, then
>
> $${\mathbb{I}\mathopen{}\left(Z ; X \mid Y\right)\mathclose{}} = 0.$$

> **NOTE:**
>
> *Proof*. Fix values $y$ and $z$ with $\mathbb{P}(Y=y, Z=z) > 0$. Dividing the defining equation of the chain by $\mathbb{P}(Z=z \mid Y=y)$ gives
>
> $$\mathbb{P}(X=x \mid Y=y, Z=z) = \mathbb{P}(X=x \mid Y=y)$$
>
> for every $x$. So the [entropy given](#def-entropy-given-value) $(Y, Z) = (y, z)$ is the entropy given $Y = y$. Averaging over $(Y, Z)$ and over $Y$ gives
>
> $${\mathbb{H}\mathopen{}\left(X \mid Y, Z\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}}.$$
>
> By [Definition 15](#def-conditional-mutual-information),
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(Z ; X \mid Y\right)\mathclose{}}
> &= {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Z, Y\right)\mathclose{}} \\
> &= {\mathbb{H}\mathopen{}\left(X \mid Y\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(X \mid Y, Z\right)\mathclose{}} \\
> &= 0.
> \end{aligned}$$

> **NOTE:**
>
> **Theorem 22 (Data processing inequality)** If $X \to Y \to Z$ is a [Markov chain](#def-markov-chain) and the [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $X$, $Y$ and $Z$ are finite, then
>
> $${\mathbb{I}\mathopen{}\left(X ; Z\right)\mathclose{}} \le {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. The [chain rule](#thm-mutual-information-chain-rule) for the pair $(Z, Y)$ and the pair $(Y, Z)$ gives
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(Z, Y ; X\right)\mathclose{}} &= {\mathbb{I}\mathopen{}\left(Y ; X\right)\mathclose{}} + {\mathbb{I}\mathopen{}\left(Z ; X \mid Y\right)\mathclose{}} \\
> {\mathbb{I}\mathopen{}\left(Y, Z ; X\right)\mathclose{}} &= {\mathbb{I}\mathopen{}\left(Z ; X\right)\mathclose{}} + {\mathbb{I}\mathopen{}\left(Y ; X \mid Z\right)\mathclose{}}.
> \end{aligned}$$
>
> The pairs $(Z, Y)$ and $(Y, Z)$ contain the same two variables, so ${\mathbb{I}\mathopen{}\left(Z, Y ; X\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(Y, Z ; X\right)\mathclose{}}$. By [Lemma 2](#lem-markov-chain-conditional-mutual-information), ${\mathbb{I}\mathopen{}\left(Z ; X \mid Y\right)\mathclose{}} = 0$. By [Theorem 21](#thm-conditional-mutual-information-nonnegative), ${\mathbb{I}\mathopen{}\left(Y ; X \mid Z\right)\mathclose{}} \ge 0$. Therefore
>
> $$\begin{aligned}
> {\mathbb{I}\mathopen{}\left(Y ; X\right)\mathclose{}}
> &= {\mathbb{I}\mathopen{}\left(Z ; X\right)\mathclose{}} + {\mathbb{I}\mathopen{}\left(Y ; X \mid Z\right)\mathclose{}} \\
> &\ge {\mathbb{I}\mathopen{}\left(Z ; X\right)\mathclose{}}.
> \end{aligned}$$
>
> By [Theorem 10](#thm-mutual-information-symmetric), ${\mathbb{I}\mathopen{}\left(Y ; X\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$ and ${\mathbb{I}\mathopen{}\left(Z ; X\right)\mathclose{}} = {\mathbb{I}\mathopen{}\left(X ; Z\right)\mathclose{}}$, so ${\mathbb{I}\mathopen{}\left(X ; Z\right)\mathclose{}} \le {\mathbb{I}\mathopen{}\left(X ; Y\right)\mathclose{}}$.

> **NOTE:**
>
> **Example 24 (Each extra noisy copy loses information)**  
>
> For the chain $X_1 \to X_2 \to X_3$ in [Example 23](#exm-markov-chain-noisy-copies), the chunk computes the [mutual information](#def-mutual-information) of $X_1$ with $X_2$ and with $X_3$, in [bits](#def-bit). Each variable is a fair coin. The variable $X_3$ differs from $X_1$ when exactly one of the two copies flips, which has [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $2 \times 0.2 \times 0.8 = 0.32$.
>
> Show code
>
> ``` r
> h_coin <- function(flip) -flip * log2(flip) - (1 - flip) * log2(1 - flip)
> i_x1_x2 <- 1 - h_coin(flip = 0.2)
> i_x1_x3 <- 1 - h_coin(flip = 0.32)
> c(i_x1_x2 = i_x1_x2, i_x1_x3 = i_x1_x3)
> #>    i_x1_x2    i_x1_x3 
> #> 0.27807191 0.09561854
> ```
>
> Here ${\mathbb{I}\mathopen{}\left(X_1 ; X_3\right)\mathclose{}} = 0.096$ bits is below ${\mathbb{I}\mathopen{}\left(X_1 ; X_2\right)\mathclose{}} = 0.278$ bits ([Theorem 22](#thm-data-processing-inequality)).

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

Grinstead, Charles M., and J. Laurie Snell. 1997. *Introduction to Probability*. 2nd ed. American Mathematical Society.

International Electrotechnical Commission. 2008. *Quantities and Units — Part 13: Information Science and Technology*. IEC 80000-13:2008. International Electrotechnical Commission.

Jelinek, F., R. L. Mercer, L. R. Bahl, and J. K. Baker. 1977. “Perplexity—a Measure of the Difficulty of Speech Recognition Tasks.” *The Journal of the Acoustical Society of America* 62 (S1): S63. <https://doi.org/10.1121/1.2016299>.

Leinster, Tom. 2021. *Entropy and Diversity: The Axiomatic Approach*. Cambridge University Press. <https://doi.org/10.1017/9781108963558>.

MacKay, David J. C. 2003. *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.

Quinlan, J. R. 1986. “Induction of Decision Trees.” *Machine Learning* 1 (1): 81–106. <https://doi.org/10.1007/BF00116251>.

Rényi, Alfréd. 1961. “On Measures of Entropy and Information.” In *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability, Volume 1: Contributions to the Theory of Statistics*, edited by Jerzy Neyman. University of California Press. <https://projecteuclid.org/euclid.bsmsp/1200512181>.

Wikipedia contributors. 2026. *Rényi Entropy — Wikipedia, the Free Encyclopedia*. <https://en.wikipedia.org/wiki/R%C3%A9nyi_entropy>.

Back to top
