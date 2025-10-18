# subject.py
"""
Subject class to store subject name and marks.
"""

class Subject:
    def __init__(self, name, marks):
        # Validate marks to be between 0 and 100
        if not 0 <= marks <= 100:
            raise ValueError(f"Marks for {name} must be between 0 and 100. Received: {marks}")

        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name}: {self.marks}"