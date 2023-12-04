from lib.Project import Project


"""
Constructs with id, name, link, notes
"""
def test_contructs():
    project = Project(1, 'beanie hat', 'test link', 'test notes')
    assert project.id == 1
    assert project.name == 'beanie hat'
    assert project.link == 'test link'
    assert project.notes == 'test notes'

"""
contents are equal
"""
def test_equal():
    project1 = Project(1, 'beanie hat', 'test link', 'test notes')
    project2 = Project(1, 'beanie hat', 'test link', 'test notes')
    assert project1 == project2

"""
represents projects as string
"""
def test_return_a_string():
    project1 = Project(1, 'beanie hat', 'test link', 'test notes')
    assert str(project1) == "Project(1, beanie hat, test link, test notes)"

"""
is_valid returns true when given projects with name, link and created_at properties
"""
def test_is_valid_true():
    assert Project(1, 'beanie hat', 'test link', '').is_valid() == True
    assert Project(1, 'beanie hat', 'test link', None).is_valid() == True
    assert Project(1, 'beanie hat', 'test link', 'test note').is_valid() == True

"""
is_valid returns false when given projects without name or link properties
"""
def test_is_valid_false():
    assert Project(1, '', 'test link', 'test note').is_valid() == False
    assert Project(1, None, '', 'test note').is_valid() == False
    assert Project(1, 'name', None, 'test note').is_valid() == False

"""
error_message returns error message when project is invalid
"""
def test_generate_error_messages():
    error_message1 = Project(1, '', 'test link', 'test note').generate_error_message()
    assert error_message1 == "Error: name must have a value"
    error_message2 = Project(1, 'name', None, 'test note').generate_error_message()
    assert error_message2 == "Error: link must have a value"