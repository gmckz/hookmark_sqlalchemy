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
