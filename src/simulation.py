"""
Simulación conceptual del campo aplicado y respuesta tisular.
"""

import numpy as np
from .config import FieldParameters
from .coil_geometry import Coil
from .bioem_model import estimar_respuesta_tisular
from .waveforms import onda_sinusoidal, onda_pulsada, onda_modulada


def generar_campo(params: FieldParameters, coil: Coil, tiempo_s: float, pasos: int = 1000):
    t = np.linspace(0, tiempo_s, pasos)

    if params.forma_onda == "sinusoidal":
        onda = onda_sinusoidal(t, params.frecuencia_hz)
    elif params.forma_onda == "pulsada":
        onda = np.array([onda_pulsada(tt, params.frecuencia_hz) for tt in t])
    elif params.forma_onda == "modulada":
        onda = onda_modulada(t, params.frecuencia_hz, params.frecuencia_hz / 10)
    else:
        raise ValueError("Forma de onda no reconocida")

    # Campo axial generado por la bobina
    campo = coil.campo_axial(corriente_a=1.0) * onda
    return t, campo


def simular_protocolo(params: FieldParameters, coil: Coil):
    """
    Ejecuta una simulación conceptual completa:
    - Genera campo EM
    - Estima respuesta tisular
    """
    t, campo = generar_campo(params, coil, tiempo_s=params.duracion_min * 60)
    respuesta = estimar_respuesta_tisular(params)
    return t, campo, respuesta
