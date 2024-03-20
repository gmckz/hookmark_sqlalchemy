import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'hookmark.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    link = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"<Project {self.id} {self.name} {self.link}>"


@app.route("/projects", methods=['GET'])
def get_all_projects():
    projects = Project.query.all()
    serialised_projects = {"projects":[{"id":project.id, "name":project.name, "link":project.link, "notes":project.notes} for project in projects]}
    return serialised_projects, 200

@app.route("/projects/<int:project_id>/", methods=['GET'])
def get_a_project(project_id):
    project = Project.query.get_or_404(project_id)
    serialised_project = {"id":project.id, "name":project.name, "link":project.link, "notes":project.notes}
    return jsonify(serialised_project), 200