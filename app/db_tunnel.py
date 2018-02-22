# functions for communicating with the database,
# and for storing (overwriting database contents)

from app import app, models, db
# from flask import connect_db, g


# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#     return g.sqlite_db


# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()


def get_task(id):
    return id


def save_task(task, title, description):
    print("New Task (id=", task.id, "):",
          "title: " + title, ", descr: " + description)
    return
