from lib.Project import Project
from datetime import datetime

timestamp = datetime(2023, 11, 9, 12)

"""
Constructs with id, name, link, notes and created_at
"""
def test_contructs():
    project = Project(1, 'beanie hat', 'test link', 'test notes', timestamp)
    assert project.id == 1
    assert project.name == 'beanie hat'
    assert project.link == 'test link'
    assert project.notes == 'test notes'
    assert project.created_at == timestamp

"""
contents are equal
"""
def test_equal():
    project1 = Project(1, 'beanie hat', 'test link', 'test notes', timestamp)
    project2 = Project(1, 'beanie hat', 'test link', 'test notes', timestamp)
    assert project1 == project2

"""
represents projects as string
"""
def test_return_a_string():
    project1 = Project(1, 'beanie hat', 'test link', 'test notes', timestamp)
    assert str(project1) == "Project(1, beanie hat, test link, test notes, 2023-11-09 12:00:00)"

"""
is_valid returns true when given users with name, link and created_at properties
"""
def test_is_valid_true():
    assert Project(1, 'beanie hat', 'test link', '', timestamp).is_valid() == True
    assert Project(1, 'beanie hat', 'test link', None, timestamp).is_valid() == True
    assert Project(1, 'beanie hat', 'test link', 'test note', timestamp).is_valid() == True

"""
is_valid returns false when given users without name, link or created_at properties
"""
def test_is_valid_false():
    assert Project(1, '', 'test link', 'test note', timestamp).is_valid() == False
    assert Project(1, None, '', 'test note', timestamp).is_valid() == False
    assert Project(1, 'name', None, 'test note', timestamp).is_valid() == False