class Extensions:
    def __init__(self, title, description, icon, version, manifest_json, programming_languages):
        self.title = title
        self.description = description
        self.icon = icon
        self.version = version
        self.manifest_json = True
        self.programming_languages = []
    
    def get_title_and_description(self):
        return self.title and self.description
    
    def get_icon(self):
        return self.icon
    
    def get_manifest_json(self):
        return self.manifest_json
    
    def get_programming_languages(self):
        return self.programming_languages
    
    def say(self):
        print(self.title, self.description, self.icon)

quicksearcher = Extensions("QuickSearcher", "QuickSearcher brings trusted resources in to your hands!", "eee.png", 1.0, True, "JavaScript, Python")
quicksearcher.say()