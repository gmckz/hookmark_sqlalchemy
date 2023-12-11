from lib.Project import Project
from datetime import datetime
from lib.exceptions import ProjectNotFoundException, DatabaseQueryException

class ProjectRepository:
    def __init__(self, connection):
        self._connection = connection

    def find(self, project_id):
        try:
            rows = self._connection.execute('SELECT * FROM projects WHERE id=%s', [project_id])
            if len(rows) > 0:
                row = rows[0]
                return Project(row["id"], row["name"], row["link"], row["notes"])
            else:
                raise ProjectNotFoundException(f'Project with id: {project_id} does not exist.')
        except DatabaseQueryException as e:
            raise DatabaseQueryException('Error executing database query in find method')
    
    def all(self):
        try:
            rows = self._connection.execute('SELECT * FROM projects')
            projects = []
            for row in rows:
                project = Project(row["id"], row["name"], row["link"], row["notes"])
                projects.append(vars(project))
            return projects
        except DatabaseQueryException as e:
            raise DatabaseQueryException('Error executing database query in all method') from e
    
    def create(self, project):
        try:
            if project.is_valid():
                self._connection.execute(
                        'INSERT INTO projects (name, link, notes) VALUES (%s, %s, %s)',\
                        [project.name, project.link, project.notes]
                    )
            else:
                return project.generate_error_message()
        except DatabaseQueryException as e:
            raise DatabaseQueryException('Error executing database query in create method') from e

        
    def update(self, project):
        if project.is_valid():
            self._connection.execute(
                    'UPDATE projects SET name = %s, link = %s, notes = %s WHERE id = %s',
                    [project.name, project.link, project.notes, project.id]
            )
        else:
            return project.generate_error_message()
        
    def delete(self, project_id):
        err = f"Project with id {project_id} does not exist"
        project = self.find(project_id)
        if isinstance(project, Project):
            self._connection.execute(
                'DELETE FROM projects WHERE id = %s', [project_id]
            )
            return f"Project with id {project_id} deleted"
        else:
            return err