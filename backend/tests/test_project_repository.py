from lib.project_repository import ProjectRepository
from lib.Project import Project
import pytest
from lib.exceptions import ProjectNotFoundException, InvalidProjectException
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
Calling ProjectRepository.find with a non-existent id raises an exception
"""
def test_find_project_invalid_id(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    with pytest.raises(ProjectNotFoundException) as e:
        repository.find(7)
    error_message = str(e.value)
    assert error_message == "Project with id: 7 does not exist."
    
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
    with pytest.raises(InvalidProjectException) as e:
        repository.create(project1)
    error_message1 = str(e.value)
    assert error_message1 == "Error: name and link must have a value"

    project2 = Project(4, "", "www.test.com", "this project is invalid")
    with pytest.raises(InvalidProjectException) as e:
        repository.create(project2)
    error_message2 = str(e.value)
    assert error_message2 == "Error: name must have a value"
    
    project3 = Project(4, "name", None, "this project is invalid")
    with pytest.raises(InvalidProjectException) as e:
        repository.create(project3)
    error_message3 = str(e.value)
    assert error_message3 == "Error: link must have a value"

"""
Calling ProjectRepository.update() with a valid project object
updates the project with the corresponding id to the new object
"""
def test_update_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    project1 = Project(4, "Initial name", "www.test.com", "initial comment")
    repository.create(project1)
    project2 = Project(4, "New name", "www.test.com", "new comment")
    repository.update(project2)
    assert repository.find(4) == project2

"""
Calling ProjectRepository.update() with an invalid project object
returns an error message and the project is not updated
"""
def test_cannot_create_invalid_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    project1 = Project(4, "", None, "this project is invalid")
    with pytest.raises(InvalidProjectException) as e:
        repository.update(project1)
    error_message1 = str(e.value)
    assert error_message1 == "Error: name and link must have a value"

    project2 = Project(4, "", "www.test.com", "this project is invalid")
    with pytest.raises(InvalidProjectException) as e:
        repository.update(project2)
    error_message2 = str(e.value)
    assert error_message2 == "Error: name must have a value"
    
    project3 = Project(4, "name", None, "this project is invalid")
    with pytest.raises(InvalidProjectException) as e:
        repository.update(project3)
    error_message3 = str(e.value)
    assert error_message3 == "Error: link must have a value"

"""
Calling ProjectRepository.delete() with a project id
deletes the project from the database
"""
def test_delete_project(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    response = repository.delete(1)
    assert response == "Project with id 1 deleted"
    with pytest.raises(ProjectNotFoundException) as e:
        repository.find(1)
    error_message = str(e.value)
    assert error_message == "Project with id: 1 does not exist."

"""
Calling ProjectRepository.delete() with invalid project id
returns error message
"""
def test_delete_project_error(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    repository = ProjectRepository(db_connection)
    with pytest.raises(ProjectNotFoundException) as e:
        repository.find(5)
    error_message = str(e.value)
    assert error_message == "Project with id: 5 does not exist."