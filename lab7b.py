# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Jude Flores
# Date: November 11th, 2026
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

# TO DO 1: Copy the code from your lab7a.py file and paste here.
import numpy as np
list = []
for i in range(20, 50):
    list.append(i)
array1 = np.array(list)
array2 = np.arange(20, 50)
# TO DO 2: Reshape array1 reshapes array2 according to instructions given in readme.md file.
array1 = np.reshape(array1, (5, 6))
print("Array 1: \n",array1)
array2=np.reshape(array2, (2,3,5))
print("Array 2: \n",array2)
# TO DO 3: Create array5 according to instructions given in readme.md file.
array5 = np.zeros([5,5])
array5 = np.diag([45, 7, 61, 8, 9])
print("Array 5: \n",array5)
# TO DO 4: Create array6 according to instructions given in readme.md file.
array6 = np.random.randn(7,7)
print("Array6: \n", array6)
# TO DO 5: Run the script.

