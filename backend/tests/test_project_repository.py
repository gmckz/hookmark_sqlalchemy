from datetime import datetime
from lib.project_repository import ProjectRepository
from lib.Project import Project

"""
Calling ProjectRepository.find returns a project object corresponding to the id
"""
def test_find_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    project = repository.find(1)
    assert project == Project(1, "cable knit hat", "www.google.com", "test note", datetime(2023, 11, 9, 15, 35))