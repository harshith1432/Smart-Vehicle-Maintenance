from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user, login_required
from models.models import db, Vehicle
from datetime import datetime

vehicle = Blueprint('vehicle', __name__)

@vehicle.route('/')
@login_required
def list_vehicles():
    vehicles = Vehicle.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', vehicles=vehicles)

@vehicle.route('/add', methods=['GET', 'POST'])
@login_required
def add_vehicle():
    if request.method == 'POST':
        new_vehicle = Vehicle(
            user_id=current_user.id,
            name=request.form.get('name'),
            brand=request.form.get('brand'),
            model=request.form.get('model'),
            vehicle_type=request.form.get('vehicle_type'),
            registration_number=request.form.get('registration_number'),
            purchase_date=datetime.strptime(request.form.get('purchase_date'), '%Y-%m-%d').date() if request.form.get('purchase_date') else None,
            current_odometer=int(request.form.get('current_odometer', 0)),
            fuel_type=request.form.get('fuel_type'),
            average_mileage=float(request.form.get('average_mileage', 0))
        )
        db.session.add(new_vehicle)
        db.session.commit()
        flash('Vehicle added successfully!', 'success')
        return redirect(url_for('analytics.dashboard'))
    return render_template('add_vehicle.html')

@vehicle.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_vehicle(id):
    v = Vehicle.query.get_or_404(id)
    if v.user_id != current_user.id:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('analytics.dashboard'))
    
    if request.method == 'POST':
        v.name = request.form.get('name')
        v.brand = request.form.get('brand')
        v.model = request.form.get('model')
        v.vehicle_type = request.form.get('vehicle_type')
        v.current_odometer = int(request.form.get('current_odometer', 0))
        v.fuel_type = request.form.get('fuel_type')
        v.average_mileage = float(request.form.get('average_mileage', 0))
        db.session.commit()
        flash('Vehicle updated successfully!', 'success')
        return redirect(url_for('vehicle.details', id=v.id))
        
    return render_template('edit_vehicle.html', vehicle=v)

@vehicle.route('/delete/<int:id>')
@login_required
def delete_vehicle(id):
    v = Vehicle.query.get_or_404(id)
    if v.user_id == current_user.id:
        db.session.delete(v)
        db.session.commit()
        flash('Vehicle deleted.', 'info')
    return redirect(url_for('analytics.dashboard'))

@vehicle.route('/details/<int:id>')
@login_required
def details(id):
    v = Vehicle.query.get_or_404(id)
    if v.user_id != current_user.id:
        return redirect(url_for('analytics.dashboard'))
    return render_template('vehicle_details.html', vehicle=v)
