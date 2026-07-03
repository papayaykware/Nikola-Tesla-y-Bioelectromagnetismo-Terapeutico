"""
Motor metaestructural METFI para integrar modelos EM con niveles,
flujos e invariantes del ecosistema conceptual.
"""

from dataclasses import dataclass
from .bioem_model import TissueResponse
from .metaestructura import NodoMETFI, FlujoMETFI


@dataclass
class InvarianteMETFI:
    nombre: str
    valor: float
    descripcion: str


@dataclass
class OperadorMETFI:
    nombre: str
    descripcion: str

    def aplicar(self, flujo: FlujoMETFI) -> FlujoMETFI:
        """
        Operador conceptual: transforma la magnitud del flujo.
        """
        nuevo_flujo = FlujoMETFI(
            origen=flujo.origen,
            destino=flujo.destino,
            magnitud=flujo.magnitud * 1.1,  # ejemplo conceptual
            descripcion=f"{flujo.descripcion} + operador {self.nombre}"
        )
        return nuevo_flujo


def respuesta_a_niveles(respuesta: TissueResponse):
    """
    Traduce una respuesta tisular a nodos METFI en distintos niveles.
    """
    nodo_fisico = NodoMETFI("Campo EM", 1, "Estimulación electromagnética")
    nodo_bio = NodoMETFI("Tejido", 2, "Respuesta celular inicial")
    nodo_sistema = NodoMETFI("Sistema orgánico", 3, "Modulación fisiológica")

    flujo_1 = FlujoMETFI(nodo_fisico, nodo_bio, respuesta.delta_vm, "Acoplamiento EM-membrana")
    flujo_2 = FlujoMETFI(nodo_bio, nodo_sistema, respuesta.delta_NO, "Modulación bioquímica")

    return [nodo_fisico, nodo_bio, nodo_sistema], [flujo_1, flujo_2]


def calcular_invariantes(respuesta: TissueResponse):
    """
    Define invariantes metaestructurales derivados de la respuesta tisular.
    """
    inv_total = respuesta.delta_NO + respuesta.delta_vm

    return [
        InvarianteMETFI(
            nombre="Invariante de acoplamiento EM-biológico",
            valor=inv_total,
            descripcion="Suma conceptual de efectos eléctricos y bioquímicos"
        )
    ]
