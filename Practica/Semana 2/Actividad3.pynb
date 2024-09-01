# Actividad 3

N = 200

# Para el vector U = [U1 U2]T , genere dos variables Rayleigh, U1 ~ U(0;2) y U2 ~ U(0;3)

U1 = np.random.uniform(0, 2, N)
U2 = np.random.uniform(0, 3, N)

U = np.vstack((U1, U2))

# Para el vector X = [X1 X2]T genere muestras de las variables X1 y X2 a partir de U1 y U2, tal
# que X1 = 0.5 U1 – 0.3 U2 y X2 = 0.7 U1 + 0.2 U2

X1 = 0.5 * U1 - 0.3 * U2
X2 = 0.7 * U1 + 0.2 * U2

X = np.vstack((X1, X2))

# Para el vector Y = [Y1 Y2]T, genere muestras de las variables Y1 y Y 2 a partir de U1 y U2, tal
# que Y1 = 1.2 U1 – 0.1 U2 y Y2 = U1 + 0.1 U2

Y1 = 1.2 * U1 - 0.1 * U2
Y2 = U1 + 0.1 * U2

Y = np.vstack((Y1, Y2))

# Gráfico de dispersión y cálculo de coeficientes de correlación

print(np.corrcoef(U1,U2))

plt.scatter(U[0,:], U[1,:])
plt.xlabel('U1')
plt.ylabel('U2')
plt.show()

print(np.corrcoef(X1,X2))

plt.scatter(X[0,:], X[1,:])
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()

print(np.corrcoef(Y1,Y2))

plt.scatter(Y[0,:], Y[1,:])
plt.xlabel('Y1')
plt.ylabel('Y2')
plt.show()
