# TODO: change file name and blueprints name
from flask import jsonify, request, blueprints
from services.main_server import select_all_with_psycopg2
from flask_sqlalchemy import SQLAlchemy
from models.target import Target
from models.target_country import TargetCountry

db = SQLAlchemy()

main_bp = blueprints.Blueprint('main', __name__)
@main_bp.route('/hello2')
def hello2():
    return "hello2"
@main_bp.route('/get')
def get_with_psycopg2():
    request_info = {
        "ip": request.remote_addr,
        "endpoint": request.url,
        "method": request.method
    }
    result = select_all_with_psycopg2(request_info)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'message': 'No data'}), 404


@main_bp.route('/mission')
def get_all_targets():
    try:
        print("before query")
        targets = Target.query.all()
        print(targets)
        if targets:
            result = []
            for target in targets:
                country = TargetCountry.query.get(target.country_id)
                result.append({
                    'id': target.id,
                    'name': target.name,
                    'description': target.description,
                    'country': country.name if country else None
                })
            return jsonify(result), 200
        else:
            return jsonify({'message': 'No data'}), 404
    except Exception as e:
        print(e)

@main_bp.route('/mission/<int:id>')
def get_target_by_id(id):
    target = Target.query.get(id)
    if not target:
        return jsonify({'message': 'Target not found'}), 404
    country = TargetCountry.query.get(target.country_id)
    return jsonify({
        'id': target.id,
        'name': target.name,
        'description': target.description,
        'country': country.name if country else None
    }), 200
