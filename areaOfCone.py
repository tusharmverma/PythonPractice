PI = 3.14
LOWER_RADIUS = 34
HEIGHT = 20 
TOP_RADIUS = 19
BASE = LOWER_RADIUS - TOP_RADIUS
L = ((BASE**2)+(HEIGHT**2))**0.5
area = PI*(LOWER_RADIUS+TOP_RADIUS)*L
print("L = ",L)
print("The Area {:.3f}".format(area))
