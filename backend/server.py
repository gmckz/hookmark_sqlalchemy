import os
from flask import Flask, request
from flask_cors import CORS
from lib.database_connection import get_flask_database_connection
from lib.project_repository import ProjectRepository
from lib.Project import Project

app = Flask(__name__)
CORS(app)
# Landing page API route
@app.route("/")
def page_test():
    return "Hello welcome to my page"

@app.route("/projects/<int:project_id>", methods=['GET'])
def get_a_project(project_id):
    connection = get_flask_database_connection(app)
    repository = ProjectRepository(connection)
    return vars(repository.find(project_id))

@app.route("/projects", methods=['GET'])
def get_all_projects():
    connection = get_flask_database_connection(app)
    repository = ProjectRepository(connection)
    projects = {"projects": repository.all()}
    return projects

@app.route("/projects", methods=["POST"])
def create_project():
    connection = get_flask_database_connection(app)
    repository = ProjectRepository(connection)
    json_body = request.get_json()
    data = json_body['data']
    project = Project(None, data['name'], data['link'], data['notes'])
    repository.create(project)
    return repository.all()[-1]
    


if __name__ == "__main__":
    app.run(debug=True)
