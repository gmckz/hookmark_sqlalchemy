import os
from flask import Flask
from lib.database_connection import get_flask_database_connection
from lib.project_repository import ProjectRepository

app = Flask(__name__)

# Landing page API route
@app.route("/")
def page_test():
    return "Hello welcome to my page"

@app.route("/projects/<int:project_id>", methods=['GET'])
def get_a_project(project_id):
    connection = get_flask_database_connection(app)
    repository = ProjectRepository(connection)
    return vars(repository.find(project_id))

if __name__ == "__main__":
    app.run(debug=True)
