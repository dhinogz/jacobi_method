# -- Metodo de Jacobi | Ax = b --

# Usaremos la libreria de numpy ya que facilita el uso de las matrices en Python
import numpy as np 

# Matriz A (x, y, z)
A = np.array([[5., -2., 3.,], [-3., 9., 1.], [2., -1., -7.]])

# Vector x (empieza en ceros)
x = np.array([0., 0., 0.])
#             x1  x2  x3

# Vector b
b = np.array([-1., 2., 3.])

# numero de iteraciones
N = 10                  

# Iterar N cantidad de veces. En nuestro caso, son 10
for i in range(N):
    print("Iteracion "+ str(i) + ": " + str(x))

    # usaremos x_n para guardar nuestra respuesta cada iteracion
    x_n = np.zeros_like(x)

    for j in range(b.shape[0]):
        # abajo de la diagonal
        diagonal1 = np.dot(A[j, :j], x[:j])
        # arriba de la diagonal
        diagonal2 = np.dot(A[j, j+1:], x[j+1:])
        # Ax = b => x = b / A
        x_n[j] = (b[j] - diagonal1 - diagonal2) / A[j, j]
        
    x = x_n

print("Respuesta: " + str(x))
