from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db, User, Admin, Volunteer, Event, Donation, VolunteerEvent
from api.auth import auth_bp
from api.volunteers import volunteers_bp
from api.donations import donations_bp
from api.events import events_bp
from api.users import users_bp
from datetime import datetime
from werkzeug.security import generate_password_hash


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    CORS(app, supports_credentials=True, origins=["http://localhost:8000", "http://127.0.0.1:8000"])

    with app.app_context():
        db.create_all()
        seed_data()

    app.register_blueprint(auth_bp)
    app.register_blueprint(volunteers_bp)
    app.register_blueprint(donations_bp)
    app.register_blueprint(events_bp)
    app.register_blueprint(users_bp)

    @app.route('/')
    def index():
        return jsonify({'message': 'Nayi Disha Foundation API is running!'}), 200

    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'healthy'}), 200
    
    @app.route('/api/dashboard/stats')
    def dashboard_stats():
        total_donations = sum(float(d.amount) for d in Donation.query.all())
        total_volunteers = Volunteer.query.count()
        total_events = Event.query.count()
        total_users = User.query.count()
        
        return jsonify({
            'total_donations': total_donations,
            'total_volunteers': total_volunteers,
            'total_events': total_events,
            'total_users': total_users
        }), 200

    return app


def seed_data():
    if not Admin.query.filter_by(username='admin').first():
        admin = Admin(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        
        user1 = User(fullname='Rahul Sharma', email='rahul@example.com', role='user')
        user1.set_password('password123')
        user2 = User(fullname='Priya Patel', email='priya@example.com', role='volunteer')
        user2.set_password('password123')
        user3 = User(fullname='Amit Kumar', email='amit@example.com', role='user')
        user3.set_password('password123')
        
        db.session.add_all([user1, user2, user3])
        
        vol1 = Volunteer(fullname='Priya Patel', email='priya@example.com', phone='9876543210', skills='Teaching, First Aid', availability='Weekends', user_id=2)
        vol2 = Volunteer(fullname='Sunita Devi', email='sunita@example.com', phone='9876543211', skills='Cooking, Community Outreach', availability='Weekdays')
        vol3 = Volunteer(fullname='Rohan Mehta', email='rohan@example.com', phone='9876543212', skills='IT Support, Social Media', availability='Flexible')
        
        db.session.add_all([vol1, vol2, vol3])
        
        event1 = Event(event_name='Annual Fundraiser Gala', description='Join us for our annual fundraising event to support education for underprivileged children', event_date=datetime(2026,7,15,18,0), location='New Delhi')
        event2 = Event(event_name='Blood Donation Camp', description='Free blood donation camp in association with Red Cross', event_date=datetime(2026,8,10,9,0), location='Mumbai')
        event3 = Event(event_name='Tree Plantation Drive', description='Help us plant 1000 trees in the city', event_date=datetime(2026,9,5,7,0), location='Bangalore')
        
        db.session.add_all([event1, event2, event3])
        
        don1 = Donation(donor_name='Rahul Sharma', email='rahul@example.com', amount=10000, payment_method='credit_card', user_id=1)
        don2 = Donation(donor_name='Anonymous', amount=5000, payment_method='upi')
        don3 = Donation(donor_name='Amit Kumar', email='amit@example.com', amount=25000, payment_method='net_banking', user_id=3)
        don4 = Donation(donor_name='Neha Singh', email='neha@example.com', amount=3000, payment_method='debit_card')
        
        db.session.add_all([don1, don2, don3, don4])
        
        ve1 = VolunteerEvent(volunteer_id=1, event_id=1)
        ve2 = VolunteerEvent(volunteer_id=1, event_id=2)
        ve3 = VolunteerEvent(volunteer_id=2, event_id=3)
        ve4 = VolunteerEvent(volunteer_id=3, event_id=2)
        
        db.session.add_all([ve1, ve2, ve3, ve4])
        
        db.session.commit()
        print('Sample data created successfully!')


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
