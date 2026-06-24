from flask import Blueprint, request, jsonify
from models import db, Donation
from datetime import datetime

donations_bp = Blueprint('donations', __name__, url_prefix='/api/donations')


@donations_bp.route('/', methods=['POST'])
def add_donation():
    data = request.get_json()

    donation = Donation(
        donor_name=data.get('donor_name'),
        email=data.get('email'),
        amount=data.get('amount'),
        payment_method=data.get('payment_method', 'cash')
    )

    db.session.add(donation)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Donation added successfully', 'donation': donation.to_dict()}), 201


@donations_bp.route('/', methods=['GET'])
def get_donations():
    donations = Donation.query.all()
    return jsonify([d.to_dict() for d in donations]), 200


@donations_bp.route('/report', methods=['GET'])
def generate_report():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = Donation.query
    if start_date:
        start = datetime.fromisoformat(start_date)
        query = query.filter(Donation.donation_date >= start)
    if end_date:
        end = datetime.fromisoformat(end_date)
        query = query.filter(Donation.donation_date <= end)

    donations = query.all()
    total_amount = sum(float(d.amount) for d in donations)

    return jsonify({
        'total_donations': len(donations),
        'total_amount': total_amount,
        'donations': [d.to_dict() for d in donations]
    }), 200
