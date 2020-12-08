from src.notes_storage.notes_storage import NotesStorage

class NotesService(object):
    def __init__(self):
        self.storage = NotesStorage()

    def add(self, note):
        self.storage.add(note)

    def averageOf(self, name):
        notes = self.storage.getAllNotesOf(name)
        
        if type(name) != str:
            raise TypeError("incorrect name type") 
        if not notes:
            return "Name not found"
        return sum(note.note for note in notes) / len(notes)

    def clear(self):
        self.storage.clear()