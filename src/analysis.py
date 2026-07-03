"""
Funciones de análisis y registro de resultados de simulaciones conceptuales.
"""

from .bioem_model import TissueResponse


def resumen_respuesta(respuesta: TissueResponse) -> str:
    return (
        f"ΔNO ≈ {respuesta.delta_NO:.3f} (relativo), "
        f"ΔVm ≈ {respuesta.delta_vm:.3f} (relativo)"
    )
