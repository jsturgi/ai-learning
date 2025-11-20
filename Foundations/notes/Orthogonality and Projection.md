# Orthogonality and Projection

## Introduction to Orthogonality

The angle between two vectors **u** and **v** can be found using:

$$\cos(\theta) = \frac{u \cdot v}{||u|| \cdot ||v||} = \frac{x_1x_2 + y_1y_2}{\sqrt{x_1^2 + y_1^2} \cdot \sqrt{x_2^2 + y_2^2}}$$

**Angle between vectors** $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ and $\begin{pmatrix} 3 \\ -4 \end{pmatrix}$ = 90° = 180°/2

**Note:** This raised idea of 2 independent vectors that are orthogonal.

### Definition: Orthogonality

Two vectors are orthogonal if their dot product = 0, and we write **u** ⊥ **v**. If additionally ||**u**|| = ||**v**|| = 1 (both are unit vectors), then we call them orthonormal vectors, then such a pair orthonormal.

**The 0-vector is orthogonal to every vector in the vector space.**

Orthogonality is the generalization of the concept of perpendicularity. To tell two vectors are at 90° we no longer have to consider the actual vectors, we just have to compute their inner product.

For example:
- $x = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ and $y = \begin{pmatrix} -4 \\ 2 \end{pmatrix}$
- $\langle x, y \rangle = x^T y = 1(-4) + 2(2) = 0$

We express **u** = $\langle u_1, u_2 \rangle$ - linearly.

So **x** ⊥ **y** and ||**x**|| = $\sqrt{5}$, and they are not orthonormal but orthogonal.

**Vectors that are orthogonal with respect to an inner product do not have to be orthogonal!**

A set of n-dimensional vectors is just an n×1 matrix, or (n - 1) rows and 1 column vector.

### Definition: Orthogonal Matrix

If square matrix $A \in \mathbb{R}^{n×n}$ is orthogonal, matrix iff its columns are orthogonal to each other.

$$A^T A = I_n A^T A = I_n$$ (orthogonal $A^T = A^{-1}$ => inverse is transpose)

## Length and Angles

The length of a vector **x** is not changed when transforming it using an orthogonal matrix:

$$||A\vec{x}|| = \sqrt{(A\vec{x})^T(A\vec{x})} = \sqrt{\vec{x}^T A^T A \vec{x}} = \sqrt{\vec{x}^T \vec{x}} = ||\vec{x}||$$

The angle between two vectors **x**, **y** is preserved by their inner product, it also unchanged.

$$\cos(\theta) = \frac{(A\vec{x}) \cdot (A\vec{y})}{||A\vec{x}|| \cdot ||A\vec{y}||} = \frac{\vec{x}^T A^T A \vec{y}}{\sqrt{\vec{x}^T A^T A \vec{x}} \cdot \sqrt{\vec{y}^T A^T A \vec{y}}}$$

Since $A^T A = I$, this gives us the angle between $\vec{x}$ and $\vec{y}$.

### Orthogonal Matrices Properties

Orthogonal matrices preserve both angles and distances.

**Definition (Orthonormal Basis):** Consider an n-dimensional vector space V and a basis {**v**₁, ..., **vₙ**}.

If $\langle \vec{v}_i, \vec{v}_j \rangle = 0$ for $i \neq j$ (so they are pairwise orthogonal), then the basis is called an **orthogonal basis**.

The simplest basis for an English Vector Space is the **standard orthonormal basis**:

$$\mathbf{b}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \mathbf{b}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$ for 2D, or $\mathbf{b}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$ for 3D, etc.

Consider **u** = N-dimensional Vector Space V that is not an Orthonormal Basis space (UEVS). Then we use the orthogonal complement of **V** (= {**v**^⊥} = {**w**}). N-1 dimensional subspace of V and contains all vectors in V that are orthogonal to every vector in U, i.e., every vector $\vec{x} \in V^{\perp}$ satisfies:

$$U \cup U^{\perp} = \mathbb{R}^n$$ or equivalently **x** ⊥ **V** ∀**x**

$$\mathbf{x} = \sum_i \lambda_i \sum_j \mu_j \vec{w}_j, \vec{v}_i, \vec{w}_j \in \mathbb{R}$$

(By that it is a basis of U and {**w**₁, ..., **wₘ**} is a basis of V^⊥)

The orthogonal complement on the x-y plane is a subspace in 3D vector space. This means we need to find all vectors that are perpendicular to every vector in the plane space.

**Definition (Projection):** Let V be a subspace of $\mathbb{R}^n$ and $U \subset V$ a subspace of V. A linear mapping $\pi: V \to U$ is called a **projection** iff:

**Projection exhibits the property are simply:** $\pi_U \circ \pi_U = \pi_U$

The projection $\pi_U(x)$ is onto U's subspace or generally. Similarly, whether a matrix is the basis of a basis and equal to 1 or 0, or if span 1 or -1/2 or equal.

In 3-space, we illustrate the constant $\lambda$. The projection on the U, and the projection points to between any 2 in 3D space.

## Projection in Detail

Finding the projection going: $(\lambda u)$ & $\text{span}(\lambda u) \to \lambda u$:

- We use $\lambda$ as a parameter. We look at $u$ as orthogonal subspace.
- If $||u_1|| u_1 = 0.5||u_1||$ $\implies$ $||\lambda u_1|| = |\lambda| \cdot ||u_1|| \cdot u_1^T u_1$

Our projection π of length $||\vec{u}||$ over the length of $||\vec{u}||$ => it is the coordinate of $\vec{u}$ on a perpendicular to that one.

Using the idea of the inner product:

$$||\pi_U(x)|| = \frac{108}{143} ||x|| = |\cos \theta| \cdot ||x|| \cdot \frac{108}{143} = |\cos \theta| \cdot 143$$

We are $\lambda u$ for non-zero $\vec{u}$

**Finding the projection matrix $\pi$:** This is a linear basis on the definition of linear defined:

$$\pi_U(\lambda u) = \lambda u \rightarrow u \cdot \lambda \vec{u} \cdot \frac{\vec{u}}{\vec{u}^T\vec{u}} \cdot \frac{\vec{u}}{||\vec{u}||} \cdot \frac{\vec{u}}{||\vec{u}||^2}$$

We call this a symmetric relation in $\lambda u$, so $\pi_U \cdot \pi_{Suby}$

**The projection matrix $\pi_U$ projects everything onto the line through the origin with direction $\vec{u}$.**

## Example: Projection onto a Line

$$\vec{u} = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$$

$$\frac{\vec{u}\vec{u}^T}{\vec{u}^T\vec{u}} = \frac{1}{1^2 + 2^2 + 2^2} \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} \begin{pmatrix} 1 & 2 & 2 \end{pmatrix} = \frac{1}{9} \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}$$

**This is our projection onto the line (one eigenvalue is the unit).** The composition is perpendicular.

## Null Space vs Row Space vs Column Space

### Null Space and Row Space

- **Null space**: {**x** | Space}
- **Row Space**: {Column Space}

For a space **r** ⊥ **C** (Orthogonal **r**):

- **Nullspace**

### Orthogonal Vectors (Perpendiculars)

**When from a right triangle:**

$$\sum_k (\text{each column}) = 0$$

**Perpendicular test:**

$$||v||^2 + ||u||^2 = ||u+v||^2$$ only true when $x_k y_k = 0$ (right through!) Relations:

$$\sum^n_{k=1} (x_k)(y_k) = x^T y$$ (angle property by Orthogonal in right angle)

### Dot product of Orthogonal vectors = 0

Suppose $S$ is orthogonal to subspace **T**; means: every vector in **S** is perpendicular to every vector in **T**:

Row Space is orthogonal to the **N**(A) Nullspace.

$$A\vec{x} = 0$$

Now: $$A = \begin{bmatrix} \text{row}_1(A) \\ \vdots \\ \text{row}_m(A) \end{bmatrix}, A\vec{x} = 0 \implies \begin{cases} (\text{row}_1A) \cdot \vec{x} = 0 \\ \vdots \\ (\text{row}_m A) \cdot \vec{x} = 0 \end{cases}$$

Only the non-zero rows are orthogonal components in $\mathbb{R}^n$.

Note: $A\vec{x} = 0$ also then we know that every non-zero row some column like $\lambda \in \mathbb{R}$. Then from $(AA^T)^T \vec{x} = AA^T \vec{x}$

Then more columns than question: $A^T \vec{b}$ like $3 \times 5$ and $A^T A \vec{x} = A^T \vec{b}$

$$A = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 10 \end{bmatrix}$$ and x = $\begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$

Note: $AA^T$ also has same form more column like Gaussian elimination: $A^T A$ is $5 \times 5$ Rank = 3 => $5-3=2$

## $A^T A$ is Invertible

$A^T A$ is invertible exactly if A has independent columns.

$$P = \frac{A(A^T A)^{-1}A^T}{A^T \vec{b}}, \text{find } \vec{x} = A^{-1}\vec{b}$$

**Making?**

$$P = \frac{A}{A^T \vec{b}}$$

$$\text{col space}(A) = \text{line through } \text{col}(A^T) = \{ P \vec{b}, P^T \vec{b} \}$$

Take approximate. Square

Why? Because $A\vec{x} = \vec{b}$ has a solution.

**Solve $A\vec{x} = \vec{b}$ for projection of $\vec{b}$ onto colspace.**

Thus: do we project $\vec{b}$ onto the plane?

**Projection $\rho = A\vec{x}_1, e_2, \vec{e}_1 = A\vec{x}$**

**P: for Proj b ⊥ the is perpendicular to the plane**

$$A_1^T(\vec{b} - A\vec{x}) = 0, A_2^T(\vec{b} - A\vec{x}) = 0$$

$$A^T(\vec{b} - A\vec{x}) = 0 \in N(A^T)$$

E is col-space (A): $\vec{b} = A\vec{x} + \vec{b} \in CA^T \implies AA^T = A^T \vec{b}$$

$$A(A^T A)^{-1}A^T \vec{b} = \lambda I \cdot A_1 + A_3(A^T) \implies \text{square matrix: It shouldn't have any inverse}$$

$$A^T A, A^T \vec{b}$$

**Least Square fitting baseline:**

$$C(1)v_1(2, 3, v_1, 3, 4, x)$$

$$\text{in } \mathbb{R}^n$$

$$A^T A = A^T \vec{b}$$ is best solution

**May solve:** $P = A(A^TA)^{-1}A^T$ If $\vec{b}$ is close to the $P\vec{b}$ set of columns of vectors.

$$P = \begin{bmatrix} (A^T A)^{-1}A^T \\ \vdots \end{bmatrix}$$ even as $P\vec{b} = b$

## Colspace, Nullspace & Transformations

$$\text{Find } \vec{b} = \begin{pmatrix} 1 \\ 3 \\ 4 \end{pmatrix}, A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{pmatrix}$$

**Most agreeable to $A\vec{x}$**

$$p = \frac{A(A^T A)^{-1}A^T}{\text{transformations}}$$

$$A(A^T)$$ e-error vector

$$N(A^T) = \text{e-value}$$

**Example:**

$$\text{Find } \vec{b} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, \text{ exact equation is } AA^T$$

$$\begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix}$$ $\implies$

$$E^{-1} = \begin{pmatrix} 5 & -3 \\ -3 & 3 \end{pmatrix} \cdot \frac{1}{6}$$

**Normal equation:**

$$A^T A\vec{x} = A^T\vec{b}$$

$$\begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix} \begin{pmatrix} \hat{x}_1 \\ \hat{x}_2 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$$

**Best line:** $y = \frac{2}{3}x + \frac{5}{6}$

$$\text{error-vector: } E = b - A\hat{x} = \begin{pmatrix} \frac{1}{6} \\ -\frac{1}{6} \\ 0 \end{pmatrix}$$

**Then:** $||E||^2 = \left(\frac{1}{6}\right)^2 + \left(-\frac{1}{6}\right)^2 + 0^2 \cdot p = E = \frac{1}{18}$

**If A has independent columns, then $A^T A$ is invertible.** To prove: x = normal If:

$$A^TAx=0 \implies x^TA^TAx=0 \implies (Ax)^T(Ax) \implies Ax=0$$

Therefore there independent solve => $x = 0$

**Column definitely independent if there's perpendicular non-vectors.**

### Orthogonal Vectors

Orthogonal vectors: $\vec{q}_1 \vec{q}_2^T = \begin{bmatrix} 0 & -6 & 0 \\ -4 & 0 & 0 \end{bmatrix}$

**Orthogonal basis:** $\vec{q}_1, \vec{q}_2$

**Orthogonal matrix:** 0 Square matrix

$$Q = \begin{bmatrix} \vec{q}_1 & -\vec{q}_2 \end{bmatrix} \implies Q^TQ = \begin{bmatrix} 0 & -1 \\ 0 & -2 \end{bmatrix} \begin{bmatrix} 0 & 0 \\ -1 & -2 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 5 \end{bmatrix}$$

So it works. Q matrix. Q orthonor. Square to be considered as orthogonal matrix. $QQ^T = I$ when $Q$ is $q \times Q \text{ (Square)}$

**Examples:**

$$I = Q = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$

$$Q = \begin{bmatrix} \frac{4}{10} & -\frac{6}{10} & 0 \\ \frac{6}{10} & \frac{4}{10} & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

## Projection with Orthonormal Columns

If Q has orthonormal columns (forget only its column space):

$$P = Q(Q^TQ)^{-1}Q^T = Q \cdot I \cdot Q^T = Q \cdot Q^T = I = Q \text{ is Square}$$

**Identity**

$$LQCQ(Q^T) = QQ^T$$

$$A^T Qx = Q^Tb \implies Ix = Q^Tb \implies x = Q^Tb$$

$$x = Q^Tb$$

**Gram-Schmidt:** Algorithm to get from any-known or S to orthogonal vectors A to B
(dependent vectors A&B)

Orthonormal $q_1, q_2$:

$$q_1 = \frac{A}{||A||}, q_2 = \frac{B - (q_1 \cdot B)q_1}{||B - (q_1 \cdot B)q_1||}, A^TB \cdot q_1 = \frac{A^T B}{||A||} \cdot \frac{A^T}{||A||^2} = C \cdot A^T$$

$$B = \frac{1}{||A||} \begin{pmatrix} B_1 \\ B_2 \end{pmatrix} - \frac{A}{||A||} = \frac{1}{3} \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} -1 \\ 1 \end{pmatrix}$$

Then: $|q(A)| = ca(Q)$

$$Q = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{-1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}$$

$$A = QR \implies \text{co-express of Gram-Schmidt} \; [x_1 \; x_2 \; \cdots x_n] = \begin{bmatrix} q_1 & q_2 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} R \\ R_i \end{bmatrix}$$

$$A^T A = Q \cdot R$$

(Rank of $A^T A$ = Rank of A)

**Example:**

$$Q = \begin{bmatrix} 1 & -2 & 2 \\ 0 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix}$$

**Orthogonal but n't**

$$Q = \begin{pmatrix} \frac{1}{3} \\ \frac{2}{3} \\ \frac{2}{3} \end{pmatrix}$$

$$P = Q(Q^TQ)^{-1}Q^T = QQ^T = I = Q \text{ is Square}$$

**Identity**

$$LQCQ(Q^T) = QQ^T$$

$$A^T Qx = Q^Tb \implies x = Q^Tb$$

$$A^TQx = Q^Tb \implies x = Q^Tb \implies Q^Tb = QQ^Tb$$

$$S = Q\vec{b}_n$$

**Gram-Schmidt:** Algorithm to go to from any vectors A&B to orthogonal vector A&B by orthogonalize $q_1, q_2$:

$$q_1 = \frac{A}{||A||}, AB\cdot q_2 = \frac{||A||}{||B||} \cdot q_1 = \frac{A^TB}{||A||} \cdot \frac{A}{||A||} = \frac{A^TB}{||A||^2} \cdot A = CAA^T$$

then: $\frac{1}{3} \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$, $B= \begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix}$, then $A = \frac{1}{3} \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$, $ca(A) = ca(Q)$

$$Q = \begin{bmatrix} \frac{1}{3} & \frac{-2}{3\sqrt{2}} \\ \frac{2}{3} & \frac{1}{3\sqrt{2}} \\ \frac{2}{3} & \frac{1}{3\sqrt{2}} \end{bmatrix}$$

$$A = QR$$

e.g. co-express (can-shift it $(\tfrac{1}{3}a)^T \cdot (\tfrac{1}{3}a)^T$

$$A = \begin{bmatrix} q_1 & q_2 \\ -1 & e_2 \end{bmatrix}$$ ideal square w/line (essentially of that bot)

We're going in line of just bot

$$b = (CA = \tfrac{1}{3})$$ (can shift $(CA)(\tfrac{1}{3}a)^T$ (can start))

$$C = 3$$

$$\text{Char-Vektor: } E = \begin{bmatrix} \frac{6}{18} \\ \frac{16}{18} \\ \frac{14}{18} \end{bmatrix}, p = E = \frac{14}{18}$$
