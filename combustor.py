cp = 1005  # J/kg-K

def combustor(T2, T3):
    q_in = cp * (T3 - T2)
    return T3, q_in