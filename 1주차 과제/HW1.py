import numpy as np

A = np.array([[2, 5], 
              [1, 3],
              [4, 1]])
              
B = np.array([[4, -1], 
              [2, 3],
              [6, 2]])

C = np.array([[1, 2, 2],
              [3, 4, 5]])

print("(a)", A+B)
print("(b)", B-A)
print("(c)", B@C)
print("(d)", C@A)
