"""
Created by: Kyle Matthew
Created on: Feb 2026
This module does basic math
"""

from microbit import *
from time import *


display.clear()
display.sleep(10)

# given
display.scroll("A rectangle has dimensions 5 cm & 3 cm.")
display.sleep(10)

# In Perimeter
display.scroll("The perimeter would be:" + str(2*(5+3)))
display.sleep(10)

# In Area
display.scroll("The area would be:" + str(5*3))
display.sleep(10)
