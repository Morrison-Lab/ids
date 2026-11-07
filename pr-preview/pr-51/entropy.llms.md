# Entropy and mutual information

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-06 16:27:10 (PST)

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
> *Remark 4* (Differential entropy differs from entropy). A [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) value is not a probability, so the [surprisal](https://morrison-lab.github.io/pds/expectation.html#def-surprisal-continuous) of a continuous value and the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a continuous random variable (the differential entropy) behave differently from their discrete counterparts:
>
> - **Sign.** A density can exceed $1$, so the surprisal ${s\mathopen{}\left(x\right)\mathclose{}}$ and the differential entropy can be negative, as in the [uniform example](https://morrison-lab.github.io/pds/expectation.html#exm-entropy-uniform) ([Cover and Thomas 2006, sec. 8.1](#ref-cover2006elements)). The entropy of a discrete random variable is never negative.
> - **Units.** Rescaling changes the differential entropy: ${H\mathopen{}\left(aX\right)\mathclose{}} = {H\mathopen{}\left(X\right)\mathclose{}} + \log |a|$ for a constant $a \ne 0$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.4). Measuring the same quantity in metres rather than centimetres therefore changes it. Adding a constant does not: ${H\mathopen{}\left(X + c\right)\mathclose{}} = {H\mathopen{}\left(X\right)\mathclose{}}$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.3).
> - **Not a limit of entropy.** Round a continuous $X$ to bins of width $\Delta$, which gives a discrete random variable $X^\Delta$. Then ${H\mathopen{}\left(X^\Delta\right)\mathclose{}} + \log \Delta \to {H\mathopen{}\left(X\right)\mathclose{}}$ as $\Delta \to 0$ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.3.1). The entropy ${H\mathopen{}\left(X^\Delta\right)\mathclose{}}$ itself grows without bound as $\Delta \to 0$, so the differential entropy is not its limit.

> **NOTE:**
>
> *Remark 5* (Surprisal and the Fisher information). When the probabilities depend on a parameter $\theta$, the [surprisal](#def-surprisal) of an outcome $x$ is $-\log \operatorname{p}(x \mid \theta)$, which is minus the log-likelihood. Its derivative with respect to $\theta$ is minus the [score](https://morrison-lab.github.io/sds/intro-MLEs.html#def-score). The expected squared score is the [expected (Fisher) information](https://morrison-lab.github.io/sds/intro-MLEs.html#def-einf), which is also the second derivative, at the true parameter value, of the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) between the model at that value and the model at the varying value ([proved in the sds notes](https://morrison-lab.github.io/sds/intro-MLEs.html#thm-fisher-kl-curvature)).

## 2 Joint and conditional entropy

> **NOTE:**
>
> **Definition 4 (Joint entropy)** Let $X$ and $Y$ be discrete random variables with joint probability mass function $p(x, y) \stackrel{\text{def}}{=}\mathbb{P}(X=x, Y=y)$. Their **joint entropy** is the entropy of the pair $(X, Y)$:
>
> $$H(X, Y) \stackrel{\text{def}}{=}-\sum_{x, y} p(x, y) \log p(x, y),$$
>
> where the sum runs over the pairs with $p(x, y) > 0$.

> **NOTE:**
>
> **Definition 5 (Entropy given one value)** For $X$ and $Y$ as in [Definition 4](#def-joint-entropy), write $p(y \mid x) \stackrel{\text{def}}{=}\mathbb{P}(Y=y \mid X=x)$. The **entropy of** $Y$ given $X=x$, for a value $x$ with $\mathbb{P}(X=x) > 0$, is
>
> $$H(Y \mid X=x) \stackrel{\text{def}}{=}-\sum_{y} p(y \mid x) \log p(y \mid x),$$
>
> where the sum runs over the values $y$ with $p(y \mid x) > 0$.

> **NOTE:**
>
> **Definition 6 (Conditional entropy)** For $X$ and $Y$ as in [Definition 4](#def-joint-entropy), write $p(x) \stackrel{\text{def}}{=}\mathbb{P}(X=x)$. The **conditional entropy** of $Y$ given $X$ averages the [entropy of](#def-entropy-given-value) $Y$ given each value of $X$ over the distribution of $X$:
>
> $$H(Y \mid X) \stackrel{\text{def}}{=}\sum_{x} p(x) \, H(Y \mid X=x),$$
>
> where the sum runs over the values $x$ with $p(x) > 0$.

> **NOTE:**
>
> **Theorem 1 (Chain rule for entropy)** For discrete random variables $X$ and $Y$,
>
> $$H(X, Y) = H(X) + H(Y \mid X).$$

> **NOTE:**
>
> *Proof*. Use the notation of [Definition 5](#def-entropy-given-value) and [Definition 6](#def-conditional-entropy), with every sum over the pairs with $p(x, y) > 0$. Since $p(x, y) = p(x) \, p(y \mid x)$,
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

> **NOTE:**
>
> **Definition 7 (Joint surprisal)** Let $X$ and $Y$ be [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with [joint probability mass function](https://morrison-lab.github.io/pds/random-variables.html#def-joint-pmf) $p(x, y) \stackrel{\text{def}}{=}\mathbb{P}(X=x, Y=y)$. The **joint surprisal** of a pair of [outcomes](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) $(x, y)$ with $p(x, y) > 0$ is the [surprisal](#def-surprisal) of that pair:
>
> $${s\mathopen{}\left(x, y\right)\mathclose{}} \stackrel{\text{def}}{=}-\log p(x, y).$$

> **NOTE:**
>
> **Definition 8 (Conditional surprisal)** For $X$ and $Y$ as in [Definition 7](#def-joint-surprisal), the **conditional surprisal** of an [outcome](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) $y$ given an outcome $x$ with $\mathbb{P}(X=x) > 0$ and $\mathbb{P}(Y=y \mid X=x) > 0$ is
>
> $${s\mathopen{}\left(y \mid x\right)\mathclose{}} \stackrel{\text{def}}{=}-\log \mathbb{P}(Y=y \mid X=x).$$

> **NOTE:**
>
> **Example 3 (Joint and conditional surprisal of a noisy copy)**  
>
> Let $X$ be a fair coin toss, coded $0$ or $1$. Let $Y$ be a noisy copy of $X$: it equals $X$ with probability $0.8$ and the other value with probability $0.2$. Take the pair of values $x = 0$ and $y = 1$. The joint [probability](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) is $\mathbb{P}(X=0, Y=1) = 0.1$, the probability of $X=0$ is $0.5$, and the conditional probability is $\mathbb{P}(Y=1 \mid X=0) = 0.2$. The chunk computes the three [surprisals](#def-surprisal), in [bits](#def-bit).
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
> The [joint surprisal](#def-joint-surprisal) is ${s\mathopen{}\left(0, 1\right)\mathclose{}} = 3.322$ bits, the surprisal of $x = 0$ alone is ${s\mathopen{}\left(0\right)\mathclose{}} = 1$ bit, and the [conditional surprisal](#def-conditional-surprisal) is ${s\mathopen{}\left(1 \mid 0\right)\mathclose{}} = 2.322$ bits.

> **NOTE:**
>
> **Theorem 2 (Chain rule for surprisal)** For [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) $X$ and $Y$ and [outcomes](https://morrison-lab.github.io/pds/probability-basics.html#def-experiment-outcome) $x$ and $y$ with $\mathbb{P}(X=x, Y=y) > 0$,
>
> $${s\mathopen{}\left(x, y\right)\mathclose{}} = {s\mathopen{}\left(x\right)\mathclose{}} + {s\mathopen{}\left(y \mid x\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Since $\mathbb{P}(X=x, Y=y) = \mathbb{P}(X=x) \, \mathbb{P}(Y=y \mid X=x)$,
>
> $$\begin{aligned}
> {s\mathopen{}\left(x, y\right)\mathclose{}}
> &= -\log \mathbb{P}(X=x, Y=y) \\
> &= -\log \mathopen{}\left[\mathbb{P}(X=x) \, \mathbb{P}(Y=y \mid X=x)\right]\mathclose{} \\
> &= -\log \mathbb{P}(X=x) - \log \mathbb{P}(Y=y \mid X=x) \\
> &= {s\mathopen{}\left(x\right)\mathclose{}} + {s\mathopen{}\left(y \mid x\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Corollary 1 (Conditional surprisal as a difference)** For $X$, $Y$, $x$ and $y$ as in [Theorem 2](#thm-surprisal-chain-rule),
>
> $${s\mathopen{}\left(y \mid x\right)\mathclose{}} = {s\mathopen{}\left(x, y\right)\mathclose{}} - {s\mathopen{}\left(x\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. Subtract ${s\mathopen{}\left(x\right)\mathclose{}}$ from both sides of [Theorem 2](#thm-surprisal-chain-rule):
>
> $$\begin{aligned}
> {s\mathopen{}\left(x, y\right)\mathclose{}} - {s\mathopen{}\left(x\right)\mathclose{}}
> &= {s\mathopen{}\left(x\right)\mathclose{}} + {s\mathopen{}\left(y \mid x\right)\mathclose{}} - {s\mathopen{}\left(x\right)\mathclose{}} \\
> &= {s\mathopen{}\left(y \mid x\right)\mathclose{}}.
> \end{aligned}$$

> **NOTE:**
>
> **Example 4 (Chain rule for surprisal with a noisy copy)**  
>
> For the pair of values in [Example 3](#exm-joint-conditional-surprisal), the chunk recomputes the three [surprisals](#def-surprisal) in [bits](#def-bit).
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
> The [surprisal](#def-surprisal) of $x = 0$ plus the [conditional surprisal](#def-conditional-surprisal) of $y = 1$ given $x = 0$ is $3.322$ [bits](#def-bit). This sum is the [joint surprisal](#def-joint-surprisal) ${s\mathopen{}\left(0, 1\right)\mathclose{}} = 3.322$ bits ([Theorem 2](#thm-surprisal-chain-rule)). Subtracting ${s\mathopen{}\left(0\right)\mathclose{}} = 1$ bit from the joint surprisal recovers ${s\mathopen{}\left(1 \mid 0\right)\mathclose{}} = 2.322$ bits ([Corollary 1](#cor-conditional-surprisal-difference)).

> **NOTE:**
>
> *Remark 6* (The chain rule for entropy is the chain rule for surprisal on average). The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a pair is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [joint surprisal](#def-joint-surprisal), and the [conditional entropy](#def-conditional-entropy) is the expectation of the [conditional surprisal](#def-conditional-surprisal):
>
> $$\begin{aligned}
> {H\mathopen{}\left(X, Y\right)\mathclose{}} &= {\mathbb{E}\mathopen{}\left[{s\mathopen{}\left(X, Y\right)\mathclose{}}\right]\mathclose{}} \\
> {H\mathopen{}\left(Y \mid X\right)\mathclose{}} &= {\mathbb{E}\mathopen{}\left[{s\mathopen{}\left(Y \mid X\right)\mathclose{}}\right]\mathclose{}}.
> \end{aligned}$$
>
> Taking the expectation of both sides of [Theorem 2](#thm-surprisal-chain-rule) therefore gives [Theorem 1](#thm-entropy-chain-rule).

## 3 Mutual information

> **NOTE:**
>
> **Definition 9 (Mutual information)** The **mutual information** between discrete random variables $X$ and $Y$ with finite entropies is the reduction in the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of $Y$ from learning $X$:
>
> $$I(X; Y) \stackrel{\text{def}}{=}H(Y) - H(Y \mid X),$$
>
> where $H(Y \mid X)$ is the [conditional entropy](#def-conditional-entropy).

> **NOTE:**
>
> **Theorem 3 (Mutual information is symmetric)** For discrete random variables $X$ and $Y$ with finite entropies,
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
> The right side is $I(X; Y)$ by [Definition 9](#def-mutual-information), and the left side is $I(Y; X)$ by the same definition.

> **NOTE:**
>
> *Remark 7* (Mutual information as a divergence). Cover and Thomas ([2006, sec. 2.3](#ref-cover2006elements)) define mutual information as the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of the joint distribution of $(X, Y)$ from the product of its marginals, and show that this equals $H(Y) - H(Y \mid X)$ ([Cover and Thomas 2006, sec. 2.4](#ref-cover2006elements)). Since a Kullback–Leibler divergence is never negative, and is $0$ only when the two distributions are equal ([Cover and Thomas 2006, sec. 2.6](#ref-cover2006elements)), $I(X; Y) \ge 0$, with equality exactly when $X$ and $Y$ are independent. Learning $X$ never raises the entropy of $Y$ on average.

> **NOTE:**
>
> **Definition 10 (Information gain)** A decision tree splits the points at a node into branches. The **information gain** of the split is the entropy of the class labels at the node, minus the entropy of the labels in each branch, weighted by the share of the node’s points that branch holds ([Quinlan 1986](#ref-quinlan1986induction)).

> **NOTE:**
>
> *Remark 8* (Information gain is mutual information). Draw one point uniformly at random from the node of [Definition 10](#def-information-gain), and let $Y$ be its class and $X$ the branch it falls into. Then the entropy at the node is $H(Y)$, the weighted entropy left in the branches is $H(Y \mid X)$, and the information gain is the [mutual information](#def-mutual-information) $I(X; Y)$.

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
> Draw one point uniformly at random from the node, let $Y$ be its color, and let $X$ be the branch it falls into ([Remark 8](#rem-information-gain)). The information gain of each split ([Definition 10](#def-information-gain)) is then $I(X; Y)$. Use base-2 logarithms throughout.
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
> 3.  By [Definition 9](#def-mutual-information), the gain is $H(Y) - H(Y \mid X)$:
>
>     - split A: $1 - 0.764 = 0.236$ bits
>     - split B: $1 - 0.689 = 0.311$ bits
>
>     Split B has the larger gain. Both splits isolate a branch of one color, so the gain depends on the other, mixed branch. B’s mixed branch, $5$ red against $10$ green, is more lopsided than A’s $6$ against $10$, so it has less entropy, and it also holds fewer of the points, $15$ against $16$, so its entropy gets less weight.

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

International Electrotechnical Commission. 2008. *Quantities and Units — Part 13: Information Science and Technology*. IEC 80000-13:2008. International Electrotechnical Commission.

MacKay, David J. C. 2003. *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.

Quinlan, J. R. 1986. “Induction of Decision Trees.” *Machine Learning* 1 (1): 81–106. <https://doi.org/10.1007/BF00116251>.

Back to top
