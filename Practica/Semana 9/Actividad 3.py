# Sean A y B dos variables aleatorias independientes con distribución U(0,1). Se define la
# siguiente función x(t) = At + B, con 0 <= t < 2. Suponiendo que se trata de un proceso
# continuo muestreado a una tasa Ts = 0.01. Generando 1000 realizaciones, estime la media y varianza en función del tiempo t (𝜇(t) y 𝜎2(t)),
# superponiendo las realizaciones a la media estimada 𝜇(t). Aparte grafique la varianza 𝜎2(t)

Ts = 0.01
t = np.arange(0, 2, Ts)  # 0 <= t < 2 con pasos de 0.01
num_realizaciones = 1000
realizaciones = np.zeros((num_realizaciones, len(t)))


for i in range(num_realizaciones):
    A = np.random.uniform(0, 1)
    B = np.random.uniform(0, 1)
    realizaciones[i, :] = A * t + B


media_temporal = np.mean(realizaciones, axis=0)
media_teorica = t / 2 + 0.5

plt.figure()
plt.grid()
for i in range(num_realizaciones):
    plt.plot(t, realizaciones[i, :], color="salmon", alpha=0.1)
plt.plot(t, media_temporal, label="Media estimada", color="blue")
plt.plot(t, media_teorica, label="Media teórica", color="red")
plt.legend()
plt.show()

varianza_temporal = np.var(realizaciones, axis=0)
varianza_teorica = t**2 / 12 + 1 / 12

plt.plot(varianza_temporal, label = "Varianza temporal", color = 'teal')
plt.plot(varianza_teorica, color='tomato', label = "Varianza teorica")
plt.grid()
plt.legend()
plt.show()