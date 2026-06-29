from flask import Flask
from application.models import db,User,Role
from flask_security import Security, SQLAlchemyUserDatastore
from flask_cors import CORS
from application.celery_init import celery_init_app
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.sqlite3"
    app.config["SECRET_KEY"] = "mysecretkey"
    app.config["SECURITY_TOKEN_AUTHENTICATION_HEADER"] = "Authentication-Token"
    db.init_app(app)
    CORS(app)
    ds = SQLAlchemyUserDatastore(db, User, Role )
    app.security=Security(app ,datastore=ds , register_blueprint= False)

    @app.security.unauthz_handler
    def unauthz_handler(func_name,params):
        return {"message" : "You are not Autherised to view this resource."},403
    
    @app.security.unauthn_handler
    def unauthn_handler(mechanisms ,headers):
        return {"message" : "Please provide correct token."} , 401
    
    app.app_context().push()
    return app


app = create_app()
celery = celery_init_app(app)

# celery worker command : celery -A app.celery worker --loglevel INFO

from application.api import *
from application.initial_data import *


if __name__ =="__main__":
    app.run(debug=True)