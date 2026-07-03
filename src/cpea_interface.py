"""
Interfaz conceptual entre bioelectromagnetismo y CPEA.
"""

from dataclasses import dataclass
from .bioem_model import TissueResponse


@dataclass
class EstadoCPEA:
    estabilidad: float
    coherencia: float
    descripcion: str


def respuesta_a_cpea(respuesta: TissueResponse) -> EstadoCPEA:
    """
    Traducción conceptual:
    - ΔNO → estabilidad sistémica
    - ΔVm → coherencia funcional
    """
    estabilidad = 1.0 + respuesta.delta_NO
    coherencia = 1.0 + respuesta.delta_vm

    return EstadoCPEA(
        estabilidad=estabilidad,
        coherencia=coherencia,
        descripcion="Estado conceptual derivado de estimación tisular"
    )
