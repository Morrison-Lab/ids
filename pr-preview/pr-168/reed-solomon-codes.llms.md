# Reed–Solomon codes and list decoding

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-09 03:17:28 (PST)

A [Reed–Solomon code](error-correcting-codes.llms.md#def-reed-solomon-code) recovers the message when fewer than $d / 2$ symbols are corrupted, where $d$ is its [minimum distance](error-correcting-codes.llms.md#def-hamming-distance). Past that point a received word can be near several codewords, and a decoder can return all of them as a list.

## 1 List decoding

> **NOTE:**
>
> **Definition 1 (List-decodable code)** Let $C$ be a [block code](error-correcting-codes.llms.md#def-block-code) of length $n$ over the alphabet $\Sigma$, and let $e \ge 0$ and $L \ge 1$ be [integers](https://morrison-lab.github.io/mcs/number-systems.html#def-integers). Then $C$ is $(e, L)$-list-decodable if every received word $r \in \Sigma^n$ has at most $L$ codewords $c$ with ${\Delta\mathopen{}\left(c, r\right)\mathclose{}} \le e$. To **list decode** a received word $r$ is to find all of those codewords.

> **NOTE:**
>
> **Example 1 (A received word with two codewords nearby)**  
>
> Take the [Reed–Solomon code](error-correcting-codes.llms.md#def-reed-solomon-code) with $q = n = 5$ and $k = 2$ from [the small example](error-correcting-codes.llms.md#exm-reed-solomon), whose codewords are the values of the 25 lines $m_0 + m_1 t$ at the points $0, 1, 2, 3, 4$. Its [minimum distance](error-correcting-codes.llms.md#def-hamming-distance) is $4$, so every received word has at most one codeword within distance $1$. Within distance $2$ it can have more. The R chunk below lists the lines within distance $2$ of the received word $r = (1, 3, 1, 0, 4)$.
>
> Show code
>
> ``` r
> points <- 0:4
> lines <- expand.grid(m0 = 0:4, m1 = 0:4)
> codeword <- function(m0, m1) (m0 + m1 * points) %% 5
> received <- c(1, 3, 1, 0, 4)
> distance <- function(m0, m1) sum(codeword(m0, m1) != received)
> lines$distance <- mapply(distance, lines$m0, lines$m1)
> lines[lines$distance <= 2, ]
> ```
>
> Two lines are within distance $2$ of $r$, so this received word has a list of size 2 at distance $2$. A decoder that outputs one codeword must choose between them.

> **NOTE:**
>
> **Theorem 1 (A bound on the list size of a Reed–Solomon code)** Let $C$ be the [Reed–Solomon code](error-correcting-codes.llms.md#def-reed-solomon-code) with length $n$ and $k$ message symbols, and let $e \in \{0, 1, \ldots, n - k\}$. Then every received word has at most
>
> $$\frac{\binom{n}{k}}{\binom{n - e}{k}}$$
>
> codewords within [Hamming distance](error-correcting-codes.llms.md#def-hamming-distance) $e$. So $C$ is $(e, L)$-list-decodable for every $L$ at least the value above.

> **NOTE:**
>
> *Proof*. Fix a received word $r$ and let $S$ be the codewords $c$ with ${\Delta\mathopen{}\left(c, r\right)\mathclose{}} \le e$. Count the pairs $(c, T)$, where $c \in S$ and $T$ is a choice of $k$ positions at which $c$ and $r$ agree.
>
> Each $c \in S$ differs from $r$ in at most $e$ positions, so it agrees with $r$ in at least $n - e$ positions. Since $n - e \ge k$, it has at least $\binom{n - e}{k}$ choices of $T$. So there are at least $|S| \binom{n - e}{k}$ pairs.
>
> Now fix a choice $T$ of $k$ positions. Two distinct codewords that both agree with $r$ on $T$ agree with each other on $T$. By [the distance theorem](error-correcting-codes.llms.md#thm-reed-solomon-distance), distinct codewords differ in at least $n - k + 1$ positions, so they agree in at most $k - 1$ positions, which is fewer than $k$. So at most one codeword $c$ agrees with $r$ on $T$. There are $\binom{n}{k}$ choices of $T$, so there are at most $\binom{n}{k}$ pairs.
>
> Combine the two counts:
>
> $$|S| \binom{n - e}{k} \le \binom{n}{k}.$$
>
> Divide both sides by $\binom{n - e}{k}$, which is nonzero because $n - e \ge k$.

> **NOTE:**
>
> **Example 2 (The list size for the length-5 Reed–Solomon code)**  
>
> Take $n = 5$, $k = 2$ and $e = 2$, as in [Example 1](#exm-list-decoding-reed-solomon). [Theorem 1](#thm-reed-solomon-list-size) gives $\binom{5}{2} / \binom{3}{2}$ as the largest list size.
>
> Show code
>
> ``` r
> choose(5, 2) / choose(3, 2)
> #> [1] 3.333333
> ```
>
> The list size is a whole number, so it is at most 3. The received word of [Example 1](#exm-list-decoding-reed-solomon) has 2.

> **NOTE:**
>
> *Remark 1* (Efficient list decoding of Reed–Solomon codes). [Theorem 1](#thm-reed-solomon-list-size) says how long the list can be, but it does not say how to find the list quickly. Guruswami and Sudan ([1999](#ref-guruswami1999improved)) gave a polynomial-time algorithm that finds the list for a [Reed–Solomon code](error-correcting-codes.llms.md#def-reed-solomon-code).

## References

Guruswami, Venkatesan, and Madhu Sudan. 1999. “Improved Decoding of Reed–Solomon and Algebraic-Geometry Codes.” *IEEE Transactions on Information Theory* 45 (6): 1757–67. <https://doi.org/10.1109/18.782097>.

Back to top
