import csv
import numpy as np
import re
with open('colliders.csv', 'r') as f:
    reader = csv.reader(f)
    row = next(reader)
f.close()

print(type(re.findall(r"[-+]?\d*\.\d+|\d+", row[1])[1]))
#print('lon0: ', lon0)