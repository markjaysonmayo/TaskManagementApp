# Connects python to mysql
user_pass = input('Enter password: ')
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=user_pass) # Change passwd to your personal MariaDB passwd

# Displays the connection log
print(mydb)
if(mydb):
    print("\nSuccessfully connected.")
else:
    print("\nFailed to connect.")

# Setup the tasklistdb
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE database tasklistdb")
    print("Database 'tasklistdb' successfully created.")
except:
    print("Database creation failed or database already exists!")
mycursor.execute("USE tasklistdb")

# Creates category table
try:
    t1 = "CREATE TABLE category (categid int PRIMARY KEY AUTO_INCREMENT, title VARCHAR(30) NOT NULL, description VARCHAR(50))"
    mycursor.execute(t1)
    print("table 'category' successfully created.")
except:
    print("table 'category' creation failed.")

# Creates task table
try:
    t2 = "CREATE TABLE task (taskid int AUTO_INCREMENT,title VARCHAR(30), description VARCHAR(50), deadline DATE, status VARCHAR(50), categid INT(10), CONSTRAINT task_taskid_pk PRIMARY KEY(taskid), CONSTRAINT task_categid_fk FOREIGN KEY(categid) REFERENCES category(categid))"
    mycursor.execute(t2)
    print("table 'task' successfully created.")
except:
    print("table 'task' creation failed.")

