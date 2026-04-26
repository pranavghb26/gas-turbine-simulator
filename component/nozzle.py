import math
cp = 1005

def nozzle(T4, T_ambient):
    # Exit velocity using energy equation
    V_exit = math.sqrt(2 * cp * (T4 - T_ambient))
    return V_exit