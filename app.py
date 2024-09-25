from flask import Flask
import logging

from blueprints.main_blueprint import main_bp
from db_postgres import connection_pool

logging.basicConfig(filename='db_logs.log', level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main_bp)

# Closing the connection pool when app shuts down
@app.teardown_appcontext
def close_pool(exception=None):
    if connection_pool:
        connection_pool.closeall()


if __name__ == '__main__':
    app.run(debug=True)
