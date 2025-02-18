# Appointment Backend

## Setup


# Deployed API

The backend is deployed on Render. You can access it at:
```sh
https://apponitment-backend.onrender.com

```
# Clone the repository
```sh
git clone https://github.com/shadiyaali/Apponitment-Backend
```
# Setup Virtual Environment and Install Dependencies

```sh
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
# Run Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```


## API Endpoints

# Doctor Endpoints

# List all employees (Doctors Or Nurses)
```sh
GET /booking/employees/
https://apponitment-backend.onrender.com/booking/employees/

```
# Create a new employee
```sh
POST /booking/employees/
https://apponitment-backend.onrender.com/booking/employees/

```
Content-Type: application/json
Example JSON
Create a Doctor 
``` json:
{
    "name": "Dr. John Doe",
    "department": "Cardiology",
    "email": "johndoe@example.com",
    "phone": "1234567890",
    "employee_type": "Doctor"  
}

```
Create a Nurse
``` json 
{
    "name": "Dr. John Doe",
    "department": "Cardiology",
    "email": "johndoe@example.com",
    "phone": "1234567890",
    "employee_type": "Nurse"  
}
```
# Retrieve an employee
```sh
GET /booking/employees/<id>/
https://apponitment-backend.onrender.com/booking/employees/<id>/

```
# Update an employee
```sh
PUT /booking/employees/<id>/
https://apponitment-backend.onrender.com/booking/employees/<id>/


```
Example JSON
```json:
{
    "department": "Neurology"
}

```
# Delete an employee
```sh
GET /booking/employees/<id>/
https://apponitment-backend.onrender.com/booking/employees/<id>/

```

# Patient Endpoints

# List all patients
```sh
GET /booking/patients/
https://apponitment-backend.onrender.com/booking/patients/
```
# Create a new patient
```sh
POST /booking/patients/
https://apponitment-backend.onrender.com/booking/patients/
```
Example JSON
```json:
{
    "name": "Jane Doe",
    "age": 30,
    "gender": "Female",
    "phone": "9876543210",
    "email": "janedoe@example.com"
}

```
# Retrieve a patient
```sh
GET /booking/patients/<id>/
https://apponitment-backend.onrender.com/booking/patients/<id>/
```
# Update a patient
```sh
PUT /booking/patients/<id>/
https://apponitment-backend.onrender.com/booking/patients/<id>/
```
Example JSON
```json:
{
    "age": 35
}
```
# Delete a patient
```sh
DELETE /booking/patients/<id>/
https://apponitment-backend.onrender.com/booking/patients/<id>/
```

# Appointment Endpoints

# List all appointments
```sh
GET /booking/appointments/
https://apponitment-backend.onrender.com/booking/appointments/
```
# Create a new appointment
```sh
POST /booking/appointments/
https://apponitment-backend.onrender.com/booking/appointments/


```
Example JSON
json:
```s
{
    "patient": 1,   #patient id
    "doctor": 2,    #employee id(doctor)
    "date": "2024-07-15",
    "time": "10:00:00"
    
}

```
# Retrieve an appointment
```sh
GET /booking/appointments/<id>/
https://apponitment-backend.onrender.com/booking/appointments/<id>/
```
# Update an appointment
```sh
PUT /booking/appointments/<id>/
https://apponitment-backend.onrender.com/booking/appointments/<id>/
```
Example JSON
``` json:
{
    "status": "Completed"
}
```
# Delete an appointment
```sh
DELETE /booking/appointments/<id>/
https://apponitment-backend.onrender.com/booking/appointments/<id>/
```

# Attendance Endpoints
# List all attendance records
```sh
GET /booking/attendance/
https://apponitment-backend.onrender.com/booking/attendance/
```
# Create an attendance record for an employee
```sh
POST /booking/attendance/
https://apponitment-backend.onrender.com/booking/attendance/
```
Content-Type: application/json
Example JSON:
```sh
{
    "employee": 1,  #employee id
    "date": "2024-07-15",
    "status": "Present" 
}
```

# Retrieve an attendance record
```sh
GET /booking/attendance/<id>/
https://apponitment-backend.onrender.com/booking/attendance/<id>/
```
# Update an attendance record
```sh
PUT /booking/attendance/<id>/
https://apponitment-backend.onrender.com/booking/attendance/<id>/
```
Example JSON:
```sh
{
    "is_present": "false"
}
```
# Delete an attendance record
```sh
DELETE /booking/attendance/<id>/
https://apponitment-backend.onrender.com/booking/attendance/<id>/
```

# Appointment Status Count

This API endpoint returns the count of appointments for each status (`Pending`, `Completed`, `Cancelled`) for the current day, filtered by appointments 

```sh
GET booking/appointments-status-count/
https://apponitment-backend.onrender.com/booking/appointments-status-count/

```
Response of Status Count
```sh
{
    "Pending ": 3,
    "Completed  ": 2,
    "Cancelled  ": 1
}
```

# Today Employees Count
This endpoint returns the count of employees present today, categorized by employee type (total, doctors, and nurses)

```sh
GET booking/employee-count-today/
https://apponitment-backend.onrender.com/booking/employee-count-today/

```

Response of Employees Count

```sh
{
    "total_employees_today": 25,
    "doctor_count_today": 15,
    "nurse_count_today": 10
}
```
# Today Appointments Details

This endpoint retrieves a list of appointments scheduled for today, including patient and doctor details, appointment date, time, and status
```sh
GET booking/appointments-today/
https://apponitment-backend.onrender.com/booking/appointments-today/

```
Response of Appointments Details
```sh
[
    {
        "token_number": 1,
        "patient": {
            "id": 6,
            "name": "Jane Doe",
            "age": 30,
            "gender": "Female",
            "phone": "9876543210",
            "email": "janeffdfdsdoe@example.com"
        },
        "doctor": {
            "id": 1,
            "name": "John Doe",
            "department": "Cardiology",
            "email": "johndoe@example.com",
            "phone": "1234567890"
        },
        "date": "2025-02-16",
        "time": "08:00:00",
        "status": "Pending"
    }
]
```


# Error Response Examples

Duplicate Employee
```sh 
{
    "error": "Employee with this email already exists."
}
```
Employee Not Found
```sh
{
    "error": "Employee not found!"
}
```
Patient Errors

Duplicate Patient
```sh
{
    "error": "Patient with this email  already exists."
}
```
Patient Not Found
```sh
{
    "error": "Patient not found!"
}
```
Appointment Errors
Doctor Already Booked
```sh 
{
    "error": "Doctor is already booked at this time!"
}
```
Patient Already Has an Appointment
```sh
{
    "error": "Patient already has an appointment at this time!"
}
```
Cannot Select Past Date and Time
```sh
{
    "error": "Cannot select past date and time for an appointment!"
}
```

Doctor Not Present on the Given Date

```sh
{
  "detail": "The doctor {doctor_name} is not present on {appointment_date}."
}
```
Appointment Not Found
```sh
{
    "error": "Appointment not found!"
}
```
Attendance Record Already Exists (for the same employee and date)
```sh
{
    "error": "Attendance record for this employee already exists on this date."
}
```
Invalid Date Format (if the date provided in the attendance record is in an incorrect format)
```sh
{
    "error": "Invalid date format. Please use 'YYYY-MM-DD'."
}
```


### Running Tests

To ensurebthe functionality of the API, you can run the tests

1. ** Run Unit Tests**:
     ```bash
     python manage.py test core 
     ```



