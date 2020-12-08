from unittest import TestCase, main
from unittest.mock import *
import assertpy
from assertpy import assert_that

from src.notes_service.notes_service import NotesService
from src.notes_storage.notes_storage import NotesStorage
from src.note.note import Note


class TestNotesService(TestCase):
    def setUp(self):
        self.temp = NotesService()

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_notes_service_get_all_notes_of(self, getAllNotesOf):
        self.temp.add(Note("Michał", 5.0))
        self.temp.add(Note("Michał", 4.5))
        self.temp.add(Note("Michał", 4.0))
        getAllNotesOf.return_value = [Note("Michał", 5.0), Note("Michał", 4.5), Note("Michał", 4.0)]
        assert_that(self.temp.averageOf("Michał")).is_equal_to(4.5)

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_notes_service_get_all_notes_of_nonexistent_student(self, getAllNotesOf):
        self.temp.add(Note("Michał", 3.5))
        getAllNotesOf.return_value = []
        assert_that(self.temp.averageOf("Andrzej")).is_equal_to("Name not found")

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_notes_service_get_all_notes_of_raises_typeError_with_not_str(self, getAllNotesOf):
        assert_that(self.temp.averageOf).raises(TypeError).when_called_with(["Michał"])

    @patch.object(NotesStorage, "add")
    def test_notes_service_add_raises_typeError_with_not_note_instance(self, add):
        add.side_effect = TypeError("note must be an instance of Note")
        assert_that(self.temp.add).raises(TypeError).when_called_with(["Michał", 4.0])

    def test_notes_service_clear(self):
        self.temp.add(Note("Michał", 3.5))
        self.temp.clear()
        self.temp.storage.notes = []
        assert_that(self.temp.storage.notes).is_equal_to([])

    def tearDown(self):
        self.temp = None
