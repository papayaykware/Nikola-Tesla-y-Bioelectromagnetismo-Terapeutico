"""
Definición de protocolos estándar de exploración bioelectromagnética.
"""

from .config import FieldParameters


def protocolo_regeneracion_basico() -> FieldParameters:
    return FieldParameters(
        frecuencia_hz=50.0,
        intensidad_mt=2.0,
        duracion_min=20.0,
        forma_onda="pulsada",
    )


def protocolo_dolor_cronico() -> FieldParameters:
    return FieldParameters(
        frecuencia_hz=1000.0,
        intensidad_mt=1.0,
        duracion_min=15.0,
        forma_onda="modulada",
    )
