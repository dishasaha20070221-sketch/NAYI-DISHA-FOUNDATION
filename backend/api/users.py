from flask import Blueprint, request, jsonify
from models import db, User

users_bp = Blueprint('users', __name__, url_prefix='/api/users')


@users_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'success': False, 'message': 'Email already registered'}), 400

    user = User(
        fullname=data.get('fullname'),
        email=data.get('email'),
        role=data.get('role', 'user')
    )
    user.set_password(data.get('password'))

    db.session.add(user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'User registered successfully', 'user': user.to_dict()}), 201


@users_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if data.get('fullname'):
        user.fullname = data.get('fullname')
    if data.get('email'):
        user.email = data.get('email')
    if data.get('role'):
        user.role = data.get('role')
    if data.get('password'):
        user.set_password(data.get('password'))

    db.session.commit()

    return jsonify({'success': True, 'message': 'User updated successfully', 'user': user.to_dict()}), 200


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': True, 'message': 'User deleted successfully'}), 200
