# Hospital-Records
The following is a project I submitted in school for final evaluation during my last year of highschool. The stated goal was to write a python code to do a couple of limited operation on an existing SQL database via python.
I decided to be a bit more ambitious and design a complete UI with the help of python that would simulate a "virtual" hospital with the help of two updatable tables for patients and staff members with varying levels of access for different people - patients, staff members and the administrator who has full control.
One can add new records, change existing records, delete records, create a new database from the python interface without ever interacting with MySQL directly.
I used **mysql.connector** python library for python-mysql interaction.
My reference material- the school textbook - contained only a limited information on mysql-connector and classes(OOPs). Therefore, I was forced to stumble my way through OOPs tutorials and mysql-connector docs to complete the project.
I tried using tkinter to develop a UI for my program, however due to my limited exposure to designing at the time, the process was slow-going and I was forced to drop the idea as the deadline drew close and multiple bugs kept cropping up. 

## What Can It Do?
I have decided to forgo the careful description of each function in the program in favour of elaborating what it can do.
The program is based on the setting that the user is visiting a hospital focused on covid patients. The user might be a potential patient, an existing patient(or their relative), an employee, a job-seeker or the administrator.
 - A potential patient is asked a number of questions for covid symptoms and based on their score, they are diagnosed for covid, with results ranging from "negative" and "mild" to "How are you alive?!". If the patient is tested positive, they are required to provide information which is then saved as a new row in the table of patients in MySQL.
 - Every new patient is assigned to a doctor with the minimum number of current patients. Every doctor's unique SID is saved on a seperate text file along with current number of patients.
 - An existing patient can access and update information their information. Any changes automatically updates the MySQL database. Whenever a patient access their record, there is a chance that the patient condition deteriorates or improve. If the patient is tested negative or dies, their record is deleted from the database and the number of patients of the related doctor is decreased.
 - An employee can also access and update their information. An employe can also resign, deleting their record.
 - A job seeker can assign for various (made-up) positions and fill other details. Each applicant's data is saved in the table of staff members awaiting inspection by the admin.
 - The admin has full control over the database. They can kick out any patient/employee, update any information, and access all records. The admin can review all the applicants and choose to select from them. Any new doctor is added to file 'attendants.txt' with 0 patients.
 - All the patients and staff members are assigned respectively unique ids and the each patient is provided an empty bed number To keep track of the different ids, these ids are saved in a text file seperately along with assigned bed numbers. (There are an infinite number of beds in the hospital.)
 - A patient/employee can search for their record by their unique ids or names.

## Layout
The code is contained within hree files-
  * addit.py
  * all_functions.py
  * project-menu.py
The project-menu file contain all the __main__ of the project, i.e., the part where user interacts with the code. The all_functions file contains all the functions which are used for interaction with MySQL databases and data manipulation. The addit file contains additional functions which are of use but not directly related to MySQL interaction.
There are 3 text files-
  * project.txt contain the unique patient and staff ids along with the assigned bed numbers.
  * attendants.txt contain the name of doctors along with the number of assigned patients.
  * host_data.txt contain the data necessary to access MySQL database, i.e, the host-name, user-name and password.

## Future Plans
This program was my first big underdtaking as a project and while amititious and meticulously bug-free (or atleast able to catch all errors), the code is predictbly redundant in many places. Moreover, a lot of it could have been simplified if not improved if I had used some other libraries that I did know at the time - like numpy for handling data.
It was my first time using class independently (without a source to copy code from), and it shows. Most importantly, I was not able to create a GUI from tkinter.
Going forward, once I am more familiar with github, I would like to code a UI with tkinter or some other language better suited for it and complete this project by creating an actual GUI.
