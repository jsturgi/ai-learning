from matrix import Matrix
from vector import Vector
print("Initialization testing")
m1 = Matrix([[1,2], [3,4]])

print(m1)

try:
    m2 = Matrix([[1,2], [3,4,5]])
except ValueError as e:
    print(f"Caught error: {e}")
m2 = Matrix([[3,4], [5,6]])

print("math operations testing")
print(m1.__add__(m2))
print(m1.__sub__(m2))
print(m1.__matmul__(m2))

print("Transpose Test")
m3 = Matrix([[1, 2, 3],
               [4, 5, 6]])
print(m3)
print(m3.transpose())

print("scaling test")
print(Matrix.scaling(3,2,8,9))

print("Identity")
print(Matrix.identity(3))

eigentest = Vector([1,1])
eigenMtest = Matrix([[2,0], [0,1]])

x = eigentest.normalize() # Start with normalized vector
print(f"x0: {x}")

for i in range(5):
    x = eigenMtest.multiply_vector(x)
    x = x.normalize()
    print(f"x{i+1}: {x}")

v = Vector([1,0])
result = Vector([2,0])

dot = v.dot(result)
print(dot)


print("\n=== Power Iteration Test ===")
A = Matrix([[2, 0], [0, 1]])
eigenval, eigenvec = A.power_iter()
print(f"Eigenvalue: {eigenval}")
print(f"Eigenvector: {eigenvec}")

B = Matrix([[10, 0], [0, 1]])  # λ₁=10, λ₂=1, ratio=0.1
eigenval, eigenvec = B.power_iter(tolerance=0.00001) 
C = Matrix([[2, 0], [0, 1.9]])  # λ₁=2, λ₂=1.9, ratio=0.95
eigenval, eigenvec = C.power_iter(tolerance=0.00001)

print("\n=== Find Top K Eigenvalues Test ===")
D = Matrix([
    [5,0,0],
    [0,3,0],
    [0,0,1]
])
test = D.find_top_k_eigenvalues(3)
print(test)
print(test[0][1].dot(test[1][1]))
