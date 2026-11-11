#!/usr/bin/env python3
# Author: Jude Flores
# Date: November 11th, 2026
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.
import pandas as pd
# TO DO 2: Create a series according to instructions given in readme.md file.

# TO DO 3: Perform the operations on this series given in readme.md file.

# TO DO 4: Run the script.
grade_list = ["<50", "50-59", "60-69", "70-79", "80-89", "90-100"]
grades=pd.Series(grade_list, index=["F", "D", "C", "B", "A", "A+"])
print(grades)
print(grades["C"])
print(grades.loc[["C", "A+"]])
print(grades.iloc[2])
print(grades*3)
