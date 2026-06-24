from flask import Blueprint, request, jsonify
from models import db, Volunteer

volunteers_bp = Blueprint('volunteers', __name__, url_prefix='/api/volunteers')


@volunteers_bp.route('/', methods=['POST'])
def register_volunteer():
    data = request.get_json()

    volunteer = Volunteer(
        fullname=data.get('fullname'),
        email=data.get('email'),
        phone=data.get('phone'),
        skills=data.get('skills'),
        availability=data.get('availability')
    )

    db.session.add(volunteer)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Volunteer registered successfully', 'volunteer': volunteer.to_dict()}), 201


@volunteers_bp.route('/', methods=['GET'])
def get_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([v.to_dict() for v in volunteers]), 200


@volunteers_bp.route('/<int:volunteer_id>', methods=['DELETE'])
def delete_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)
    db.session.delete(volunteer)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Volunteer deleted successfully'}), 200
