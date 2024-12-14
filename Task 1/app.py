from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for simplicity (will use SQLite/PostgreSQL in Task 2)
database = {}
current_id = 1

# Endpoint 1: Add app details
@app.route('/add-app', methods=['POST'])
def add_app():
    global current_id
    data = request.json

    if not data or not all(key in data for key in ('app_name', 'version', 'description')):
        return jsonify({'error': 'Invalid data, all fields (app_name, version, description) are required'}), 400

    app_entry = {
        'id': current_id,
        'app_name': data['app_name'],
        'version': data['version'],
        'description': data['description']
    }
    database[current_id] = app_entry
    current_id += 1

    return jsonify({'message': 'App added successfully', 'app': app_entry}), 201

# Endpoint 2: Get app details by ID
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_entry = database.get(id)
    if not app_entry:
        return jsonify({'error': f'No app found with ID {id}'}), 404

    return jsonify({'app': app_entry}), 200

# Endpoint 3: Delete app by ID
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    if id not in database:
        return jsonify({'error': f'No app found with ID {id}'}), 404

    deleted_app = database.pop(id)
    return jsonify({'message': 'App deleted successfully', 'app': deleted_app}), 200

if __name__ == '__main__':
    app.run(debug=True)