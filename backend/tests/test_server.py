from datetime import datetime
import json
"""
When I make a GET request to /projects/:id
I get a 200 response and the name, link and notes are returned for that project as a dict
"""
def test_get_a_project(db_connection, web_client):
    db_connection.seed('seeds/hookmark_database.sql')
    response = web_client.get('/projects/1')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {"id": 1, "name": "cable knit hat", "link": "www.test.com", "notes": "test note", "created_at": datetime(2023, 11, 9, 15, 35).strftime('%a, %d %b %Y %H:%M:%S GMT')}

"""
When I make a GET request to /projects
I get a 200 response and a list of projects is returned
"""
def test_get_all_projects(db_connection, web_client):
    db_connection.seed('seeds/hookmark_database.sql')
    response = web_client.get('/projects')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {
        "projects": [
            {
                "id": 1,
                "name": 'cable knit hat',
                "link": 'www.test.com',
                "notes": 'test note',
                "created_at": datetime(2023, 11, 9, 15, 35, 0).strftime('%a, %d %b %Y %H:%M:%S GMT')
            },
            {
                "id": 2,
                "name": 'jumper',
                "link": 'www.test.com',
                "notes": 'test note 2',
                "created_at": datetime(2023, 11, 14, 14, 14, 14).strftime('%a, %d %b %Y %H:%M:%S GMT')
            },
            {
                "id": 3,
                "name": 'cardigan',
                "link": 'www.test.com',
                "notes": 'test note 3',
                "created_at": datetime(2023, 11, 14, 14, 15, 0).strftime('%a, %d %b %Y %H:%M:%S GMT')
            },
        ]}