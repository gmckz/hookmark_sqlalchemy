from datetime import datetime
from lib.project_repository import ProjectRepository
from lib.Project import Project

"""
Calling ProjectRepository.find returns a project object corresponding to the id
"""
def test_find_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    project1 = repository.find(1)
    assert project1 == Project(1, "cable knit hat", "www.test.com", "test note")
    project2 = repository.find(2)
    assert project2 == Project(2, "jumper", "www.test.com", "test note 2")
    project3 = repository.find(3)
    assert project3 == Project(3, "cardigan", "www.test.com", "test note 3")
    
"""
Calling ProjectRepository.all returns a list of all project objects
"""
def test_all_projects(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    projects = repository.all()
    assert len(projects) == 3
    assert projects[0] == {
                "id": 1,
                "name": 'cable knit hat',
                "link": 'www.test.com',
                "notes": 'test note'
            }
    assert projects[1] == {
                "id": 2,
                "name": 'jumper',
                "link": 'www.test.com',
                "notes": 'test note 2',
            }
    assert projects[2] == {
                "id": 3,
                "name": 'cardigan',
                "link": 'www.test.com',
                "notes": 'test note 3',
            }

"""
After calling ProjectRepository.create() with a valid project object 
a new project is added to the database
"""
def test_create_new_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    project = Project(4, "knitted blanket", "www.test.com/knitted-blanket", "Using dk yarn in pink")
    repository.create(project)
    projects = repository.all()
    assert len(projects) == 4
    assert projects[3] == {
        "id": 4,
        "name": "knitted blanket",
        "link": "www.test.com/knitted-blanket",
        "notes": "Using dk yarn in pink",
    }

"""
Calling ProjectRepository.create() with an invalid project object
returns an error message and the project is not added to the database
"""
def test_cannot_create_invalid_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    project1 = Project(4, "", None, "this project is invalid")
    project2 = Project(4, "", "www.test.com", "this project is invalid")
    project3 = Project(4, "name", None, "this project is invalid")
    assert repository.create(project1) == "Error: name and link must have a value"
    assert repository.create(project2) == "Error: name must have a value"
    assert repository.create(project3) == "Error: link must have a value"