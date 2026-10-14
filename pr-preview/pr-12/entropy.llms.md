# Entropy and mutual information

Code

Published

Last modified: 2026-10-14 11:05:50 (PDT)

This page builds on the definitions of [entropy, cross-entropy and Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#sec-entropy) in *Probability for Data Science*.

## 1 Surprisal

> **NOTE:**
>
> **Definition 1 (Surprisal)** The **surprisal** of an outcome \\x\\ of a discrete random variable \\X\\ with \\\operatorname{P}(X=x) \> 0\\ is
>
> \\s(x) \stackrel{\text{def}}{=}-\log \operatorname{P}(X=x).\\
>
> With base-2 logarithms, surprisal is measured in *bits*; with natural logarithms, in *nats*.

> **NOTE:**
>
> **Example 1 (Counting bits with fair coins)** One toss of a fair coin has \\2\\ equally likely outcomes, and one binary digit is enough to record which one happened. Two tosses have \\4\\ outcomes, and two binary digits record them. In general, \\k\\ tosses have \\n = 2^k\\ equally likely outcomes, and \\k = \log_2 n\\ binary digits record them.
>
> Each of those \\n\\ outcomes has probability \\p = 1/n\\, so
>
> \\ \begin{aligned} k &= \log_2 n \\ &= \log_2 \frac{1}{p} \\ &= -\log_2 p, \end{aligned} \\
>
> which is the [surprisal](#def-surprisal) of the outcome, in bits.
>
> Ten tosses that all land heads have probability \\2^{-10}\\, so
>
> \\ \begin{aligned} s(\text{ten heads}) &= -\log_2 2^{-10} \\ &= 10 \text{ bits}. \end{aligned} \\

> **NOTE:**
>
> *Remark 1* (Unlikely outcomes carry more information). Surprisal is large when an outcome was unlikely, and it falls to \\0\\ as the outcome becomes certain. Correctly predicting heads on one toss of a fair coin is worth \\1\\ bit; correctly predicting ten heads in a row is worth \\10\\ bits. MacKay ([2003, sec. 2.4](#ref-mackay2003information)) calls \\s(x)\\ in bits the *Shannon information content* of the outcome \\x\\.

> **NOTE:**
>
> *Remark 2* (Entropy is expected surprisal). The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a discrete random variable \\X\\ is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [surprisal](#def-surprisal):
>
> \\ \begin{aligned} H(X) &= \operatorname{E}\mathopen{}\left\[-\log \operatorname{P}(X)\right\]\mathclose{} \\ &= \operatorname{E}\mathopen{}\left\[s(X)\right\]\mathclose{}. \end{aligned} \\
>
> So \\H(X)\\ is the average number of bits (with base-2 logarithms) needed to record an outcome of \\X\\ when each outcome \\x\\ costs \\s(x)\\ bits. The [source coding theorem](source-coding.llms.md#thm-source-coding), on a later page of these notes, makes that average precise: no uniquely decodable code does better.

## 2 Joint and conditional entropy

> **NOTE:**
>
> **Definition 2 (Joint entropy)** Let \\X\\ and \\Y\\ be discrete random variables with joint probability mass function \\p(x, y) \stackrel{\text{def}}{=}\operatorname{P}(X=x, Y=y)\\. Their **joint entropy** is the entropy of the pair \\(X, Y)\\:
>
> \\H(X, Y) \stackrel{\text{def}}{=}-\sum\_{x, y} p(x, y) \log p(x, y),\\
>
> where the sum runs over the pairs with \\p(x, y) \> 0\\.

> **NOTE:**
>
> **Definition 3 (Entropy given one value)** For \\X\\ and \\Y\\ as in [Definition 2](#def-joint-entropy), write \\p(y \mid x) \stackrel{\text{def}}{=}\operatorname{P}(Y=y \mid X=x)\\. The **entropy of \\Y\\ given \\X=x\\**, for a value \\x\\ with \\\operatorname{P}(X=x) \> 0\\, is
>
> \\H(Y \mid X=x) \stackrel{\text{def}}{=}-\sum\_{y} p(y \mid x) \log p(y \mid x),\\
>
> where the sum runs over the values \\y\\ with \\p(y \mid x) \> 0\\.

> **NOTE:**
>
> **Definition 4 (Conditional entropy)** For \\X\\ and \\Y\\ as in [Definition 2](#def-joint-entropy), write \\p(x) \stackrel{\text{def}}{=}\operatorname{P}(X=x)\\. The **conditional entropy** of \\Y\\ given \\X\\ averages the [entropy of \\Y\\ given each value of \\X\\](#def-entropy-given-value) over the distribution of \\X\\:
>
> \\H(Y \mid X) \stackrel{\text{def}}{=}\sum\_{x} p(x) \\ H(Y \mid X=x),\\
>
> where the sum runs over the values \\x\\ with \\p(x) \> 0\\.

> **NOTE:**
>
> **Theorem 1 (Chain rule for entropy)** For discrete random variables \\X\\ and \\Y\\,
>
> \\H(X, Y) = H(X) + H(Y \mid X).\\

> **NOTE:**
>
> *Proof*. Use the notation of [Definition 3](#def-entropy-given-value) and [Definition 4](#def-conditional-entropy), with every sum over the pairs with \\p(x, y) \> 0\\. Since \\p(x, y) = p(x) \\ p(y \mid x)\\,
>
> \\ \begin{aligned} H(X, Y) &= -\sum\_{x, y} p(x, y) \log p(x, y) \\ &= -\sum\_{x, y} p(x, y) \log \mathopen{}\left\[p(x) \\ p(y \mid x)\right\]\mathclose{} \\ &= -\sum\_{x, y} p(x, y) \log p(x) - \sum\_{x, y} p(x, y) \log p(y \mid x) \\ &= -\sum\_{x} \log p(x) \sum\_{y} p(x, y) - \sum\_{x} p(x) \sum\_{y} p(y \mid x) \log p(y \mid x) \\ &= -\sum\_{x} p(x) \log p(x) + \sum\_{x} p(x) \\ H(Y \mid X=x) \\ &= H(X) + H(Y \mid X). \end{aligned} \\
>
> The fourth line groups the terms by \\x\\ and uses \\p(x, y) = p(x) \\ p(y \mid x)\\ in the second sum; the fifth uses \\\sum\_{y} p(x, y) = p(x)\\ and the definition of \\H(Y \mid X=x)\\.

## 3 Mutual information

> **NOTE:**
>
> **Definition 5 (Mutual information)** The **mutual information** between discrete random variables \\X\\ and \\Y\\ with finite entropies is the reduction in the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of \\Y\\ from learning \\X\\:
>
> \\I(X; Y) \stackrel{\text{def}}{=}H(Y) - H(Y \mid X),\\
>
> where \\H(Y \mid X)\\ is the [conditional entropy](#def-conditional-entropy).

> **NOTE:**
>
> **Theorem 2 (Mutual information is symmetric)** For discrete random variables \\X\\ and \\Y\\ with finite entropies,
>
> \\I(X; Y) = H(X) - H(X \mid Y) = I(Y; X).\\

> **NOTE:**
>
> *Proof*. The [chain rule](#thm-entropy-chain-rule) expands \\H(X, Y)\\ in either order:
>
> \\H(X) + H(Y \mid X) = H(X, Y) = H(Y) + H(X \mid Y).\\
>
> Subtracting \\H(X \mid Y) + H(Y \mid X)\\ from the outer two expressions gives
>
> \\H(X) - H(X \mid Y) = H(Y) - H(Y \mid X).\\
>
> The right side is \\I(X; Y)\\ by [Definition 5](#def-mutual-information), and the left side is \\I(Y; X)\\ by the same definition.

> **NOTE:**
>
> *Remark 3* (Mutual information as a divergence). Cover and Thomas ([2006, sec. 2.3](#ref-cover2006elements)) define mutual information as the [Kullback–Leibler divergence](https://morrison-lab.github.io/pds/expectation.html#def-kl-divergence) of the joint distribution of \\(X, Y)\\ from the product of its marginals, and show that this equals \\H(Y) - H(Y \mid X)\\ ([Cover and Thomas 2006, sec. 2.4](#ref-cover2006elements)). Since a Kullback–Leibler divergence is never negative, and is \\0\\ only when the two distributions are equal ([Cover and Thomas 2006, sec. 2.6](#ref-cover2006elements)), \\I(X; Y) \ge 0\\, with equality exactly when \\X\\ and \\Y\\ are independent. Learning \\X\\ never raises the entropy of \\Y\\ on average.

> **NOTE:**
>
> **Definition 6 (Information gain)** A decision tree splits the points at a node into branches. The **information gain** of the split is the entropy of the class labels at the node, minus the entropy of the labels in each branch, weighted by the share of the node’s points that branch holds ([Quinlan 1986](#ref-quinlan1986induction)).

> **NOTE:**
>
> *Remark 4* (Information gain is mutual information). Draw one point uniformly at random from the node of [Definition 6](#def-information-gain), and let \\Y\\ be its class and \\X\\ the branch it falls into. Then the entropy at the node is \\H(Y)\\, the weighted entropy left in the branches is \\H(Y \mid X)\\, and the information gain is the [mutual information](#def-mutual-information) \\I(X; Y)\\.

> **NOTE:**
>
> **Exercise 1 (Choosing between two splits)** A node holds \\20\\ points, \\10\\ red and \\10\\ green. Two candidate splits each send the points into two branches:
>
> | split | branch | red   | green  |
> |-------|--------|-------|--------|
> | A     | yes    | \\4\\ | \\0\\  |
> |       | no     | \\6\\ | \\10\\ |
> | B     | yes    | \\5\\ | \\10\\ |
> |       | no     | \\5\\ | \\0\\  |
>
> Draw one point uniformly at random from the node, let \\Y\\ be its color, and let \\X\\ be the branch it falls into ([Remark 4](#rem-information-gain)). The information gain of each split ([Definition 6](#def-information-gain)) is then \\I(X; Y)\\. Use base-2 logarithms throughout.
>
> 1.  Compute \\H(Y)\\.
>
> 2.  For each split, compute \\H(Y \mid X = x)\\ for both branches, and then \\H(Y \mid X)\\.
>
> 3.  Compute the information gain \\I(X; Y)\\ for each split. Which split has the larger gain?

> **NOTE:**
>
> *Solution 1*.
>
> 1.  Half the points are red, so
>
>     \\ \begin{aligned} H(Y) &= -\tfrac{1}{2} \log_2 \tfrac{1}{2} - \tfrac{1}{2} \log_2 \tfrac{1}{2} \\ &= 1 \text{ bit}. \end{aligned} \\
>
> 2.  A branch holding one color only has entropy \\0\\. For split A, the “no” branch holds \\6\\ red and \\10\\ green points of \\16\\:
>
>     \\ \begin{aligned} H(Y \mid X = \text{no}) &= -\tfrac{6}{16} \log_2 \tfrac{6}{16} - \tfrac{10}{16} \log_2 \tfrac{10}{16} \\ &\approx 0.531 + 0.424 \\ &\approx 0.954 \text{ bits}. \end{aligned} \\
>
>     The “yes” branch holds \\4\\ of the \\20\\ points and the “no” branch \\16\\, so
>
>     \\ \begin{aligned} H(Y \mid X) &= \tfrac{4}{20} \cdot 0 + \tfrac{16}{20} \cdot 0.954 \\ &\approx 0.764 \text{ bits}. \end{aligned} \\
>
>     For split B, the “yes” branch holds \\5\\ red and \\10\\ green points of \\15\\:
>
>     \\ \begin{aligned} H(Y \mid X = \text{yes}) &= -\tfrac{1}{3} \log_2 \tfrac{1}{3} - \tfrac{2}{3} \log_2 \tfrac{2}{3} \\ &\approx 0.528 + 0.390 \\ &\approx 0.918 \text{ bits}. \end{aligned} \\
>
>     The “yes” branch holds \\15\\ of the \\20\\ points and the “no” branch \\5\\, so
>
>     \\ \begin{aligned} H(Y \mid X) &= \tfrac{15}{20} \cdot 0.918 + \tfrac{5}{20} \cdot 0 \\ &\approx 0.689 \text{ bits}. \end{aligned} \\
>
> 3.  By [Definition 5](#def-mutual-information), the gain is \\H(Y) - H(Y \mid X)\\:
>
>     - split A: \\1 - 0.764 = 0.236\\ bits
>     - split B: \\1 - 0.689 = 0.311\\ bits
>
>     Split B has the larger gain. Both splits isolate a branch of one color, so the gain depends on the other, mixed branch. B’s mixed branch, \\5\\ red against \\10\\ green, is more lopsided than A’s \\6\\ against \\10\\, so it has less entropy, and it also holds fewer of the points, \\15\\ against \\16\\, so its entropy gets less weight.

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

MacKay, David J. C. 2003. *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.

Quinlan, J. R. 1986. “Induction of Decision Trees.” *Machine Learning* 1 (1): 81–106. <https://doi.org/10.1007/BF00116251>.

Back to top
