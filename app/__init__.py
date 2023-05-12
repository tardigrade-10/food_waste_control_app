from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
# app.register_blueprint(views)

db = Config.init_app(app)


from app import views
