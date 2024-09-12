import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Parámetros para la primera distribución
mean1 = [0, 0]
cov1 = [[1, 0], [0, 1]]

# Crear una cuadrícula de puntos
x1 = np.linspace(-3, 3, 100)
y1 = np.linspace(-3, 3, 100)
X_grid1, Y_grid1 = np.meshgrid(x1, y1)

# Evaluar la función de densidad sobre la cuadrícula
pos1 = np.dstack((X_grid1, Y_grid1))
rv1 = multivariate_normal(mean1, cov1)
Z1 = rv1.pdf(pos1)

# Parámetros para la segunda distribución
mean2 = [0.8, 1]
cov2 = [[0.7, 0.8], [0.8, 1.75]]

# Crear una cuadrícula de puntos
x2 = np.linspace(-4, 4, 100)
y2 = np.linspace(-4, 4, 100)
X_grid2, Y_grid2 = np.meshgrid(x2, y2)

# Evaluar la función de densidad sobre la cuadrícula
pos2 = np.dstack((X_grid2, Y_grid2))
rv2 = multivariate_normal(mean2, cov2)
Z2 = rv2.pdf(pos2)

# Crear la figura y los ejes
fig = plt.figure(figsize=(12, 6))

# Subplot 1: Gráfico 3D para la primera distribución
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X_grid1, Y_grid1, Z1, cmap='viridis', alpha=0.6)
ax1.contour3D(X_grid1, Y_grid1, Z1, 10, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Densidad')
ax1.set_title('3D: Distribución Normal Bivariada (mean=[0, 0], cov=[[1, 0], [0, 1]])')

# Subplot 2: Gráfico 2D para la primera distribución
ax2 = fig.add_subplot(122)
contour2D = ax2.contour(X_grid1, Y_grid1, Z1, levels=10, cmap='viridis')
plt.colorbar(contour2D, ax=ax2)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('2D: Curvas de Nivel (mean=[0, 0], cov=[[1, 0], [0, 1]])')

plt.tight_layout()
plt.show()

# Crear la figura y los ejes para la segunda distribución
fig = plt.figure(figsize=(12, 6))

# Subplot 1: Gráfico 3D para la segunda distribución
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X_grid2, Y_grid2, Z2, cmap='viridis', alpha=0.6)
ax1.contour3D(X_grid2, Y_grid2, Z2, 10, cmap='viridis')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Densidad')
ax1.set_title('3D: Distribución Normal Bivariada (mean=[0.8, 1], cov=[[0.7, 0.8], [0.8, 1.75]])')

# Subplot 2: Gráfico 2D para la segunda distribución
ax2 = fig.add_subplot(122)
contour2D = ax2.contour(X_grid2, Y_grid2, Z2, levels=10, cmap='viridis')
plt.colorbar(contour2D, ax=ax2)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('2D: Curvas de Nivel (mean=[0.8, 1], cov=[[0.7, 0.8], [0.8, 1.75]])')

plt.tight_layout()
plt.show()
