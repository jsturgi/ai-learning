# Day 1.5 11/4/2025
## Roadmap Version 1.3

## What I learned today:
- I learned how to write a dockerfile and a docker-compose.yaml file.  I also configured a custom container image from scratch! I've just pulled existing images in the past.
- I got a refresher on vectors, their properties, and their operations.  Its been a few years since I've used anything Linear Algebra related so it was a good refresher.
- I implemented a vector class in the jupyter notebook.  Unfortunately, my original plan was generated with full implementation and I saw it as I was reading the task.  I've since updated my learning agent's rules and updated all my daily plans so this won't happen again.

## What I built Today
- Vector class from scratch**
- a dev container based on python 3.11 with datascience. libraries installed (pandas, matplot, numpy, scikit, etc)
- a dockerfile and docker-compose file
- a callable graph function using matplotlib

## Implementation Details
- used magic methods in my vector class
- used list comprehension** in my dot product and vector addition solutions.
- used base vector methods to implement normalization, angle between, and projection

## Challenges I Faced
- Initally, the roadmap was generated using a virtual environment.  I decided it wasn't worth the hassle and considering that most professionals use containers, it would be a good time to start getting familiar with docker. 
- As mentioned previously, the vector solution was generated with the daily roadmaps. I tried to come up with my own solution but after seeing the list comprehension solution, it was difficult to come up with a solution that wasn't just expanding the list comprehension into multiple lines so I just accepted it for today and fixed the issue moving forward.
- There were multiple rules and refactors I needed to run to get to my current version (1.3). The rules I added were - no implementation provided ever (empty functions with docstrings is okay), academic sources. must be referenced if learning a mathematical/theory topic (ie the vector lecture I watched today), and this wasn't a problem with the initial version, but I added an extra practice file for each week.
- I struggled with Vector Projection, but I worked through it with some assistance from Claude on the math, and was able to finish my implementation and understand it!

## Insights
-  The way vector multiplication was described in the MIT lecture made sense - its always been something that has confused me.  
- There was a vector mindmap in the vector section from the ml math textbook that helped me remember how the different aspects of linear algebra are connected.
- It's been so long since I've used a list comprehension that it didn't come to mind until I saw it and realized what it was.

## Math Intuition Questions
1. What does it mean when the dot product of tow vectors is zero?
    It means the vectors are perpendicular (orthogonal)
2. What does a negative dot product tell you?
    vectors point in somewhat opposite directions with no perpendicularity. positive dot - vectors point in same direction, 0 - perpendicular, negative dot - opposite dir
3. Why is vector magnitude always non-negative?
    You can't have a negative length. It would simply not exist once magnitude = 0.
4. What happens to the magnitude as you scale a vector?
    The vector scales by whatever value the scalar is.  Scalars affect the magnitude, but not the direction of the vector.

## Time Spent:
6 hours

## Mood:
Feeling excited and motivated!

## End of Day Checklist

- [x] Docker environment set up successfully
- [x] Git repo created and pushed to GitHub with .gitignore
- [x] Studied primary academic source (MIT 18.06 Lecture 1 OR "Math for ML" Chapter 2.1)
- [x] Watched supplemental video (3Blue1Brown) for visual intuition
- [x] Implemented Vector class with all basic operations
- [x] Created vector addition visualization
- [x] Extended Vector class with normalize, angle, projection
- [x] Journal entry written with reflections
- [x] Can explain: "What is a vector?" in plain English to a non-technical person

# Day 2 11/5/2025
## Roadmap Version 1.4
Added Multiple Language implementations (optional)
## Time Spent
- Theory block: 6:30
- Implementation: 2:15

# Day 3 11/7/2025
## Roadmap Version 1.4
## Time Spent
- Theory: 1:30
## Foundational Math Study Day
- 3:00 - determinants/eigenvalues
- 4:00 - orthogonality
# Day 4 11/8/2025
## Foundational Math Study Day 2
- 1:00 - Determinants
- 2:00 - Orthogonality
## Schedule Outlier
- Called into work 2 hours early, cutting into study time.

# Day 5-6 11/9-10/2025
- Very hectic weekend. Not able to get much done. Worked 32 hours over a 48 period Saturday night - Monday morning.  1 hour of sleep between a 12 hour close into a 12 hour open.  Going to get back on track.
Theory:
Determinants: :50
SVA: 1:20
Total Time: 2:10
# Day 7 11/11
Theory: 
SVA: 2:45
Imp:
MatMult: 1:30

Total: 4:15

# Week 1 Recap:
## Total Time Spent: 
32:15
## Progress
    - Finished Day 1.
    - Halfway through Day 2, realized my foundational math knowledge was not sufficient.
    - Studied Linear Algebra extensively. Topics Covered: SVA, Determinants, Eigenvectors/Values, Orthogonality, Matrices, Vectors, Vector Spaces, Basis/Subspaces
## Implemented:
    - 2D Matrix and Vector Class
    - Matrix Transformation Visualizer
## Breakthroughs:
    - Finally figured out how Matrix Multiplication works
    - Was able to start piecing together how the different aspects of Linear Algebra work together.
    - Learned about how Python order of operations with custom classes works (rmult)
    - Refamiliarized myself with Python List manipulation and iteration
## Challenges:
    - I struggled with Implementation because I didn't understand the math
    - Time management was a struggle this week due to working 54 hours at work + finding time for the gym. (I go 6x a week).

# Day 2 - Finished - [11/12/25]

## What I Learned Today
- Linear combination: any vector = a*v₁ + b*v₂
- Matrices describe where basis vectors land
- Matrix-vector multiplication = applying transformation
- Determinant measures area scaling

## What I Built Today
- Matrix class from scratch
- Matrix-vector multiplication
- Transformation visualizer showing original vs transformed space
- Rotation, scaling, and shear matrices

## Geometric Insights
- Matrices aren't numbers - they're transformations!
- Columns of matrix = where basis vectors go
- Grid visualization makes transformations concrete
- Determinant = 0 means space collapses to lower dimension

## Challenges & Solutions
- During my theory block, I was struggling with how to do mat mult, but I eventually got it figured out.
- I struggled connecting the geometric meaning of how matrix multiplication works with how it is 
computed by hand.  This made it a little difficult to implement, but I was able to get it to work.
- I was struggling with both implementation and the theory, so I built a study agent who will help me 
understand difficult concepts without telling me the solution to my problem.

## Aha Moments
- Mat Mult clicked when I was working through the Math for Machine Learning Chapter.  
- It took a lot of work with my study agent, but I was able to connect the geometric meaning
of matrix multiplication to transformations, and was able to implement it.


## Tomorrow's Goal
- Implement PCA (Principal Component Analysis)
- Apply eigenvalues and eigenvectors
- Image compression project

## Questions
- How do transformations work in 3D?
In 3D, the rotation is applied based off a fixed axis, while in 2D, it is simply applied to the entire matrix. The axis that the transformation is based off of will stay the same while the other two axis are transformed.  Consider the Earth spinning: 
The y axis that we spin around stays the same, while the transformation is applied on our x and z axis. The scale of these transformations are felt more the further away you are from the zero point of the axis - if you're standing on the north pole, you'll barely move. If you're standing on the equator, you'll travel ~40,000 km per day! This helps us visualize how rotation affects points differently based on distance: points closer to the axis move through smaller circles, while points farther away move through larger circles, even though the angle of rotation is the same everywhere.  
Scaling is similar in 3D to 2D. WWe are still stretching and compressing based off the transformation applied. But now, wwe have a 3rd scaling factor, allowing us to stretch/compress in a 3rd direction. Instead of just stretching by the x or compressing by the y, we can now elongate based off the z axis.  The key insight here is that matrices are still a representation of where the basis vectors land, we're just working in a 3 dimensional space instead of 2 dimensional.
- What are eigenvalues geometrically?
An eigenvector is a vector that stays on its own line (same or opposite direction) when a transformation is applied. The eigenvalue tells you how much it's scaled - positive means same direction, negative means flipped.
- When is a transformation reversible?
A transformation is reversible when the determinant of the transformation is nonzero. This is because when the determinant is 0, the transformation will result in going down a dimension, meaning we lose the information required to describe the original matrix in its original dimensional space.  When the determinant is nonzero, we retain the information required to revert to its original form. If we scale by (2,3) we can still return to our original state by scaling (1/2,1/3).

## Time: 14.5 hours
```

---

## End of Day Checklist

- [x] Studied primary academic sources (MIT 18.06 Lectures 2-3 OR "Math for ML" Ch 2.2-2.5)
- [x] Watched supplemental videos (3Blue1Brown Ep 2, 4) for visual intuition
- [x] Implemented Matrix class with multiply_vector
- [x] Created transformation visualizer
- [x] Visualized at least 4 different transformations (rotation, scaling, shear, custom)
- [x] Understood core concept: matrices = "where basis vectors land"
- [x] Can explain matrix-vector multiplication geometrically
- [x] Implemented matrix multiplication (composition) and tested non-commutativity
- [x] Journal entry completed with geometric insights

