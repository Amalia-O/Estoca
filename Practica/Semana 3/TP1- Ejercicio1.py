import numpy as np
import matplotlib.pyplot as plt

# Utilizando la transformación de Box Muller, genere dos variables aleatorias con distribución
# normal Z1 ∼ N(0; 1) y Z2 ∼ N(0; 1) a partir de dos variables uniformes U1 ∼ U(0; 1) y
# U2 ∼ U(0; 1). Para ello utilice las siguientes transformaciones: Z1 = √ −2 ln(U1) cos(2πU2), Z2 = √ −2 ln(U1) sin(2πU2).

N = 10000
# Generar muestras uniformes en [0, 1)
U1 = np.random.uniform(0, 1, N)
U2 = np.random.uniform(0, 1, N)

# Aplicar la transformación inversa
Z1 = ( -2 * np.log(U1) )**(1/2) * np.cos(2 * np.pi * U2)
Z2 = ( -2 * np.log(U1) )**(1/2) * np.sin(2 * np.pi * U2)

# Estime la media y varianza de Z1 y Z2 y grafique los histogramas correspondientes. Realice tambi´en
# un gr´afico de dispersi´on (scatter plot) de Z2 versus Z1 y calcule el coeficiente de correlaci´on
# de Pearson entre ambas variables simuladas para verificar su independencia.

print("Media de Z1:", np.mean(Z1))
print("Varianza de Z1:", np.var(Z1))
print("Media de Z2:", np.mean(Z2))
print("Varianza de Z2:", np.var(Z2))
print("Coeficiente de correlación de Pearson:")
print(np.corrcoef(Z1, Z2))

plt.figure(figsize=(12, 6))
plt.scatter(Z1, Z2, color = 'lightblue', edgecolor = 'dodgerblue')
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(Z1, bins=50, density=True, label = 'Histograma muestral de  $Z_1$', edgecolor = 'dodgerblue', color = 'lightblue')
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(Z2, bins=50, density=True, label = 'Histograma muestral de  $Z_2$', edgecolor = 'dodgerblue', color = 'lightblue')
plt.show()

# Aplicando Box Muller para la obtener muestras normales estándar, genere tres nuevas
# variables aleatorias normales X1 ∼ N(0; 2), X2 ∼ N(1; 2) y X3 ∼ N(1; 4).

N = 10000
# Generar muestras uniformes en [0, 1)
U1 = np.random.uniform(0, 1, N)
U2 = np.random.uniform(0, 1, N)
U3 = np.random.uniform(0, 1, N)
U4 = np.random.uniform(0, 1, N)

# Aplicar la transformación inversa
Z1 = ( -2 * np.log(U1) )**(1/2) * np.cos(2 * np.pi * U2)
Z2 = ( -2 * np.log(U1) )**(1/2) * np.sin(2 * np.pi * U2)

Z3 = ( -2 * np.log(U3) )**(1/2) * np.cos(2 * np.pi * U4)
Z4 = ( -2 * np.log(U3) )**(1/2) * np.sin(2 * np.pi * U4)
# X =rho Z + mu , Z∼ N(0; 1) → X ∼ N(µ; σ2)

X1 = 2**(1/2) * Z1
X2 = 2**(1/2) * Z2 + 1
X3 = 4**(1/2) * Z3 + 1

# Estime en cada caso la media y varianza para su comparación con los valores teóricos.

print("Media de X1:", np.mean(X1))
print("Varianza de X1:", np.var(X1))
print("Media de X2:", np.mean(X2))
print("Varianza de X2:", np.var(X2))
print("Media de X3:", np.mean(X3))
print("Varianza de X3:", np.var(X3))

# Grafique los histogramas de cada variable superpuesto a las curvas de densidad de probabilidad teóricas para verificar la coincidencia.

# Funcion de densidad teórica
x1 = np.linspace(-np.max(X1), np.max(X1), 100)
pdf1_teorica = (1 / (2 * 2 * np.pi)**(1/2) ) * np.exp(-(x1 - 0)**2 / (2 * 2))

x2 = np.linspace(-np.max(X2), np.max(X2), 100)
pdf2_teorica = (1 / (2 * 2 * np.pi)**(1/2) ) * np.exp(-(x2 - 1)**2 / (2 * 2))

x3 = np.linspace(-np.max(X3), np.max(X3), 100)
pdf3_teorica = (1 / (2 * 4 * np.pi)**(1/2) ) * np.exp(-(x3 - 1)**2 / (2 * 4))

# Grafico
import matplotlib.colors as mcolors

plt.figure(figsize=(12, 6))
plt.hist(X1, bins=50, density=True,color = 'peachpuff',  edgecolor ='lightsalmon', label='Histograma muestral de $X_1$')
plt.plot(x1, pdf1_teorica, 'tomato', label='PDF teórica de $X_1$')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(X2, bins=50, density=True, label='Histograma muestral de $X_2$', edgecolor ='lightsalmon',  color = 'peachpuff')
plt.plot(x2, pdf2_teorica, 'tomato', label='PDF teórica de $X_2$')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(X3, bins=50, density=True, color = 'peachpuff', edgecolor ='lightsalmon',  label='Histograma muestral de $X_3$')
plt.plot(x3, pdf3_teorica, 'tomato', label='PDF teórica de $X_3$')
plt.legend()
plt.show()