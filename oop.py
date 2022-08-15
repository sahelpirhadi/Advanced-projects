class mobile:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

class cpu(mobile):
    def get_name(self):
        print("This mobile has HighTech %s CPU " % self.name)
        
        
brand = cpu("Intel","Sony")
brand.get_name()
