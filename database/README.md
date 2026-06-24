# Nayi Disha Foundation - MySQL Database

## Database Overview
This is the MySQL database design for the Nayi Disha Foundation NGO website.

## Database Name
`nayi_disha_foundation`

## Tables

### 1. `users`
Stores general user accounts.
- `id` (INT, PK, AUTO_INCREMENT): Unique user identifier
- `fullname` (VARCHAR): User's full name
- `email` (VARCHAR, UNIQUE): User's email
- `password` (VARCHAR): Hashed password
- `role` (ENUM): User role ('user' or 'volunteer')
- `created_at` (TIMESTAMP): Account creation time

### 2. `admin`
Stores admin user accounts.
- `admin_id` (INT, PK, AUTO_INCREMENT): Unique admin identifier
- `username` (VARCHAR, UNIQUE): Admin username
- `password` (VARCHAR): Hashed password
- `created_at` (TIMESTAMP): Account creation time

### 3. `volunteers`
Stores volunteer information.
- `volunteer_id` (INT, PK, AUTO_INCREMENT): Unique volunteer identifier
- `fullname` (VARCHAR): Volunteer's full name
- `email` (VARCHAR, UNIQUE): Volunteer's email
- `phone` (VARCHAR): Volunteer's phone number
- `skills` (TEXT): Volunteer's skills
- `availability` (VARCHAR): Volunteer's availability
- `registered_at` (TIMESTAMP): Registration time
- `user_id` (INT, FK): Links to users.id (if volunteer has a user account)

### 4. `events`
Stores NGO events.
- `event_id` (INT, PK, AUTO_INCREMENT): Unique event identifier
- `event_name` (VARCHAR): Event name
- `description` (TEXT): Event description
- `event_date` (DATETIME): Event date and time
- `location` (VARCHAR): Event location
- `created_at` (TIMESTAMP): Event creation time

### 5. `donations`
Stores donation records.
- `donation_id` (INT, PK, AUTO_INCREMENT): Unique donation identifier
- `donor_name` (VARCHAR): Donor's name
- `email` (VARCHAR): Donor's email
- `amount` (DECIMAL): Donation amount
- `payment_method` (ENUM): Payment method (credit_card, debit_card, upi, net_banking, cash)
- `donation_date` (TIMESTAMP): Donation time
- `user_id` (INT, FK): Links to users.id (if donor has a user account)

### 6. `volunteer_events`
Join table for many-to-many relationship between volunteers and events (volunteers register for events).
- `id` (INT, PK, AUTO_INCREMENT): Unique record identifier
- `volunteer_id` (INT, FK): Links to volunteers.volunteer_id
- `event_id` (INT, FK): Links to events.event_id
- `registered_at` (TIMESTAMP): Registration time
- Unique constraint on (volunteer_id, event_id) to prevent duplicate registrations

## Relationships
- `volunteers.user_id` → `users.id` (One-to-One/One-to-Many)
- `donations.user_id` → `users.id` (One-to-Many)
- `volunteer_events.volunteer_id` → `volunteers.volunteer_id` (Many-to-One)
- `volunteer_events.event_id` → `events.event_id` (Many-to-One)

## Setup Instructions
1. Open MySQL CLI or a tool like phpMyAdmin/MySQL Workbench
2. Execute the `nayi_disha_db.sql` script to create the database, tables, and insert sample data
3. Default admin credentials:
   - Username: `admin`
   - Password: `admin123` (hashed using bcrypt)
