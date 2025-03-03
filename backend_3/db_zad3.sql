CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    fio VARCHAR(100),
    phone VARCHAR(100),
    email VARCHAR(100),
    dob DATE,
    gender VARCHAR(100),
    bio VARCHAR(255)
);

CREATE TABLE langs(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE fav_langs(
    user_id INT,
    lang_id INT,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(lang_id) REFERENCES langs(id) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (user_id, lang_id)
);

INSERT INTO langs(name) VALUES
('Pascal'),
('C'),
('C++'),
('JavaScript'),
('PHP'), 
('Python'),
('Java'),
('Haskell'), 
('Clojure'), 
('Prolog'), 
('Scala'), 
('Go');

INSERT INTO users(fio,phone,email,dob,gender,bio) VALUES
('artem','89181817423','arkoldasov@bk.ru','2005-11-06','Male','Empty');

SELECT id FROM users
WHERE fio='artem';

SELECT id FROM langs
WHERE name='C';

INSERT INTO fav_langs(user_id,lang_id)
SELECT u.id, l.id FROM
users u JOIN langs l ON l.name="C"
WHERE u.fio="artem";