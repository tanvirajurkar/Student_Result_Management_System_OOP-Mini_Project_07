# student.py
"""
Student class to manage subjects and marks.
"""

from subject import Subject
from utils import get_grade

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = {}

    def add_subject(self, subject_name, marks):
        """Creates a Subject object and stores it in the student's subjects dictionary."""
        # The Subject constructor will handle the 0-100 validation
        subject = Subject(subject_name, marks)
        self.subjects[subject_name] = subject

    def calculate_average(self):
        """Calculates the total marks and average for the student."""
        if not self.subjects:
            return 0, 0.0

        total_marks = sum(subj.marks for subj in self.subjects.values())
        num_subjects = len(self.subjects)
        average = total_marks / num_subjects

        return total_marks, average

    def generate_report(self):
        """Generates a detailed report string for the student."""
        total_marks, average = self.calculate_average()
        grade = get_grade(average)

        report = f"\n--- Report for {self.name} ({self.student_id}) ---"
        report += "\n**Subject Marks:**"
        for subject_obj in self.subjects.values():
            report += f"\n  - {subject_obj}"

        report += "\n-------------------------------------"
        report += f"\nTotal Marks: {total_marks}"
        report += f"\nAverage: {average:.2f}"
        report += f"\nGrade: {grade}"
        report += "\n-------------------------------------"

        return report

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Subjects: {len(self.subjects)}"