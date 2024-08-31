# Actividad 4

# Defino la señal de entrada x al sistema

M = 100
n = np.arange(M)
x = sp.signal.square(2 * np.pi * 0.02 * n)

# Coeficientes del sistema FIR
h = np.array([4, 3, 3.5, 4, 3, 2.5, 0.5, 0.3, 0.2])

# y(n) = h(n)*x(n)
# Calcular la salida y(n) usando la convolución
y_conv = sp.signal.convolve(h, x)
n_conv = np.arange(len(y_conv))

# Calcular la salida y(n) usando lfilter
y_filter = sp.signal.lfilter(h, 1, x)
n_filter = np.arange(len(y_filter))

# Graficar la salida lfilter usando plot
plot( [n_filter], [y_filter], title = 'Salida en el tiempo usando lfilter', xlabel= 'n', ylabel = 'Magnitud')

# Graficar la salida conv usando plot
plot( [n_conv], [y_conv], Color = 'orange' , title = 'Salida en el tiempo usando Convolucion', xlabel= 'n', ylabel = 'Magnitud' )

###### Análisis en frecuencia ######

# Definir el número de puntos para la FFT
N_fft = 512

# Calcular la FFT de la salida usando convolución
Y_conv = np.fft.fft(y_conv, N_fft)
frequencies_conv = np.fft.fftfreq(N_fft, d=1)

# Calcular la FFT de la salida usando lfilter
Y_filter = np.fft.fft(y_filter, N_fft)
frequencies_filter = np.fft.fftfreq(N_fft, d=1)

# Aplicar fftshift para centrar las frecuencias
Y_conv_shifted = np.fft.fftshift(Y_conv)
frequencies_conv_shifted = np.fft.fftshift(frequencies_conv)

Y_filter_shifted = np.fft.fftshift(Y_filter)
frequencies_filter_shifted = np.fft.fftshift(frequencies_filter)

# Graficar la salida y(n) usando lfilter
plot([frequencies_filter_shifted], [np.abs(Y_filter_shifted)], xlim = (-0.2, 0.2), title = 'Respuesta en Frecuencia |Y(f)| usando Lfilter'
     , xlabel = 'Frecuencia (Hz)', ylabel = 'Magnitud')

# Graficar la salida y(n) usando Convolución
plot([frequencies_conv_shifted], [np.abs(Y_conv_shifted)], Color = 'orange', xlim = (-0.2, 0.2), title = 'Respuesta en Frecuencia |Y(f)| usando Convolución'
     , xlabel = 'Frecuencia (Hz)', ylabel = 'Magnitud')

zeros = np.roots(b)
print(zeros)  #cero complejo conjugado

poles = np.roots(a)
print(poles)  #polo doble real

plt.figure(figsize=(12, 12))

# Graficar los ceros en el plano z
plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Ceros')

#Graficar los polos en el plano z
plt.scatter(np.real(poles), np.imag(poles), color='red', label='Polos')

# Graficar el círculo unitario
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_artist(circle)

# Configurar los límites de los ejes
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# Configuración del gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Diagrama de Polos y Ceros')
plt.grid()
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

##### Que ocurre si los coeficientes del denominador ahora son a = {1 -1.2}? ####

# Defino los parámetros

b = np.array([3, 1.5, 2])
a = np.array([1, -1.2])

# La funcion freqz devuelve las frecuencias en términos de pi radianes por muestra, no Hz
w,h = sp.signal.freqz(b, a)

# Graficar el módulo de la respuesta en frecuencia
plt.figure(figsize=(10, 6))
plt.plot(w / np.pi, np.abs(h))  # w está en términos de pi radianes por muestra
plt.title('Respuesta en Frecuencia del Sistema IIR')
plt.xlabel('Frecuencia normalizada (π rad/muestra)')
plt.ylabel('Magnitud')
plt.grid()
plt.show()

zeros = np.roots(b)
print(zeros)  #cero complejo conjugado

poles = np.roots(a)
print(poles)  #polo doble real

plt.figure(figsize=(12, 12))

# Graficar los ceros en el plano z
plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Ceros')

#Graficar los polos en el plano z
plt.scatter(np.real(poles), np.imag(poles), color='red', label='Polos')

# Graficar el círculo unitario
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_artist(circle)

# Configurar los límites de los ejes
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# Configuración del gráfico
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlabel('Re')
plt.ylabel('Im')
plt.title('Diagrama de Polos y Ceros')
plt.grid()
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#Conclusión, se achancha la rta en frec
