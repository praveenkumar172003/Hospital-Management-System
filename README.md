# Hospital Management System
## Overview
The Hospital Management System (HMS) is a software application designed to manage patient and prescription data. It facilitates storing, updating, and viewing patient information and prescription details, making the process easier for hospital management and healthcare staff.
## Features
* **Patient Information Management:** Capture key patient details such as Patient ID, Name, Date of Birth, Address, NHS Number, etc.
* **Prescription Management:** Add, view, and manage medication information, including tablet names, dosage, daily doses, storage instructions, and expiry dates.
* **Database Connectivity:** The system connects to a MySQL database to store patient and prescription data.
* **User Interface:** A user-friendly interface built using the Tkinter library for easy navigation and operation.
## Components
* **Patient Information:**

  * Patient ID
  * NHS Number
  * Name
  * Date of Birth
  * Address
* **Prescription Information:**

  * Tablet Name
  * Reference Number
  * Dose
  * Number of Tablets
  * Lot Number
  * Issue Date
  * Expiry Date
  * Daily Dose
  * Side Effects
  * Storage Instructions
  * Further Information
* **MySQL Database:**

  * The system uses a MySQL database to store patient and prescription data.
  * The database table new_table contains all the fields for patient and prescription information.
## Installation
### Prerequisites
To run this application, you need to install the following:

  * Python (version 3.13 recommended)
  * Tkinter (for the graphical user interface)
  * MySQL Server (for storing data)

You can install Tkinter using the following command:
```
pip install tk
```
To interact with MySQL, install the MySQL connector for Python:
```
pip install mysql-connector-python
```
## Database Setup
You need to create a MySQL database and a table to store the information. Use the following SQL to create the database and table:
```
CREATE DATABASE Mydata;

USE Mydata;

CREATE TABLE `new_table` (
  `NameofTablets` int NOT NULL,
  `Reference_No` varchar(45) NOT NULL,
  `dose` varchar(45) DEFAULT NULL,
  `Numberoftablets` varchar(45) DEFAULT NULL,
  `lot` varchar(45) DEFAULT NULL,
  `issuedate` varchar(45) DEFAULT NULL,
  `expdate` varchar(45) DEFAULT NULL,
  `dailydose` varchar(45) DEFAULT NULL,
  `storage` varchar(45) DEFAULT NULL,
  `nhsnumber` varchar(45) DEFAULT NULL,
  `patientname` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `patientaddress` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Reference_No`,`NameofTablets`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```
## Connecting to the Database
You will need to modify the database connection parameters in the Python code to match your MySQL setup.
```
con = mysql.connector.connect(host="localhost", user="root", password="your_password", database="Mydata", auth_plugin='mysql_native_password')
```
Replace your_password with the MySQL root password.

## Usage
### Running the Program
* After setting up the database and installing the dependencies, run the Python script.
* The application window will appear with input fields for patient and prescription data.
* Add or update records as needed, and click the buttons to perform various actions such as viewing prescriptions, updating data, or clearing fields.
* The data will be saved in the MySQL database.
## Buttons
* **Prescription:** Adds a new prescription to the database.
* **Prescription Data:** Displays existing prescriptions in a table.
* **Update:** Updates the current prescription data.
* **Delete:** Deletes selected data.
* **Clear:** Clears all input fields.
* **Exit:** Exits the application.
## Viewing Data
Prescription data will be displayed in the table at the bottom of the application, and you can scroll horizontally and vertically to view all entries.

## Troubleshooting
* Ensure that the MySQL server is running and accessible.
* Verify that the Python packages (mysql-connector-python and tkinter) are correctly installed.
* Check for any connection errors in the console.
## Contributing
Feel free to fork and contribute to this project. To report bugs or suggest new features, please open an issue.
