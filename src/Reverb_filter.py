"""
Programa para aplicar filtros de reverberación a una señal de audio.
Autores:
        JOSEPH MATEO SANGURIMA BACULIMA"""
import numpy as np
from matplotlib import pyplot as plt

from importer import seleccionar_archivo_wav, guardar_archivo_wav
from TFourier import graficos, transformada_fourier
from reverb_Aplication import ir_reverb_caja

nombre, sample_rate, audio = seleccionar_archivo_wav()

if nombre is not None:
    print(f"El archivo WAV seleccionado es: {nombre}")

    tf_audio, freqs = transformada_fourier(audio, sample_rate)

    print("tf_audio:", len(tf_audio))
    print("freqs:", len(freqs))
    print("Transformada de Fourier aplicada correctamente")
    print("cantidad de Frecuencias:", len(freqs))

    #menu para elegir el tipo de reverberacion
    print("Seleccione el tipo de reverberación:")
    print("1. Reverberación de caja")
    print("2. Reverberación de muelle")
    print("3. Reverberación de tubo")
    print("4. Reverberación de sala")
    print("Seleccione una opción:")
    #opcion = int(input())
    opcion = 1

    #graficar la transformada de fourier
    if tf_audio is not None and freqs is not None:
        if opcion == 1:
            print("Aplicando reverberación de caja...")
            impulse_response, h_freqs = ir_reverb_caja(sample_rate, len(freqs))
            print("Respuesta al impulso aplicada correctamente")
            print("cantidad de Frecuencias:", len(h_freqs))
            tf_output_signal = tf_audio * impulse_response

            #graficar tf_output_signal
            plt.figure(figsize=(10, 6))
            plt.plot(freqs, np.abs(tf_output_signal))
            plt.title("Transformada de Fourier de la señal de salida")
            plt.xlabel("Frecuencia (Hz)")
            plt.ylabel("|Y(jw)|")
            plt.grid(True)
            plt.show()




            # Aplicar la transformada inversa de Fourier
            output_signal = np.fft.ifft(tf_output_signal).real

            guardar_archivo_wav(sample_rate, output_signal)




