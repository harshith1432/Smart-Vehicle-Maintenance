from models.models import MaintenanceRecord, Vehicle

class MaintenancePredictor:
    # Service intervals in KM
    INTERVALS = {
        'Oil change': 3000,
        'General service': 5000,
        'Brake check': 6000,
        'Tire replacement': 20000,
        'Battery replacement': 40000,
        'Coolant replacement': 15000,
        'Chain lubrication': 500
    }

    @staticmethod
    def predict_next_service(vehicle_id):
        predictions = []
        for service_type, interval in MaintenancePredictor.INTERVALS.items():
            last_record = MaintenanceRecord.query.filter_by(
                vehicle_id=vehicle_id, 
                service_type=service_type
            ).order_by(MaintenanceRecord.odometer_reading.desc()).first()
            
            vehicle = Vehicle.query.get(vehicle_id)
            
            if last_record:
                next_km = last_record.odometer_reading + interval
            else:
                next_km = interval # Assume starting from 0 if no records
                
            remaining_km = next_km - vehicle.current_odometer
            
            predictions.append({
                'service_type': service_type,
                'last_odometer': last_record.odometer_reading if last_record else 0,
                'next_odometer': next_km,
                'remaining_km': remaining_km,
                'status': 'Urgent' if remaining_km <= 200 else ('Soon' if remaining_km <= 500 else 'Good')
            })
            
        return predictions

    @staticmethod
    def calculate_health_score(vehicle_id):
        predictions = MaintenancePredictor.predict_next_service(vehicle_id)
        if not predictions:
            return 100
            
        total_score = 0
        for p in predictions:
            if p['remaining_km'] < 0:
                total_score += 0 # Overdue
            elif p['remaining_km'] < 200:
                total_score += 40
            elif p['remaining_km'] < 500:
                total_score += 70
            else:
                total_score += 100
                
        avg_score = total_score / len(predictions)
        return round(avg_score, 1)
