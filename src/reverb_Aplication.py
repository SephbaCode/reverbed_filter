import numpy as np
from matplotlib import pyplot as plt

def ir_reverb_caja(sample_rate, n_samples):
    print("cantidad de muestras:", n_samples)
    # Parámetros de reverberación de caja
    a = 0.6  # Atenuación de las reflexiones
    T = 0.05  # Período entre reflexiones (segundos)
    delay_samples = int(T * sample_rate)  # Retardo en muestras

    # Crear la respuesta al impulso de la reverberación H(jw)
    impulse_response = np.zeros(n_samples)
    for n in range(10):  # Simular 10 ecos
        if n * delay_samples < n_samples:
            impulse_response[n * delay_samples] = a ** n

    # Calcular la transformada de Fourier de la respuesta al impulso
    tf_impulse_response = np.fft.fft(impulse_response)
    freqs = np.fft.fftfreq(n_samples, 1 / sample_rate)

    # Graficar la respuesta al impulso en el dominio de la frecuencia
    plt.figure(figsize=(10, 6))
    plt.plot(freqs[:n_samples // 2], np.abs(tf_impulse_response)[:n_samples // 2])
    plt.title("Transformada de Fourier de la respuesta al impulso")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|H(jw)|")
    plt.grid(True)
    plt.show()

    return tf_impulse_response, freqs