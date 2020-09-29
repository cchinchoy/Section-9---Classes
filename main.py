"""Project name : Class Homework
    File name : main.py
    Programmer : Colin B. Chin Choy
"""

class Vehicle:
    def __init__(self,make,model,year,weight,needsmaintenance,tripsincemaintenance):
        self.Make = make
        self.Model = model
        self.Year = year
        self.Weight = weight
        self.NeedsMaintenance = False
        self.TripSinceMaintenance = 0
    def getMake(self):
        return self.Make
    def getModel(self):
        return self.Model
    def getYear(self):
        return self.Year
    def getWeight(self):
        return self.Weight
    def setMake(self,make):
        self.Make = make
    def setModel(set,model):
        self.Model = Model
    def setYear(self,year):
        self.Year = year
    def setWeight(self,weight):
        self.Weight = weight
    def Maintenance(self):
        if(self.TripSinceMaintenance>= 100):
            self.NeedsMaintenance = True

class Cars(Vehicle):
    def __init__ (self,make,model,year,weight,needsmaintenance,tripsincemaintenance,isdriving,repaired):
        Vehicle.__init__(self,make,model,year,weight,needsmaintenance,tripsincemaintenance)
        self.isDriving = False
        self.Repair = False
    def Drive(self):
        if self.NeedsMaintenance == True:
            self.isDriving = False
            print("Vehicle needs Maintenance and cannot be driven")
        else:
            self.isDriving = True
        if self.TripSinceMaintenance > 100:
            self.NeedsMaintenance = True
        else:
            self.TripSinceMaintenance += 1
    def Stop(self):
        self.isDriving = False
    def Repaired(self):
        self.TripSinceMaintenance = 0
        self.NeedsMaintenance = False
    def __str__(self):
        return("The "+self.Make+" "+self.Model+" made in "+str(self.Year)+" weighs "+str(self.Weight)+" needs maintenance: "+str(self.NeedsMaintenance)+" and is at "+str(self.TripSinceMaintenance)+" from 100 for maintenance")

class Planes(Vehicle):
    def __init__ (self,make,model,year,weight,needsmaintenance,tripsincemaintenance,isflying,repaired):
        Vehicle.__init__(self,make,model,year,weight,needsmaintenance,tripsincemaintenance)
        self.isFlying = False
        self.Repair = False

    def Fly(self):
        if self.NeedsMaintenance != True:
            self.isFlying = True
            if self.TripSinceMaintenance > 100:
                self.NeedsMaintenance = True
            else:
                self.TripSinceMaintenance += 1

    def Land(self):
        self.isFlying = False

    def Repaired(self):
        self.TripSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        return("The "+self.Make+" "+self.Model+" manufactured in "+str(self.Year)+" weighs "+str(self.Weight)+" needs maintenance: "+str(self.NeedsMaintenance)+" and is at "+str(self.TripSinceMaintenance)+" from 100 for maintenance")

def printCars():
    print(car1)
    print(car2)
    print(car3)

#--------------------------------------------------------------------------------------
car1 = Cars("Nissan","Sunny","2005","1200lbs",False,0,False,False)
car2 = Cars("Toyota","Sorento","2010","3200lbs",False,0,False,False)
car3 = Cars("Kia","Blaze","2015","2200lbs",False,0,False,False)
plane1 = Planes("Boeing","747","2005","52200lbs",False,0,False,False)

print("Setting car1 to TripSinceMaintenance to 100, then print....")
print("Setting car2 and car3 to varying numbers.....")
car1.TripSinceMaintenance = 100
car2.TripSinceMaintenance = 34
car3.TripSinceMaintenance = 65
print("\n")
printCars()
print("\n")
print("setting car1's drive switch then print again...")
print("\n")
car1.Drive()
print("\n")
printCars()
print("\n")
print("setting car to drive to see the switch change")
car1.Drive()
printCars()
print("\n")
printCars()
