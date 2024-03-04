import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="learning"
)
mycur=mydb.cursor()
#mycur.execute("create table employee (name varchar(35), age int, salary int)")
#mycur.execute("desc employee")
def list():
    mycur.execute("select * from employee")
    for i in mycur:
        print("Name: %s \t Age: %s \t Salary: %s" % i)
def add():
    name = input('Enter your Name: ')
    age = int(input('Enter your Age: '))
    salary = int(input('Enter your Salary: '))
    values = [(name, age, salary)]
    mycur.executemany("INSERT into employee values (%s,%s,%s)",
                       [(name, age, salary)])
    mydb.commit()
    print('Employee details added successfully\n')
def edit():
    name_to_be_edited = input('Enter the name to be edited: ')
    name = input('Enter your Name: ')
    age = int(input('Enter your Age: '))
    salary = int(input('Enter your Salary: '))
    mycur.execute("UPDATE employee set name=%s, age=%s, salary=%s where name=%s", (name, age, salary, name_to_be_edited))
    mydb.commit()
    print('Details updated successfully\n')
def delete():
    name_to_be_deleted = input('Please enter name to be deleted: ')
    mycur.execute("DELETE from employee where name=%s", (name_to_be_deleted,))
    mydb.commit()
    print("Employee deleted successfully\n")
option = -1
while True:
    print('========================================================================\n')
    print('Menu\n')
    print('Please select your input\n')
    print('1. List')
    print('2. Add')
    print('3. Edit')
    print('4. Delete')
    print('5. Exit')
    choice = int(input('Select your choice: '))
    if choice==1:
        list()
    elif choice==2:
        add()
    elif choice==3:
        edit()
    elif choice==4:
        delete()
    elif choice==5:
        break
    else:
        print("Invalid option")
