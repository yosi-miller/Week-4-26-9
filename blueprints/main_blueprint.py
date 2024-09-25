# TODO: change file name and blueprints name
import selectors

from flask import jsonify, request, blueprints

from services.main_server import select_all_with_psycopg2

main_bp = blueprints.Blueprint('main', __name__, url_prefix='/')

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