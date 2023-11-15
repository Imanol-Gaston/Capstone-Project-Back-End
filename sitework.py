from flask import Flask, request, jsonify
from flask_cors import CORS

from models import db, Profile
from config import config

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()
        
    return app

enviroment = config['development']
app = create_app(enviroment)
CORS(app)

@app.route('/api/v1/profiles', methods=['GET'])
def get_profiles():
    profiles = [ profile.json() for profile in Profile.query.all() ] 
    return jsonify({'profiles': profiles })

@app.route('/api/v1/profiles/<id>', methods=['GET'])
def get_profile(id):
    profile = Profile.query.filter_by(id=id).first()
    if profile is None:
        return jsonify({'message': 'User does not exists'}), 404
    
    return jsonify({'profile': profile.json() })

@app.route('/api/v1/profiles', methods=['POST'])
def create_profile():
    print(request)
    print(request.json)
    json = request.get_json(force=True)

    if json.get('user_id') is None:
        return jsonify({'message': 'Bad request'}), 400

    profile = Profile.create(json['user_id'], json['brief_description'], json['fullname'], json['full_description'])

    return jsonify({'profile': profile.json() })

@app.route('/api/v1/profiles/<id>', methods=['PUT'])
def update_profile(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/api/v1/profiles/<id>', methods=['DELETE'])
def delete_profile(id):
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__sitework__':
    app.run(debug=True)

