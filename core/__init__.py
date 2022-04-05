from flask import Flask
import os


app = Flask(__name__, template_folder='../templates')

# change to name of your database; add path if necessary
db_name = 'fyyurapp2'
app.config.from_object('config')

import views