# Perfect secrecy

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-12 00:38:18 (PST)

A cipher hides a message from an eavesdropper who sees only the ciphertext. [Mutual information](entropy.llms.md#def-mutual-information) says exactly how much the ciphertext can reveal, and so how much key a cipher needs.

## 1 Perfect secrecy

> **NOTE:**
>
> **Definition 1 (Perfect secrecy)** Let $M$ be a message, let $K$ be a key [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt) of $M$, and let $C$ be the ciphertext made from $M$ and $K$, all [discrete random variables](https://morrison-lab.github.io/pds/random-variables.html#def-discrete-rv) with finite [entropies](https://morrison-lab.github.io/pds/expectation.html#def-entropy). The key and the ciphertext together determine the message. The cipher has **perfect secrecy** when the ciphertext tells an eavesdropper nothing about the message, that is, when $M$ and $C$ have zero [mutual information](entropy.llms.md#def-mutual-information):
>
> $${\mathbb{I}\mathopen{}\left(M ; C\right)\mathclose{}} = 0.$$
>
> The definition is from ([Shannon 1949](#ref-shannon1949communication)).

> **NOTE:**
>
> **Example 1 (The one-time pad with a two-bit message)**  
>
> Let the message take the four values $0, 1, 2, 3$ (two [bits](entropy.llms.md#def-bit)) with [probabilities](https://morrison-lab.github.io/pds/probability-basics.html#def-probability) $0.4, 0.3, 0.2, 0.1$. The key is [uniform](https://morrison-lab.github.io/pds/random-variables.html#def-uniform) on the same four values, and the ciphertext is the bitwise exclusive or of message and key. The R chunk below builds the [joint distribution](https://morrison-lab.github.io/pds/random-variables.html#def-joint-distribution) of message and ciphertext, and computes the [mutual information](entropy.llms.md#def-mutual-information) between them.
>
> Show code
>
> ``` r
> prior <- c(0.4, 0.3, 0.2, 0.1)
> joint <- matrix(0, nrow = 4, ncol = 4)
> for (m in 0:3) {
>   for (k in 0:3) {
>     c_value <- bitwXor(m, k)
>     joint[m + 1, c_value + 1] <- joint[m + 1, c_value + 1] + prior[m + 1] / 4
>   }
> }
> cipher_prob <- colSums(joint)
> product <- outer(prior, cipher_prob)
> max_gap <- max(abs(joint - product))
> mutual_info <- sum(joint * log2(joint / product))
> c(max_gap = max_gap, mutual_info = mutual_info)
> #>     max_gap mutual_info 
> #>           0           0
> ```
>
> The ciphertext is uniform, with probability $0.25$ on each value, and the largest gap between the joint distribution and the product of the two [marginal distributions](https://morrison-lab.github.io/pds/random-variables.html#def-marginal) is $0$. So the mutual information is $0$ bits: the pad has [perfect secrecy](#def-perfect-secrecy) for these message probabilities.

> **NOTE:**
>
> **Theorem 1 (Perfect secrecy needs a key with at least the entropy of the message)** Let $M$, $K$ and $C$ be as in [Definition 1](#def-perfect-secrecy), and suppose the cipher has [perfect secrecy](#def-perfect-secrecy). Then the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of the key is at least the entropy of the message:
>
> $${\mathbb{H}\mathopen{}\left(K\right)\mathclose{}} \ge {\mathbb{H}\mathopen{}\left(M\right)\mathclose{}}.$$

> **NOTE:**
>
> *Proof*. By [Definition 1](#def-perfect-secrecy), ${\mathbb{I}\mathopen{}\left(M ; C\right)\mathclose{}} = 0$, so $M$ and $C$ are [independent](https://morrison-lab.github.io/pds/independence.html#def-indpt), and the equality case of [conditioning reduces entropy](entropy.llms.md#cor-conditioning-reduces-entropy) gives the first step:
>
> $${\mathbb{H}\mathopen{}\left(M\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(M \mid C\right)\mathclose{}}.$$
>
> The [chain rule](entropy.llms.md#thm-entropy-chain-rule) expands both [conditional entropies](entropy.llms.md#def-conditional-entropy) below:
>
> $${\mathbb{H}\mathopen{}\left(M \mid C\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(M, C\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(C\right)\mathclose{}}, \qquad {\mathbb{H}\mathopen{}\left(K \mid C\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(K, C\right)\mathclose{}} - {\mathbb{H}\mathopen{}\left(C\right)\mathclose{}}.$$
>
> Apply the chain rule to $(M, C)$ and $K$ jointly in two orders:
>
> $${\mathbb{H}\mathopen{}\left(M, C, K\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(C, K\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(M \mid C, K\right)\mathclose{}}, \qquad {\mathbb{H}\mathopen{}\left(M, C, K\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(M, C\right)\mathclose{}} + {\mathbb{H}\mathopen{}\left(K \mid M, C\right)\mathclose{}}.$$
>
> The key and the ciphertext determine the message, so ${\mathbb{H}\mathopen{}\left(M \mid C, K\right)\mathclose{}} = 0$. A conditional entropy is nonnegative, so ${\mathbb{H}\mathopen{}\left(K \mid M, C\right)\mathclose{}} \ge 0$. Equating the two expansions then gives ${\mathbb{H}\mathopen{}\left(M, C\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(C, K\right)\mathclose{}}$. Subtract ${\mathbb{H}\mathopen{}\left(C\right)\mathclose{}}$ from both sides:
>
> $${\mathbb{H}\mathopen{}\left(M \mid C\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(K \mid C\right)\mathclose{}}.$$
>
> By [conditioning reduces entropy](entropy.llms.md#cor-conditioning-reduces-entropy) again, ${\mathbb{H}\mathopen{}\left(K \mid C\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(K\right)\mathclose{}}$. Chain the three comparisons:
>
> $${\mathbb{H}\mathopen{}\left(M\right)\mathclose{}} = {\mathbb{H}\mathopen{}\left(M \mid C\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(K \mid C\right)\mathclose{}} \le {\mathbb{H}\mathopen{}\left(K\right)\mathclose{}}.$$

> **NOTE:**
>
> **Example 2 (The key of a one-time pad is as long as the message)**  
>
> The R chunk below computes the [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of the message and of the key of [Example 1](#exm-perfect-secrecy).
>
> Show code
>
> ``` r
> prior <- c(0.4, 0.3, 0.2, 0.1)
> key_prob <- rep(1 / 4, 4)
> message_entropy <- -sum(prior * log2(prior))
> key_entropy <- -sum(key_prob * log2(key_prob))
> c(message_entropy = message_entropy, key_entropy = key_entropy)
> #> message_entropy     key_entropy 
> #>        1.846439        2.000000
> ```
>
> The message has $1.846$ [bits](entropy.llms.md#def-bit) of entropy, and the key has $2$ bits, so the key’s entropy is at least the message’s, as [Theorem 1](#thm-perfect-secrecy-key-entropy) requires. A key with fewer than $1.846$ bits of entropy could not give this message [perfect secrecy](#def-perfect-secrecy).

> **NOTE:**
>
> *Remark 1* (Source of the definition and the theorem). [Perfect secrecy](#def-perfect-secrecy) and the [theorem on the key](#thm-perfect-secrecy-key-entropy) are from ([Shannon 1949](#ref-shannon1949communication)). The proof above uses only the [chain rule](entropy.llms.md#thm-entropy-chain-rule) and [conditioning reduces entropy](entropy.llms.md#cor-conditioning-reduces-entropy), both of which are results about [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy).

## References

Shannon, C. E. 1949. “Communication Theory of Secrecy Systems.” *Bell System Technical Journal* 28 (4): 656–715. <https://doi.org/10.1002/j.1538-7305.1949.tb00928.x>.

Back to top
