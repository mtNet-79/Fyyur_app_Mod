from flask import Flask
import os



# class MyFlaskApp(Flask):
#   def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
#     if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
#       with self.app_context():
#         load_Data()
#     super(MyFlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)



app = Flask(__name__, template_folder='../templates')
app.config.from_object('config')

# with app.app_context():
#     load_Data()





import views