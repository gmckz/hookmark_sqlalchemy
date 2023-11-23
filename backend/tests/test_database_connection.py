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
    db_connection.execute("INSERT INTO projects (name, link, notes, created_at) VALUES ('jumper', 'www.jumperlink.com', 'sample note', '2023-12-01 12:00:00')")
    result = db_connection.execute("SELECT * FROM projects")
    assert result == [
        {"id": 1, "name": "cable knit hat", "link": "www.test.com", "notes": "test note", "created_at" : datetime(2023, 11, 9, 15, 35, 0)},
        {"id": 2, "name": "jumper", "link": "www.test.com", "notes": "test note 2", "created_at" : datetime(2023, 11, 14, 14, 14, 14)},
        {"id": 3, "name": "cardigan", "link": "www.test.com", "notes": "test note 3", "created_at" : datetime(2023, 11, 14, 14, 15, 0)},
        {"id": 4, "name": "jumper", "link": "www.jumperlink.com", "notes": "sample note", "created_at" : datetime(2023, 12, 1, 12)}
    ]