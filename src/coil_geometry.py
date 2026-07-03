"""
Modelos geométricos simplificados de bobinas tipo Tesla
para estimación conceptual de inductancia y campo axial.
"""

from dataclasses import dataclass
from math import pi


@dataclass
class Coil:
    radio_m: float
    vueltas: int
    longitud_m: float

    def inductancia_aprox(self) -> float:
        """
        Fórmula aproximada de inductancia para solenoide largo:
        L ≈ μ0 * N^2 * A / l
        """
        mu0 = 4 * pi * 1e-7
        area = pi * self.radio_m**2
        return mu0 * (self.vueltas**2) * area / self.longitud_m

    def campo_axial(self, corriente_a: float) -> float:
        """
        Campo axial aproximado en el centro del solenoide:
        B ≈ μ0 * N * I / l
        """
        mu0 = 4 * pi * 1e-7
        return mu0 * self.vueltas * corriente_a / self.longitud_m
