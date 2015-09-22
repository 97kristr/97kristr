class Crop:
    """En mat skörd"""
    #constructor

    def __init__(self, growth_rate, light_need, water_need, needs, report, set_growth, get_growth):
     #uppger alla attributer    
        self._growth = 0
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.light_need = light_need
        self.water_need = water_need
        self.status = "Seed"
        self.type = "Generic"
        self.needs = "Water and seed"
        self.report = "Needs more water"
        self.set_growth = growth_rate
        self.get_growth = self.days_growing*self.growth_rate
        
        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class
        
def main ():
    """en metod som innehåller alla print satser, dessa skriver ut svaren"""
    #instaniate the class
    new_crop = Crop(1,4,3,6,7,8,2)
    #test to see whether it works or not
    print(new_crop.status)
    print(new_crop.light_need)
    print(new_crop.water_need)
    print(new_crop.needs)
    print(new_crop.report)
    print(new_crop.set_growth)
    print(new_crop.get_growth)
    new_crop2 = Crop(2,5,7,1,8,3,6)
    print(new_crop2.status)
    print(new_crop2.light_need)
    print(new_crop2.water_need)
    print(new_crop2.needs)
    print(new_crop2.report)
    print(new_crop2.set_growth)
    print(new_crop2.get_growth)
        
    
if __name__ == "__main__":
    main()
    
