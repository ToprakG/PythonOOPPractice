import time

class Country:
    def __init__(self, name, population, land_in_km, traditional_stuff, description_paragraph, average_earnings):
        self.name = name
        self.population = population
        self.land_in_km = land_in_km
        self.traditional_stuff = []
        self.description_paragraph = description_paragraph
        self.average_earnings = average_earnings
    
    def get_population(self):
        print(self.population)
    
    def get_description(self):
        print(self.description_paragraph)
    
    def get_average_earnings(self):
        print(self.average_earnings)
    
    def say(self):
        print("Hi! I am a country. Let me show you a short paragraph about me:")
        print(self.description_paragraph)
    
Turkey = Country("Turkey", 84000000, 100000, "Zeybek, Baklava, Horon", "Hi! My name is Turkey. I am connecting Asia to Europe. We have so many cultures in here for every region. For example, in Southeastern part of Turkey you will find the food capital Gaziantep. We are still developing but we are a strong country. Ataturk founded Turkey in 1923 when the Ottoman Empire fell. Ataturk made Turkey completely new. He got some laws, he loved children and he tried to make the education best level.", 2000)
Turkey.say()
time.sleep(20)
Turkey.get_population()
time.sleep(5)
Turkey.get_average_earnings()