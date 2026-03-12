from flask import Blueprint, render_template, jsonify
from flask_login import current_user, login_required
from services.analytics_service import AnalyticsService
from models.models import Vehicle
from services.maintenance_predictor import MaintenancePredictor

analytics = Blueprint('analytics', __name__)

@analytics.route('/dashboard')
@login_required
def dashboard():
    vehicles = Vehicle.query.filter_by(user_id=current_user.id).all()
    metrics = AnalyticsService.get_summary_metrics(current_user.id)
    
    vehicle_data = []
    for v in vehicles:
        health = MaintenancePredictor.calculate_health_score(v.id)
        vehicle_data.append({
            'vehicle': v,
            'health_score': health,
            'health_color': 'danger' if health < 50 else ('warning' if health < 80 else 'success')
        })
        
    return render_template('dashboard.html', 
                          vehicle_data=vehicle_data, 
                          metrics=metrics)

@analytics.route('/api/spending')
@login_required
def spending_api():
    data = AnalyticsService.get_monthly_spending(current_user.id)
    return jsonify(data)

@analytics.route('/api/breakdown')
@login_required
def breakdown_api():
    data = AnalyticsService.get_expense_breakdown(current_user.id)
    return jsonify(data)
