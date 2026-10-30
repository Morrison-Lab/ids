# Differential entropy

Code

Published

Last modified: 2026-10-30 14:49:10 (PDT)

This page extends the [surprisal and entropy](entropy.llms.md) of discrete random variables to [continuous random variables](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv).

## 1 Surprisal and entropy of a continuous random variable

> **NOTE:**
>
> **Definition 1 (Surprisal of a value of a continuous random variable)** The **surprisal** of a possible value \\x\\ of a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) \\X\\ with [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) \\f\\ and \\f(x) \> 0\\ is
>
> \\{s\mathopen{}\left(x\right)\mathclose{}} \stackrel{\text{def}}{=}-\log f(x).\\
>
> This extends the [surprisal](entropy.llms.md#def-surprisal) of a value of a discrete random variable, with the density \\f(x)\\ in place of the probability \\\mathbb{P}(X=x)\\.

> **NOTE:**
>
> **Definition 2 (Differential entropy)** The **differential entropy** of a [continuous random variable](https://morrison-lab.github.io/pds/random-variables.html#def-continuous-rv) \\X\\ with [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) \\f\\ is the [expectation](https://morrison-lab.github.io/pds/expectation.html#def-expectation) of its [surprisal](#def-surprisal-continuous), when that expectation exists ([Cover and Thomas 2006, sec. 8.1](#ref-cover2006elements)):
>
> \\h(X) \stackrel{\text{def}}{=}{\mathbb{E}\mathopen{}\left\[{s\mathopen{}\left(X\right)\mathclose{}}\right\]\mathclose{}} = -\int\_{{\mathopen{}\left\\x : f(x) \> 0\right\\\mathclose{}}} f(x) \log f(x) \\ dx.\\

> **NOTE:**
>
> **Example 1 (Differential entropy of a uniform random variable)** Let \\X\\ be uniformly distributed on the interval from \\0\\ to \\a \> 0\\, so that its [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) is \\f(x) = 1/a\\ for \\0 \< x \< a\\ and \\0\\ elsewhere. Every value in the interval has [surprisal](#def-surprisal-continuous) \\{s\mathopen{}\left(x\right)\mathclose{}} = -\log (1/a) = \log a\\, so the [differential entropy](#def-differential-entropy) is \\\log a\\ ([Cover and Thomas 2006](#ref-cover2006elements), Example 8.1.1):
>
> \\ \begin{aligned} h(X) &= -\int_0^a \frac{1}{a} \log \frac{1}{a} \\ dx \\ &= \log a. \end{aligned} \\
>
> With \\a = 1/2\\ and base-2 logarithms, \\h(X) = -1\\ [bit](entropy.llms.md#def-bit).

> **NOTE:**
>
> *Remark 1* (Differential entropy differs from entropy). A [density](https://morrison-lab.github.io/pds/random-variables.html#def-pdf) value is not a probability, so the [surprisal](#def-surprisal-continuous) of a continuous value and the [differential entropy](#def-differential-entropy) behave differently from their discrete counterparts:
>
> - **Sign.** A density can exceed \\1\\, so the surprisal \\{s\mathopen{}\left(x\right)\mathclose{}}\\ and the differential entropy can be negative, as in [Example 1](#exm-differential-entropy-uniform) with \\a \< 1\\ ([Cover and Thomas 2006, sec. 8.1](#ref-cover2006elements)). The [entropy](https://morrison-lab.github.io/pds/expectation.html#def-entropy) of a discrete random variable is never negative.
> - **Units.** Rescaling changes the differential entropy: \\h(aX) = h(X) + \log \|a\|\\ for a constant \\a \ne 0\\ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.4). Measuring the same quantity in metres rather than centimetres therefore changes \\h\\. Adding a constant does not: \\h(X + c) = h(X)\\ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.6.3).
> - **Not a limit of entropy.** Round \\X\\ to bins of width \\\Delta\\, which gives a discrete random variable \\X^\Delta\\. Then \\{H\mathopen{}\left(X^\Delta\right)\mathclose{}} + \log \Delta \to h(X)\\ as \\\Delta \to 0\\ ([Cover and Thomas 2006](#ref-cover2006elements), Theorem 8.3.1). The entropy \\{H\mathopen{}\left(X^\Delta\right)\mathclose{}}\\ itself grows without bound as \\\Delta \to 0\\, so \\h(X)\\ is not its limit.

## References

Cover, Thomas M., and Joy A. Thomas. 2006. *Elements of Information Theory*. 2nd ed. Wiley-Interscience. <https://doi.org/10.1002/047174882X>.

Back to top
