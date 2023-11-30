from lib.Project import Project
from datetime import datetime

class ProjectRepository:
    def __init__(self, connection):
        self._connection = connection

    def find(self, project_id):
        rows = self._connection.execute('SELECT * FROM projects WHERE id=%s', [project_id])
        row = rows[0]
        return Project(row["id"], row["name"], row["link"], row["notes"], row["created_at"])
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM projects')
        projects = []
        for row in rows:
            project = Project(row["id"], row["name"], row["link"], row["notes"], row["created_at"])
            projects.append(vars(project))
        return projects
    
    def create(self, project):
        if project.is_valid():
            self._connection.execute(
                    'INSERT INTO projects (name, link, notes, created_at) VALUES (%s, %s, %s, %s)',\
                    [project.name, project.link, project.notes, project.created_at]
                )
        else:
            return project.generate_error_message()