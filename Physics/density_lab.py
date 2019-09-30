"""
Some very simple data analysis for the results of the density lab

Cyrus | MIT License| 2019
"""
import math
import matplotlib.pyplot as plt
import numpy as np

small_cylinder = {
    "diameter":[2.355, 2.345, 2.34, 2.35, 2.34, 2.35, 2.35, 2.345, 2.34, 2.34], 
    "height":[2.35, 2.35, 2.36, 2.35, 2.35, 2.35, 2.345, 2.345, 2.355, 2.355], 
    "weight":[225.3, 225.2, 225.2, 225.2, 225.2, 225.3, 225.2, 225.2, 225.3, 225.2]}

large_cylinder = {
    "diameter":[4.255, 4.245, 4.25, 4.265, 4.26, 4.27, 4.26, 4.265, 4.26, 4.255], 
    "height":[4.59, 4.58, 4.58, 4.59, 4.58, 4.58, 4.62, 4.6, 4.58, 4.585], 
    "weight":[201.2, 201.2, 201.1, 201.2, 201.2, 201.2, 201.3, 201.3, 201.2, 201.2]} 

def std_err(data):
    mean = sum(data)/len(data)
    return (1/math.sqrt(len(data))) * math.sqrt(sum([(i - mean)**2 for i in data])/(len(data) - 1)) * 1/math.sqrt(len(data))

average = lambda data: sum(data)/len(data)

fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)
axs[0].hist(small_cylinder["diameter"], bins=12)
axs[1].hist(small_cylinder["height"], bins=12)
axs[2].hist(small_cylinder["weight"], bins=12)

print("SMALL CYLINDER: \nStd Err of diameter = ", std_err(small_cylinder["diameter"]))
print("Std Err of height = ", std_err(small_cylinder["height"]))
print("Std Err of weight = ", std_err(small_cylinder["weight"]))
print("Density (g/cm^3)= ", average(small_cylinder["weight"]) / (((average(small_cylinder["diameter"])/2)**2)*average(small_cylinder["height"])*math.pi))

plt.show()

fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)
axs[0].hist(large_cylinder["diameter"], bins=12)
axs[1].hist(large_cylinder["height"], bins=12)
axs[2].hist(large_cylinder["weight"], bins=12)

print("\nLARGE CYLINDER: \nStd Err of diameter = ", std_err(large_cylinder["diameter"]))
print("Std Err of height = ", std_err(large_cylinder["height"]))
print("Std Err of weight = ", std_err(large_cylinder["weight"]))
print("Density (g/cm^3)= ", average(large_cylinder["weight"]) / (((average(large_cylinder["diameter"])/2)**2)*average(large_cylinder["height"])*math.pi))
plt.show()
