# Hospital-Records
The following is a project I submitted in school for final evaluation during my last year of highschool. The stated goal was to write a python code to do a couple of limited operation on an existing SQL database via python.
I decided to be a bit more ambitious and design a complete UI with the help of python that would simulate a "virtual" hospital with the help of two updatable tables for patients and staff members with varying levels of access for different people - patients, staff members and the administrator who has full control.
One can add new records, change existing records, delete records, create a new database from the python interface without ever interacting with MySQL directly.
My reference material- the school textbook - contained only a limited information on mysql-connector and class in python, which is the main library used for python-MySQL interaction. Therefore, I was forced to stumble my way through OOPs tutorials and mysql-connector docs to complete the project.
I tried using tkinter to develop a UI for my program, however due to my limited exposure to designing at the time, the process was slow-going and I was forced to drop the idea as the deadline drew close and multiple bugs kept cropping up. 

## What Can It Do?
I have decided to forgo the careful description of each function in the program in favour of elaborating what it can do.
The program is based on the setting that the user is visiting a hospital focused on covid patients.. The user might be a potential patient, an existing patient(or their relative), an employee, a job-seeker or the administrator.
 - A potential patient is asked a number of questions for covid symptoms and based on their score, they are diagnosed for covid, with results ranging from "negative" and "mild" to "How are you alive?!". If the patient is tested positive, they are required to provide information which is then saved as a new row in the table of patients in MySQL.
 - 
 - An existing patient can update information their information. Whenever a patient access their record, there is a chance that the patient condition deteriorates or improve. If the patient is tested negative or dies, their record is deleted from the database.
 - 

## Layout
The code is devided into three files-
  * addit.py
  * all_functions.py
  * project-menu.py
The project-menu file contain all the __main__ of the project, i.e., the part where user interacts with the code. The all_functions file contains all the functions which are used for interaction with MySQL databases and data manipulation. The addit file contains additional functions which are of use but not directly related to MySQL interaction.

## Future Plans
This program was my first big underdtaking as a project and while amititious and meticulously bug-free (or atleast able to catch all errors), the code is predictbly redundant in many places. Moreover, a lot of it could have been simplified if not improved if I had used some other libraries that I did know at the time - like numpy for handling data.
It was my first time using class independently (without a source to copy code from), and it shows. Most importantly, I was not able to create a GUI from tkinter.
Going forward, once I am more familiar with github, I would like to code a UI with tkinter or some other language better suited for it and complete this project by creating an actual GUI.
