"""
Interfaz mínima para integrar modelos EM con la metaestructura METFI.
"""

from dataclasses import dataclass
from .bioem_model import TissueResponse


@dataclass
class NodoMETFI:
    nombre: str
    nivel: int
    descripcion: str


@dataclass
class FlujoMETFI:
    origen: NodoMETFI
    destino: NodoMETFI
    magnitud: float
    descripcion: str


def respuesta_a_flujo(respuesta: TissueResponse) -> FlujoMETFI:
    """
    Traduce una respuesta tisular conceptual a un flujo METFI.
    """
    origen = NodoMETFI("BioEM", 2, "Interacción campo-tejido")
    destino = NodoMETFI("Fisiología", 3, "Respuesta celular inicial")

    magnitud = respuesta.delta_NO + respuesta.delta_vm

    return FlujoMETFI(
        origen=origen,
        destino=destino,
        magnitud=magnitud,
        descripcion="Flujo conceptual derivado de estimación tisular",
    )
