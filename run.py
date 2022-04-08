# from flask_script import Manager
from core import app


# manager = Manager(app)

def load_Data():
    import datainput
    datainput.add_genres()

# @manager.command
# def runserver():
#     app.run()
#     load_Data()


if __name__ == "__main__":
    app.run()
    load_Data()
