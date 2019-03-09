
class Planet:

    def __init__(self, url, name, residents):
        self.url_id = url
        self.name = name
        self.residents_list = residents

    def __str__(self):
        return "{}".format(self.name)