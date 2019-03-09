class Person:

    def __init__(self, url, name, home_world):
        self.url_id = url
        self.name = name
        self.home_world = home_world

    def __str__(self):
        return "{}".format(self.name)