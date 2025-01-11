import numpy as np
from matplotlib import pyplot as plt

def ir_reverb_caja(sample_rate, n_samples, atenuacion=0.6, periodo=0.05, reflexiones=10):

    # Crear la frecuencia angular normalizada
    freqs = np.fft.fftfreq(n_samples, d=1/sample_rate)
    omega = 2 * np.pi * freqs  # Frecuencia angular (rad/s)

    # Crear H(jw) como una suma de componentes de reflexión
    H_jw = np.ones(n_samples, dtype= np.complex128)  # Componente directa
    for k in range(1, reflexiones + 1):
        H_jw += atenuacion**k * np.exp(-1j * k * omega * periodo)

    # Graficar |H(jw)| en el rango de 0 a 1000 Hz
    plt.figure(figsize=(10, 6))
    plt.plot(freqs[:n_samples // 2], (np.abs(H_jw[:n_samples // 2]))**2)# Solo la parte positiva de las frecuencias

    plt.title("Respuesta al impulso H(jw)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("|H(jw)|")
    plt.grid(True)
    plt.xlim(0, 200)  # Limitar a 0-1000 Hz
    plt.show()

    # grafica de la fase de h_jw
    plt.figure(figsize=(10, 6))
    # parte positiva y negativa
    plt.plot(freqs[:n_samples // 2], np.angle(H_jw[:n_samples // 2]))
    plt.title("Fase de H(jw)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Fase")
    plt.grid(True)
    #  limitar de -100 a 1000 Hz
    plt.xlim(0, 100)
    plt.show()


    return H_jw, freqs