#!/usr/bin/env python3
# Author: Jude Flores
# Date:November 11th, 2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np
# Creating a 2D NumPy array
arr_2d = np.array([[10, 20, 30, 40, 50],[60, 70, 80, 90, 100],[110, 120, 130, 140, 150],[160, 170, 180, 190, 200]])
print(arr_2d)
slice_1 = arr_2d[0:2, -3:]
print("First two rows and last three columns\n",slice_1)
middle=arr_2d[1:3,1:3]
print("Middle 2x2 subarray \n", middle)
slice3 = arr_2d[::2, ::2]
print("Every other row and column \n", slice3)