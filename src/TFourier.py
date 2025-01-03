import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def transformada_fourier(audio, sample_rate):

    # Aplicar la transformada de Fourier
    tf_audio = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(audio), 1 / sample_rate)



    #graficar la transformada de fourier
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, np.abs(tf_audio))
    plt.title("Transformada de Fourier de la señal de audio")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|X(jw)|")
    plt.grid(True)
    plt.show()

    return tf_audio, freqs

#funcion para graficar X(jw),H(jw) y Y(jw)
def graficos(f_audio, freqs, impulse_response, output_signal):
    # visualizar la transformada de fourier de la señal de audio, la respuesta al impulso y la señal de salida
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(freqs, np.abs(f_audio))
    plt.title("Transformada de Fourier de la señal de audio")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|X(jw)|")
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(freqs, np.abs(impulse_response))
    plt.title("Transformada de Fourier de la respuesta al impulso")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|H(jw)|")
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(freqs, np.abs(output_signal))
    plt.title("Transformada de Fourier de la señal de salida")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|Y(jw)|")
    plt.grid(True)


