-- Nayi Disha Foundation - MySQL Database Design

-- Create Database
CREATE DATABASE IF NOT EXISTS nayi_disha_foundation;
USE nayi_disha_foundation;

-- 1. Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('user', 'volunteer') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Admin Table
CREATE TABLE IF NOT EXISTS admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Volunteers Table
CREATE TABLE IF NOT EXISTS volunteers (
    volunteer_id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20),
    skills TEXT,
    availability VARCHAR(100),
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- 4. Events Table
CREATE TABLE IF NOT EXISTS events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(200) NOT NULL,
    description TEXT,
    event_date DATETIME NOT NULL,
    location VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5. Donations Table
CREATE TABLE IF NOT EXISTS donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_name VARCHAR(100) NOT NULL,
    email VARCHAR(120),
    amount DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('credit_card', 'debit_card', 'upi', 'net_banking', 'cash') NOT NULL,
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

-- 6. Volunteer Events (Join Table - Many-to-Many Relationship)
CREATE TABLE IF NOT EXISTS volunteer_events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    volunteer_id INT NOT NULL,
    event_id INT NOT NULL,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    UNIQUE KEY unique_volunteer_event (volunteer_id, event_id)
);


-- ==============================================
-- Insert Sample Records
-- ==============================================

-- Insert Admin
INSERT INTO admin (username, password) VALUES
('admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5Gy7WqKfH7VFi'); -- password: admin123

-- Insert Users
INSERT INTO users (fullname, email, password, role) VALUES
('Rahul Sharma', 'rahul@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5Gy7WqKfH7VFi', 'user'),
('Priya Patel', 'priya@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5Gy7WqKfH7VFi', 'volunteer'),
('Amit Kumar', 'amit@example.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5Gy7WqKfH7VFi', 'user');

-- Insert Volunteers
INSERT INTO volunteers (fullname, email, phone, skills, availability, user_id) VALUES
('Priya Patel', 'priya@example.com', '9876543210', 'Teaching, First Aid', 'Weekends', 2),
('Sunita Devi', 'sunita@example.com', '9876543211', 'Cooking, Community Outreach', 'Weekdays', NULL),
('Rohan Mehta', 'rohan@example.com', '9876543212', 'IT Support, Social Media', 'Flexible', NULL);

-- Insert Events
INSERT INTO events (event_name, description, event_date, location) VALUES
('Annual Fundraiser Gala', 'Join us for our annual fundraising event to support education for underprivileged children', '2026-07-15 18:00:00', 'New Delhi'),
('Blood Donation Camp', 'Free blood donation camp in association with Red Cross', '2026-08-10 09:00:00', 'Mumbai'),
('Tree Plantation Drive', 'Help us plant 1000 trees in the city', '2026-09-05 07:00:00', 'Bangalore');

-- Insert Donations
INSERT INTO donations (donor_name, email, amount, payment_method, user_id) VALUES
('Rahul Sharma', 'rahul@example.com', 10000.00, 'credit_card', 1),
('Anonymous', NULL, 5000.00, 'upi', NULL),
('Amit Kumar', 'amit@example.com', 25000.00, 'net_banking', 3),
('Neha Singh', 'neha@example.com', 3000.00, 'debit_card', NULL);

-- Insert Volunteer Events (Assign volunteers to events)
INSERT INTO volunteer_events (volunteer_id, event_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 2);
