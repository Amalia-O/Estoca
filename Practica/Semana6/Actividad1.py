import numpy as np
import matplotlib.pyplot as plt
import cv2

# Para la imagen img_01.png provista en el campus, defina realizaciones de un vector X = [X1 , X2]T 
# seleccionando cada par de píxeles contiguos en la imagen (ver esquema en siguiente filmina)

img = cv2.imread('/usr/img_01.jpg', cv2.IMREAD_GRAYSCALE)

alto, ancho = img.shape

X1 = []
X2 = []

for i in range(alto - 1):       # Recorrer las filas
        for j in range(ancho):  # Recorrer las columnas
            X1.append( img[i, j] )    # Primer píxel del par (arriba)
            X2.append(img[i + 1, j])  # Segundo píxel del par (abajo)


X = np.array ([X1, X2])

# Haga un gráfico de dispersión del vector X

plt.scatter(X[0,:], X[1,:], color = 'lightblue', edgecolor = 'dodgerblue')
plt.xlabel('$X_1$')
plt.ylabel('$X_2$')
plt.show()

# Estime la matriz de covarianza de X 
# Estimación de la matriz de covarianza según Semana 4 - Actividad 2, pero nose porque da mal. Uso formula

cov_X = np.cov(X)
mean_X = np.mean(X, axis=1, keepdims=True)
print(mean_X)
print(cov_X)

# Obtener matrices de autovectores P y autovalores ⋀: CX = P⋀PT

DY, PY = np.linalg.eig(cov_X) #autovalores (array), autovectores (matriz)

print(DY)
print(PY)

# Ordenar autovectores en orden decreciente de autovalores.

idx = DY.argsort()[::-1]
DY = DY[idx]
PY = PY[:,idx]

print("eigen ordenados")
print(DY)
print(PY)

# Definir cantidad r de componentes a conservar y definir matriz truncada V.

r = 1

V = PY[:,0:r]

# Calcular las componentes proyectadas y reducidas YR = VT(X – 𝞵X).

YR = np.dot(V.T, X - mean_X)

# Reconstruir X a partir de las componentes desacopladas XR = V YR + 𝞵X

XR = np.dot(V, YR) + mean_X

# Rearmar imagen

img_reconstruida = np.reshape(XR[0,:], (alto-1, ancho))
plt.imshow(img_reconstruida, cmap='gray')
plt.show()

# Haga un gráfico de dispersión de Y. Compute las proyecciones Y en las direcciones principales. 

Y = np.dot(PY.T, X - mean_X)

plt.scatter(Y[0,:], Y[1,:], color = 'lightblue', edgecolor = 'dodgerblue')
plt.xlabel('$Y_1$')
plt.ylabel('$Y_2$')
plt.show()

