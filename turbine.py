gamma = 1.4
cp = 1005

def turbine(T3, compressor_work, efficiency):
    # Required work (at least compressor work)
    required_work = compressor_work / efficiency

    T4 = T3 - required_work / cp
    work = cp * (T3 - T4)

    return T4, work