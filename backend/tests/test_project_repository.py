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
    assert project1 == Project(1, "cable knit hat", "www.test.com", "test note", datetime(2023, 11, 9, 15, 35))
    project2 = repository.find(2)
    assert project2 == Project(2, "jumper", "www.test.com", "test note 2", datetime(2023, 11, 14, 14, 14, 14))
    project3 = repository.find(3)
    assert project3 == Project(3, "cardigan", "www.test.com", "test note 3", datetime(2023, 11, 14, 14, 15))

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
                "notes": 'test note',
                "created_at": datetime(2023, 11, 9, 15, 35, 0)
            }
    assert projects[1] == {
                "id": 2,
                "name": 'jumper',
                "link": 'www.test.com',
                "notes": 'test note 2',
                "created_at": datetime(2023, 11, 14, 14, 14, 14)
            }
    assert projects[2] == {
                "id": 3,
                "name": 'cardigan',
                "link": 'www.test.com',
                "notes": 'test note 3',
                "created_at": datetime(2023, 11, 14, 14, 15, 0)
            }

"""
After calling ProjectRepository.create() with a valid project object 
a new project is added to the database
"""
def test_create_new_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    project = Project(4, "knitted blanket", "www.test.com/knitted-blanket", "Using dk yarn in pink", datetime(2023, 11, 28, 12, 27, 00))
    repository.create(project, datetime(2023, 11, 28, 12, 27, 00))
    projects = repository.all()
    assert len(projects) == 4
    assert projects[3] == {
        "id": 4,
        "name": "knitted blanket",
        "link": "www.test.com/knitted-blanket",
        "notes": "Using dk yarn in pink",
        "created_at": datetime(2023, 11, 28, 12, 27, 00),
    }