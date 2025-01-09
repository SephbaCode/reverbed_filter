"""
Programa para aplicar filtros de reverberación a una señal de audio.
Autores:
        Joseph M. Sangurima
        José M. Solórzano
        Lenin S. Anguisaca
        """

import numpy as np
from matplotlib import pyplot as plt

from importer import seleccionar_archivo_wav, guardar_archivo_wav
from TFourier import transformada_fourier
from reverb_Aplication import ir_reverb_caja

def aplicar_reverb_caja(sample_rate, len_freqs, tf_audio):

    #introducir atenuacion ,periodo y reflexiones. si la entrada es vacia usar los valores por defecto
    print("Aplicando reverberación de caja...")

    atenuacion = input("Introduzca el valor de atenuación (0.6 por defecto): ")
    atenuacion = float(atenuacion) if atenuacion else 0.6

    periodo = input("Introduzca el valor del periodo (0.05 por defecto): ")
    periodo = float(periodo) if periodo else 0.05

    reflexiones = input("Introduzca el número de reflexiones (10 por defecto): ")
    reflexiones = int(reflexiones) if reflexiones else 10

    #crear respuesta al impulso
    tf_impulse_response, h_freqs = ir_reverb_caja(sample_rate, len_freqs, atenuacion, periodo, reflexiones)
    print("Respuesta al impulso aplicada correctamente")

    #multiplicar la transformada de fourier de la señal de audio por la respuesta al impulso
    print("Multiplicando la transformada de Fourier de la señal de audio por la respuesta al impulso...")
    tf_output_signal = tf_audio * tf_impulse_response

    plt.figure(figsize=(10, 6))
    plt.plot(freqs[:len(freqs) // 2], np.abs(tf_output_signal)[:len(freqs) // 2])
    plt.title("Transformada de Fourier de la señal de salida")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|Y(jw)|")
    plt.grid(True)
    plt.show()

    # Aplicar la transformada inversa de Fourier y guardar audio
    output_signal = np.fft.ifft(tf_output_signal).real
    print("Guardando señal de audio...")
    guardar_archivo_wav(sample_rate, output_signal)
    print("Señal de salida guardada correctamente")


# programa principal
print("Programa para aplicar filtros de reverberación a una señal de audio")
print("Seleccione un archivo WAV para aplicar el filtro de reverberación...")
# Seleccionar un archivo WAV
nombre, sample_rate, audio = seleccionar_archivo_wav()

if nombre is not None:
    print(f"El archivo WAV seleccionado es: {nombre}")

    tf_audio, freqs = transformada_fourier(audio, sample_rate)

    print("tf_audio:", len(tf_audio))
    print("freqs:", len(freqs))
    print("Transformada de Fourier aplicada correctamente")
    print("cantidad de Frecuencias:", len(freqs))

    #graficar la transformada de fourier
    if tf_audio is not None and freqs is not None:
        aplicar_reverb_caja(sample_rate, len(freqs), tf_audio)
    else:
        print("Error al aplicar la transformada de Fourier de la senial de entrada")






