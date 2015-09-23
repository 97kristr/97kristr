import random

class Crop:
    """En mat skörd"""
    #constructor

    def __init__(self, growth_rate, light_need, water_need):
     #uppger alla attributer    
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        
        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class
        
    def needs(self):
        return('light need',self._light_need,'water need',self._water_need)
    
    def report(self):
        return('type',self._type,'status',self._status,'growth',self._growth,'days growing',self)
    
    def _update_status(self):
        if self._growth > 15:
            self._status = 'Old'
        elif self._growth > 10:
            self._status = 'Mature'
        elif self._growth > 5:
            self._status = 'Young'
        elif self._growth > 0:
            self._status = 'Seedling'
        elif self._growth == 0:
            self._status = 'Seed'
        
    def grow (self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        
        self._days_growing += 1
        
        self._update_status()
        
def auto_grow(Crop, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        Crop.grow(light,water)
        
def main ():
    """en metod som innehåller alla print satser, dessa skriver ut svaren"""
    #instaniate the class
    new_crop = Crop(1,4,3)
    #test to see whether it works or not
    print(new_crop.needs())
    print(new_crop.report())

    auto_grow(new_crop, 30)
        
    
if __name__ == "__main__":
    main()
    
