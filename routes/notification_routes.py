from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from models.models import db, Notification

notification = Blueprint('notification', __name__)

@notification.route('/')
@login_required
def list_notifications():
    notifications = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.created_at.desc()).all()
    return render_template('notifications.html', notifications=notifications)

@notification.route('/read/<int:id>')
@login_required
def mark_as_read(id):
    n = Notification.query.get_or_404(id)
    if n.user_id == current_user.id:
        n.is_read = True
        db.session.commit()
    return redirect(url_for('notification.list_notifications'))
