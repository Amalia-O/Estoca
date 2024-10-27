# Genere 1000 realizaciones de un proceso estocástico iid Random Step, definido como:
# X(n) = 2 Z(n) – 1, Donde Z(n) es un proceso Bernoulli con p = 0.7, para todo n = 0, ..., N-1, con una
# duración de N = 100 muestras.

# Estime la media y la varianza en funcion del tiempo n
N = 1000
p = 0.7

X = [0]

for i in range (0,N):
  if( np.random.random() < p):
    X.append(1)
  else:
    X.append(-1)

# Media: mu_X = E[2 Z_n - 1] = 2p-1 CTE
# Var: rho^2_X = E[ (X_n - mu_X)^2 ] = 4E[ (Z_n -p)^2 ] = 4 rho_Z^2 = 4p(1-p)

media_teorica = np.mean(X)
varianza_teorica = np.var(X)

media_temporal = []
varianza_temporal = []

for i in range(0,N):
  media_temporal.append(np.mean(X[0:i]))
  varianza_temporal.append(np.var(X[0:i]))

plt.plot(media_temporal, label = "Media temporal", color = 'teal')
plt.hlines(y=media_teorica, xmin = 0, xmax = N, linewidth=2, color='tomato', label = "Media teorica")
plt.grid()
plt.legend()
plt.show()

plt.plot(varianza_temporal, label = "Media temporal", color = 'teal')
plt.hlines(y=varianza_teorica, xmin = 0, xmax = N, linewidth=2, color='tomato', label = "Media teorica")
plt.grid()
plt.legend()
plt.show()