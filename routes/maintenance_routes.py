from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from models.models import db, MaintenanceRecord, Vehicle, Expense
from datetime import datetime

maintenance = Blueprint('maintenance', __name__)

@maintenance.route('/add/<int:vehicle_id>', methods=['GET', 'POST'])
@login_required
def add_record(vehicle_id):
    v = Vehicle.query.get_or_404(vehicle_id)
    if v.user_id != current_user.id:
        return redirect(url_for('analytics.dashboard'))
        
    if request.method == 'POST':
        record = MaintenanceRecord(
            vehicle_id=vehicle_id,
            service_type=request.form.get('service_type'),
            service_date=datetime.strptime(request.form.get('service_date'), '%Y-%m-%d').date(),
            odometer_reading=int(request.form.get('odometer_reading')),
            cost=float(request.form.get('cost')),
            notes=request.form.get('notes')
        )
        # Update vehicle odometer if it's higher
        if record.odometer_reading > v.current_odometer:
            v.current_odometer = record.odometer_reading
            
        db.session.add(record)
        db.session.commit()
        
        # Also log as an expense
        expense = Expense(
            vehicle_id=vehicle_id,
            category='Service',
            amount=record.cost,
            date=record.service_date,
            description=f"Service: {record.service_type}"
        )
        db.session.add(expense)
        db.session.commit()
        
        flash('Maintenance record added!', 'success')
        return redirect(url_for('vehicle.details', id=vehicle_id))
        
    return render_template('add_maintenance.html', vehicle=v)

@maintenance.route('/history/<int:vehicle_id>')
@login_required
def history(vehicle_id):
    v = Vehicle.query.get_or_404(vehicle_id)
    if v.user_id != current_user.id:
        return redirect(url_for('analytics.dashboard'))
    records = MaintenanceRecord.query.filter_by(vehicle_id=vehicle_id).order_by(MaintenanceRecord.service_date.desc()).all()
    return render_template('maintenance_history.html', vehicle=v, records=records)
