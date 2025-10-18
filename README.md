# Student Result Management (Student Version)

student\_result\_system/
│── main.py          # Entry point (menu-driven interface)
│── subject.py       # Subject class
│── student.py       # Student class
│── result\_system.py # ResultSystem class (manages all students)
│── report.py        # Reporting functions
│── exceptions.py    # Custom exceptions
│── utils.py         # Helper functions (grade calculation, validation)
│── README.md        # Instructions for students



## Problem Statement

Create a system to manage student results. Each student has multiple subjects with marks. The system should generate average and performance reports.

## Topics Covered

* Classes \& Objects
* Lists and Dictionaries
* Exception Handling
* Reports \& Summaries
* Modular Programming

## Step-by-Step Workflow

1. Implement Subject class
2. Implement Student class
3. Implement ResultSystem class
4. Add grade calculation in utils
5. Add reporting functions
6. Build menu in main.py



\##Student Breakdown:

Student A → builds Subject + Student classes → handed to Student B.

Student B → builds ResultSystem, utils, exceptions using A’s models → handed to Student C.

Student C → builds report + main.py to integrate everything and provide user interface.

