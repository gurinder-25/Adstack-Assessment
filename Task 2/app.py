from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuring SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'app_name': self.app_name,
            'version': self.version,
            'description': self.description
        }

# Initialize database
with app.app_context():
    db.create_all()


# Endpoint 1: Add app details
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.json

    if not data or not all(key in data for key in ('app_name', 'version', 'description')):
        return jsonify({'error': 'Invalid data, all fields (app_name, version, description) are required'}), 400

    new_app = App(
        app_name=data['app_name'],
        version=data['version'],
        description=data['description']
    )
    db.session.add(new_app)
    db.session.commit()

    return jsonify({'message': 'App added successfully', 'app': new_app.to_dict()}), 201

# Endpoint 2: Get app details by ID
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_entry = App.query.get(id)
    if not app_entry:
        return jsonify({'error': f'No app found with ID {id}'}), 404

    return jsonify({'app': app_entry.to_dict()}), 200

# Endpoint 3: Delete app by ID
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app_entry = App.query.get(id)
    if not app_entry:
        return jsonify({'error': f'No app found with ID {id}'}), 404

    db.session.delete(app_entry)
    db.session.commit()

    return jsonify({'message': 'App deleted successfully', 'app': app_entry.to_dict()}), 200

if __name__ == '__main__':
    app.run(debug=True)
