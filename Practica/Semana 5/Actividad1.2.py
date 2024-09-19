# Se quiere utilizar una transformación lineal Y = A Z + b que permita convertir un vector
# aleatorio normal estándar con parámetros CZ y 𝜇Z en otro vector con parámetros
# CY = [0.7 0.8 ; 0.8 1.75] y 𝜇Y= [0.8 1.0]T.

# Suponiendo que la diagonalización de la covarianza de Y es CY = P⋀PT , utilice la
# transformación afín para obtener el vector aleatorio Y a partir de las muestras generadas de Z. 
# Haga un gráfico de dispersión del vector Y (Y2 vs Y1) superpuesta a las curvas de nivel de la densidad conjunta fY(y). 
# Grafique también los histogramas de cada componente.

# Z1, Z2 sigue valiendo. CY = A CZ AT
# A = PY⋀Y1/2
Z = np.array([Z1, Z2]).T

DY, PY = np.linalg.eig(np.array([[0.7, 0.8], [0.8, 1.75]]))
A = PY @ ((np.diag(DY))**(0.5)) @ Z.T
A = A.T + np.array([0.8, 1.0])
Y = Z @ np.array([[0.7, 0.8], [0.8, 1.75]]) + np.array([0.8, 1.0])

plt.hist(A[:,0],bins=50, density=True, label = 'Histograma muestral de  $Y_1$', edgecolor = 'dodgerblue', color = 'lightblue')
x = np.linspace(-4, 4, 100)
plt.plot(x, (1 / (0.7 * np.sqrt(2 * np.pi))) * np.exp(- (x- 0.8)**2 /(2* 0.7)), color = 'tomato', label = 'PDF teórica')
plt.show()

plt.hist(A[:,1],bins=50, density=True, label = 'Histograma muestral de  $Y_2$', edgecolor = 'dodgerblue', color = 'lightblue')
x = np.linspace(-4, 4, 100)
plt.plot(x, (1 / (1.75 * np.sqrt(2 * np.pi))) * np.exp(- (x- 1)**2 /(2* 1.75)), color = 'tomato', label = 'PDF teórica')
plt.show()

# Gráfico de dispersión con curvas de nivel teóricas de la PDF
plt.scatter(A[:,0], A[:,1],  color = 'peachpuff',  edgecolor ='lightsalmon')

x_grid = np.linspace(-6, 6, 100)
y_grid = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(x_grid, y_grid)

# Define la distribución normal bivariada
mean = [0.8, 1]
cov = [[0.7, 0.8], [0.8, 1.75]]  # matriz de covarianza (identidad)

Z_density = multivariate_normal.pdf(np.dstack((X, Y)), mean=mean, cov=cov)

# Curvas de nivel
contour = plt.contour(X, Y, Z_density, levels=10, cmap='magma')
plt.clabel(contour, inline=True, fontsize=8)

# Etiquetas y título
plt.title('Gráfico de dispersión con curvas de nivel teóricas de la PDF')
plt.xlabel('$Y_1$')
plt.ylabel('$Y_2$')
plt.grid()
plt.axis('equal')  # Para mantener la proporción del gráfico
plt.show()