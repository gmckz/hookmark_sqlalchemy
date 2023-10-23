import os
from flask import Flask
from lib.database_connection import get_flask_database_connection

app = Flask(__name__)

# Landing page API route
@app.route("/")
def page_test():
    return "Hello welcome to my page"

if __name__ == "__main__":
    app.run(debug=True)

    