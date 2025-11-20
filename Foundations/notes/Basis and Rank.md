# Basis and Rank

## Definitions and Fundamental Concepts

### Spanning Set
**Definition:** Consider a vector space $V = \{V_1, V_2\}$ and any set of vectors $\vec{x_1}, \vec{x_2}, \ldots, \vec{x_p} \in V$. If every vector $\vec{v} \in V$ can be expressed as a linear combination of vectors $\vec{x_i}$, this is called a **spanning set** of $V$.

- The set of all linear combinations in $\mathbb{R}$ is called the **span** of $A$
- **IEA span** is either equal to $V = \text{span}[\vec{x}]$ or $V = \text{span}[x_1, \ldots, x_n]$

### Basis

**Definition:** Consider a vector space $V = \{\vec{y_1}, \ldots\}$ and $\vec{A} \subseteq \mathbb{R}^n$. A spanning set $\vec{A} \subseteq A^n$ is called minimal if there exists no smaller set $\vec{B} \subseteq \vec{A}$ that spans $V$.

Equivalently, a minimal spanning set of $V$ is minimal and is called a **basis** of $V$.

Therefore: **A basis is a minimal spanning set and a maximal linearly independent set of vectors.**

Let $V = \{\vec{V_1}, \ldots\}$ be a vector space and $\mathcal{B} = \{\vec{B_1}, \vec{B}\}$. Then the following statements are equivalent:

- $\mathcal{B}$ is a basis of $V$
- $\mathcal{B}$ is a minimally spanning set
- $\mathcal{B}$ is a maximally linearly independent set of vectors in $V_i$ (i.e., adding any other vector to this set will make it linearly dependent)

Every vector $\vec{v} \in V$ is a unique combination of vectors from $\mathcal{B}$ and even if we combine a unique $\vec{v}: \vec{v} = \sum \vec{b_i} = \sum \vec{b_i}$ and $\vec{x_i} \in \{\mathcal{B}_i\} \in \mathbb{R}$ we get $\sum \vec{b_i} \neq \sum \vec{b_{i+1}}$.

### Standard Basis in $\mathbb{R}^3$

In $\mathbb{R}^3$, the canonical/standard basis is:

$$\mathcal{B} = \begin{Bmatrix} \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \end{Bmatrix}$$

Every vector space $V$ generates from $\mathcal{B}$. There can be many bases or a same space, but at least one basis exists.

### Dimension

**Definition:** The dimension of $V$ is the number of basis vectors of $V$.

We call it a minimal spanning set (or the intuition is to be a vector in $\mathbb{R}^n$).

---

## Finding a Basis

A basis of a subspace $U = \text{span}\{\vec{x_1}, \ldots, \vec{x_p} \in \mathbb{R}^n\}$ can be found by removing the following steps:

1. Write the spanning vectors as columns in a matrix $B$
2. Determine the **row-echelon form** of $B$
3. The **span-wise matrix** of $V$ is the pivot column; use a basis of $U$

### Example

$$\begin{bmatrix} 2 & 3 & 4 \\ 3 & 3 & 1 \\ 4 & 4 & 1 \end{bmatrix} \to \rho \begin{bmatrix} 2 & 3 & 4 \\ 3 & 3 & 1 \\ 4 & 4 & 1 \end{bmatrix} \to \begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & 3 \\ 0 & 0 & 0 \end{bmatrix}$$

Thus, it has a pivot in columns 1, 2, $\ldots, x_1, x_2$, which leads to linear independence in columns 1 and 2 in $B$.

---

## Rank

**Definition:** The **rank** of a matrix $A \in \mathbb{R}^{m \times n}$ equals the number of linearly independent columns of $A$.

### Properties of Rank

**Number of rows:**
- The rank of $A \in \mathbb{R}^{m \times n}$ is at most $\min\{m, n\}$ - The column rank cannot be $> \min\{m, n\}$ (also called $\text{rank}(A)$). A basis of $M$ can be used to express $\text{rank}(A)$.
- The rank of $A \in \mathbb{R}^{m \times n}$ is an integer $U \subseteq \mathbb{R}^n$ with $\text{dim}(U) = \text{rank}(A)$. A basis of $M$ can be found by setting Gaussian elimination on $A$.

**Column rank and row rank:**
- For all $A \in \mathbb{R}^{m \times n}$, $\text{rank}(A^T) = \text{rank}(A)$ (where $A^T$ is the transpose to $A$)
- For all $A \in \mathbb{R}^{m \times n}$, the column of solutions for $Ax = 0$ belongs to dimension $n - \text{rank}(A)$ (assigned system)

**Full rank:**
A matrix $A \in \mathbb{R}^{m \times n}$ has **full rank** if it has rank equal to the largest possible rank for a matrix of the same dimensions.

- In particular, if $A \in \mathbb{R}^{m \times n}$ is only one zero vector (rank $= m$ if $m < n$) or (rank $= n$ if $m > n$) then $A$ is at **zero solution**.
- The Null Space of $A$ is $A$ is only one zero vector rank $= m$, $\text{dim}(A) = 0$ with no unique solution.

Since $\mathcal{B}$ is unique with respect to non-unique solutions, then there are no consistent solutions to these systems (i.e., at least one unique solution).

There will be at least one free variable.

---

## Vector Space and Span

Vectors $V_1, \ldots, V_r$ **span a space**: The space consists of all combinations of those vectors.

**Basis for a space** is a sequence of vectors with 2 properties:
1. **Independent**
2. **Span the space**
