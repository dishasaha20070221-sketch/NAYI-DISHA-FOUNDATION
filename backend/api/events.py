from flask import Blueprint, request, jsonify
from models import db, Event
from datetime import datetime

events_bp = Blueprint('events', __name__, url_prefix='/api/events')


@events_bp.route('/', methods=['POST'])
def create_event():
    data = request.get_json()

    event = Event(
        event_name=data.get('event_name'),
        description=data.get('description'),
        event_date=datetime.fromisoformat(data.get('event_date')),
        location=data.get('location')
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Event created successfully', 'event': event.to_dict()}), 201


@events_bp.route('/', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([e.to_dict() for e in events]), 200


@events_bp.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.get_json()

    if data.get('event_name'):
        event.event_name = data.get('event_name')
    if data.get('description'):
        event.description = data.get('description')
    if data.get('event_date'):
        event.event_date = datetime.fromisoformat(data.get('event_date'))
    if data.get('location'):
        event.location = data.get('location')

    db.session.commit()

    return jsonify({'success': True, 'message': 'Event updated successfully', 'event': event.to_dict()}), 200


@events_bp.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Event deleted successfully'}), 200
