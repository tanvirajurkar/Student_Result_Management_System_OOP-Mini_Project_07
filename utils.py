# utils.py
"""
Utility functions for calculations.

Functions:
- get_grade(average) → returns grade (A, B, C, Fail)
"""

def get_grade(average):
    """
    Returns the grade based on the student's average score.
    - A: 90–100
    - B: 75–89
    - C: 50–74
    - Fail: < 50
    """
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"