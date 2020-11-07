class User:
    def __init__(self, name, surname, username, icon, posts):
        self.name = name
        self.surname = surname
        self.username = username
        self.icon = icon
        self.posts = []

    def get_icon(self):
        return self.icon

    def get_posts(self):
        return self.posts
