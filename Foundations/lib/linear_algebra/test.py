from matrix import Matrix

m1 = Matrix([[1,2], [3,4]])

print(m1)

try:
    m2 = Matrix([[1,2], [3,4,5]])
except ValueError as e:
    print(f"Caught error: {e}")
