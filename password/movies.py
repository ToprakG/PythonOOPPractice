class Movies:
    def __init__(self, title, description, image, topic, main_characters, event):
        self.title = title
        self.description = description
        self.image = image
        self.topic = topic
        self.main_characters = []
        self.event = event
    
    def get_topic(self):
        return self.topic
    
    def get_main_characters(self):
        return self.main_characters
    
    def calculate_title_len(self):
        return len(self.title)
    
    def say(self):
        print("Hi I am a movie.")
    
Harry = Movies("Harry Potter 1", "Harry discovers that he is a magician and invited to Hogwarts Wizarding School", "lol.png", "Harry Beating Voldemort", "Harry Potter, Hermione Granger, Ron Weasley", "Harry arrives to Hogwarts Wizarding School and meets Ron and Hermione which they will be friends forever. But Harry finds out that Voldemort is in the school.")
Harry.say()