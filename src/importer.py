import tkinter as tk
from tkinter import filedialog

import numpy as np
from scipy.io import wavfile


def seleccionar_archivo_wav():
    try:
        # Crear la ventana principal de Tkinter (oculta)
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal

        # Abrir un cuadro de diálogo para seleccionar un archivo WAV
        archivo_wav = filedialog.askopenfilename(
            title="Seleccionar archivo WAV",
            filetypes=[("Archivos WAV", "*.wav")]
        )

        # Leer el archivo WAV; sample rate = frecuencia de muestreo, audio = señal de audio
        sample_rate, audio = wavfile.read(archivo_wav)

        # Si el audio tiene dos canales (estéreo), convertirlo a mono
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)

        nombre = archivo_wav.split("/")[-1]

    except Exception as e:
        nombre, sample_rate, audio = None, None, None
        print(f"Error al procesar el archivo: {e}")

    return nombre, sample_rate, audio

def guardar_archivo_wav(sample_rate, output_signal):
    try:
        # Crear la ventana principal de Tkinter (oculta)
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal

        # Abrir un cuadro de diálogo para guardar un archivo WAV
        archivo_wav = filedialog.asksaveasfilename(
            title="Guardar archivo WAV",
            filetypes=[("Archivos WAV", "*.wav")]
        )

        # Guardar la señal de salida en un archivo WAV
        wavfile.write(archivo_wav, sample_rate, output_signal.astype(np.int16))

    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


