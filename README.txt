=== Task Record System ===
CMSC 127 Section ST-1L, Group 4
============================================

----------- DATABASE & DEV TEAM ------------
Cueto, Adrian
Esguerra, Joshua
Mayo, Mark Jayson
Rodriguez, Clarissa

============================================

---------- SOFTWARE REQUIREMENTS -----------
1. Python 3.x.x
2. MariaDB (https://mariadb.com/downloads/)
3. MySQL Connector for Python (install by running the command `pip install mysql-connector-python`)

============================================

---------- CONTENTS OF THE FILE -----------
1. app.py (main application)
2. setup.py (sets up the database)
3. README.txt (user guide)
4. tasklistdb.sql (sql dump file)

============================================

------ HOW TO SETUP AND USE THE APP --------
# SETUP the environment:
    1. Refer to the DBMS credentials:
        DATABASE: tasklistdb
        USER    : root
        passwd  : admin's personal passwd
    2. Install mysql connector: 
        Open or change the directory of your terminal to `group04_st1l` folder
        Run `pip install mysql-connector-python`

# USING setup.py: 
    1. Run `setup.py`:
        This creates the database 'tasklistdb' with the 'category' and 'task' tables
    2. Run `app.py`:
        Runs the DBMS app to manage the database

OR

# USING sql dump file (tasklistdb.sql):
    1. Locate where the sql file is using command prompt/terminal
    2. Access the MariaDB shell and login as root
    3. Run the ff. commands: 
        create database tasklistdb;
        use tasklistdb;
        source tasklistdb.sql;
    4. Run the `app.py` by simply double clicking it or by opening it in another terminal
    5. The program would ask to enter your MariaDB password
    6. Then, choose the instructions you wish to do in the menu

============================================

------------- FUNCTIONALITIES --------------
1. Add Task
    - This will create a new task and the user will be prompted to enter the ff:
        + Title
        + Description
        + Deadline (user must follow the "YYYY-MM-DD" format to avoid errors)
        + Status (Next up, Missed, In progress, Done)
        + Category
            -- The user must first create a category to be able to include it in the task.
            -- The user must decline the 'add task to category' statement if there are no categories yet to avoid errors.
            -- Categories will be selected using their Category ID (categid)
            -- Tasks can be created without categories (categid = NULL)
        NOTE: The taskid will be created automatically through auto-increment

2. Add Category
    - This will create a new category and the user will be prompted to enter the ff:
        + Title
        + Description
        NOTE: The categid will also be created automatically through auto-increment

3. View All Tasks
    - Prints all the details of the current tasks in the database

4. View and Edit a Task
    - The user will select a task from the existing tasks in the database.
    - The details of the selected task will then be displayed and another menu will be shown to edit the task
        + Edit Title (changes the title of the task)
        + Edit Description (changes the description of the task)
        + Edit Deadline (changes the deadline of the task)
        + Edit Status (changes the status of the task)
        + Change/Remove from Category
        + Delete Task
        + Back (returns back to the main menu)

5. View All Categories
    - Prints all the details of the current categories in the database

6. View and Edit a Category
    - The user will select a category from the existing categories in the database.
    - The details of the selected category will then be displayed and another menu will be shown to edit the category
        + Edit Title (changes the title of the task)
        + Edit Description (changes the description of the task)
        + Delete Category (Deletes the category and changes the categid of the connected tasks to NULL)
        + Back (returns back to the main menu)
7. Exit
    - Terminates the DBMS app

==============================