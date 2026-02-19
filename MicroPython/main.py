"""
Created by: Kyle Matthew
Created on: Feb 2026
This module does basic math
"""

from microbit import *
from time import sleep


display.clear()
sleep(1)

# given
display.scroll("A rectangle has dimensions 5 cm & 3 cm.")
sleep(1)

# In Perimeter
display.scroll("The perimeter would be:" + str(2 * (5 + 3)))
sleep(1)

# In Area
display.scroll("The area would be:" + str(5 * 3))
sleep(1)
