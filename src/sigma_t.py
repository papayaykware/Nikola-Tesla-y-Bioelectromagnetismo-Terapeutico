"""
Módulo SIGMA‑T: operadores sistémicos aplicados a estados METFI
derivados de bioelectromagnetismo terapéutico.
"""

from dataclasses import dataclass
from .metaestructura import NodoMETFI, FlujoMETFI
from .bioem_model import TissueResponse


@dataclass
class OperadorSigmaT:
    nombre: str
    factor: float
    descripcion: str

    def aplicar_a_flujo(self, flujo: FlujoMETFI) -> FlujoMETFI:
        """
        Aplica un operador SIGMA‑T a un flujo METFI.
        """
        return FlujoMETFI(
            origen=flujo.origen,
            destino=flujo.destino,
            magnitud=flujo.magnitud * self.factor,
            descripcion=f"{flujo.descripcion} | Operador SIGMA‑T: {self.nombre}"
        )

    def aplicar_a_respuesta(self, respuesta: TissueResponse) -> TissueResponse:
        """
        Aplica un operador SIGMA‑T directamente a la respuesta tisular.
        """
        return TissueResponse(
            delta_NO=respuesta.delta_NO * self.factor,
            delta_vm=respuesta.delta_vm * self.factor
        )


def operador_regenerativo():
    return OperadorSigmaT(
        nombre="Regenerativo",
        factor=1.15,
        descripcion="Potencia conceptual la respuesta regenerativa tisular"
    )


def operador_analgesico():
    return OperadorSigmaT(
        nombre="Analgesico",
        factor=0.85,
        descripcion="Reduce conceptual la excitabilidad tisular"
    )
