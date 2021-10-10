###############
# Data preparation
###############
import csv
header = next(csv.reader(open('C:\\Labs\\Module1\\LAB\\M01_L02_Lab01\\linnerud.csv','r')))
header
import numpy as np
data = np.loadtxt('C:\\Labs\\Module1\\LAB\\M01_L02_Lab01\\linnerud.csv', delimiter=',', skiprows=1)
weights_pounds = data.T[1]

###############
# Processing data
###############
weights_kg = weights_pounds / 2.2046

###############
# Calculate basic statistics
###############
np.mean(weights_kg)
np.std(weights_kg)
np.min(weights_kg)
np.max(weights_kg)
np.median(weights_kg)

np.percentile(weights_kg,25)
np.percentile(weights_kg,50)
np.percentile(weights_kg,75)

###############
# Random choice
###############
index = np.random.randint(0,20,3)
print(weights_kg[index])

###############
# Count by range
###############
np.count_nonzero(weights_kg[(weights_kg < 70)])
np.count_nonzero(weights_kg[(weights_kg >= 70) & (weights_kg < 80)])
np.count_nonzero(weights_kg[(weights_kg >= 80) & (weights_kg < 90)])
np.count_nonzero(weights_kg[(weights_kg >= 90)])
