from user import User

class Post:
    def __init__(self, content, likes, reply):
        self.content = content
        self.likes = likes
        self.reply = []

    def return_post(self):
        if User:
            try:
                if Post in self.posts:
                    return self.username, self.content, self.likes, self.reply
                else:
                    pass
            except ConnectionError:
                return "Error! Connection error.."
        else:
            pass

    def like(self):
        print("Liking post..")
        self.likes += 1

    def reply(self):
        replying = input("Reply:")
        self.reply.append(replying)
        