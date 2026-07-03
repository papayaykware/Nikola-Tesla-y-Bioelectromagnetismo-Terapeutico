"""
Interfaz NEXUS‑EEG: traducción conceptual de efectos EM en patrones EEG.
"""

from dataclasses import dataclass
from .bioem_model import TissueResponse


@dataclass
class EstadoEEG:
    delta: float
    theta: float
    alpha: float
    beta: float
    gamma: float
    descripcion: str


def respuesta_a_eeg(respuesta: TissueResponse) -> EstadoEEG:
    """
    Traducción conceptual:
    - ΔVm → modulación de ritmos rápidos (beta, gamma)
    - ΔNO → modulación de ritmos lentos (delta, theta, alpha)
    """

    delta = 1.0 + respuesta.delta_NO * 0.4
    theta = 1.0 + respuesta.delta_NO * 0.3
    alpha = 1.0 + respuesta.delta_NO * 0.2

    beta = 1.0 + respuesta.delta_vm * 0.5
    gamma = 1.0 + respuesta.delta_vm * 0.7

    return EstadoEEG(
        delta=delta,
        theta=theta,
        alpha=alpha,
        beta=beta,
        gamma=gamma,
        descripcion="Estado EEG conceptual derivado de estimación tisular"
    )
