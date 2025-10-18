# result_system.py
"""
ResultSystem class to manage all students.
"""

from student import Student
from exceptions import StudentNotFoundError

class ResultSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        """Adds a Student object to the system."""
        self.students[student.student_id] = student

    def _get_student(self, student_id):
        """Internal helper to retrieve a student, raising an exception if not found."""
        student = self.students.get(student_id)
        if student is None:
            raise StudentNotFoundError(f"Student with ID '{student_id}' not found.")
        return student

    def add_subject_marks(self, student_id, subject_name, marks):
        """Finds student and adds marks to a subject."""
        student = self._get_student(student_id)
        student.add_subject(subject_name, marks)

    def generate_student_report(self, student_id):
        """Calls the student's report generation method."""
        student = self._get_student(student_id)
        return student.generate_report()

    def list_all_students(self):
        """Returns a list of summary strings for all students."""
        if not self.students:
            return ["No students registered in the system."]
            
        summary_list = ["--- All Registered Students ---"]
        for student in self.students.values():
            summary_list.append(str(student))
        summary_list.append("-------------------------------")
        return summary_list