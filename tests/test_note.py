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

    def test_note_init_name_throws_typeError_with_not_string(self):
        assert_that(Note).raises(TypeError).when_called_with(["Imie"], 2.0)

    def test_note_init_name_throws_exception_with_empty_string(self):
        assert_that(Note).raises(Exception).when_called_with("", 2.0)

    def test_note_init_note_throws_typeError_with_not_float(self):
        assert_that(Note).raises(TypeError).when_called_with("Andrzej", 2+1j)

    def test_note_init_note_throws_Exception_with_value_greater_than_6(self):
        assert_that(Note).raises(Exception).when_called_with("Andrzej", 6.1)

    def test_note_init_note_throws_Exception_with_value_smaller_than_2(self):
        assert_that(Note).raises(Exception).when_called_with("Andrzej", 1.999999999)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    main()
