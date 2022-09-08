from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


# declaring app and database
app = Flask(__name__,static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mainDB.db'
app.config.from_object("config.DevelopmentConfig")
# app._static_folder = <'/static'>

app.config['SECRET_KEY'] = 'a838c70bf0027155373a84e0872deb51'
# to get random secret key, use python interactive mode.
# in interactive mode-
# >>> import secrets
# >>> secrets.token_hex(16)

db = SQLAlchemy(app)

from server import fb_routes, opr_routes, fb_queue, opr_queue, fb_add, opr_add, ig_add, ig_queue, ig_routes, urlTaker