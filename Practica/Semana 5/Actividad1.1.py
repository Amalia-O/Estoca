# Gráfico de dispersión con curvas de nivel teóricas de la PDF
plt.scatter(Z1, Z2,  color = 'peachpuff',  edgecolor ='lightsalmon')

x_grid = np.linspace(-4, 4, 100)
y_grid = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x_grid, y_grid)

# Define la distribución normal bivariada
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # matriz de covarianza (identidad)

Z_density = multivariate_normal.pdf(np.dstack((X, Y)), mean=mean, cov=cov)

# Curvas de nivel
contour = plt.contour(X, Y, Z_density, levels=10, cmap='magma')
plt.clabel(contour, inline=True, fontsize=8)

# Etiquetas y título
plt.title('Gráfico de dispersión con curvas de nivel teóricas de la PDF')
plt.xlabel('$Z_1$')
plt.ylabel('$Z_2$')
plt.grid()
plt.axis('equal')  # Para mantener la proporción del gráfico
plt.show()