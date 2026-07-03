"""
Generación conceptual de formas de onda para protocolos EM.
"""

import numpy as np


def onda_sinusoidal(t, frecuencia_hz, amplitud=1.0):
    return amplitud * np.sin(2 * np.pi * frecuencia_hz * t)


def onda_pulsada(t, frecuencia_hz, duty_cycle=0.5):
    periodo = 1.0 / frecuencia_hz
    fase = t % periodo
    return 1.0 if fase < duty_cycle * periodo else 0.0


def onda_modulada(t, frecuencia_portadora, frecuencia_moduladora, amplitud=1.0):
    moduladora = np.sin(2 * np.pi * frecuencia_moduladora * t)
    portadora = np.sin(2 * np.pi * frecuencia_portadora * t)
    return amplitud * moduladora * portadora
