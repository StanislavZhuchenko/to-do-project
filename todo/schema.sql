DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS list;

CREATE TABLE user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
first_name TEXT,
second_name TEXT
);

CREATE TABLE list (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
title TEXT NOT NULL,
description TEXT,
due_date DATETIME,
status TEXT NOT NULL,
priority TEXT NOT NULL,
FOREIGN KEY (user_id) REFERENCES user (id)
);
