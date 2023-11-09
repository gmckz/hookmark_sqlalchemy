from lib.Project import Project
from datetime import datetime

"""
Constructs with id, name, link, notes and created_at
"""
def test_contructs():
    timestamp = datetime.now()
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
    timestamp = datetime.now()
    project1 = Project(1, 'beanie hat', 'test link', 'test notes', timestamp)
    project2 = Project(1, 'beanie hat', 'test link', 'test notes', timestamp)
    assert project1 == project2

"""
represents projects as string
"""
def test_return_a_string():
    timestamp = datetime(2023, 11, 9, 12)
    project1 = Project(1, 'beanie hat', 'test link', 'test notes', timestamp)
    assert str(project1) == "Project(1, beanie hat, test link, test notes, 2023-11-09 12:00:00)"