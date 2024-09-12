import numpy as np
import matplotlib.pyplot as plt

# Genere N = 1000 muestras para definir los siguientes vectores aleatorios.:

N = 200

# 1. X = [X1 X2]T , a partir de dos variables Rayleigh, X1 ~ Rayl(3) y X2 ~ Rayl(2).

X1 = np.random.rayleigh(3, N)
X2 = np.random.rayleigh(2, N)

# 2. V = [V1 V2]T a partir de una transformación de X, tal que V = BX.
X = np.array([X1, X2])

B1 = [0.6,-0.2]
B2 = [0.4, 0.7]
B = np.array([B1, B2])
V = B @ X

# 3. U = [U1 U2]T, a partir de una transformación de X, tal que U = HX.

H1 = [0.6, -0.2]
H2 = [0.4, 0.2]
H = np.array([H1, H2])
U = H @ X
# Haga el gráfico de dispersión (ej: scatter(x1, x2)) y calcule el coeficiente 𝜌 de correlación entre las componentes de cada vector.

print(np.corrcoef(X[0,:], X[1,:]))
plt.scatter(X[0,:], X[1,:], color = 'lightblue', edgecolor = 'dodgerblue')
plt.axis([-2, 12, 0, 14])
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()

print(np.corrcoef(V[0,:], V[1,:]))
plt.scatter(V[0,:], V[1,:], color = 'lightblue', edgecolor = 'dodgerblue')
plt.axis([-2, 12, 0, 14])
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()

print(np.corrcoef(U[0,:], U[1,:]))
plt.scatter(U[0,:], U[1,:], color = 'lightblue', edgecolor = 'dodgerblue')
plt.axis([-2, 12, 0, 14])
plt.xlabel('U1')
plt.ylabel('U2')
plt.show()

#Defina el límite de los ejes del gráfico con axis([-2 12 0 14])