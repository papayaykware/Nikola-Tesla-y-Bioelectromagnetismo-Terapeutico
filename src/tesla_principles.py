"""
Modelos simplificados de principios de Tesla relevantes
para bioelectromagnetismo terapéutico.
"""

from math import pi


def frecuencia_resonante_lc(inductancia_h, capacitancia_f):
    """
    Calcula la frecuencia de resonancia de un circuito LC ideal.

    f = 1 / (2π * sqrt(L * C))
    """
    return 1.0 / (2.0 * pi * (inductancia_h * capacitancia_f) ** 0.5)


def energia_campo_bobina(inductancia_h, corriente_a):
    """
    Energía almacenada en una bobina ideal:

    E = 1/2 * L * I^2
    """
    return 0.5 * inductancia_h * corriente_a**2
