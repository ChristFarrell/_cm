## What does "linear" mean in linear algebra? Why is it called "algebra"?
Linear means the relationship follows addition and scalar multiplication rules:
- $f(x + y) = f(x) + f(y)$
- $f(cx) = cf(x)$

linear can also show a constant proportional relationship between two variables. It is called algebra because it deals with symbols and equations.

## What is "space" in mathematics? Why is "vector space" called space?
A space in general is a set that has a certain additional structure, such as a vector space, a metric space, or a topological space. A vector space is called a "space" because it refers to the set of objects (vectors) that satisfy the axioms of vector addition and scalar multiplication, which means that these operations do not change the type of the objects, and the results remain within the "space".

## What is the relationship between matrices and vectors? What does a matrix represent?
AThe relationship is that a vector is a matrix with only one row (row vector) or one column (column vector). Matrices represent an arrangement of numbers or other elements organized in rows and columns and can be used to represent a wide variety of things, such as systems of linear equations, linear transformations, or multidimensional data.

## How can matrices represent translation, scaling, and rotation operations in 2D/3D geometry?
In the scalling of 2D, matrix will be like this
```
| sᵪ 0 |
| 0  sᵧ|
```
In the rotation of 2D, matrix will be like this
```
| cos (θ) -sin(θ)|
| sin (θ) cos(θ) |
```
In the translation of 3D, we can take example of matrix 4x4 and it will be like this
```
| 1 0 0 tx |
| 0 1 0 ty |
| 0 0 1 tz |
| 0 0 0 1  |
```

## What is the meaning of a determinant? How can the determinant of a matrix be calculated using a recursive formula? What is the relationship between determinant and volume?
Determinant is tells how a matrix scales area/volume. If det = 0 , it means transformation collapses space (not invertible). By using recursive formula, we can find the determinant, by formula<br>
det(A) = Σ(-1)ⁱ⁺ʲ aᵢⱼ Mᵢⱼ<br>

From there, Mᵢⱼ = minor matrix determinant. The relation between the determinant and the volume of a matrix shows that the absolute value of the determinant of a matrix is ​​equal to the volume of the parallelepiped spanned by the column (or row) vectors of the matrix. It is formulated as | det(A) |. If the determinant is positive, then the volume does not change orientation. If the determinant is negative, then the orientation of the object is reversed after the transformation. If the determinant of a matrix is ​​zero, then the matrix is ​​singular.

### I. How can determinant be calculated quickly using diagonalization?
The determinant can be calculated quickly using diagonalization when the matrix is ​​already diagonal, because the determinant is the product of the main diagonal elements.
```
| a 0 0 |
| 0 b 0 |
| 0 0 c |

Det(A) = a x b x c
```

However, If the matrix is ​​not diagonal, a theorem states that the determinant of matrix A is equal to the determinant of a diagonal matrix with the same eigenvalues. Using the formula A = P D P⁻¹, the final result will lead to det(A) = det(D) = ∏λᵢ.

### II. How can determinant be calculated quickly using LU decomposition?
The determinant of a matrix A can be calculated quickly using the LU decomposition because, since L is a lower triangular matrix, the product of L is 1. Therefore, det(A) = ∏(Diagonal of U).

## What is the meaning of eigenvalues ​​and eigenvectors? What are the uses of eigenvalue decomposition?
Eigenvalues ​​and eigenvectors are concepts from linear algebra. An eigenvalue (λ) is a scalar that indicates how much a vector changes direction, while an eigenvector (v) is a nonzero vector whose direction remains unchanged when multiplied by a matrix (A), only its length does. The equation is (Av = λv). Both are useful for simplifying matrices, analyzing vibrations, reducing data dimensionality (PCA), and solving systems of differential equations.

## What is QR decomposition?
The formula of QR decomposition is A = QR, That used for solving systems & eigenvalue algorithms.
- Q: orthogonal matrix
- R: upper triangular matrix

## How can eigenvalue decomposition be achieved by repeatedly using QR decomposition?
The process itself work by making QR decomposition separates rotation Q from scaling R. After rearranging (RQ), we perform a transformation that gradually brings the matrix closer to diagonal form. At the end, the diagonal = eigenvalues.

## What is SVD decomposition? What is its relationship with eigenvalue decomposition?
Linear SVD is Singular Value Decomposition, which factors a matrix into three component matrices: rotation, rescaling, and second rotation. The formula of SVD Decomposition is A = U Σ Vᵀ, WHERE
- U, V  : orthogonal matrices
- Σ     : diagonal with singular values

SVD and Eigen Decomposition can produce identical results, where Singular values ​​= √eigenvalues ​​of AᵀA.

## What is principal component analysis? What is its relationship with SVD decomposition?
PCA (Principal Component Analysis) is a method for: reducing data dimensions (dimension reduction). The step itself contains subtract mean, compute covariance matrix, and find eigenvectors/eigenvalues. SVD can be used as an efficient method to implement PCA, especially for large data sets, because SVD can implement PCA without the need to calculate the covariance matrix directly.