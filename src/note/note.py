class Note(object):
    def __init__(self, name, note):
        self.name = name
        self.note = note

    @property #getter
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

    @property #getter
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        if type(value) != float:
            raise TypeError("note must be of float type")
        elif value > 6.0:
            raise Exception("note can't be bigger than 6.0")
        elif value < 2.0:
            raise Exception("note can't be smaller than 2.0")
        self._note = value
