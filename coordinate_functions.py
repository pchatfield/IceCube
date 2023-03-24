import math

def cartesian(azimuth, zenith):
    x = math.cos(azimuth)*math.sin(zenith)
    y = math.sin(azimuth)*math.sin(zenith)
    z = math.cos(zenith)

    return x, y, z