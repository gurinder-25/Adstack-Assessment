from app import db, App, app  # Import `app` from your Flask app module

# Pre-fill sample data
def populate_sample_data():
    sample_apps = [
        {"app_name": "Weather Wizard", "version": "1.0", "description": "A weather forecasting app."},
        {"app_name": "Task Tracker", "version": "2.3", "description": "An app to track daily tasks."},
        {"app_name": "Fitness Pro", "version": "3.1", "description": "A fitness and health monitoring app."}
    ]

    with app.app_context():  # Create application context
        for app_data in sample_apps:
            new_app = App(
                app_name=app_data['app_name'],
                version=app_data['version'],
                description=app_data['description']
            )
            db.session.add(new_app)

        db.session.commit()
        print("Sample data added successfully!")

if __name__ == "__main__":
    populate_sample_data()
