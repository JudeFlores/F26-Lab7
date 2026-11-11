#!/usr/bin/env python3
# Author:Jude Flores
# Date:November 11th, 2026
# Purpose: Create Arrays.
# Usage: ./lab7a.py

#1
import numpy as np
list = []
for i in range(20, 50):
    list.append(i)
array1 = np.array(list)
array2 = np.arange(20, 50)
print(array1)
print(array2)
#2
array3 =np.arange(1,10).reshape(3,3)
print(array3)
#3
array4 = np.array([[["january", "February"], ["March", "April"], ["May", "June"]],
                    [["July", "August"], ["September", "October"], ["November", "December"]]])
print (array4)