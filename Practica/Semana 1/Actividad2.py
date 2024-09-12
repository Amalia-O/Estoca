import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

# Algunas funciones

# Funcion genérica para plotear
def plot(x_axes, y_axes, labels=None, title=None, xlabel=None, ylabel=None, xlim=None, ylim=None,
         line_styles=None, marker_styles=None, plot_type='plot', Color = None):
    """
    Función para graficar múltiples conjuntos de datos en un solo gráfico, donde cada conjunto de datos
    para el eje x tiene un conjunto de datos asociado para el eje y. También permite especificar estilos de línea
    y tipo de gráfico (plot o stem).

    Parámetros:
    - x_axes: Lista de arrays de datos para el eje x.
    - y_axes: Lista de arrays de datos para el eje y.
    - labels: Lista de etiquetas para cada conjunto de datos (opcional).
    - title: Título del gráfico (opcional).
    - xlabel: Etiqueta del eje x (opcional).
    - ylabel: Etiqueta del eje y (opcional).
    - xlim: Tupla de límites para el eje x (opcional).
    - ylim: Tupla de límites para el eje y (opcional).
    - line_styles: Lista de estilos de línea para cada conjunto de datos (opcional).
    - marker_styles: Lista de estilos de marcador para cada conjunto de datos (opcional).
    - plot_type: Tipo de gráfico ('plot' o 'stem'). Por defecto es 'plot'.
    """
    plt.figure(figsize=(10, 4))

    # Verificar que x_axes, y_axes, line_styles y marker_styles tengan la misma longitud
    if len(x_axes) != len(y_axes):
        raise ValueError("x_axes y y_axes deben tener la misma longitud.")

    # Graficar cada conjunto de datos
    for i, (x_axis, y_axis) in enumerate(zip(x_axes, y_axes)):
        style = line_styles[i] if line_styles and i < len(line_styles) else '-'
        marker = marker_styles[i] if marker_styles and i < len(marker_styles) else ''
        label = labels[i] if labels and i < len(labels) else None

        if plot_type == 'plot':
            plt.plot(x_axis, y_axis, style + marker, label=label, color = Color)
        elif plot_type == 'stem':
            plt.stem(x_axis, y_axis, linefmt=style, markerfmt=marker, basefmt=' ', label=label )
        else:
            raise ValueError("plot_type debe ser 'plot' o 'stem'.")

    # Configurar título y etiquetas de ejes si se especifican
    if title is not None:
        plt.title(title)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)

    # Configurar límites de los ejes si se especifican
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)

    if labels:
        plt.legend()

    plt.grid()
    plt.show()


# Zero padding
def apply_zero_padding(signal, n):
    # Agregar Zero padding
    signal_padded = np.pad(signal, (0, n ), mode='constant')

    # Calcular la FFT de la señal con padding
    fft_result_padded = np.fft.fft(signal_padded)

    # Calcular las frecuencias correspondientes
    frequencies_padded = np.fft.fftfreq(len(signal_padded), d=1)

    # Aplicar fftshift para centrar las frecuencias
    fft_result_padded_shifted = np.fft.fftshift(fft_result_padded)
    frequencies_shifted_padded = np.fft.fftshift(frequencies_padded)

    # Devolver la señal con padding, la FFT desplazada y las frecuencias desplazadas
    return signal_padded, fft_result_padded_shifted, frequencies_shifted_padded


# Actividad 2

# Crear una señal de ejemplo
M = 20
n = np.arange(M)
signal = np.sin(2 * np.pi * 0.2 * n)

# Calculo de la fft
fft_result = np.fft.fft(signal)
frequencies_original = np.fft.fftfreq(M, d=1)


# La función np.fft.fftfreq() devuelve las frecuencias correspondientes a cada bin de la FFT.
# Se debe usar esta función con el número total de puntos DESPUÉS del zero padding para obtener las frecuencias correctas.
# No es necesario aplicarla si no se hizo ni decimación ni interpolación.

#Llamado a la funcion
singal_padded, fft_result_padded_shifted, frequencies_shifted_padded = apply_zero_padding(signal, 0)
singal_padded20, fft_result_padded20_shifted, frequencies_shifted_padded20 = apply_zero_padding(signal, 20)
signal_padded40, fft_result_padded40_shifted, frequencies_shifted_padded40 = apply_zero_padding(signal, 40)
signal_padded80, fft_result_padded80_shifted, frequencies_shifted_padded80 = apply_zero_padding(signal, 80)


# Graficar ambas FFTs con la funcion plot

plot([frequencies_shifted_padded, frequencies_shifted_padded20, frequencies_shifted_padded40, frequencies_shifted_padded80],
     [np.abs(fft_result_padded_shifted), np.abs(fft_result_padded20_shifted) , np.abs(fft_result_padded40_shifted), np.abs(fft_result_padded80_shifted)],
     labels =['Sin padding', 'Con 20 ceros', 'Con 40 ceros', 'Con 80 ceros'], line_styles=['-', '--', '--', '--'], xlabel = 'frecuencia (Hz)', ylabel = 'Magnitud', plot_type = 'plot' )
