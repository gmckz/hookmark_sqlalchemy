DROP TABLE IF EXISTS projects;
DROP SEQUENCE IF EXISTS projects_id_seq;

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name text,
    link text,
    notes text,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO projects (name, link, notes, created_at) VALUES ('cable knit hat', 'www.test.com', 'test note', '2023-11-09 15:35:00');
INSERT INTO projects (name, link, notes, created_at) VALUES ('jumper', 'www.test.com', 'test note 2', '2023-11-14 14:14:14');
INSERT INTO projects (name, link, notes, created_at) VALUES ('cardigan', 'www.test.com', 'test note 3', '2023-11-14 14:15:00');

