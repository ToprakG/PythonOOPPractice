class Writer:
    def __init__(self, )
class Books(Writer):
    def __init__(self, title, description, is_illustrated, writer, topic, total_pages):
        self.title = title
        self.description = description
        self.is_illustrated = True or False
        self.writer = writer
        self.topic = topic
        self.total_pages = total_pages
    
    def get_writer(self):
        return self.writer
    
    def get_is_illustrated(self):
        return self.is_illustrated
    
    def get_total_pages(self):
        return self.total_pages

    def say(self):
        print("I am a book lol.")

hello = Books("Hello", "This is lol", False, "Toprak", "Hello", 100)
hello.say()
print(hello.get_writer())