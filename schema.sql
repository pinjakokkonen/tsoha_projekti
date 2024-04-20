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
    place TEXT
    );

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY, 
    course_id INTEGER REFERENCES courses, 
    user_id INTEGER REFERENCES users
    );

INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place) VALUES ('tanssi', 'baletti', 'ohjaaja', 5, 'maanantaisin 21.00', 'sali 1');
INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place) VALUES ('palloilulajit', 'tennis', 'ohjaaja', 5, 'keskiviikkoisin 18.00', 'kenttä 2');
INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place) VALUES ('palloilulajit', 'jalkapallo', 'ohjaaja', 5, 'sunnuntaisin 17.30', 'kenttä 2');
INSERT INTO courses (sport, course_name, instructor, max_enrollments, event_time, place) VALUES ('muut', 'kuntosali', 'ohjaaja', 5, 'torstaisin 11.00', 'sali 1');