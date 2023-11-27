from lib.Project import Project

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