# """
# exocat

# Exoplanet Classification Code

# Authors: Benjamin Cadell
# Mélissa M. Azombo
# Khang Nguyen

# This script features the Mass classification component according to Plávalová and Rosaev (2024)
# Author @ Mélissa M. Azombo.
# """


import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt
import astropy
from astropy.constants import M_jup, GM_jup

print("M_jup", M_jup)                 # Jupiter mass in kg
print("M_jup.value", M_jup.value)           # numeric value
print("M_jup in kg", M_jup.to('kg'))        # explicit unit conversion

print(GM_jup)                # Jupiter GM in m3 / s2

M_Jup = M_jup.value

# Creating a class for the Mass subclassification

# Setting the class codes

mercury_class = "M"
earth_class = "E"
super_earth_subneptune_class = "S"
neptune_class = "N"
jupiter_class = "J"
dwarf_class = "D"

# Setting the class limits

# Mercury class limit < 0.0007M_Jup
mercury_class_upper_limit = 0.0007*M_Jup

# Earth class limit >= 0.0007M_Jup AND < 0.007M_Jup*
earth_class_upper_limit = 0.007*M_Jup

# SuperEarth/ SubNeptune limit >= 0.007M_Jup AND < 0.07M_Jup*
super_earth_subneptune_class_upper_limit = 0.07*M_Jup

# Neptune class limit >= 0.07M_Jup AND < 0.04M_Jup*
neptune_class_upper_limit = 0.04*M_Jup

# Jupiter class limit >= 0.04M_Jup AND <= 14M_Jup*
jupiter_class_upper_limit = 14*M_Jup

# * To not have crossover inbetween subclasses. Otherwise, these are all <= and will for now be coded as such



def exo_mass_subclass(masses):
    mass_classes = {mercury_class: []
                    earth_class: []
                    super_earth_subneptune_class: []
                    neptune_class: []
                    jupiter_class: []
                    dwarf_class: []
                    }  

    for m_p in masses:
        # Mercury class limit < 0.0007M_Jup
        if m_p < mercury_class_limit:
            mass_classes[mercury_class].append(m_p)

        # Earth class limit >= 0.0007M_Jup AND < 0.007M_Jup*
        elif m_p >= mercury_class_upper_limit AND <= earth_class_upper_limit:
            mass_classes[earth_class].append(m_p)

        # SuperEarth/ SubNeptune limit >= 0.007M_Jup AND < 0.07M_Jup*
        elif m_p >= earth_class_upper_limit AND <= super_earth_subneptune_class_upper_limit:
            mass_classes[super_earth_subneptune_class].append(m_p)

        # Neptune class limit >= 0.07M_Jup AND < 0.04M_Jup*
        elif m_p >= super_earth_subneptune_class_upper_limit AND <= neptune_class_upper_limit:
            mass_classes[neptune_class].append(m_p)

        # Jupiter class limit >= 0.04M_Jup AND <= 14M_Jup*
        elif m_p >= neptune_class_upper_limit AND jupiter_class_upper_limit:
            mass_classes[jupiter_class].append(m_p)
        
        # Dwarf class limit > 14M_Jup*
        elif m_p > jupiter_class_upper_limit:
            mass_classes[dwarf_class].append(m_p)
    return mass_classes
    for key, value in mass_classes.items():
        if value == m_p:
            return key

            
            


    




     