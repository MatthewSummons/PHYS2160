# 2(b).py
# Model  fitting the Volume Pressure of a peculiar gas
# Created by Shaheer Ziya on 17/3/2022 UTC+08 16:00

import matplotlib.pyplot as plt
import numpy as np
Polynomial = np.polynomial.Polynomial


# Volume in litres, Pressure in standard atmospheres
data = np.array((
  #  V      P
  (0.608, 0.05),
  (0.430, 0.10),
  (0.304, 0.20),
  (0.215, 0.40),
  (0.192, 0.50)
))

print(data[:][:0])
data = 1 / data[:0] 

