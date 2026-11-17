# Voting-Eligibility-System

Project Overview

The Voting Eligibility System is a Python-based project designed to check whether a person is eligible to vote in India.

The program takes the person’s name, age, and Indian citizenship status as input. It checks the eligibility criteria and displays whether the person is eligible or not eligible to vote, along with the reason for ineligibility.

The program also allows users to check multiple voters and displays the total number of voters checked, eligible voters, and ineligible voters.

Features

* Accepts the person’s name, age, and citizenship status.
* Checks voting eligibility based on age and Indian citizenship.
* Uses functions to perform eligibility checks.
* Uses if-elif-else conditional statements.
* Handles invalid age input using try-except.
* Validates age between 0 and 120.
* Prevents empty name input.
* Accepts citizenship status in yes/no format.
* Uses while loops for repeated user input.
* Displays reasons for ineligibility.
* Calculates total voters, eligible voters, and ineligible voters.

Eligibility Criteria

A person is eligible to vote if:

1. The person’s age is 18 years or above.
2. The person is an Indian citizen.

Both conditions must be satisfied.

Technologies Used

* Programming Language: Python 3
* Code Editor: Visual Studio Code

Python Concepts Used

* Variables and Data Types
* Functions
* If-Elif-Else Statements
* While Loops
* Try-Except Exception Handling
* Return Statements
* String Methods (strip() and lower())
* User Input and Output

How to Run the Project

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the Python file.
4. Open the terminal.
5. Run the following command:

python voting_eligibility.py

6. Enter the required details when prompted.

Sample Output

Enter your name: Aman
Enter your age: 25
Are you an Indian citizen? (yes/no): yes
Aman is eligible to vote.
Do you want to check another voter? (yes/no): no
Total voters checked: 1
Eligible voters: 1
Ineligible voters: 0

Invalid Input Handling

The program handles different invalid inputs:

* Empty name.
* Non-numeric age.
* Age below 0 or above 120.
* Invalid citizenship response.
* Invalid response when checking another voter.

Learning Outcomes

Through this project, I learned:

* How to create and call Python functions.
* How to use conditional statements.
* How to implement while loops.
* How to handle errors using try-except.
* How to validate user input.
* How to use return True and return False.
* How to maintain counters using variables.
* How to implement real-life decision-making logic using Python.

Conclusion

The Voting Eligibility System is a simple Python project that demonstrates the practical application of basic programming concepts. It provides an easy way to check voting eligibility, handles invalid inputs, and maintains voter statistics.
