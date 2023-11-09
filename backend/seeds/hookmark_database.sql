DROP TABLE IF EXISTS projects;
DROP SEQUENCE IF EXISTS projects_id_seq;

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name text,
    link text,
    notes text,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO projects (name, link, notes, created_at) VALUES ('cable knit hat', 'www.google.com', 'test note', '2023-11-09 15:35:00')