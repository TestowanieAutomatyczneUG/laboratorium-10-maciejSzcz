# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

from unittest import TestCase, main
import assertpy
from assertpy import assert_that

from src.note.note import Note


class TestNote(TestCase):
    def setUp(self):
        self.temp = Note("Andrzej", 4.0)

    def test_note_init__creates_name(self):
        assert_that(self.temp).has_name("Andrzej")

    def test_note_init_creates_note(self):
        assert_that(self.temp).has_note(4.0)

    def test_note_init_null_name_throws_exception(self):
        assert_that(Note).raises(Exception).when_called_with(None, 4.0)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
