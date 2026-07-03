"""
Configuración básica de rangos y parámetros por defecto
para estudios de bioelectromagnetismo terapéutico inspirados en Tesla.
"""

from dataclasses import dataclass


@dataclass
class FieldParameters:
    frecuencia_hz: float
    intensidad_mt: float
    duracion_min: float
    forma_onda: str = "sinusoidal"


DEFAULT_PARAMS = FieldParameters(
    frecuencia_hz=1000.0,   # 1 kHz
    intensidad_mt=1.0,      # 1 mT
    duracion_min=10.0,
    forma_onda="sinusoidal",
)
