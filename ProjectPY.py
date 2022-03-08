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

#To Show List of Employees
def Show_Emp():
    query='select * from Employees;'
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)

#To Show List of Names of Employees
def Show_Emp_Names():
    query='select Name from Employees;'
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)

#To Add a Employee
def Add_Emp():
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

#To Remove a Employee
def Remove_Emp():
    a=int(input('Enter the Code of the employee you want to remove:'))
    query = 'delete from Employees where CODE = %s;'
    values = (a,)
    cursor.execute(query,values)
    mycon.commit()

#To Change Salary of Employee
def Change_Salary():
    a = int(input('Enter the new salary:'))
    b = int(input('Enter the code of the employee you want to change the salary of:'))
    query = 'update Employees set salary=%s where CODE=%s;'
    values = (a, b)
    cursor.execute(query, values)
    mycon.commit()

#To Change Position of Employee
def Change_Position():
    n = input('Enter new position :')
    e = input('Enter the code of the employee you want to change the position of :')
    query = 'update Employees set Position=%s where CODE=%s;'
    values = (n, e)
    cursor.execute(query, values)
    mycon.commit()

#To Show Cars Available for Sale
def Show_Cars():
    query='select * from cars;'
    cursor.execute(query)
    result=cursor.fetchall()
    for row in result:
        print(row)

#To Add New Cars Available for Sale
def Add_Cars():
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
    Show_Cars()

#To Remove Cars Available For Sale
def Remove_Car():
    a=int(input('Enter the Code of the car you want to remove:'))
    query = 'delete from cars where CODE = %s;'
    values = (a,)
    cursor.execute(query,values)
    mycon.commit()
    Show_Cars()

#To Change Price of Car Available for Sale
def Change_price():
    s = input('Enter the CODE of the car you want to change the price of:')
    p = input('Enter new price of the car :')
    query = 'update cars set PRICE=%s where CODE=%s;'
    values = (p, s)
    cursor.execute(query, values)
    mycon.commit()
    Show_Cars()

#To Change Colour of Car
def Change_Color():
    s = input('Enter the CODE of the car you want to change the color of:')
    p = input('Enter new color of the car:')
    query = 'update cars set Color=%s where CODE=%s;'
    values = (p,s)
    cursor.execute(query, values)
    mycon.commit()
    Show_Cars()

#To Change Stock of Car Available for Sale
def Change_Stock():
    s = input('Enter the CODE of the car you want to change the stock of:')
    p = input('Enter new stock of the car:')
    query = 'update cars set Stock=%s where CODE=%s;'
    values = (p, s)
    cursor.execute(query, values)
    mycon.commit()
    Show_Cars()

#To Sort the Cars Available for Sale
def Sortby():
    a=int(input('Enter\n(1)To sort by year\n(2)To sort by Increasing Price\n(3)To sort by Decresing Price\n(4)To sort by type of  car(SED,SUV,SPT)\n'))
    if a==1:
        query = 'Select * from cars order by Year;'
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    elif a==2:
        query = 'Select * from cars order by Price ASC;'
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    elif a==3:
        query = 'Select * from cars order by Price DESC;'
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    elif a==4:
        query = 'Select * from cars order by Type;'
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)

#To Filter the Cars Available for Sale
def Filterby():
    a=int(input('Enter (1)To Filter by Year (2)To filter by Type\n'))
    if a == 1:
        s=input('Enter Year of car you are looking for (2019,2020)')
        query = 'Select * from cars where Year=%s'
        values = (s,)
        cursor.execute(query,values)
        result = cursor.fetchall()
        for row in result:
            print(row)
    elif a == 2:
        s = input('Enter Type of car you are looking for (SUV,SED,SPT)')
        l=s.upper()
        query = 'Select * from cars where Type=%s'
        values = (l,)
        cursor.execute(query,values)
        result = cursor.fetchall()
        for row in result:
            print(row)

#To Contact Us
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
            Cust_Options()
        else:
            print('Try again')

#Password for Admin Module
def Admin():
    t=0
    while t<3:
        n = input('Enter your password:')
        if n == 'passwd' or n == 'Passwd':
            Admin_Controls()
        else:
            t=t+1
            print('Incorrect password. Please Try Again')
    print('Too many attempts. Please try again after some time.')

#All the Controls Available to the Admin
def Admin_Controls():
    print('These are the controls:')
    w = int(input('Enter:\n(1)To manage the car list\n(2)To manage the employee list\n(4)To go to Customer View\n(3)To Exit\n'))
    if w == 1:
        Car_Options()
    elif w == 2:
        Emp_Options()
    elif w==4:
        Customer()
    elif w == 3:
        exit()
    else:
        print('Invalid Input Detected. Please Try Again')
        Admin_Controls()

#Welcome for Customer
def Customer():
    print("Welcome to the showroom")
    Cust_Options()

#All the Options Availbale to the Customer
def Cust_Options():
    t = 1
    while t == 1:
        q = int(input('Please Enter\n(1)to view a list of cars available\n(2)To Sort the list\n(3)To Filter the list\n'
                      '(4)to contact us\n(5)To Exit:\n'))
        if q == 1:
            Show_Cars()
        elif q == 2:
            Sortby()
        elif q == 3:
            Filterby()
        elif q == 4:
            Contact_Us()
        elif q == 5:
            quit()
        else:
            print('Invalid Input Please Try Again')

#All the Options Available to the Admin to Modify the Cars List
def Car_Options():
    f = 1
    while f == 1:
        e = int(input('Enter:\n(1)To See the list\n(2)To Add Cars\n(3)To Remove cars\n(4)To Change the price of a car\n'
                      '(5)To Change Stock of the car\n(6)To Change the Color of the car\n(7)To go back\n(8)To exit:\n'))
        if e == 1:
            Show_Cars()
        elif e == 2:
            Add_Cars()
        elif e == 3:
            Remove_Car()
        elif e == 4:
            Change_price()
        elif e == 5:
            Change_Stock()
        elif e == 6:
            Change_Color()
        elif e == 7:
            Admin_Controls()
        elif e == 8:
            exit()
        else:
            print('Invalid Input Detected. Please Try Agian')

#All the Options Available to the Admin to Modify the Employees List
def Emp_Options():
    m = 1
    while m == 1:
        r = int(
            input('Enter:\n(1)To see the list\n(2)To see names of enployes\n(3)To add employee\n(4)To change salary\n(5)To change Positon'
                  '\n(6)To remove\n(7)To go back\n(8)To exit:\n'))
        if r == 1:
            Show_Emp()
        elif r == 2:
            Show_Emp_Names()
        elif r == 3:
            Add_Emp()
        elif r == 4:
            Change_Salary()
        elif r == 5:
            Change_Position()
        elif r == 6:
            Remove_Emp()
        elif r == 7:
            Admin_Controls()
        elif r == 8:
            exit()
        else:
            print('Invalid Input Detected. Please Try Again')
            Emp_Options()

#The First Command
def Start():
    try:
        print("Welcome to STOMPER Automobil Showroom ")
        n=input('Are you a customer or admin :')
        l=n.lower()
        if l=="customer":
            Customer()
        elif l=="admin":
            Admin()
        else:
            print('Invalid Input Detected. Please Try again')
            Start()
    except:
        print('Error Occured Please Try Agian.')
        Start()

Start()

