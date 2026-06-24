from flask import Blueprint, request, jsonify, session
from models import db, User, Admin

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    admin = Admin.query.filter_by(username=username).first()

    if admin and admin.check_password(password):
        session['admin_id'] = admin.admin_id
        session['role'] = 'admin'
        return jsonify({'success': True, 'message': 'Admin login successful', 'admin': admin.to_dict()}), 200

    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401


@auth_bp.route('/admin/logout', methods=['POST'])
def admin_logout():
    session.pop('admin_id', None)
    session.pop('role', None)
    return jsonify({'success': True, 'message': 'Admin logout successful'}), 200


@auth_bp.route('/user/login', methods=['POST'])
def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        session['user_id'] = user.id
        session['role'] = 'user'
        return jsonify({'success': True, 'message': 'User login successful', 'user': user.to_dict()}), 200

    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401
