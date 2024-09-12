# Estime la matriz de autocovarianza para los vectores aleatorios del ejercicio anterior: X, U y V.
# Analice las propiedades de la matriz y la particularidad de cada una en relación a los resultados
# del ejercicio anterior (observe la covarianza entre componentes y cómo esto se refleja en las matrices de correlación).

#La diagonal es la varianza!

# Matriz de covarianza de un vector aleatorio X:  C_X = E[(X - mu_X)(X - mu_X)T]
# Estimación de la media de un vector aleatorio ^mu_X = 1/n sum^{n}_{k=1} X_k
# Estimación de la matriz de autocovatianza de un vector aleatorio ^C_X = 1/(n-1) sum^{n}_{k=1} (X_k - ^mu_X)(X_k - ^mu_X)T

mu_X_estimado = np.mean(X, axis = 1)
X_centrado = X - mu_X_estimado[:, np.newaxis]
C_X_estimado = np.dot(X_centrado, X_centrado.T) / (N - 1)

print(C_X_estimado)

mu_U_estimado = np.mean(U, axis = 1)
U_centrado = U - mu_U_estimado[:, np.newaxis]
C_U_estimado = np.dot(U_centrado, U_centrado.T) / (N - 1)

print(C_U_estimado)

mu_V_estimado = np.mean(V, axis = 1)
V_centrado = V - mu_V_estimado[:, np.newaxis]
C_V_estimado = np.dot(V_centrado, V_centrado.T) / (N - 1)

print(C_V_estimado)
