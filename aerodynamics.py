def calculate_lift_coefficient(cl_alpha, alpha, alpha_0=0.0):
    """Calcula el coeficiente de sustentacion (CL) en regimen subsonico."""
    return cl_alpha * (alpha - alpha_0)
