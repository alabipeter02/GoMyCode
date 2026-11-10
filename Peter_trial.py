import numpy as np

#Generate random 3x3 matrices
A = np.random.randint(1,10, size=(3,3))
B = np.random.randint(1,10, size=(3,3))

print('Matrix A:')
print(A)

print('Matrix B:')
print(B)

#Matrix Addition
addition = A + B
print('\nA + B:')
print(addition)

#Matrix Multiplication
multiplication = A * B
print('\nA * B:')
print(multiplication)

#Transpose of A
transpose_A = A.T
print('\nA.T:')
print(transpose_A)

#Transpose of B
transpose_B = B.T
print('\nB.T:')
print(transpose_B)

#Scaler multiplication using pi
scaler_A = np.pi * A
scaler_B = np.pi * B
print('\nA multiplication by pi')
print(scaler_A)

print('\nB multiplication by pi')
print(scaler_B)
