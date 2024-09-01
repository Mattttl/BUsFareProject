class vehicle:
    def __init__(self,capacity,name,mileage):
        self.capacity = capacity
        self.name = name
        self.mileage = mileage
    def fare(self):
        return self.capacity*100

class bus(vehicle):
    def fare(self):

        charge = super().fare()
        charge += charge*10/100
        return charge
obj = bus(50,"bus20",1012)
print("Total bus fare cost: ",obj.fare())