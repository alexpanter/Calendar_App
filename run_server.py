# flask/run.py

# This file imports the entire app.
# The app is then run from the interpreter.

from app import app


if __name__ == '__main__':
    app.run(port = 3000, debug = True)
