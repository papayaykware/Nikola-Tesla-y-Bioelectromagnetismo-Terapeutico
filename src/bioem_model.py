"""
Modelo fenomenológico mínimo de interacción CEM-tejido
para exploración conceptual (no clínico).
"""

from dataclasses import dataclass
from .config import FieldParameters


@dataclass
class TissueResponse:
    """
    Representa una respuesta simplificada del tejido:
    - delta_NO: cambio relativo en señalización de óxido nítrico
    - delta_vm: cambio relativo en potencial de membrana
    """
    delta_NO: float
    delta_vm: float


def estimar_respuesta_tisular(params: FieldParameters) -> TissueResponse:
    """
    Modelo toy: escala la respuesta en función de frecuencia, intensidad y duración.
    Los coeficientes son arbitrarios y sirven solo como marco conceptual.
    """
    escala_intensidad = params.intensidad_mt / 10.0
    escala_tiempo = params.duracion_min / 30.0

    # Frecuencias bajas vs medias: ponderación muy simplificada
    if params.frecuencia_hz < 100.0:
        factor_frecuencia = 0.7
    elif params.frecuencia_hz < 10_000.0:
        factor_frecuencia = 1.0
    else:
        factor_frecuencia = 0.4

    delta_NO = 0.1 * escala_intensidad * escala_tiempo * factor_frecuencia
    delta_vm = 0.05 * escala_intensidad * factor_frecuencia

    return TissueResponse(delta_NO=delta_NO, delta_vm=delta_vm)
