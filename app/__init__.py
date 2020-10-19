import os
from flask import Flask
from flask_mysqldb import MySQL

# Application Definition
app = Flask(__name__,
            instance_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), '../instance'),
            instance_relative_config=True)

# Initializing configuration
app.config.from_pyfile('env.cfg', silent=True)
mysql = MySQL(app)


# Import a module / component using its blueprint handler variable (catalog_module)
from app.customers.controllers import customers_module
from app.documents.controllers import documents_module

# Register blueprint(s)
app.register_blueprint(customers_module)
app.register_blueprint(documents_module)
