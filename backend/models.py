from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('user', 'volunteer'), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    donations = db.relationship('Donation', backref='user', lazy=True)
    volunteer_profile = db.relationship('Volunteer', backref='user', uselist=False, lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at.isoformat()
        }


class Admin(db.Model):
    __tablename__ = 'admin'
    
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'admin_id': self.admin_id,
            'username': self.username,
            'created_at': self.created_at.isoformat()
        }


class Volunteer(db.Model):
    __tablename__ = 'volunteers'
    
    volunteer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    skills = db.Column(db.Text)
    availability = db.Column(db.String(100))
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    
    events = db.relationship('VolunteerEvent', backref='volunteer', lazy=True)

    def to_dict(self):
        return {
            'volunteer_id': self.volunteer_id,
            'fullname': self.fullname,
            'email': self.email,
            'phone': self.phone,
            'skills': self.skills,
            'availability': self.availability,
            'registered_at': self.registered_at.isoformat(),
            'user_id': self.user_id
        }


class Event(db.Model):
    __tablename__ = 'events'
    
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    volunteers = db.relationship('VolunteerEvent', backref='event', lazy=True)

    def to_dict(self):
        return {
            'event_id': self.event_id,
            'event_name': self.event_name,
            'description': self.description,
            'event_date': self.event_date.isoformat(),
            'location': self.location,
            'created_at': self.created_at.isoformat()
        }


class Donation(db.Model):
    __tablename__ = 'donations'
    
    donation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    donor_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_method = db.Column(db.Enum('credit_card', 'debit_card', 'upi', 'net_banking', 'cash'), nullable=False)
    donation_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)

    def to_dict(self):
        return {
            'donation_id': self.donation_id,
            'donor_name': self.donor_name,
            'email': self.email,
            'amount': float(self.amount),
            'payment_method': self.payment_method,
            'donation_date': self.donation_date.isoformat(),
            'user_id': self.user_id
        }


class VolunteerEvent(db.Model):
    __tablename__ = 'volunteer_events'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    volunteer_id = db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id', ondelete='CASCADE'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id', ondelete='CASCADE'), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('volunteer_id', 'event_id', name='unique_volunteer_event'),)
