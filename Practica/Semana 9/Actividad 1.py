# Generar una aproximación del proceso de Poisson con λ=0.5 arribos por segundo,
# a partir de un proceso Bernoulli. Tomar un intervalo de T=10 segundos y dividirlo
# en n=1000 intervalos. Simular 2000 realizaciones del proceso

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

T = 10
n = 1000
intervalo = T/n

#en cada intervalo podemos pensar que tiramos una moneda con psibilidad de cara p= λ*intervalo
p = 0.5*intervalo

#N(T) la cantidad de caras en el intervalo [0;T] : np = nλintervalo = λT.
# calculo las 2000 realizaciones

X = np.random.binomial(n , p, size = 2000)

# Estimar la funcion de probabilidad de la cantidad de arribos en [0,T]. Comparar con la teórica

Y_Teorica = np.random.poisson(lam = 5, size = 2000)

kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=10, ec="k")

plt.hist(X, **kwargs, label = "Aproximada")
plt.hist(Y_Teorica, **kwargs, label = "Teorica")
plt.legend(loc="upper right")
plt.xlabel("Cantidad de arribos")
plt.ylabel("Probabilidad")
plt.show()

# Estimar la media y la varianza del proceso y comparar con la teorica

print("La varianza teorica es", np.var(Y_Teorica))
print("La varianza estimada es", np.var(X))
print("La media teorica es", np.mean(Y_Teorica))
print("La media estimada es", np.mean(X))