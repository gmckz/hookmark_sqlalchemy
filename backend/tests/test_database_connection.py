from datetime import datetime

"""
When I seed the database 
I get some records back
"""
def test_database_connection(db_connection):
    db_connection.seed("seeds/database_connection.sql")
    db_connection.execute("INSERT INTO test_table (name) VALUES (%s)", ["second_record"])
    result = db_connection.execute("SELECT * FROM test_table")
    assert result == [
        {"id": 1, "name": "first_record"},
        {"id": 2, "name": "second_record"},
    ]

"""
When I seed the hookmark database I get some records back
"""
def test_hookmark_db_connection(db_connection):
    db_connection.seed("seeds/hookmark_database.sql")
    db_connection.execute("INSERT INTO projects (name, link, notes) VALUES ('jumper', 'www.jumperlink.com', 'sample note')")
    result = db_connection.execute("SELECT * FROM projects")
    assert isinstance(result, list)
    expected_result = [
        {"id": 1, "name": "cable knit hat", "link": "www.test.com", "notes": "test note"},
        {"id": 2, "name": "jumper", "link": "www.test.com", "notes": "test note 2"},
        {"id": 3, "name": "cardigan", "link": "www.test.com", "notes": "test note 3"},
        {"id": 4, "name": "jumper", "link": "www.jumperlink.com", "notes": "sample note"}
    ]
    for actual, expected in zip(result, expected_result):
        actual.pop('created_at', None)
        assert actual == expected