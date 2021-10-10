###############
# Data preparation
###############
import csv
header = next(csv.reader(open('C:\\Labs\\Module1\\LAB\\M01_L02_Lab01\\linnerud.csv','r')))
header
import numpy as np
data = np.loadtxt('C:\\Labs\\Module1\\LAB\\M01_L02_Lab01\\linnerud.csv', delimiter=',', skiprows=1)
weights_pounds = data.T[1] # T is transpose
print('Header : ', header[1])
print(weights_pounds)


###############
# Processing data
###############




###############
# Calculate basic statistics
###############




###############
# Random choice
###############




###############
# Count by range
###############




