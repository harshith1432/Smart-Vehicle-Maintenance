import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from models.models import db, Notification, User
from config import Config

class NotificationService:
    @staticmethod
    def create_system_notification(user_id, vehicle_id, n_type, message):
        n = Notification(
            user_id=user_id,
            vehicle_id=vehicle_id,
            type=n_type,
            message=message
        )
        db.session.add(n)
        db.session.commit()
        
        # Optionally send email if configured
        if Config.MAIL_USERNAME and Config.MAIL_PASSWORD:
            user = User.query.get(user_id)
            NotificationService.send_email(user.email, f"SVM ALERT: {n_type}", message)

    @staticmethod
    def send_email(to_email, subject, body):
        try:
            msg = MIMEMultipart()
            msg['From'] = Config.MAIL_USERNAME
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
            server.starttls()
            server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False
