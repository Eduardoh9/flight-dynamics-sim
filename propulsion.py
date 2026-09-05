def specific_net_thrust(v_exit, v_inlet, f_ratio):
    """Calcula el empuje neto especifico de un turbofan."""
    return (1 + f_ratio) * v_exit - v_inlet
