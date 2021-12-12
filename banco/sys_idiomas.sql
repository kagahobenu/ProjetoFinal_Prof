--
-- File generated with SQLiteStudio v3.3.3 on dom dez 12 11:35:22 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: alunos
CREATE TABLE alunos (
        id INTEGER PRIMARY KEY NOT NULL, 
        nome TEXT (100) NOT NULL, 
        cpf INTEGER (11) NOT NULL UNIQUE, 
        telefone INTEGER (11) NOT NULL, 
        curso TEXT (100) NOT NULL, 
        matricula INTEGER (6) NOT NULL UNIQUE, 
        semestre INTEGER (5) NOT NULL, 
        status TEXT NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
