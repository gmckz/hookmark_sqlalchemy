DROP TABLE IF EXISTS projects;
DROP SEQUENCE IF EXISTS projects_id_seq;

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name text,
    link text,
    notes text,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO projects (name, link, notes) VALUES ('cable knit hat', 'www.test.com', 'test note');
INSERT INTO projects (name, link, notes) VALUES ('jumper', 'www.test.com', 'test note 2');
INSERT INTO projects (name, link, notes) VALUES ('cardigan', 'www.test.com', 'test note 3');

