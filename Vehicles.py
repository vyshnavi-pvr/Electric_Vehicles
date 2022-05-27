#from statistics import mean
import numpy as np
class Vehicle:

    Car,Style= [],[]
    Range=[]
    Transmission,VehicleType=[],[]
    PriceRangeMin,PriceRangeMax=[],[]

    PriceAvg=[]


    Capacity=[]
    BootSpace=[]
    BaseModel,TopModel=[],[]
    
    result=[]

    def __init__(self, Car,Style, Range,Transmission,VehicleType,PriceRangeMin,PriceRangeMax,Capacity,BootSpace,BaseModel,TopModel):
        self.Car.append(Car)
        self.Style.append(Style)
        self.Range.append(Range[:3])
        self.Transmission.append(Transmission)
        self.VehicleType.append(VehicleType)
        self.PriceRangeMin.append(float(PriceRangeMin))
        self.PriceRangeMax.append(float(PriceRangeMax))
        self.Capacity.append(Capacity[0])
        self.BootSpace.append(BootSpace[:3])
        self.BaseModel.append(BaseModel)
        self.TopModel.append(TopModel)
        #self.PriceAvg=[mean(i) for i in zip(PriceRangeMin, PriceRangeMax)]
        
    # PriceAvg=[mean(i) for i in zip(PriceRangeMin, PriceRangeMax)]
    # def mean(numbers):
    #     return float(sum(numbers)) / max(len(numbers), 1)
    #print (PriceAvg)        
    # PriceAvg=[mean(i) for i in zip(PriceRangeMin,PriceRangeMax)]
    def mean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)








