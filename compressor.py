gamma = 1.4
cp = 1005  # J/kg-K

def compressor(T1, P1, pressure_ratio, efficiency):
    T2_ideal = T1 * (pressure_ratio)**((gamma-1)/gamma)
    T2 = T1 + (T2_ideal - T1)/efficiency
    
    P2 = P1 * pressure_ratio
    work = cp * (T2 - T1)
    
    return T2, P2, work