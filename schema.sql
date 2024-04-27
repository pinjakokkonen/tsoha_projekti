DROP TABLE IF EXISTS feedback CASCADE;
DROP TABLE IF EXISTS enrollments CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS diary CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT UNIQUE, 
    password TEXT
    );

CREATE TABLE courses (
    id SERIAL PRIMARY KEY, 
    sport TEXT,
    course_name TEXT, 
    instructor TEXT,
    max_enrollments INTEGER,
    event_time TEXT,
    place TEXT,
    difficulty TEXT
    );

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY, 
    course_id INTEGER REFERENCES courses, 
    user_id INTEGER REFERENCES users
    );

CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses, 
    user_id INTEGER REFERENCES users,
    created_at TIMESTAMP,
    content TEXT
    );

CREATE TABLE diary (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER REFERENCES users,
    created_at TIMESTAMP,
    content TEXT
    );

INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place, difficulty) VALUES ('tanssi', 'baletti', 'ohjaaja', 5, 'maanantaisin 21.00', 'sali 1', 'alkeistaso');
INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place, difficulty) VALUES ('palloilulajit', 'tennis', 'ohjaaja', 5, 'keskiviikkoisin 18.00', 'kenttä 2', 'edistyneet');
INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place, difficulty) VALUES ('palloilulajit', 'jalkapallo', 'ohjaaja', 5, 'sunnuntaisin 17.30', 'kenttä 2', 'keskitaso');
INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place, difficulty) VALUES ('muut', 'kuntosali', 'ohjaaja', 5, 'torstaisin 11.00', 'sali 1', 'alkeistaso');