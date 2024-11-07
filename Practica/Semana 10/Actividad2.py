# Sea una variable aleatoria A ~ N(1; 0.16) y una frecuencia 𝜔0 = 0.015𝜋. 
#Se define el siguiente proceso: X(n) = A cos(𝜔0n), de largo N=400.

# Genere 20 realizaciones del proceso y comparelas gráficamente con la media teórica.

# Cálculo de la media teorica
# E[X] = E[A cos(w0 t)] = mu_A cos(w0t)

N = np.linspace(0,400,400)
M = 20
w0 = 0.015*np.pi
muA = 1
sigmaA = 0.16

mediaTeorica = muA * np.cos(w0*N)
varianzaTeorica = sigmaA * np.cos(w0*N)**2

plt.figure(figsize = (12,6))
for i in range (M):
  A = np.random.normal(muA, sigmaA)
  X = np.abs(A) * np.cos(w0*N)
  plt.plot(X, color = "salmon", alpha = 0.5)
plt.plot(mediaTeorica, color = "black", label = "Media Teórica")
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("X(n)")
plt.grid()
plt.show()

# Genere 200 realizaciones y estime la media y varianza de X(n). Compare gráficamente
# las estimaciones con los resultados teóricos, tanto para la media como la varianza.

M = 200
realizaciones = np.zeros((M,len(N)))

for i in range (M):
  A = np.abs(np.random.normal(muA, sigmaA))
  X = A * np.cos(w0*N)
  realizaciones[i] = X

mediaEstimada = np.mean(realizaciones,axis =0)
# nose porque le tengo que aplicar raiz :(
varianzaEstimada = np.mean((realizaciones- mediaEstimada)**2, axis=0)**0.5

plt.figure(figsize = (12,6))
plt.plot(mediaTeorica, label = "Media teórica")
plt.plot(mediaEstimada, label = "Media estimada", linestyle = 'dashed')
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize = (12,6))
plt.plot(varianzaTeorica, label = "Varianza teórica")
plt.plot(varianzaEstimada, label = "Varianza estimada", linestyle = 'dashed')
plt.grid()
plt.legend()
plt.show()