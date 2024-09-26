from flask import Flask
import logging

from blueprints.main_blueprint import main_bp
from db_postgres import connection_pool

from models.target import db

logging.basicConfig(filename='db_logs.log', level=logging.INFO)

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/test1db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.register_blueprint(main_bp)

with app.app_context():
    db.init_app(app)

@app.route('/hello')
def hello():
    return 'Hello, World!'

# Closing the connection pool when app shuts down
# @app.teardown_appcontext
# def close_pool(exception=None):
#     if connection_pool:
#         connection_pool.closeall()


if __name__ == '__main__':
    app.run(debug=True)
