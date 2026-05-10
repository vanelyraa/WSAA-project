# Web Services and Applications

# Shipments Tracker
## Table of Contents
- [Project Purpose](#project-purpose)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Implementation](#implementation)
- [REST API Endpoints](#rest-api-endpoints)
- [Hosting](#hosting)
- [Technologies Used](#technologies-used)


## Project Purpose
This repository contains project submissions for the Web Services and Applications module completed as part of the Higher Diploma in Science in Computing in Data Analytics at ATU.
The purpose of this project is to develop a Flask-based web application that demonstrates the use of RESTful APIs to perform CRUD operations on relational database tables.
The application is designed as a shipment tracking system where users can:
- Perform user authentication
- Manage shipments 
- Create suppliers 
- Track shipment delivery status 
- Filter and search shipments	 

The project demonstrates:
- REST API development 
- AJAX integration 
- SQLite database management 
- User authentication using predefined login credentials
- CRUD functionality 
- Frontend/backend interaction 


## Project Structure
```text
WSAA-PROJECT/
│
├── templates/
│   └── tracker.html
│
├── createschema.py
├── dbconfig.py
├── README.md
├── requirements.txt
├── schema.sql
├── server.py
├── supplierDAO.py
└── trackerDAO.py
```


## Setup Instructions  
Clone Repository  
<pre>git clone https://github.com/vanelyraa/WSAA-project.git </pre>

Navigate the project directory:  
<pre> cd WSAA-project </pre>

Create a virtual environment (optional):  
<pre> python3 -m venv venv</pre>

Activate virtual environment (optional):  
For Windows: <pre>venv\Scripts\activate</pre>
For MacOS/Linux: <pre>source venv/bin/activate</pre>

Install Dependencies  
<pre> pip install -r requirements.txt </pre>

Create Database
Run:
<pre> python createschema.py </pre>
This creates:
- shipments.db 
- shipments table 
- suppliers table 

Run Application
<pre> python server.py </pre>

Application runs on:
<pre> http://127.0.0.1:5000 </pre>

*Login Credentials:*  
Username: admin  
Password: admin123  


## Implementation
**Overview**  
The application is a shipment tracking system built using Flask, SQLite, JavaScript, jQuery, AJAX, HTML, and CSS.
The frontend communicates with the Flask backend through REST API calls.


**Shipment Features**

*Create Shipment*
- Add planned ETA 
- Select supplier from dropdown
- Add actual ETA 
- Add item code  
The shipment is inserted into the SQLite database using a POST request.   

*Read Shipments*  
All shipments are retrieved from the database using AJAX GET requests and displayed dynamically in a table.
The table includes:
- Shipment ID 
- Status 
- Planned ETA 
- Supplier 
- Country 
- Actual ETA (supports empty/null values)
- Item Code  

*Update Shipment*  
Users can edit shipment records through the update form.
Editable fields:  
- Planned ETA 
- Supplier 
- Actual ETA 
- Item Code    
The application updates the database using PUT requests.  

*Delete Shipment*  
Users can remove shipments using the delete button.  
A confirmation message is displayed before deletion.  
The database is updated using DELETE requests.  


**Supplier Features**

*Create Supplier*  
Users can create suppliers by entering:
- Supplier name 
- Country  
Suppliers are stored on its own database table.  


**Shipment Status**

Shipment status is automatically calculated based on:
- Planned ETA 
- Actual ETA 
- Current date  

Possible statuses:
- In transit 
- Delayed 
- Delivered on time 
- Delivered late  


**Search and Filtering**

The application supports:
- Text search 
- Status filtering  

Users can locate shipments by:
- Supplier 
- Country 
- Item code 
- Shipment status  


**Authentication**

The application uses Flask-Login authentication.  
Features:
- Login system 
- Logout system 
- Route protection using @login_required  
Unauthenticated users cannot access shipment data.  


## REST API Endpoints
Shipment Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/shipments` | Retrieve all shipments |
| GET | `/shipments/<id>` | Retrieve shipment by ID |
| POST | `/shipments` | Create shipment |
| PUT | `/shipments/<id>` | Update shipment |
| DELETE | `/shipments/<id>` | Delete shipment |

Supplier Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/suppliers` | Retrieve all suppliers |
| POST | `/suppliers` | Create supplier |


## Hosting
The application is hosted on PythonAnywhere.  
<pre> https://vanelyra.pythonanywhere.com/ </pre>  


## Technologies Used
Backend
- Python 
- Flask 
- Flask-CORS 
- Flask-Login 
- SQLite  

Frontend
- HTML 
- CSS 
- JavaScript 
- jQuery 
- AJAX   

Hosting
- PythonAnywhere



