# NOTE: Baseline Aircraft is ATR-42 600
import numpy as np
import math
#----------------------DEFINING THE AIRCRAFT GEOMETRY----------------------
b=24.57 # span (m)
g=9.81 # gravity (m/s^2)
S=54.5 # wing area (m^2)
taper_r=0.53 # taper ratio
t_chr_ratio=0.18 # thickness-to-root chord ratio
t_tch_ratio=0.13 # thickness-to-tip chord ratio
i=2.5 # incidence angle (deg)
dihedral=3.5 # dihedral angle (deg)
sweep=3.1 # sweep angle (deg)
N=201 # number of spanwise sections
m_st_wing=2189 # structural weight of the wing (kg)
AR=b**2/S # aspect ratio
C_r=2*S/(b*(1+taper_r)) # root chord (m)
C_t=C_r*taper_r # tip chord (m)
y=np.linspace(-b/2,b/2,N) # spanwise positions (m)