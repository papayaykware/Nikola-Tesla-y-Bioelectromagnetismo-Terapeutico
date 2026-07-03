"""
Esquema programático del dispositivo inspirado en Tesla:
generador, bobina, acoplamiento y sensores.
"""

from dataclasses import dataclass
from .config import FieldParameters
from .bioem_model import estimar_respuesta_tisular, TissueResponse


@dataclass
class TeslaInspiredDevice:
    nombre: str
    params: FieldParameters

    def aplicar_protocolo(self) -> TissueResponse:
        """
        Ejecuta un 'protocolo' conceptual y devuelve la respuesta tisular estimada.
        """
        return estimar_respuesta_tisular(self.params)
