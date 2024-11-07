# Sea una variable aleatoria 𝛳 ~ U(0; 2𝜋) y una frecuencia 𝜔0= 0.015𝜋. 
# Se define el siguiente proceso: X(n) = A cos(𝜔0n + 𝛳), de largo N=400, donde A=1.

# Genere 20 realizaciones del proceso y comparelas gráficamente con la media teórica.
w0 = 0.015*np.pi
N = np.linspace(0,400,400)
M = 20

mediaTeorica = 0
varianzaTeorica = 0.5

plt.figure(figsize = (12,6))
for i in range (M):
  U = np.random.uniform(0,2*np.pi)
  X = np.cos(w0*N + U)
  plt.plot(X, color = "salmon", alpha = 0.5)
plt.hlines(0,0,len(N), color = "black", label = "Media Teórica")
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("X(n)")
plt.grid()
plt.show()

# Genere 2000 realizaciones y estime la media y varianza de X(n). Compare gráficamente
# las estimaciones con los resultados teóricos, tanto para la media como la varianza.

M = 200
realizaciones = np.zeros((M,len(N)))

for i in range (M):
  U = np.random.uniform(0,2*np.pi)
  X = np.cos(w0*N + U)
  realizaciones[i] = X

mediaEstimada = np.mean(realizaciones,axis =0)
varianzaEstimada = np.var(realizaciones, axis=0)

plt.figure(figsize = (12,6))
plt.hlines(mediaTeorica,0,len(N), label = "Media teórica")
plt.plot(mediaEstimada, label = "Media estimada", linestyle = 'dashed', color ="orange")
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize = (12,6))
plt.hlines(varianzaTeorica,0,len(N), label = "Varianza teórica")
plt.plot(varianzaEstimada, label = "Varianza estimada", linestyle = 'dashed', color ='orange')
plt.grid()
plt.legend()
plt.show()