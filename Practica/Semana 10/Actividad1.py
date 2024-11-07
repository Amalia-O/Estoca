# Sea un proceso random walk Y(n) = Y(n-1) + X(n), donde X(n) es un proceso random step de parámetro p.
# Genere M=20 realizaciones de un proceso random walk Y(n), de largo N=50,
# con parámetro p (considere los casos p = {0.2, 0.5, 0.8}) y comparelas gráficamente con la media teórica.

import numpy as np
import matplotlib.pyplot as plt

N = 50      # tiempo
M = 20      # Realizaciones
Y = np.zeros(N)
n = np.arange(N)

# Media = E[Y(n)] = E[Y(0)] + n mu_X = Y[0] + n (2p-1) = n(2p-1)
# Varianza = n rho_x^2 = n 4p (1-p)

p = [0.2, 0.5, 0.8]

for k in range(len(p)):
  plt.figure(figsize = (12,6))
  for i in range(M):
    for j in range (1, N):
      if (np.random.random() < p[k]):
        Y[j] = Y[j-1] + 1
      else:
        Y[j] = Y[j-1] - 1
    plt.plot(Y, drawstyle = "steps", alpha = 0.5)
  plt.grid()

  media_teorica = n * (2*p[k]-1)
  plt.plot(media_teorica, label = "Media teórica", color = 'black')
  plt.legend()
  plt.title("Random walk con p =" + str(p[k]) )
  plt.show()

# Genere 200 realizaciones del proceso Y(n) para estimar la media y varianza en función del tiempo.
# Compare gráficamente las estimaciones con los resultados teóricos, tanto para la media como la varianza.

N = 50      # tiempo
M = 200     # realizaciones
n = np.arange(N)
mediaEstimada = np.zeros(N)
varianzaEstimada = np.zeros(N)

# Media Teorica = E[Y(n)] = E[Y(0)] + n mu_X = Y[0] + n (2p-1)
# Media estimada es el promedio

# Varianza teorica = n rho_x^2 = n 4p (1-p)

p = [0.2, 0.5, 0.8]

for k in range(len(p)):

  realizaciones = np.zeros((M,N))
  for i in range(M):

    Y = np.zeros(N)
    for j in range (1, N):

      if (np.random.random() < p[k]):
        Y[j] = Y[j-1] + 1
      else:
        Y[j] = Y[j-1] - 1
    realizaciones[i] = Y

  mediaEstimada = np.mean(realizaciones, axis = 0)
  varianzaEstimada = np.var(realizaciones, axis = 0)

  mediaTeorica = (n * (2*p[k]-1))
  varianzaTeorica = n * 4 * p[k] * (1-p[k])

  plt.figure(figsize = (12,6))
  plt.plot(mediaTeorica, label = "Media teórica")
  plt.plot(mediaEstimada, label = "Media estimada", linestyle = 'dashed')
  plt.grid()
  plt.legend()
  plt.title("Esperanza con Random walk con p =" + str(p[k]) )
  plt.show()

  plt.figure(figsize = (12,6))
  plt.plot(varianzaTeorica, label = "Varianza teórica")
  plt.plot(varianzaEstimada, label = "Varianza estimada", linestyle = 'dashed')
  plt.grid()
  plt.legend()
  plt.title("Varianza con Random walk con p =" + str(p[k]) )
  plt.show()