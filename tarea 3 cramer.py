import numpy as np

A = np.array([[1, 3], [1.5, 2]])
B = np.array([300, 350])

detA = np.linalg.det(A)
detx = np.linalg.det(np.column_stack((B, A[:, 1])))
dety = np.linalg.det(np.column_stack((A[:, 0], B)))

x = detx / detA
y = dety / detA

print("número de unidades del producto A",x)
print("número de unidades del producto B",y)
