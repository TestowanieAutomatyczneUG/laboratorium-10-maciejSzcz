class Note(object):
    def __init__(self, name, note):
        self.name = name
        self.note = note

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == None:
            raise Exception("name can't be null")
        elif type(value) != str:
            raise TypeError("name must be of string type")
        elif value == "":
            raise Exception("name can't be empty")
        self._name = value
