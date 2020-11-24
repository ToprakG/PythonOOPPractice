class Website:
    def __init__(self, name, description, seo_optimized, code):
        self.name = name
        self.description = description
        self.seo_optimized = True or False
        self.code = "Private" or "Public"
    
    def get_name_and_description(self):
        print(self.name and self.description)
    
    def get_seo(self):
        return self.seo_optimized
    
    def say(self):
        print("Hi! I am a website.")
    
YouTube = Website("YouTube", "YouTube is the place for the best videos.", True, "Private")
YouTube.get_name_and_description()
print(YouTube.get_seo())
YouTube.say()