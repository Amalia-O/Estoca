# Actividad 2: Utilice el método de la transformación inversa

# Parámetros
N = 10**4
lambda_val = 0.5

# Generar muestras uniformes en [0, 1)
U = np.random.uniform(0, 1, N)

# Aplicar la transformación inversa
X = -np.log(1-U) / lambda_val

# Funcion de densidad teórica
x_vals = np.linspace(0, np.max(X), 100)
pdf_teorica = lambda_val * np.exp(-lambda_val * x_vals)

# Estimación de la media y la varianza muestrales de X

# Teoricamente: media = mu = 1/lamnda = 2
#               varianza = rho^2 = 1/lambda^2 = 4

print( np.mean(X))
print( np.var(X) )

# Construcción del histograma de las muestras de X. Normalice y compare con la función de densidad de probabilidad teórica

plt.hist(X, bins = 30, density = True, color = 'orange', alpha = 0.6, label = 'Histograma muestral')
plt.plot(x_vals, pdf_teorica, color = 'red', label = 'Función de densidad teórica')
plt.legend              
plt.show()
