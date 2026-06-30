from flask import Flask
from application.models import db,User,Role
from flask_security import Security, SQLAlchemyUserDatastore
from flask_cors import CORS
from application.celery_init import celery_init_app
from flask_caching import Cache
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.sqlite3"
    app.config["SECRET_KEY"] = "mysecretkey"
    app.config["SECURITY_TOKEN_AUTHENTICATION_HEADER"] = "Authentication-Token"
    app.config["CACHE_TYPE"] ="redis"
    app.config["CACHE_REDIS_HOST"] = "localhost"
    app.config["CACHE_REDIS_PORT"]  = 6379
    app.config["CACHE_REDIS_DB"] = 0 
    app.config["CACHE_REDIS_URL"] = 'redis://localhost:6379'
    db.init_app(app)
    CORS(app)
    ds = SQLAlchemyUserDatastore(db, User, Role )
    app.security=Security(app ,datastore=ds , register_blueprint= False)
    
    cache = Cache(app)
    @app.security.unauthz_handler
    def unauthz_handler(func_name,params):
        return {"message" : "You are not Autherised to view this resource."},403
    
    @app.security.unauthn_handler
    def unauthn_handler(mechanisms ,headers):
        return {"message" : "Please provide correct token."} , 401
    
    app.app_context().push()
    return app,cache


app,cache = create_app()
celery = celery_init_app(app)

# celery worker command : celery -A app.celery worker --loglevel INFO



from celery import Celery
from celery.schedules import crontab
from application.task import admin_report

@celery.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, admin_report.s(), name='send email at every 10 sec')


from application.api import *
from application.initial_data import *


if __name__ =="__main__":
    app.run(debug=True)