from models.models import Expense, MaintenanceRecord, Vehicle, db
from sqlalchemy import func
from datetime import datetime, timedelta

class AnalyticsService:
    @staticmethod
    def get_monthly_spending(user_id):
        # Last 6 months spending
        six_months_ago = datetime.now() - timedelta(days=180)
        
        spending = db.session.query(
            func.to_char(Expense.date, 'Mon'),
            func.sum(Expense.amount)
        ).join(Vehicle).filter(
            Vehicle.user_id == user_id,
            Expense.date >= six_months_ago
        ).group_by(func.to_char(Expense.date, 'Mon')).all()
        
        return dict(spending)

    @staticmethod
    def get_expense_breakdown(user_id):
        breakdown = db.session.query(
            Expense.category,
            func.sum(Expense.amount)
        ).join(Vehicle).filter(
            Vehicle.user_id == user_id
        ).group_by(Expense.category).all()
        
        return dict(breakdown)

    @staticmethod
    def get_summary_metrics(user_id):
        total_vehicles = Vehicle.query.filter_by(user_id=user_id).count()
        
        # Monthly cost (current month)
        first_day = datetime.now().replace(day=1)
        monthly_cost = db.session.query(func.sum(Expense.amount)).join(Vehicle).filter(
            Vehicle.user_id == user_id,
            Expense.date >= first_day
        ).scalar() or 0
        
        return {
            'total_vehicles': total_vehicles,
            'monthly_cost': float(monthly_cost)
        }
