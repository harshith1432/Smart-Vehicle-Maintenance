from flask import Flask, render_template
from config import Config
from models.models import db, User
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Initialize extensions
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    from routes.auth_routes import auth
    from routes.vehicle_routes import vehicle
    from routes.maintenance_routes import maintenance
    from routes.analytics_routes import analytics
    from routes.notification_routes import notification

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(vehicle, url_prefix='/vehicles')
    app.register_blueprint(maintenance, url_prefix='/maintenance')
    app.register_blueprint(analytics, url_prefix='/analytics')
    app.register_blueprint(notification, url_prefix='/notifications')

    # Index route
    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')

    @app.context_processor
    def inject_services():
        from services.maintenance_predictor import MaintenancePredictor
        return dict(MaintenancePredictor=MaintenancePredictor)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
