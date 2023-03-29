from unittest import TestCase, main

from OOP.exercise_unittesting.student.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Angel', {'python': ['asd', 'rad']})
        self.guy = Student('Peter')

    def test_init(self):
        self.assertEqual('Angel', self.student.name)
        self.assertEqual({'python': ['asd', 'rad']}, self.student.courses)
        self.assertEqual({}, self.guy.courses)

    def test_if_course_is_in_courses(self):
        content = self.student.enroll('python', ['asd', 'rad'], 'hi')
        self.assertEqual("Course already added. Notes have been updated.", content)

    def test_course_is_not_in_courses_and_Y(self):
        content = self.student.enroll('math', 'some note', "Y")
        self.assertIn('some note', self.student.courses['math'])
        self.assertEqual("Course and course notes have been added.", content)

    def test_course_is_not_in_courses_and_empty(self):
        content = self.student.enroll('math', "some note", '')
        self.assertIn('some note', self.student.courses['math'])
        self.assertEqual("Course and course notes have been added.", content)

    def test_course_is_not_in_courses_and_notes_are_different(self):
        content = self.student.enroll('math', "hard", 'some note')
        self.assertEqual("Course has been added.", content)

    def test_add_notes_existing_course(self):
        content = self.student.add_notes('python', 'solid')
        self.assertEqual('Notes have been updated', content)

    def test_add_notes_non_existing_course(self):
        with self.assertRaises(Exception) as content:
            self.student.add_notes('py', 'solid')
        self.assertEqual("Cannot add notes. Course not found.", str(content.exception))

    def test_existing_leave_course(self):
        content = self.student.leave_course('python')
        self.assertEqual('Course has been removed', content)

    def test_non_existing_leave_course(self):
        with self.assertRaises(Exception) as content:
            self.student.leave_course('py')
        self.assertEqual("Cannot remove course. Course not found.", str(content.exception))


if __name__ == '__main__':
    main()
