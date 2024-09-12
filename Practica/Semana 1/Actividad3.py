# Actividad 3

# En un sistema FIR: y_n = \sum^{N-1}_0 h_k x_{n-k}
# Coeficientes del sistema FIR
h = np.array([4, 3, 3.5, 4, 3, 2.5, 0.5, 0.3, 0.2]) # N=9

plot([np.arange(len(h))], [h], line_styles=['-'], xlabel = 'n', ylabel = 'Amplitud', title = 'Respuesta Impulsiva h(n)', plot_type= 'stem', marker_styles= 'o')

# Calcular la respuesta en frecuencia usando la FFT
N_fft = 512               # Definir un número adecuado de puntos para la FFT
H = np.fft.fft(h, N_fft)  # Calcular la FFT de h(n)
frequencies = np.fft.fftfreq(N_fft, d=1)

# Aplicar fftshift para centrar las frecuencias
H_shifted = np.fft.fftshift(H)
frequencies_shifted = np.fft.fftshift(frequencies)

# Graficar el módulo de la respuesta en frecuencia con funcion plot
plot([frequencies_shifted], [np.abs(H_shifted)], line_styles=['-'], xlabel = 'frecuencia (Hz)', ylabel = 'Magnitud', title = 'Módulo de la Respuesta en Frecuencia |H(f)|')

# Calcular los ceros del sistema (raíces del polinomio dado por H(z) = 4 + 3z^{-1} + ... + 0.2z^{-8})
# Que es equivalente a un polinomio estándar P(z) = 4^{8} + 3z^{7} + ... + 0.2
zeros = np.roots(h)

# Graficar los ceros en el plano z
plt.figure(figsize=(10, 10))
plt.scatter(np.real(zeros), np.imag(zeros), color='blue', label='Ceros')

# Graficar el círculo unitario
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_artist(circle)

# Los polos van a estar en el cero o en el infinito para un FIR. En este caso, infinito.

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