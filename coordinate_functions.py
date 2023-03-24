import math

def cartesian(azimuth, zenith):
    x = math.cos(azimuth)*math.sin(zenith)
    y = math.sin(azimuth)*math.sin(zenith)
    z = math.cos(zenith)

    return x, y, z

def spherical(x,y,z):
    zenith = math.acos(z/math.sqrt(x**2 + y**2 + z**2))
    azimuth = math.atan2(y,x)