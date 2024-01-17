# 0x00. MySQL Advanced

## Back-end | SQL | MySQL

### By:
- Guillaume Plessis, Senior Cloud & System Engineer at WeWork
- Guillaume, CTO at Holberton School

### Project Overview

This project focuses on advanced MySQL concepts, providing hands-on experience with database design and optimization. By completing this project, you'll gain proficiency in creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers in MySQL.

### Project Schedule

- Start Date: Jan 17, 2024, 4:00 AM
- End Date: Jan 19, 2024, 4:00 AM
- Checker Release: Jan 17, 2024, 4:00 PM
- Auto Review: Deadline

### Concepts Covered

- Advanced SQL
- MySQL cheatsheet
- MySQL Performance: How To Leverage MySQL Database Indexing
- Stored Procedure
- Triggers
- Views
- Functions and Operators
- Trigger Syntax and Examples
- CREATE TABLE Statement
- CREATE PROCEDURE and CREATE FUNCTION Statements
- CREATE INDEX Statement
- CREATE VIEW Statement

### Learning Objectives

By the end of this project, you should be able to:

- Create tables with constraints
- Optimize queries by adding indexes
- Implement stored procedures and functions in MySQL
- Implement views in MySQL
- Implement triggers in MySQL

### Requirements

- Ubuntu 18.04 LTS and MySQL 5.7 (version 5.7.30)
- All files should end with a newline
- SQL queries should have comments just before them
- All files should start with a comment describing the task
- SQL keywords should be in uppercase
- README.md file at the root of the project folder

### Usage Information

- Use "container-on-demand" to run MySQL
- Connect via SSH or WebTerminal
- Start MySQL in the container using `$ service mysql start`
- Import a SQL dump using commands provided in the README

### Project Structure

The project is organized into several tasks, each focusing on a specific aspect of advanced MySQL concepts.

#### Task 0: We are all unique!
- Create a table 'users' with specific attributes.
- Make the 'email' attribute unique.

#### Task 1: In and not out
- Create a 'users' table with additional attributes.
- Use enumeration for the 'country' attribute.

#### Task 2: Best band ever!
- Rank country origins of bands based on the number of fans.

#### Task 3: Old school band
- List bands with Glam rock as their main style, ranked by longevity.

#### Task 4: Buy buy buy
- Create a trigger that decreases the quantity of an item after adding a new order.

#### Task 5: Email validation to sent
- Create a trigger that resets the 'valid_email' attribute only when the email has been changed.

#### Task 6: Add bonus
- Create a stored procedure 'AddBonus' that adds a new correction for a student.

#### Task 7: Average score
- Create a stored procedure 'ComputeAverageScoreForUser' that computes and stores the average score for a student.

#### Task 8: Optimize simple search
- Create an index on the table 'names' for the first letter of 'name'.

#### Task 9: Optimize search and score
- Create an index on the table 'names' for the first letter of 'name' and 'score'.

#### Task 10: Safe divide
- Create a function 'SafeDiv' that safely divides two numbers, handling division by zero.

#### Task 11: No table for a meeting
- Create a view 'need_meeting' that lists students with scores under 80 and no meeting or more than 1 month.

### How to Run

Follow the provided instructions to set up the MySQL container, import SQL dumps, and execute queries.

**Note:** This README serves as a guide for understanding and executing the tasks in the project. Make sure to read each task's specific instructions and utilize the provided resources for a better understanding of the concepts.

Feel free to explore and improve upon the provided solutions!

**Repository Information:**
- GitHub repository: [alx-backend-storage](https://github.com/moulineE/alx-backend-storage)
- Directory: 0x00-MySQL_Advanced
