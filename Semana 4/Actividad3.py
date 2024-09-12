# Dados dos VeA, X1 ~ U(0,2) y X2 ~ U(0,3) independientes, con N = 1000 realizaciones

N = 1000

X1 = np.random.uniform(0, 2, N)
X2 = np.random.uniform(0, 3, N)

# Genere muestras de un vector aleatorio Y = [Y1 Y2]T a partir del vector X = [X1 X2]T aplicando una transformación
# Y = R X, donde R es una matriz de rotación (definida abajo) considerando un ángulo de rotación 𝜃 = 𝜋/10 Haga un gráfico de dispersión
# para X y para Y. Calcule su coeficiente de correlación. 

H = np.array([X1, X2])
theta = np.pi/10
R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
Y = R @ H

mu_Y_estimado = np.mean(Y, axis = 1) 
Y_centrado = Y - mu_Y_estimado[:, np.newaxis]
C_Y_estimado = np.dot(Y_centrado, Y_centrado.T) / (N - 1)

print(C_Y_estimado)

# Repita los puntos 1 y 2, pero para un ángulo rotación 𝜃 = 𝜋/4.

theta = np.pi/4
R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
Y = R @ H

mu_Y_estimado = np.mean(Y, axis = 1) 
Y_centrado = Y - mu_Y_estimado[:, np.newaxis]
C_Y_estimado = np.dot(Y_centrado, Y_centrado.T) / (N - 1)

print(C_Y_estimado)