# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:50:37 2013

@author: Sven
"""

import numpy as np
import matplotlib.pyplot as plt

# test program
print "Hello, this is a test of git."
print "This is now a much better script."

a = np.linspace(0., 10., 400)
y = np.sin(a)
plt.plot(a, y)