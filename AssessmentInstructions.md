#### Quarterly Assessment 3



### Overview

In this quarterly assessment, you will develop a comprehensive Quiz Bowl application with a graphical user interface (GUI). This project combines database management with frontend development to create a complete application experience.

## The application will have two major components:

- An administrator interface for managing quiz content (password-protected)

- A user interface for taking quizzes

# The topics of the questions (i.e., the “quiz” part) should be based in classes you are enrolled in

### Technical requirements

# Database Structure

- Create a database with 5 different tables (one for each course category)

- Each course table must contain at least 10 questions with corresponding answers

- Questions should include the question text, multiple-choice options, and correct answer

# Administrator Interface

- Implement a login screen with password protection for admin access

Create GUI forms for:
Adding new questions to the database
Viewing existing questions in the database
Deleting or modifying questions

- Include navigation between these different admin functions

# User Interface

- Create a welcome screen allowing users to select a quiz category

- Develop a quiz interface that:

- Displays questions with multiple-choice options

- Allows users to select and submit answers

- Provides immediate feedback on answers

- Tracks and displays the user's score

# Programming Requirements

- Implement a Question class to handle question display and answer validation

- Use proper error handling for database operations

- Follow object-oriented design principles

- Include appropriate comments and documentation



### Technical requirements

1. Application Entry Point

- Create a login screen that offers two paths:
Administrator access (password-protected)
Quiz taker access (no authentication required)

2. Administrator Workflow

- Create forms for:
Adding questions (category selection, question text, answer options, correct answer)
Viewing questions (filterable by category)
Modifying or deleting existing questions

3. Quiz Taker Workflow

- Welcome screen with category selection

- Quiz interface displaying questions one by one or all at once (your design choice)

- Answer submission and feedback mechanism

- Final score display


### Submission and Evaluation

# Submission Requirements

- Your GitHub repository should include:
All Python source code files
Database with preloaded data for your courses (I should be able to take the quiz)
README file with usage instructions
Commits showing progression
A copy of your schedule that shows your name and t-number



## Evaluation Criteria

- Your project will be evaluated based on:
Functionality of all features
User interface design and usability
Database design and implementation
Error handling and edge cases (i.e., I should not be able to “break” your application as a user)
Submission requirements met