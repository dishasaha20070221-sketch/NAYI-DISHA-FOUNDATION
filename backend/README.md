# Nayi Disha Foundation - Backend API

REST API built with Python Flask for the Nayi Disha Foundation NGO website.

## Project Structure
```
backend/
├── api/
│   ├── __init__.py
│   ├── auth.py          # Authentication endpoints
│   ├── volunteers.py    # Volunteer management
│   ├── donations.py     # Donation management
│   ├── events.py        # Event management
│   └── users.py         # User management
├── app.py               # Main application entry point
├── config.py            # Configuration settings
├── models.py            # Database models
└── requirements.txt     # Dependencies
```

## Setup Instructions

1. **Navigate to the backend directory**:
   ```bash
   cd "c:\Users\Disha Saha\Documents\trae_projects\NAYI DISHA FOUNDATION\backend"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:
   ```bash
   python app.py
   ```

   The server will start on http://localhost:5000

## API Endpoints

### Authentication
- `POST /api/auth/admin/login` - Admin login
- `POST /api/auth/admin/logout` - Admin logout
- `POST /api/auth/user/login` - User login

### Volunteers
- `POST /api/volunteers/` - Register volunteer
- `GET /api/volunteers/` - View all volunteers
- `DELETE /api/volunteers/<id>` - Delete volunteer

### Donations
- `POST /api/donations/` - Add donation
- `GET /api/donations/` - View all donations
- `GET /api/donations/report?start_date=...&end_date=...` - Generate donation report

### Events
- `POST /api/events/` - Create event
- `GET /api/events/` - View all events
- `PUT /api/events/<id>` - Update event
- `DELETE /api/events/<id>` - Delete event

### Users
- `POST /api/users/register` - Register user
- `GET /api/users/` - View all users
- `PUT /api/users/<id>` - Update user
- `DELETE /api/users/<id>` - Delete user

## Default Admin Credentials
- Email: `admin@nayidisha.org`
- Password: `admin123`
