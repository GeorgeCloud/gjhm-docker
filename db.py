from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from os import environ
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)

# ======= DB Setup ==========
client = MongoClient("mongodb://mongo:27017/gjhm")
db = client.get_default_database()
print('created connection')
# ===========================


# ======= Collections ==========
users = db.users
print(users)
users.create_index('username', unique=True)
playlists = db.playlists
media = db.media
reviews = db.reviews
friend_requests = db.friend_requests
# =========================


# ======= Authentication ==========
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.view'

@login_manager.user_loader
def load_user(user_id):
    return users.find_one({'_id': user_id})
# =================================
