Car Showroom Management System

This is a Python script that implements a simple car showroom management system using MySQL as the database. The script allows you to perform various operations such as adding cars, managing employee details, sorting and filtering car lists, and contacting the showroom.

Prerequisites
To run this script, you need the following:
• Python: Make sure you have Python installed on your system. You can download
it from the official Python website (https://www.python.org).
• MySQL: Install MySQL on your system and set up the necessary database and
tables. Make sure you have the MySQL connector for Python installed. You can install it using the following command:
     pip install mysql-connector-python
     
Setup
Open the script in a text editor or an integrated development environment (IDE). Modify the following lines to provide the correct database connection details:
mycon = mysql.connector.connect(host='localhost', user='root',
passwd='********', database='Project')
• host: The hostname or IP address where MySQL is running.
• user: The username to connect to the database.
• passwd: The password for the specified user.
• database: The name of the database to use.

Usage
To run the script, execute the following command in your terminal or command prompt:
  python car_showroom.py
Once the script starts running, you will be prompted to choose whether you are a customer or an admin. Enter the appropriate option to proceed.
• If you choose "customer," you can view the list of cars, sort and filter the list, and contact the showroom.
• If you choose "admin," you will be prompted to enter a password. The default password is "passwd" or "Passwd" (without quotes).Once authenticated, you can manage the car list, and employee list, or switch to the customer view.
Follow the on-screen instructions to perform different operations based on the selected view (customer or admin).
