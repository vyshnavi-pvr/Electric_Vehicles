
#Import a CSV File into Python using Pandas
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

from Vehicles import Vehicle

# df = pd.read_csv (r'EVIndia.csv')
# print (df)

 
# with open('E:\info6105_datascience\EvVehicle\EVIndia.csv', 'r') as f:
#     data = list(csv.reader(f, delimiter=";"))
# data = np.array(data)
# print(data)


my_list = []

with open('E:\info6105_datascience\EvVehicle\EVIndia.csv', 'r') as f:
    reader = csv.reader(f)
   # next(reader)
    for row in reader:
        # v = Vehicle()
        
        my_list.append(Vehicle(row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8],row[9],row[10]))


# Car,Style= [],[]
#     Range=[]
#     Transmission,VehicleType=[],[]
#     PriceRange=[]
#     Capacity=[]
#     BootSpace=[]
#     BaseModel,TopModel=[],[]


print("Car--->",Vehicle.Car)
# print(Vehicle.Car[1])
print("range--->",Vehicle.Range)

# for x in Vehicle.Range: 
#     print(x)  

print("PriceRange Min--->",Vehicle.PriceRangeMin)
print("PriceRange Max--->",Vehicle.PriceRangeMax)



print("Capacity--->",Vehicle.Capacity)
print("BootSpace--->",Vehicle.BootSpace)

print("TopModel--->",Vehicle.TopModel)


#print([Vehicle.mean(i) for i in zip(Vehicle.PriceRangeMin, Vehicle.PriceRangeMax)])
for vehiclePriceRange in zip(Vehicle.PriceRangeMin, Vehicle.PriceRangeMax):
    Vehicle.PriceAvg.append(Vehicle.mean(vehiclePriceRange))

print("PriceRange Average--->",Vehicle.PriceAvg)
plt.plot(Vehicle.Range,Vehicle.PriceAvg)
plt.title("Plot")

   # Adding the labels
plt.ylabel("y-axis (PriceAvg)")
plt.xlabel("x-axis (Range)")
plt.show()