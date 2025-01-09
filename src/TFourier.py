import numpy as np
import matplotlib.pyplot as plt

def transformada_fourier(audio, sample_rate):

    # Aplicar la transformada de Fourier
    tf_audio = np.fft.fft(audio)
    freqs = np.fft.fftfreq(len(audio), 1 / sample_rate)

    # Graficar la transformada de Fourier
    plt.figure(figsize=(10, 6))
    plt.plot(freqs[:len(freqs) // 2], np.abs(tf_audio)[:len(freqs) // 2])
    plt.title("Transformada de Fourier (Espectro Positivo)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|X(jw)|")
    plt.grid(True)
    plt.show()

    return tf_audio, freqs


