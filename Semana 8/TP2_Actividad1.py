import csv
import numpy as np
import re
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
# Detección de partículas radioactivas: Proceso aleatorio Poisson

# Vamos a fijar un segmento de tiempo de duración T = 2 s para evaluar la cantidad de cuentas N (T) con media λT en el intervalo [0,T].
# Armo un vector con las realizaciones del  experimento

realizaciones = []
i=0

file = open('/geiger.csv', 'r')
lines = file.readline()
while(lines != ''):
    realizaciones.append(lines)
    realizaciones[i] = re.sub('\D', '', realizaciones[i])
    i+=1
    lines = file.readline()
file.close()


# Calculo la cantidad de cuentas N (T) en el intervalo [0+(nT),nT+1]. Las realizaciones estan en microsegundos

# idea: si el resto de realizacion(i)[s]/(2*n) es mayor a uno entonces ya me pasae!

contadorCuentas = 0
contadorCasillas = 1

T = 2
cuentas_N_T = []

actual = 0

for j in range(len(realizaciones)):

  actual = (int( realizaciones[j]) * ( 10**(-6) ) )

  if( actual < ( (contadorCasillas)*T ) ):
    contadorCuentas +=1

  elif( actual > ((contadorCasillas+1)*T)):
    cuentas_N_T.append(contadorCuentas)
    cuentas_N_T.append(0)
    contadorCuentas = 1
    contadorCasillas += 2


  else:
    cuentas_N_T.append(contadorCuentas)
    contadorCuentas = 1     # Seteo en 1 para que la cuente en la siguiente casilla, sino esa fila no se cuenta
    contadorCasillas += 1
cuentas_N_T.append(contadorCuentas)

# Calculo la media y la varianza de las cuentas para un intervalo T

print('La varianza es: ', np.var(cuentas_N_T))
print('La media es: ', np.mean(cuentas_N_T))

# Utilice la media estimada como dato y grafique la fmp teórica asociada a la cantidad de pulsos detectados en un rango de duración T
# Corresponde a un proceso poisson N(t), con media = lambda
media = np.mean(cuentas_N_T) 

# Graficando FMP
x = np.arange(0,9)
plt.plot(x, stats.poisson.pmf(x, media), ms=8, color = 'tomato')
plt.vlines(x, 0, stats.poisson.pmf(x, media), colors='lightsalmon', lw=1)
plt.show()

# Graficando histograma
plt.hist(cuentas_N_T, bins=20, density=True, color = 'peachpuff',  edgecolor ='lightsalmon')
plt.show()