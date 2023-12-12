import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.database_connection import get_flask_database_connection
from lib.project_repository import ProjectRepository
from lib.Project import Project
from lib.exceptions import ProjectNotFoundException, DatabaseQueryException, InvalidProjectException

app = Flask(__name__)
CORS(app)
# Landing page API route
@app.route("/")
def page_test():
    return "Hello welcome to my page"

@app.route("/projects/<int:project_id>", methods=['GET'])
def get_a_project(project_id):
    try:
        connection = get_flask_database_connection(app)
        repository = ProjectRepository(connection)
        project = repository.find(project_id)
        if project:
            return vars(repository.find(project_id)), 200
        else:
            raise ProjectNotFoundException(f"Project with id: {project_id} does not exist.")
    except ProjectNotFoundException as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/projects", methods=['GET'])
def get_all_projects():
    try:
        connection = get_flask_database_connection(app)
        repository = ProjectRepository(connection)
        projects = {"projects": repository.all()}
        return projects, 200
    except DatabaseQueryException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/projects", methods=["POST"])
def create_project():
    try:
        connection = get_flask_database_connection(app)
        repository = ProjectRepository(connection)
        json_body = request.get_json()
        data = json_body['data']
        project = Project(None, data['name'], data['link'], data['notes'])
        print(project)
        if repository.create(project) == "Project created successfully.":
            return repository.all()[-1], 201
        else:
            raise InvalidProjectException()
    except InvalidProjectException as invalid_project_exception:
        return jsonify({"error": str(invalid_project_exception)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/projects", methods=["PUT"])
def update_project():
    try:
        connection = get_flask_database_connection(app)
        repository = ProjectRepository(connection)
        json_body = request.get_json()
        data = json_body['data']
        project = Project(data['id'], data['name'], data['link'], data['notes'])
        if repository.update(project) == "Project updated successfully.":
            return vars(repository.find(project.id)), 200
        else:
            raise InvalidProjectException()
    except InvalidProjectException as invalid_project_exception:
        return jsonify({"error": str(invalid_project_exception)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    try:
        connection = get_flask_database_connection(app)
        repository = ProjectRepository(connection)
        if repository.delete(project_id) == f"Project with id {project_id} deleted":
            return jsonify({"message": "Project deleted successfully"}), 200
        else:
            raise ProjectNotFoundException()
    except ProjectNotFoundException as project_not_found_exception:
        return jsonify({"error": str(project_not_found_exception)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
