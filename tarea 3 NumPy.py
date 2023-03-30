import numpy as np

#matriz de coeficientes y vector independiente
A = np.array([[1, 3], [1.5, 2]])
B = np.array([300, 350])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, B)

# Mostrar la solución
print("número de unidades del producto A: {:.2f} ".format(x[0]))
print("número de unidades del producto B: {:.2f} ".format(x[1]))
