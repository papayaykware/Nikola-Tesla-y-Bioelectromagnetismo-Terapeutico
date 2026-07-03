"""
Interfaz conceptual entre bioelectromagnetismo y TICAM (Toroidal Internal Cellular Activity Model).
"""

from dataclasses import dataclass
from .bioem_model import TissueResponse


@dataclass
class EstadoTICAM:
    coherencia_toroidal: float
    acoplamiento_em: float
    descripcion: str


def respuesta_a_ticam(respuesta: TissueResponse) -> EstadoTICAM:
    """
    ΔVm → acoplamiento EM
    ΔNO → coherencia toroidal (conceptual)
    """
    return EstadoTICAM(
        coherencia_toroidal=respuesta.delta_NO * 0.8,
        acoplamiento_em=respuesta.delta_vm * 1.2,
        descripcion="Estado toroidal conceptual derivado de estimación tisular"
    )
