#!/usr/bin/env python3
# Author: Jude Flores
# Date:November 11th, 2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py
import numpy as np
array = np.random.rand(100)
print(array[:10])
print(array[89:])
print(array[21:51])
array[50:66] = 101
print(array[50:66])

