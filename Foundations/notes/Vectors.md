# Vectors

*Source: Linear Algebra - Ch 1 Gilbert Strang & Mathematics for Machine Learning*

## The Geometry of Linear Equations

### Linear Equations Terminology

In a linear equation, n unknowns:
- **Goal**: Determine n row picture
  - x = column vector
  - b = column vector (right-hand side - algebra form)

### Row Picture vs Column Picture

**Row Picture**
- Plot each equation in n-dimensional space
- Each equation defines a line (2D), plane (3D), or hyperplane (higher dimensions)

**Column Picture**
- Express system as linear combination of column vectors
- Goal: Find the right linear combination
- In the form: $x_1 \cdot \text{col}_1 + x_2 \cdot \text{col}_2 + ... = b$
- You take $(a_1, a_2, ..., a_n)$ and find $x_1$

### Example System

```
2x - y = 0         [2  -1] [x]   [0]
-x + 2y + z = 1    [-1  2] [y] = [1]
3y + 4z = 4        [0   3] [z]   [4]
                      A      x     b
```

**Each equation is a linear combination of unknowns.**

Can be rewritten: Take each vector, show linear combination through addition.

```
   [2]    [-1]    [0]    [0]
x· [1] + y·[2] + z·[1] = [1]
   [0]    [3]    [4]    [4]
```

**Linear Combination:**
x = 0, y = 1, z = 1

### Matrix Examples

Example showing matrix operations:

```
  [3]    [-1]    [2]    [0]
x·[0] + y·[3] + z·[4] + [1]

For this matrix A, Y21 = ? matrix man
When can the three column vectors span space?
→ If all vectors lie in the same plane (i.e., are coplanar)
```

**Some Matrix A:**
- Same vector, x = b
- $Ax = b$

```
[2  5]
[1  3]
```

**Row Example:**
Then check:
- Column A: $[2a, 1] + x = [5, 3]$
- Then example = product of 2 matrices
- Can't Find A or B for every b? (Invertible matrices)

**Result (Minimal):**
```
      [1]   [7]
[2 3] · [1] = [5]
```

---

## Mathematics for Machine Learning (Ch 2)

### Linear Algebra - the study of how vectors interact with each other in vector space

In general, **vectors are objects that can be added together or multiplied by scalars** to produce another object of the same kind.

**By vector (or more generally), you can define:**

1) **Geometric Vector** - Directed segments ∈ R² whose V is in higher dimensional (Mn,n = the n × n matrix set of numbers)

2) **Algebraic** - Can be added together regularly in a nice alignment (-graph), can be multiplied by a scalar (is fine with +/-)

3) **Data Space** - Represent as series of numbers, connected together, existing in a data space (not real ℝⁿ, just conceptual space for data)

4) **Elements of ℝⁿ** (z = real # basis of a rel number) ℝⁿ is one subset the polygraph
   - $ℝ² = [-3, 6]ᵀ ∈ ℝ²$ which is a real number of 2 real numbers and it contains a coordinate

**Adding horizontal and vertical must result in total vector A+B**

**Multiplying a ℝⁿ by Scalar ℝ→ℝ results in → total vector λx+B**

**Vector ∈ ℝⁿ**: Connect vectors to an element (red arrow) in a concept

---

## The Idea of Closure

What is the largest linear result from elongation?

By in canonical (linear), Sam Will believe: Can I take this for every b? (Analogous Vector Manifold)

```
      Vector Manifold ──→ Linear Algorithmic
Canonical Metric          (result in
Vector Span               Spork)
Scalar Multiplication ──→ Value/
Vector Addition           Linear Subbed testing
                         under Algebra
                             ↓
                         Scalar
                          Option
```

### Geometric Interpretation in Margin Space (Linear)

**The visual (region) representation of Vectors:** By graphing, we can see how collision: Two Vectors Together follow the diagonal trajectory, or alternately, We can see that adding from diagonal at + cab 1 walk only in the same as adding from together and then diagonal. With calculus, we see the length of the vector under calculus Read the position

### How are Scalars Different than Vectors?

**A Scalar is a non-scalar or Rose. It has no direction or Tangent length.** A Scalar has both direction and magnitude. A Vector can be both direction or Tangent or time. We can define an operation on which to define an operation. When we want to stand on the path length to as part.

**If x,y coordinates [?]** - **Think of Vector Coordinates or Scalars of 7 only**
**B-pair coordinates [?]** - 7 in 2 are the basis vector of the n-Coordinate System
→A vector Basis of Vector Space

**A·B·Y·B·C** = Inner Combination of 7 and B. Going Vector can be apart of dim base units start
Thickness are what contain

**Auto 3D Vectors is a linear Combination of 7 and B**

---

## Span

**All possible vectors you can reach with linear combinations**

**Two 3D vectors span the entire 3D plane**
