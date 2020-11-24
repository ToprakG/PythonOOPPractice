class Apps:
    def __init__(self, title, description, type, icon, image, code):
        self.title = title
        self.description = description
        self.type = type
        self.icon = icon
        self.image = []
        self.code = code
    
    def get_title_and_description(self):
        return self.title and self.description
    
    def get_type(self):
        return self.type
    
    def get_icon(self):
        return self.icon
    
    def get_image(self):
        return self.image
    
    def say(self):
        print("I am an app xD.")
    
facebook = Apps("FaceBook", "FaceBook is the place you can socialize!", "Social Media", "lol.png", "f.image, s.image, e.image", "Private")
facebook.say()
print(facebook.get_title_and_description())