# main.py
"""
Main entry point for Student Result Management System.
"""

from result_system import ResultSystem
from student import Student
from exceptions import StudentNotFoundError
from report import all_students_report

def get_valid_input(prompt, target_type=str):
    """Helper to safely get input and convert its type."""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("Input cannot be empty.")
            return target_type(value)
        except ValueError as e:
            print(f"⚠️ Invalid input: {e}. Please try again.")
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

def add_student_flow(result_system):
    """Handles the 'Add Student' menu choice."""
    print("\n--- Add New Student ---")
    try:
        student_id = get_valid_input("Enter Student ID: ")
        name = get_valid_input("Enter Student Name: ")
        
        new_student = Student(student_id, name)
        result_system.add_student(new_student)
        print(f"✅ Student {name} (ID: {student_id}) added successfully.")
    except Exception as e:
        print(f"❌ Failed to add student: {e}")

def add_subject_marks_flow(result_system):
    """Handles the 'Add Subject Marks' menu choice."""
    print("\n--- Add Subject Marks ---")
    try:
        student_id = get_valid_input("Enter Student ID to add marks: ")
        subject_name = get_valid_input("Enter Subject Name: ")
        marks = get_valid_input("Enter Marks (0-100): ", target_type=int)
        
        result_system.add_subject_marks(student_id, subject_name, marks)
        print(f"✅ Marks for {subject_name} added successfully to student {student_id}.")
        
    except StudentNotFoundError as e:
        print(f"❌ Error: {e}")
    except ValueError as e:
        print(f"❌ Data Error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def view_student_report_flow(result_system):
    """Handles the 'View Student Report' menu choice."""
    print("\n--- View Student Report ---")
    try:
        student_id = get_valid_input("Enter Student ID to view report: ")
        report = result_system.generate_student_report(student_id)
        print(report)
    except StudentNotFoundError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def main():
    result_system = ResultSystem()

    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. Add Subject Marks")
        print("3. View Student Report")
        print("4. View All Students")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == "1":
            add_student_flow(result_system)
        elif choice == "2":
            add_subject_marks_flow(result_system)
        elif choice == "3":
            view_student_report_flow(result_system)
        elif choice == "4":
            all_students_report(result_system)
        elif choice == "5":
            print("Exiting Student Result Management System. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()