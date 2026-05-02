# Library Management CLI
A simple command-line Library Management System built with Python.
This project was developed as a beginner Python practice project. It uses basic Python concepts such as functions, dictionaries, lists, loops, conditionals, string methods, and input validation.
## Features
- Add suburbs with 2-digit suburb codes
- Add library members with 8-digit member IDs
- Validate member IDs based on suburb codes
- Add books and update book copies
- Allow members to borrow books
- Allow members to return books
- Track borrowed and available copies
- Prevent members from borrowing more than two books
- Prevent members from borrowing the same book twice
- Display a help menu with supported commands
## Commands
```text
ADD_SUBURB <Suburb_Name> <2-digit_Suburb_Code>
ADD_MEMBER <Member_Full_Name> <MemberID>
ADD_BOOK <Book_Name> <Number_of_Copies>
BORROW <MemberID> <Book_Name>
RETURN <MemberID> <Book_Name>
HELP
EXIT
```
## Example Usage
```text
ADD_SUBURB Miranda 22
ADD_MEMBER John_Smith 22123456
ADD_BOOK Python_Programming 3
BORROW 22123456 Python_Programming
RETURN 22123456 Python_Programming
HELP
EXIT
```
## How to Run
Run the program in the terminal:
```bash
python3 Library_system.py
```
Then enter commands after:
```text
Enter command:
```
## Technologies Used
- Python
- Command-line interface
- Dictionaries
- Lists
- Functions
- Loops
- Conditional statements
- Input validation
## Project Purpose
The purpose of this project is to practice basic Python programming and build a small command-based system. It focuses on data storage, input validation, and simple business logic for a library borrowing system.
## Notes
This project is designed as a beginner-level Python CLI project. It does not use classes or external libraries. The main goal is to practice fundamental programming skills and understand how to build a small interactive system using basic Python data structures.
