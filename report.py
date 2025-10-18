# report.py
"""
Reporting functions for Student Results.
"""

def student_report(student):
    """Prints a detailed report for a single student."""
    print(student.generate_report())

def all_students_report(result_system):
    """Prints a summary report for all students in the system."""
    for summary_line in result_system.list_all_students():
        print(summary_line)