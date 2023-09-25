DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS game_stats;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR (100) UNIQUE NOT NULL,
    password CHAR (60) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE scores (
    score_id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (score_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE game_stats (
    stat_id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    hours_played INT NOT NULL,
    enemies_defeated INT NOT NULL,
    metres_gained INT NOT NULL,
    damage_given INT NOT NULL,
    damage_taken INT NOT NULL,
    PRIMARY KEY (stat_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);