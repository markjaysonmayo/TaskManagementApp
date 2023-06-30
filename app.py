from datetime import datetime

# Connects python to mysql
pword = input("Enter password: ") # asks for the user's MariaDB password
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=pword,
    database="tasklistdb")
mycursor = mydb.cursor()

def insertTaskData(): # function for adding a task
    # Get task data
    iTitle = input("\nEnter task title: ")
    iDescription = input("Enter task description: ")
    # obtains date for deadline
    while True:
        iDeadline = input("Enter deadline (Format: YYYY-MM-DD): ")
        try:
            iDeadline = datetime.strptime(iDeadline, "%Y-%m-%d") # checks if the format is correct
            break
        except:
            print("Error in date format!")
    while True: # Select status
        iStatus = int(input("Select status of task ([0] Next up, [1] Missed, [2] In progress, [3] Done): "))
        if iStatus == 0:
            iStatus = "Next up"
            break
        elif iStatus == 1:
            iStatus = "Missed"
            break
        elif iStatus == 2:
            iStatus = "In progress"
            break
        elif iStatus == 3:
            iStatus = "Done"
            break   
        else:
            print("Invalid input!")         
    while True: # Ask user if the task will be added to a category
        addCategid = input("Add Task to a Category? (y/n): ")
        if addCategid == "y" or addCategid == "Y":
            selectAllCategory() #prints all the categories
            iCategid = input("Select category id: ")
            break
        elif addCategid == "n" or addCategid == "N":
            iCategid = None
            break
        else:
            print("Invalid input!")
            continue
    try:
        mycursor.execute("INSERT INTO task (title, description, deadline, status, categid) VALUES (%s, %s, %s,%s, %s)", (iTitle, iDescription, iDeadline, iStatus, iCategid))
        mydb.commit() #commit changes
        print("Task added successfully.")
    except:
        print("Invalid category!")

def insertCategory(): # function for adding a category
    iTitle = input("\nEnter category title: ")
    iDescription = input("Enter category description: ")

    mycursor.execute("INSERT INTO category(title, description) VALUES(%s,%s)",(iTitle,iDescription))
    mydb.commit()
    print("Category added successfully.")

def selectAllCategory(): # function for viewing all categories
    mycursor.execute("SELECT * FROM category")
    for x in mycursor:
        print("\nCategory ID: ", x[0])
        print("Title: ", x[1])
        print("Description: ", x[2])
        print("")


def selectAllTaskData(): # function for viewing all tasks
    mycursor.execute("SELECT * FROM task")
    for x in mycursor:
        print("\nTask ID: ", x[0])
        print("Title: ", x[1])
        print("Description: ", x[2])
        print("Deadline: ", x[3])
        print("Status: ", x[4])
        print("Category ID: ", x[5])
        print("")

def selectTask(): # function for viewing a task
    mycursor.execute("SELECT * FROM task")
    for x in mycursor:
        print("Task ID: ", x[0], "\tTitle: ", x[1])
    taskid = int(input("Enter task id: "))
    print()
    id = (taskid, )
    try:
        query = "SELECT * FROM task WHERE taskID=%s"
        mycursor.execute(query,id)
        taskRecord = mycursor.fetchone()
        
        print("Title: ", taskRecord[1])
        print("Description: ", taskRecord[2])
        print("Deadline: ", taskRecord[3])
        print("Status: ", taskRecord[4])
        print("Category: ", taskRecord[5])
        return taskid
    except:
        print("Task ID is invalid/does not exist!!")
        return None

def editTask(taskID): # function for editing and deleting a task
    if taskID == None:
        return
    # menu for editing specified task
    taskChoice = input("\n[1] Edit Title \n[2] Edit Description \n[3] Edit Deadline \n[4] Edit Status \n[5] Change/Remove from Category \n[6] Delete Task \n[7] Back \nSelect choice: ")
    if taskChoice == "1": #title
        uTitle = input("Enter new title: ") # stores the new title
        mycursor.execute("UPDATE task SET title = %s WHERE taskid = %s", (uTitle, taskID)) # changes the title of the task 
        mydb.commit() #commit changes
        print("Task title edited successfully.")

    elif taskChoice == "2": #description
        uDescription = input("Enter new description: ") # stores the new description
        mycursor.execute("UPDATE task SET description = %s WHERE taskid = %s", (uDescription, taskID)) # changes the description of the task 
        mydb.commit() #commit changes
        print("Task description edited successfully.")

    elif taskChoice == "3": #deadline
        while True:
            uDeadline = input("Enter deadline (Format: YYYY-MM-DD): ")
            try:
                uDeadline = datetime.strptime(uDeadline, "%Y-%m-%d") # checks if the format is correct
                break
            except:
                print("Error in date format!")
        mycursor.execute("UPDATE task SET deadline = %s WHERE taskid = %s", (uDeadline, taskID)) # changes the deadline of the task 
        mydb.commit() #commit changes
        print("Task deadline edited successfully.")

    elif taskChoice == "4": #status
        while True: # Select status
            uStatus = int(input("Select new status of task ([0] Next up, [1] Missed, [2] In progress, [3] Done): "))
            if uStatus == 0:
                uStatus = "Next up"
                break
            elif uStatus == 1:
                uStatus = "Missed"
                break
            elif uStatus == 2:
                uStatus = "In progress"
                break
            elif uStatus == 3:
                uStatus = "Done"
                break   
            else:
                print("Invalid input!") 
        mycursor.execute("UPDATE task SET status = %s WHERE taskid = %s", (uStatus, taskID)) # changes the status of the task 
        mydb.commit() #commit changes
        print("Task status edited successfully.")

    elif taskChoice == "5": #category
        while True: # Ask user if the category will be changed or removed from the task
            changeCategid = int(input("\n[1] Change Category \n[2] Remove from Category \nChoice: "))
            if changeCategid == 1:
                selectAllCategory() #prints all the categories
                uCategid = input("Select category id: ")
                break
            elif changeCategid == 2:
                uCategid = None
                break
            else:
                print("Invalid input!")
                continue
        try:
            mycursor.execute("UPDATE task SET categid = %s WHERE taskid = %s", (uCategid, taskID)) # changes the category of the task 
            mydb.commit() #commit changes
            print("Task category edited successfully.")
        except:
            print("Invalid category!")

    elif taskChoice == "6": # delete task
        delChoice = input("Delete this task? (y/n): ")
        if delChoice == 'y' or delChoice == 'Y':
            sql = "DELETE FROM task WHERE taskid =" + str(taskID)
            mycursor.execute(sql) # deletes the task 
            mydb.commit() #commit changes
            print("Task deleted successfully.")
        else:
            print("Task deletion aborted.")

    elif taskChoice == "7": # back
        return
    else:
        print("Invalid choice!")

def selectCategory(): # function for viewing a category
    mycursor.execute("SELECT * FROM category")
    for x in mycursor:
        print("Category ID: ", x[0], "\tTitle: ", x[1])
    categid = int(input("Enter category id: "))
    print()
    id = (categid, )
    try:
        query = "SELECT * FROM category WHERE categID=%s"
        mycursor.execute(query,id)
        categoryRecord = mycursor.fetchone()
        
        print("Title: ", categoryRecord[1])
        print("Description: ", categoryRecord[2])
        return categid
    except: #if the input of the user is invalid/specified category does not exist
        print("Category ID is invalid/does not exist!")
        return None

def editCategory(categID): # function for editing and deleting a category
    if categID == None:
        return
    # menu for editing category
    categChoice = int(input("\n[1] Edit Title \n[2] Edit Description \n[3] Delete Category \n[4] Back \nSelect choice: "))

    if categChoice == 1: # title
        uTitle = input("Enter new title: ") # stores the new title
        mycursor.execute("UPDATE category SET title = %s WHERE categid = %s", (uTitle, categID)) # changes the title of the category
        mydb.commit() # commit changes
        print("Category title edited successfully.")

    elif categChoice == 2: # description
        uDescription = input("Enter new description: ") # stores the new description
        mycursor.execute("UPDATE category SET description = %s WHERE categid = %s", (uDescription, categID)) # changes the title of the category
        mydb.commit() #commit changes
        print("Category description edited successfully.")

    elif categChoice == 3: # delete category
        delChoice = input("Delete this category? (y/n): ")
        if delChoice == 'y' or delChoice == 'Y':
            # remove connected tasks from the category to avoid errors
            mycursor.execute("UPDATE task SET categid = %s WHERE categid = %s", (None, categID))
            mydb.commit() #commit changes
            # then delete the category
            sql = "DELETE FROM category WHERE categid =" + str(categID)
            mycursor.execute(sql) # deletes the category
            mydb.commit() #commit changes
            print("Category deleted successfully.")
        else:
            print("Category deletion aborted.")

    else:
        print("Invalid choice!")



while True: # Main Menu
    choice = input("\n=== MAIN MENU === \n[1] Add Task  \n[2] Add Category \n[3] View All Tasks \n[4] View and Edit a Task  \n[5] View All Categories \n[6] View and Edit a Category  \n[7] Exit \nSelect choice: ")

    if choice == "1":
        insertTaskData()
    elif choice == "2":
        insertCategory()
    elif choice == "3":
        selectAllTaskData()
    elif choice == "4":
        taskID = selectTask() #runs the selectTask function and fetches the taskid from the user input
        editTask(taskID)
    elif choice == "5":
        selectAllCategory()
    elif choice == "6": #almost the same function as 'View and Edit a Task' option
        categID = selectCategory()
        editCategory(categID)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid input!")
    
