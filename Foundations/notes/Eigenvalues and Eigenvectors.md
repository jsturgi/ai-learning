# Eigenvalues and Eigenvectors

## Definition and Introduction

**Linear Algebra (MIT 18.06) Lecture 21 - Eigenvalues & Eigenvectors**

### Basic Definition

Let $CA - \lambda I] = 0$, where $Ax$ should be $x \cdot$ Eigenvectors.

What are the $x$'s (eigenvectors) and the $\lambda$'s (eigenvalues) for a given matrix?

- $Ax = \lambda x$ (if $A$ is $n \times n$, then there are $n$ eigenvalues)
- $Ax = \lambda x$ is equivalent to:
  - $Ax - \lambda x = 0$
  - $Ax - \lambda I x = 0$
  - $(A - \lambda I)x = 0$

**Eigenvalue: 1.0**

#### Necessary Condition for Eigenvectors

$A$ is of the same size as $x$, an eigenvector. Therefore, $Ax = A \cdot x \neq 0$.

Assuming $x$ is in the plane where the eigenvector $(Ax = \lambda x)$ lies, any vector perpendicular to the plane $(Ax - \lambda I) = 0$ is an eigenvalue. Eigenvalues can be $0$.

### How to Solve $Ax = Ax$ with 2 unknowns

**Known:** $(A - \lambda I)x = 0$
**Solving for $\lambda$:**

$Ax = \lambda x$ implies $(A-\lambda I)x = Ax - \lambda Ix = 0$

$Ax = Ax$ is the eigenvalue equation, not $(A-\lambda I)x = Ax - \lambda Ix = 0$ (this one is confusing in its phrasing)

The eigenvalue equation: $Ax = \lambda x$, where $\lambda$ is an eigenvalue.

$B = Ax \cdot (A-\lambda I) = B$ has an eigenvalue $\lambda$ with respect to the identity matrix $I$ to the left.

**Example:** $Q = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ has $\lambda = \pm 1$ for $Qx = \lambda x$

**Eigenvalues:**

$Q - \lambda I = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} -\lambda & 1 \\ 1 & -\lambda \end{bmatrix}$

$\det(Q - \lambda I) = \begin{vmatrix} -\lambda & 1 \\ 1 & -\lambda \end{vmatrix} = \lambda^2 - 1 = 0, \quad \lambda = \pm 1$

### Properties of Eigenvalues and Eigenvectors

$(n \times n)$ matrices will have $n$ eigenvalues. The sum of the eigenvalues $(\sum \lambda_i)$ is equal to the diagonal entries of $A$: $\sum a_{ii}$.

$A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}, \quad \det(A - \lambda I) = \begin{vmatrix} 3-\lambda & 1 \\ 1 & 3-\lambda \end{vmatrix}$

$= (3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8$

$D = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$

$= \frac{-(−6) \pm \sqrt{36 - 32}}{2} = \frac{6 \pm 2}{2} = \{4, 2\}$

$A + I = \begin{bmatrix} 4 & 1 \\ 1 & 4 \end{bmatrix} x = \begin{bmatrix} ? \\ ? \end{bmatrix}$

$A - 2I = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} x = \begin{bmatrix} ? \\ ? \end{bmatrix}$

---

## Page 2: Advanced Properties and Theorems

$A = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}$ Eigenvalues: $\det(A-\lambda I) = (3-\lambda)(3-\lambda) - 1 = 0$, so $\lambda = 4, 2$

If $n \times n$ is a triangular, the eigenvalues are on the diagonal.

$(A - \lambda I)x = \begin{bmatrix} 3-\lambda & 1 \\ 1 & 3-\lambda \end{bmatrix} x = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ [one vector has both $x_1$, $x_2$]

Only 1 eigenvector, $n$ eigenvalues

**Note:** Let $A \in \mathbb{R}^{n \times n}$ be a square matrix. Then, $x \in \mathbb{R}^n$ is an eigenvector of $A$ and $\lambda \in \mathbb{R}$ (or $\lambda \in \mathbb{C}$) is the eigenvalue equation.

The following statements are equivalent:

1. $x$ is an eigenvector of $A$ with $\lambda = \lambda_0$
2. $x$ is in $\ker(A - \lambda_0 I)$ where $A - \lambda_0 I$ is not invertible

**Definition:** $E(\lambda_0$ vers and $E(\lambda_0 \neq 0)$ has greater that graph the same direction (are collin extended). Two vectors are the eigenvectors correspond **if** it's also an eigenspace.

If $x$ is an eigenvector of $A$ mapping with respect to $\lambda$, then terms of $A(kx)$ yields that $k \cdot x$ is an eigenvector of $A$ with respect to $A(kx) = k(Ax)$. One must have $k \neq 0$ because relative to the null eigenvector.

**Theorem:** $x \in \mathbb{R}^n$ is an eigenvector of $A \in \mathbb{R}^{n \times n}$ and $\lambda$ is a root of the characteristic polynomial of $(A,B,C)$

**Definition:** (Algebraic Multiplicity) Let $\lambda_0$ be an eigenvalue of $A \in \mathbb{R}^{n \times n}$. The algebraic multiplicity of $\lambda_0$, $m_A(\lambda_0)$, is the number of times $\lambda_0$ appears as a root in the characteristic equation.

$\det(A - \lambda I) = (-1)^n (\lambda - \lambda_1)(\lambda - \lambda_2) \cdots (\lambda - \lambda_n)$ (no real eigenvalues can be a distinct eigenvalue $\lambda_0$ less complex in distinct form.)

**Note:** The characteristic polynomial has the same diagonal components. $m_A(\lambda) = m_A(\lambda)$ for any diagonal $A$

**Theorem:** $\det(A)$ has the characteristic polynomial $(-1)^n \det(\lambda I - A)$. What has no eigenvector $\lambda_0$ (without a single eigenvector in certain root intuitively, where is in the same direction (also known), even.

**Proof:** Eigenvalues are determined based on eigenvector variables with $\lambda$ $(-1)^n$ roots of $\det(\lambda I - A)$

- The eigenvector $\sum_{i=1}^n \lambda_i = \text{tr}(A) = \sum_{i=1}^n a_{ii}$ for $i = \lambda I$ have $a_{ii} = \lambda I$ or $a_{ii} = \lambda I + 2$
- Signature, another theorem features features. Among three factors real properties
- Eigenvectors are normal under forms (base).

---

## Page 3: Eigenvalue Analysis and Theorems

$A = \begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}$, given $\det(A-\lambda I) = \det \begin{bmatrix} \lambda - \lambda & 1 \\ 0 & \lambda - \lambda \end{bmatrix} = (\lambda - \lambda)(\lambda - \lambda) = 0$

$\lambda = (\lambda - \lambda)^2 = (2-\lambda)(3-\lambda)$, so $\lambda = 2$, $\det \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 2x_1 + x_2 \\ 0 + 2x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$, so $x_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \to \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} = 2 \times \begin{bmatrix} 1 \\ 0 \end{bmatrix}$, so $\lambda = 2$ for $x = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$

**Definition (Eigenvalues uniquely):** Let $\lambda_0$ be an eigenvector of a square matrix $A$. Then the number of linearly independent eigenvectors corresponding to $\lambda_0$ is the nullspace dimension of $(A - \lambda_0 I)$, given by $\text{dim}(\mathcal{N}(A - \lambda_0 I))$. This is known as the **geometric multiplicity** of $\lambda_0$.

Let $\text{dim}(\mathcal{N}(A-\lambda_0 I)) = $ the eigenspace of $\lambda_0$.

### Key Theorems

**Theorem 14.10:** The eigenvectors of a matrix $A \in \mathbb{R}^{n \times n}$ and a distinct eigenvector $\lambda_0$ less complex (especially conjugated).

**Dimensions of eigenvector space** is bound by each eigenvector space:

**Theorem 14.11 (Spectral Theorem):** If $A \in \mathbb{R}^{n \times n}$ is symmetric, then exists an orthonormal basis of the eigenvectors (often seen $\perp$ orthonorm) of eigenvalues of $A$, in each eigenvector of $\mathbb{R}^n$.

**Theorem 14.12:** The algebraic of an matrix $A \in \mathbb{R}^{n \times n}$ is the value of its eigenvalues.

$\det(A) = \prod_{i=1}^n \lambda_i$, where $\lambda_1, \lambda_2, \ldots, \lambda_n \in \mathbb{R}$ are exactly repeated eigenvalues of $A$.

**Theorem 14.13:** The trace of $A$ in matrix $A \in \mathbb{R}^{n \times n}$ is the sum of all its eigenvalues.

$\text{tr}(A) = \sum_{i=1}^n a_{ii}$, where $\lambda_i \in \mathbb{R}$ are possibly repeated eigenvalues of $A$.
