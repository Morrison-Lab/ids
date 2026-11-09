# Low-density parity-check codes

Code

- [Show All Code](javascript:void(0))

- [Hide All Code](javascript:void(0))

- 

  ------------------------------------------------------------------------

- [View Source](javascript:void(0))

Published

Last modified: 2026-11-09 11:37:04 (PST)

A [linear code](error-correcting-codes.llms.md#def-linear-code) is described by a [parity-check matrix](error-correcting-codes.llms.md#def-linear-code). When it has few ones, each check involves only a few positions of the word.

## 1 Sparse parity checks

> **NOTE:**
>
> **Definition 1 (Regular low-density parity-check code)** Let $j, k \ge 1$ be [integers](https://morrison-lab.github.io/mcs/number-systems.html#def-integers). A $(j, k)$-regular LDPC code (low-density parity-check code) consists of the words $y \in \mathbb{F}_{2}^n$ with $H y = 0$, where $H$ has $j$ ones in every column and $k$ ones in every row, and zeros elsewhere. The rows of $H$ need not be independent. When no row is a sum of other rows, $H$ is a [parity-check matrix](error-correcting-codes.llms.md#def-linear-code) of this [linear code](error-correcting-codes.llms.md#def-linear-code).

> **NOTE:**
>
> **Example 1 (A** $(2, 3)$-regular code of length 6)  
>
> Take four items, labeled $1, 2, 3, 4$, and the six pairs of them. Let $H$ have a row for each item and a column for each pair, with a 1 where the item lies in the pair. Every pair holds two items and every item lies in three pairs, so $H$ has two ones in each column and three in each row, and it gives a $(2, 3)$-regular [LDPC code](#def-ldpc-code) of length 6. The R chunk below builds $H$, checks the counts, and counts the words $y$ with $H y = 0$ modulo 2.
>
> Show code
>
> ``` r
> pairs <- t(combn(4, 2))
> H <- sapply(seq_len(nrow(pairs)), function(e) as.integer(1:4 %in% pairs[e, ]))
> H
> #>      [,1] [,2] [,3] [,4] [,5] [,6]
> #> [1,]    1    1    1    0    0    0
> #> [2,]    1    0    0    1    1    0
> #> [3,]    0    1    0    1    0    1
> #> [4,]    0    0    1    0    1    1
> colSums(H)
> #> [1] 2 2 2 2 2 2
> rowSums(H)
> #> [1] 3 3 3 3
> words <- as.matrix(expand.grid(rep(list(0:1), 6)))
> is_codeword <- apply(words, 1, function(y) all((H %*% y) %% 2 == 0))
> sum(is_codeword)
> #> [1] 8
> ```
>
> There are 8 codewords, so the [dimension](https://morrison-lab.github.io/mds/linear-algebra-subspaces.html#def-dimension) is $\log_2$ of that number, which is 3.

> **NOTE:**
>
> **Theorem 1 (The rate of a regular LDPC code)** Let $C$ be a $(j, k)$-regular [LDPC code](#def-ldpc-code) of length $n$. Then the [rate](channel-capacity.llms.md#def-code-rate) of $C$ is at least $1 - j / k$.

> **NOTE:**
>
> *Proof*. Let $H$ be as in the definition of $C$, with $m$ rows and $n$ columns. Count the ones of $H$ in two ways. Each of the $n$ columns holds $j$ ones, so $H$ has $n j$ ones. Each of the $m$ rows holds $k$ ones, so $H$ has $m k$ ones. So $n j = m k$, and $m = n j / k$.
>
> The codewords are the words $y$ with $H y = 0$, so their number is $2^{n - r}$, where $r$ is the [rank](https://morrison-lab.github.io/mds/linear-algebra-subspaces.html#def-rank) of $H$. The rank of $H$ is at most its number of rows, so $r \le m$, and $C$ has at least $2^{n - m}$ codewords. Its [rate](channel-capacity.llms.md#def-code-rate) is $(n - r) / n$, which is at least $(n - m) / n = 1 - j / k$.

> **NOTE:**
>
> **Example 2 (The rate of the length-6 code)**  
>
> For the $(2, 3)$-regular [LDPC code](#def-ldpc-code) of [Example 1](#exm-ldpc-code), [Theorem 1](#thm-ldpc-rate) gives a [rate](channel-capacity.llms.md#def-code-rate) of at least $1 - 2 / 3$. It has 8 codewords, so its rate is $\log_2(8) / 6$.
>
> Show code
>
> ``` r
> 1 - 2 / 3
> #> [1] 0.3333333
> log2(8) / 6
> #> [1] 0.5
> ```
>
> The rate is $1/2$, which is larger than $1/3$. The four rows of $H$ add to zero modulo 2, because every column has two ones, so $H$ has [rank](https://morrison-lab.github.io/mds/linear-algebra-subspaces.html#def-rank) 3, not 4.

> **NOTE:**
>
> *Remark 1* (Where LDPC codes come from). Gallager ([1962](#ref-gallager1962low)) introduced [low-density parity-check codes](#def-ldpc-code), and MacKay ([2003](#ref-mackay2003information)) covers them in his book.

## References

Gallager, Robert G. 1962. “Low-Density Parity-Check Codes.” *IEEE Transactions on Information Theory* 8 (1): 21–28. <https://doi.org/10.1109/TIT.1962.1057683>.

MacKay, David J. C. 2003. *Information Theory, Inference, and Learning Algorithms*. Cambridge University Press.

Back to top
