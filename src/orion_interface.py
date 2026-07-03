"""
Interfaz ORION‑AGI: representación computacional de estados metaestructurales.
"""

from dataclasses import dataclass
from .metaestructura import NodoMETFI, FlujoMETFI
from .sigma_t import OperadorSigmaT
from .nexus_eeg import EstadoEEG


@dataclass
class EstadoORION:
    nodos: list
    flujos: list
    eeg: EstadoEEG
    descripcion: str


def construir_estado_orion(nodos, flujos, eeg: EstadoEEG) -> EstadoORION:
    """
    Construye un estado conceptual para ORION‑AGI.
    """
    return EstadoORION(
        nodos=nodos,
        flujos=flujos,
        eeg=eeg,
        descripcion="Estado ORION‑AGI derivado de integración METFI‑SIGMA‑T‑NEXUS‑EEG"
    )
