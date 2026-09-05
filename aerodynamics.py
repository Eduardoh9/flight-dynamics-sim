def calculate_lift_coefficient(cl_alpha, alpha, alpha_0=0.0):
    """Calcula el coeficiente de sustentacion (CL) en regimen subsonico."""
    return cl_alpha * (alpha - alpha_0)
EPSILON = 1e-9

def prandtl_glauert_correction(cl_incompressible, mach):
    """Aplica factor de correccion de Prandtl-Glauert para flujo compresible subsonico."""
    import math
    if mach >= 1.0:
        raise ValueError("Regimen transonico/supersonico no valido para Prandtl-Glauert")
    return cl_incompressible / math.sqrt(1.0 - mach**2)
