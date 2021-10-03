-- drop old table if it exists.
DROP TABLE IF EXISTS saves;

-- create new table.
CREATE TABLE saves (
    name NVARCHAR(50) NOT NULL,
    password NVARCHAR(50) NOT NULL,
    gamestate NVARCHAR(MAX) NOT NULL,
    CONSTRAINT PK_saves PRIMARY KEY (name, password)
);