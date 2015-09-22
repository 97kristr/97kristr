class Crop:
    """A generic food crop"""
    #constructor

    def __init__(self, growth_rate, light_need, water_need):
        #set the attributes with an initial value
        
        self._growth = 0
        self.days_growing = 0
        self.growth_rate = growth_rate
        self.light_need = light_need
        self.water_need = water_need
        self.status = "Seed"
        self.type = "Generic"
        
        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class
        
def main ():
    #instaniate the class
    new_crop = Crop(1,4,3)
    #test to see whether it works or not
    print(new_crop.status)
    print(new_crop.light_need)
    print(new_crop.water_need)
    new_crop2 = Crop(2,5,7)
    print(new_crop2.status)
    print(new_crop2.light_need)
    print(new_crop2.water_need)
    
if __name__ == "__main__":
    main()
