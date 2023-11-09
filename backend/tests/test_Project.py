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