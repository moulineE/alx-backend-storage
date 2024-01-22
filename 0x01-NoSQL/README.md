# 0x01. NoSQL

## Project Description

This project, part of the curriculum at Holberton School, focuses on working with NoSQL databases, specifically MongoDB. The project is designed to provide hands-on experience with MongoDB, Python, and PyMongo.

## Project Details

- **Authors:**
  - Emmanuel Turlay, Staff Software Engineer at Cruise
  - Guillaume, CTO at Holberton School
- **Weight:** 1
- **Start Date:** January 22, 2024, 4:00 AM
- **End Date:** January 24, 2024, 4:00 AM
- **Checker Release Date:** January 22, 2024, 4:00 PM
- **Auto Review:** Will be launched at the deadline

## Resources

Students are encouraged to read or watch the following resources to gain a better understanding of the concepts related to NoSQL and MongoDB:

- [NoSQL Databases Explained](#)
- [What is NoSQL?](#)
- [MongoDB with Python Crash Course - Tutorial for Beginners](#)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](#)
- [Aggregation](#)
- [Introduction to MongoDB and Python](#)
- [mongo Shell Methods](#)
- [The mongo Shell](#)

## Learning Objectives

By the end of this project, students are expected to be able to explain the following concepts without the help of Google:

### General

- What NoSQL means
- Difference between SQL and NoSQL
- ACID (Atomicity, Consistency, Isolation, Durability)
- Document storage
- NoSQL types
- Benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All files should end with a new line
- The first line of all files should be a comment: `// my comment`
- A `README.md` file, at the root of the project folder, is mandatory
- The length of your files will be tested using `wc`

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## More Info

For the installation of MongoDB 4.2 on Ubuntu 18.04, follow the official installation guide provided. Also, make sure to install PyMongo by running `pip3 install pymongo`.

If there are potential issues during the documents creation or if the error "Data directory /data/db not found., terminating" occurs, create the directory with the command `sudo mkdir -p /data/db`.

If `/etc/init.d/mongod` is missing, an example of the file is provided.

For running MongoDB in a container, you can use "container-on-demand." Ask for a container with Ubuntu 18.04 and MongoDB via SSH or WebTerminal. In the container, start MongoDB before using it with the command `$ service mongod start`.

## Tasks

### 0. List all databases

Write a script that lists all databases in MongoDB.

### 1. Create a database

Write a script that creates or uses the database `my_db`.

### 2. Insert document

Write a script that inserts a document in the collection `school` with the attribute name set to "Holberton school."

### 3. All documents

Write a script that lists all documents in the collection `school`.

### 4. All matches

Write a script that lists all documents with `name="Holberton school"` in the collection `school`.

### 5. Count

Write a script that displays the number of documents in the collection `school`.

### 6. Update

Write a script that adds a new attribute `address` with the value "972 Mission street" to all documents with `name="Holberton school"`.

### 7. Delete by match

Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.

### 8. List all documents in Python

Write a Python function that lists all documents in a collection.

### 9. Insert a document in Python

Write a Python function that inserts a new document in a collection based on kwargs.

### 10. Change school topics

Write a Python function that changes all topics of a school document based on the name.

### 11. Where can I learn Python?

Write a Python function that returns the list of schools having a specific topic.

### 12. Log stats

Write a Python script that provides some stats about Nginx logs stored in MongoDB.

## Usage

Follow the guidelines in the `README.md` for each task to run and test your scripts.

## Repository Information

- **GitHub Repository:** [alx-backend-storage](https://github.com/moulineE/alx-backend-storage)
- **Directory:** 0x01-NoSQL
- **Files:** Refer to the respective file names mentioned for each task in the tasks section.
