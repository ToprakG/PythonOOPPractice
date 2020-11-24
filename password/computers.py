class Computer:
    def __init__(self, name, age, model, operating_system):
        self.name = name
        self.age = age
        self.model = model
        self.operating_system = operating_system
    
    def get_name_and_age(self):
        print(self.name,self.age)
    
    def get_model(self):
        print(self.model)
    
    def get_os(self):
        print(self.operating_system)
    
    def say(self):
        print("hi!")
    
my_mac = Computer("Mac", 1, 2019, "MacOS")
my_mac.get_name_and_age()
my_mac.get_os()
my_mac.say()