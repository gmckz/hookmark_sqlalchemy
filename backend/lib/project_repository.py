from lib.Project import Project
from datetime import datetime

class ProjectRepository:
    def __init__(self, connection):
        self._connection = connection

    def find(self, project_id):
        rows = self._connection.execute('SELECT * FROM projects WHERE id=%s', [project_id])
        row = rows[0]
        return Project(row["id"], row["name"], row["link"], row["notes"])
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM projects')
        projects = []
        for row in rows:
            project = Project(row["id"], row["name"], row["link"], row["notes"])
            projects.append(vars(project))
        return projects
    
    def create(self, project):
        if project.is_valid():
            self._connection.execute(
                    'INSERT INTO projects (name, link, notes) VALUES (%s, %s, %s)',\
                    [project.name, project.link, project.notes]
                )
        else:
            return project.generate_error_message()
        
    def update(self, project):
        if project.is_valid():
            self._connection.execute(
                    'UPDATE projects SET name = %s, link = %s, notes = %s WHERE id = %s',
                    [project.name, project.link, project.notes, project.id]
            )
        else:
            return project.generate_error_message()