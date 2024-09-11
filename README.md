# Car Showroom Management System

This Python project implements a **Car Showroom Management System** using **MySQL** as the backend database. The system allows for operations such as adding new cars, managing employee details, sorting and filtering the car list, and contacting the showroom. This system can be accessed in two modes: **Admin** and **Customer**.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Admin Operations](#admin-operations)
- [Customer Operations](#customer-operations)

## Features

- **Admin View**:
  - Add, remove, and manage cars in the showroom.
  - Manage employee details, such as adding new employees, changing salaries, and updating positions.
  - Sort and filter cars based on various parameters such as price, year of production, or type.
  - Admin authentication using a simple password system.

- **Customer View**:
  - View a list of available cars.
  - Sort and filter cars to help find specific vehicles.
  - Contact the showroom via phone, email, or by visiting the physical location.
  
## Prerequisites

Before running this project, you need to have the following installed on your system:

1. **Python 3.x**: Make sure you have Python installed. You can download it from the official [Python website](https://www.python.org).
2. **MySQL**: Install and set up MySQL. You can download it from [MySQL website](https://www.mysql.com).
3. **MySQL Connector for Python**: Install this connector to enable communication between Python and MySQL. You can install it using the following command:
   ```bash
   pip install mysql-connector-python
   ```

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine or download the zip file and extract it.

```bash
git clone https://github.com/your-username/car-showroom-management.git
```

### Step 2: Configure the MySQL Database

1. Open your MySQL client and create the required database and tables.
2. For the `Project` database, you can create tables like `Employees` and `Cars` with appropriate columns.

```sql
CREATE DATABASE Project;

USE Project;

CREATE TABLE Employees (
  CODE INT PRIMARY KEY,
  Position VARCHAR(50),
  Name VARCHAR(100),
  Salary INT,
  Joining_Date DATE
);

CREATE TABLE Cars (
  CODE INT PRIMARY KEY,
  Name VARCHAR(100),
  Year INT,
  Type VARCHAR(50),
  Company VARCHAR(100),
  Price INT,
  Stock INT,
  Color VARCHAR(50)
);
```

### Step 3: Configure the Python Script

Modify the following lines in your Python script to match your MySQL configuration.

```python
mycon = mysql.connector.connect(
    host='localhost', 
    user='root', 
    passwd='YourPasswordHere', 
    database='Project'
)
```

Replace the following details:
- `host`: The hostname where MySQL is running (default: `'localhost'`).
- `user`: The username to connect to the database (default: `'root'`).
- `passwd`: The password for your MySQL user.
- `database`: The name of your database (e.g., `Project`).

### Step 4: Run the Script

Once everything is set up, you can run the script:

```bash
python car_showroom.py
```

## Usage

When you run the script, you will be prompted to choose if you are an **Admin** or a **Customer**.

### Customer Mode

1. You can view the list of cars available for sale.
2. You can filter cars based on **Year** or **Type** (SUV, SED, SPT).
3. You can sort cars based on **Year** and **Price** (Ascending or Descending).
4. You can contact the showroom via phone, email, or by visiting the location.

### Admin Mode

1. You will be prompted for a password. The default password is `passwd` or `Passwd`.
2. Once logged in, you can manage:
   - **Car list**: Add, remove, update car details (price, stock, color).
   - **Employee list**: Add, remove, update employee details (salary, position).
3. Admins can also view the system as a customer by switching to **Customer Mode**.

## Admin Operations

The following operations are available in **Admin Mode**:

- **Car Operations**:
  - View all cars in the showroom.
  - Add new cars to the system.
  - Remove cars from the system.
  - Change the price, stock, and color of any car.
  - Sort cars by year, increasing or decreasing price.
  
- **Employee Operations**:
  - View all employee details.
  - Add new employees to the system.
  - Remove employees from the system.
  - Change the salary or position of any employee.
  
- **Switch to Customer Mode**: Admins can also switch to customer mode without logging out.

## Customer Operations

In **Customer Mode**, the following actions can be performed:

- View the list of cars available for sale.
- Sort cars based on different criteria:
  - By **Year**.
  - By **Price** (Ascending or Descending).
  - By **Type** (SUV, SED, or SPT).
  
- Filter cars by:
  - **Year** of production.
  - **Type** of car.
  
- Contact the showroom via:
  - **Email**.
  - **Phone** (Toll-free).
  - **Physical location** (Address provided).
