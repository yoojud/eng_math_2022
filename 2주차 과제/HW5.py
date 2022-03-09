import numpy as np

A = np.array([[2, 3, 4],
              [4, 8, 2],
              [1, 2, 1]])

print("(d) A가 대칭행렬인지 보여라.")
print(np.array_equal(A,A.T))
