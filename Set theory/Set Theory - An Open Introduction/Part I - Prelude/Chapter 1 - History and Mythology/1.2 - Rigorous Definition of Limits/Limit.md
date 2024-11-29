---
aliases:
  - limit
---
- "As $x$ approaches $c$, $g(x)$ tends without limit to $l$."
$$
\lim_{x \rightarrow c} g(x) = l.
$$
- More precisely,
$$
(\forall \epsilon > 0)(\exists \delta > 0) \forall x \, (\vert x - c \vert < \delta \rightarrow \vert g(x) - l \vert < \epsilon)
$$
- Roughly, you can make your error less than $\epsilon$ by choosing arguments which are no more than $\delta$ away from $c$.
___
- The [[Gradient|gradient]] of $f$ at $c$ is given by:
$$
f'(c)=\lim_{x \rightarrow 0} \frac{f(c+x)-f(c)}{x} \text{ where a limit exists.}
$$
___
Conceptually made the [[Infinitesimal|infinitesimal]] obsolete.