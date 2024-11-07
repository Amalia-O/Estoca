# Sea X(n) un proceso aleatorio gaussiano blanco N(0,2), de largo N=1000, cuyas muestras
# son independientes. A partir de éste se define el siguiente proceso:
#     Y(n) = 0.5 X(n) + 0.75 X(n-1)

# Genere una realización del proceso y grafíquelo.

N = 1000
Y = np.zeros(N)

mediaTeorica = 0
varianzaTeorica = 0.5**2 *2 + (0.75**2 *2)


for i in range (1, N):
  X = np.random.normal(0,2)
  Y[i] = 0.5*X + 0.75*Y[i-1]

plt.figure(figsize = (12,6))
plt.plot(Y, linewidth = 0.8)
plt.xlabel("Tiempo")
plt.ylabel("Y(n)")
plt.grid()
plt.show()

# Genere 2000 realizaciones y estime la media y varianza
M = 2000
realizaciones = np.zeros((M,N))

for i in range (M):
  for j in range (1, N):
    X = np.random.normal(0,2)
    Y[j] = 0.5*X + 0.75*Y[j-1]
  realizaciones[i] = Y

mediaEstimada = np.mean(realizaciones,axis =0)
# mismo problema de la raiz :(
varianzaEstimada = np.mean((realizaciones- mediaEstimada)**2, axis=0)**0.5

plt.figure(figsize = (12,6))
plt.hlines(mediaTeorica,0,N, label = "Media teórica")
plt.plot(mediaEstimada, label = "Media estimada", linestyle = 'dashed', color ="orange")
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize = (12,6))
plt.hlines(varianzaTeorica,0,N, label = "Varianza teórica")
plt.plot(varianzaEstimada, label = "Varianza estimada", linestyle = 'dashed', color ='orange')
plt.grid()
plt.legend()
plt.show()