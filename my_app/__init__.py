from flask import Flask
import os


app = Flask(__name__)

# change to name of your database; add path if necessary
db_name = 'fyyurapp'
app.config.from_object('my_app.config')

import my_app.hello.views