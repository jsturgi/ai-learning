# Eigenfaces for Recognition

## Introduction

**Decompose** face images into a small set of characteristic feature images called "eigenfaces". Recognition is performed by projecting a new image into the subspace spanned by the eigenfaces ("face space") and then classifying the face by comparing its position in face space with the positions of known individuals.

## The Eigenface Approach

The goal is to **extract relevant information** in face images, encode as efficiently as possible, and compare one face image with a database of models encoded similarly.

⇒ Confine the variation in a collection of face images to a **lower dimensional face space**.

Mathematically, we wish to find the **principal components** of the distribution of faces, or the **eigenvectors** of the covariance matrix of the set of face images, treating an image as a point (or vector) in a very high-dimensional space.

These eigenvectors can be thought of as a set of features that together categorize the variation between face images. There eigenfaces can be thought of as a set of features - or a PCA of the variations between faces.

Each individual face can be represented as a **linear combination** of the eigenfaces. The best M eigenfaces span the face space.

## Approach to Facial Recognition

1) Acquire an initial set of face images (**training set**). Keeping only the M images that correspond to the highest eigenvalues. These M images define the face space.

2) Calculate the eigenfaces for the training set, because a given face space expressed, the eigenfaces can be **updated or recalculated**.

3) Calculate the corresponding distribution in M-dimensional weight space for each known individual by projecting their face images onto the face space.

## Approach to Recognize New Face Images

1) Calculate the set of weights based on the input image and the M eigenvectors by projecting the input image onto each of the eigenfaces.

2) Determine if the image is a face by checking to see if the image is sufficiently close to the "face space".

3) If it is a face, classify the weight pattern as either a known person or as unknown.

4) (Optional) Update the eigenfaces and/or weight patterns and incorporate into the known faces.

5) (Optional) If the same unknown face is seen several times, calculate its characteristic weight pattern and incorporate into the known faces.

## Calculating Eigenfaces

⇒ By a theorem that best accounts for the distribution of face images within the entire image space.

(If the number of data points in the image space is less than the dimension of the space (M<N), will be only M-1, rather than N² meaningful eigenfaces)

Eigenvectors: λₖ = (1/M)Σⱼ(Γⱼϕₖ)² where Uₖ,Uₖ = δₖₗ
The eigenvector is (variance > 0 if λₖ > ε
λₖ: Eigenvalue, δₖₗ: otherwise λₖ = Eigenvalue

The associated eigenvalue allow us to rank the eigenvectors according to their usefulness in characterizing the variation among the images.

## Using Eigenfaces to Classify a Face Image

The eigenface images calculate from the eigenvalue problem. Keep an arbitrary set with which to describe face images. The eigenfaces shown in that subspace of the original N² image space.

The M† significant eigenvectors of the L matrix are chosen as those with the largest associated eigenvalues.

Eigenvalues:
- Face image Γ = orthonormal
A new face image is projected onto "face space" by a simple operation: Wᵤ = Uᵏᵀ(Γ-Ψ).

There are four possibilities for an input image and its pattern vector:

1) Near face space and near a face class  2) Near a face space and not near a known face class  3) Distant from face space and near a face class
4) Distant from face space and not near a known face class

---

## Summary of Eigenface Recognition Procedure

1) Collect a large, characteristic images of the known individuals
2) Calculate the eigenfaces U, find its eigenvectors and eigenvalues, and choose the M† eigenvectors with the highest-associated eigenvalues.
3) Compute the mean vector μ, by averaging the eigenface pattern vectors (calculate from the original face images of the individual)
4) For each known individual, calculate the class vector μ. Representing the eigenface pattern vectors to each class, and the distance to face space.
5) For each new face image to be identified, calculate its pattern vector, the distance to each class, and the distance to the original set of face images, and the eigenfaces may be recalculated.
6) If the new image is classified as an unknown individual, that image maybe added to the original set of face images, and the eigenfaces may be recalculated.

The concept of **face space** allows the ability to learn and subsequently recognize new faces in an unsupervised manner.
