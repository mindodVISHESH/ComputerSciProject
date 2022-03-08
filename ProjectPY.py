import mysql.connector
mycon = mysql.connector.connect(host='localhost', user='root', passwd='ALIbinsalem', database='Project')
if mycon.is_connected():
    print('Connection established sucessfully.')
else:
    print('Connection not established.')
cursor = mycon.cursor()
##########################################################################################################
cdatabase= "create database Project"
#cursor.execute(cdatabase)

#Employees_Admin
def create_Table_EMP():
    query='create table Employees(CODE int primary key,Position varchar(10),Name varchar(35),Salary int,DOJ date);'
    cursor.execute(query)
def add_emp():
    n=int(input('Enter the number of employees you want to enter:'))
    for i in range(n):
        a=int(input('Enter the CODE:'))
        b=input('Enter the position:')
        c=input('Enter the full name:')
        d=int(input('Enter the salary:'))
        e=input('Enter the date of joining(YYYY-MM-DD):')
        query="insert into Employees values(%s,%s,%s,%s,%s);"
        values=(a,b,c,d,e,)
        cursor.execute(query,values)
        mycon.commit()
        print("successfully added to table")
def show_ALL_EMP_names():
    query='select Name from Employees;'
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)
def show_emp():
    query='select * from Employees;'
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)
def change_salary():
    a = int(input('Enter the new salary:'))
    b = int(input('Enter the code of the employee you want to change the salary of:'))
    query = 'update Employees set salary=%s where CODE=%s;'
    values = (a, b)
    cursor.execute(query, values)
    mycon.commit()
def change_position():
    n = input('Enter new position :')
    e = input('Enter the code of the employee you want to change the position of :')
    query = 'update Employees set Position=%s where CODE=%s;'
    values = (n, e)
    cursor.execute(query, values)
    mycon.commit()
def remove_emp():
    a=int(input('Enter the Code of the employee you want to remove:'))
    query = 'delete from Employees where CODE = %s;'
    values = (a,)
    cursor.execute(query,values)
    mycon.commit()
#Customer_Table
def create_Table_cars():
    query='create table cars(CODE int primary key,Name varchar(35),Year int,Type char(3),Company varchar(30), Price int);'
    #Typeofcar
    #SUV,SED-sedan,SPT-sport
    cursor.execute(query)
def add_cars():
    n=int(input('Enter the number of cars you want to enter:'))
    for i in range(n):
        a=int(input('Enter the CODE:'))
        b=input('Enter the name of the car:')
        c=int(input('Enter the year it was produced:'))
        d=input('Enter the type of car(SUV or SED-sedan or SPT-sport):')
        e=input('Enter the company of the car:')
        f=int(input('Enter the price of car in DHS:'))
        g=int(input('Enter the stock of cas:'))
        h=input('Enter the color of car')
        query="insert into cars values(%s,%s,%s,%s,%s,%s,%s,%s);"
        values=(a,b,c,d,e,f,g,h)
        cursor.execute(query,values)
        mycon.commit()
        print("successfully added to table")
    show_cars()
def show_cars():
    query='select * from cars;'
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)
def change_price():
    s = input('Enter the CODE of the car you want to change the price of:')
    p = input('Enter new price of the car :')
    query = 'update cars set PRICE=%s where CODE=%s;'
    values = (p, s)
    cursor.execute(query, values)
    mycon.commit()
    show_cars()
def change_Color():
    s = input('Enter the CODE of the car you want to change the color of:')
    p = input('Enter new color of the car:')
    query = 'update cars set Color=%s where CODE=%s;'
    values = (p,s)
    cursor.execute(query, values)
    mycon.commit()
    show_cars()
def change_Stock():
    s = input('Enter the CODE of the car you want to change the stock of:')
    p = input('Enter new stock of the car:')
    query = 'update cars set Stock=%s where CODE=%s;'
    values = (p, s)
    cursor.execute(query, values)
    mycon.commit()
    show_cars()
def remove_car():
    a=int(input('Enter the Code of the car you want to remove:'))
    query = 'delete from cars where CODE = %s;'
    values = (a,)
    cursor.execute(query,values)
    mycon.commit()
    show_cars()
def Sortby():
    a=int(input('Enter (1)To sort by year\n(2)To sort by Increasing Price\n(3)To sort by Decresing Price\n(4)To sort by type of  car(SED,SUV,SPT)'))
    if a==1:
        query = 'Select * from cars order by years;'
        cursor.execute(query)
    elif a==2:
        query = 'Select * from cars order by Price ASC;'
        cursor.execute(query)
    elif a==3:
        query = 'Select * from cars order by Price DSC;'
        cursor.execute(query)
    elif a==4:
        query = 'Select * from cars order by Type;'
        cursor.execute(query)
def Filterby():
    a=int(input('Enter (1)To Filter by Year (2)To filter by Type'))
    if a == 1:
        s=input('Enter Year of car you are looking for (2019,2020)')
        query = 'Select * from cars where Year=%s'
        values = (s,)
        cursor.execute(query,values)
    elif a == 2:
        s = input('Enter Type of car you are looking for (SUV,SED,SPT)')
        l=s.upper()
        query = 'Select * from cars where Type=%s'
        values = (l,)
        cursor.execute(query,values)
def Contact_Us():
    t=1
    while t==1:
        a=int(input('Contact us by (1)Mail (2)Phone (3)Location\nEnter 1,2,3 or 4 to go back:\n'))
        if a ==1:
            print('This is our email:\nhelp@stomper.com')
        elif a==2:
            print('Call us on our toll free number:\n800-4357(HELP):\n')
        elif a==3:
            print('Visit us at:\n'
                '107, Warehouse Road\n'
                'Bussines Center\n'
                'Dubai, UAE')
        elif a==4:
            control()
        else:
            print('Try again')
#admin
def admin():
    n = input('Enter your password:')
    if n == 'passwd' or n == 'Passwd':
        a()
    else:
        print('Incorrect password')
def a():
    print('These are the controls:')
    w = int(input('Enter:\n(1)To manage the car list\n(2)To manage the employee list\n'))
    if w == 1:
        car()
    if w==2:
        emp()
def car():
     f = 1
     while f == 1:
         e = int(input(
             'Enter:\n(1)To See the list\n(2)To Add Cars\n(3)To Remove cars\n(4)To Change the price of a car\n(5)To Change Stock of the car\n(6)To Change the Color of the car\n'
             '(7)To go back\n(8)To exit:\n'))
         if e == 1:
             show_cars()
         if e == 2:
             add_cars()
         if e == 3:
             remove_car()
         if e == 4:
             change_price()
         if e==5:
            change_Stock()
         if e==6:
             change_Color()
         if e == 7:
             a()
         if e == 8:
             exit()
def emp():
    m = 1
    while m == 1:
        r = int(
            input('Enter:\n(1)To see the list\n(2)To add employee\n(3)To change salary\n(4)To change Positon'
                  '\n(5)To remove\n(6)To go back\n(7)To exit:\n'))
        if r == 1:
            show_emp()
        if r == 2:
            add_emp()
        if r == 3:
            change_salary()
        if r == 4:
            change_position()
        if r == 5:
            remove_emp()
        if r == 6:
            a()
        if r == 7:
            exit()
#customer
def customer():
    print("Welcome to the showroom")
    control()
def control():
    t = 1
    while t == 1:
        q = int(input('Please Enter\n(1)to view a list of cars available\n(2)to contact us\n(3)To Exit:\n'))
        if q == 1:
            show_cars()
        elif q == 2:
            Contact_Us()
        elif q == 3:
            quit()
        else:
            print('Try again')

print("Welcome to STOMPER Automobil Showroom ")
n=input('Are you a customer or admin :')
l=n.lower()
if l=="customer":
    customer()
elif l=="admin":
    admin()
else:
    print('Try again')
