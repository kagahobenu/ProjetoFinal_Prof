--
-- File generated with SQLiteStudio v3.3.3 on sex dez 10 12:02:10 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: alunos
CREATE TABLE alunos (id INTEGER PRIMARY KEY NOT NULL, nome TEXT (100) NOT NULL, cpf INTEGER (11) NOT NULL UNIQUE, telefone INTEGER (11) NOT NULL, curso TEXT (100) NOT NULL, matricula INTEGER (6) NOT NULL UNIQUE, semestre INTEGER (5) NOT NULL, status TEXT NOT NULL);
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (1, 'Pedro Leopoldo José', 21345678901, 87996574134, 'Espanhol', 213456, 2021.2, 'cursando');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (2, 'Ana Leticia Souza', 12345678901, 81998765432, 'Francês', 123456, 2021.2, 'matriculada');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (3, 'Horácio Silva Santos', 35697846134, 81996523486, 'Alemão', 235698, 2021.2, 'concluído');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (4, 'Ademar Gomes da Silva Junior', 86571326450, 81996874513, 'Inglês', 254963, 2021.2, 'desistente');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (5, 'Douglas Alipio Cruz', 96598435621, 87996584123, 'Espanhol', 245879, 2021.2, 'cursando');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (6, 'Alice Serafim Silva', 23456987126, 81965238472, 'Inglês', 263597, 2021.2, 'matriculado');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (7, 'Nina Amanda da Rosa', 47036328886, 92983713292, 'Inglês', 245891, 2021.2, 'cursando');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (8, 'Enzo Tiago Noah Ferreira', 98085830590, 96998883825, 'Francês', 268749, 2021.2, 'desistente');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (9, 'Vinicius Enrico Eduardo Freitas', 78692994308, 41996315172, 'Espanhol', 231546, 2021.2, 'matriculado');
INSERT INTO alunos (id, nome, cpf, telefone, curso, matricula, semestre, status) VALUES (10, 'Manoel João Tomás Costa', 14339401404, 34991280108, 'Alemão', 214563, 2021.2, 'cursando');

-- Table: funcionarios
CREATE TABLE funcionarios (id INTEGER PRIMARY KEY NOT NULL, nome TEXT (100) NOT NULL, cpf INTEGER (11) NOT NULL UNIQUE, matricula INTEGER (6) UNIQUE NOT NULL, cargo TEXT (100) NOT NULL, nivel TEXT (100) NOT NULL);
INSERT INTO funcionarios (id, nome, cpf, matricula, cargo, nivel) VALUES (1, 'Ademar Gomes da Silva', 26598743167, 125634, 'gerente', '3');
INSERT INTO funcionarios (id, nome, cpf, matricula, cargo, nivel) VALUES (2, 'Alesson Dionisio Diniz', 32654198776, 145623, 'coordenador de curso', '2');
INSERT INTO funcionarios (id, nome, cpf, matricula, cargo, nivel) VALUES (3, 'Marcelo Holanda Melo', 54698713668, 148967, 'agente administrativo', '1');
INSERT INTO funcionarios (id, nome, cpf, matricula, cargo, nivel) VALUES (4, 'Otavio Luiz Cardoso', 98567412336, 198745, 'coordenador de unidade', '3');
INSERT INTO funcionarios (id, nome, cpf, matricula, cargo, nivel) VALUES (5, 'Cristina Maria Novas', 87456321097, 178345, 'agente administrativo', '2');
INSERT INTO funcionarios (id, nome, cpf, matricula, cargo, nivel) VALUES (6, 'Renata Regina Regane', 62351478924, 134562, 'agente administrativo', '1');

-- Table: interessados
CREATE TABLE interessados (
    id       INTEGER      PRIMARY KEY
                          NOT NULL,
    nome     TEXT (100)   NOT NULL,
    cpf      INTEGER (11) NOT NULL,
    telefone INTEGER (11) NOT NULL,
    curso    TEXT (100)   NOT NULL,
    status   TEXT (100)   NOT NULL
);
INSERT INTO interessados (id, nome, cpf, telefone, curso, status) VALUES (1, 'Luana Maria Lupércia', 26974563215, 87995486213, 'Inglês', 'contactado');
INSERT INTO interessados (id, nome, cpf, telefone, curso, status) VALUES (2, 'Roberto Pessoa Moraes', 65897415368, 81984561230, 'Espanhol', 'não contactado');
INSERT INTO interessados (id, nome, cpf, telefone, curso, status) VALUES (3, 'Epitáfio José de Castro', 75849612304, 81996784512, 'Francês ', 'confirmado');
INSERT INTO interessados (id, nome, cpf, telefone, curso, status) VALUES (4, 'Suzana Ferreira da Silva', 65987412935, 87996872541, 'Francês', 'não confirmado');
INSERT INTO interessados (id, nome, cpf, telefone, curso, status) VALUES (5, 'Patrícia Cavalcanti Araújo', 47859613650, 87994781635, 'Alemão', 'contactar posteriormente');

-- Table: professores
CREATE TABLE professores (id INTEGER PRIMARY KEY NOT NULL, nome TEXT (100) NOT NULL, cpf INTEGER (11) NOT NULL, telefone INTEGER (11) NOT NULL, cuso TEXT (100) NOT NULL, matricula INTEGER (6) UNIQUE NOT NULL, quant INTEGER (2) NOT NULL, status TEXT (100) NOT NULL);
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (1, 'Renato Almeida Rodrigues', 798415263045, 81993457218, 'Inglês', 145263, 4, 'ativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (2, 'Maria Luiza Stonks', 845961237064, 87997854123, 'Alemão', 156324, 4, 'ativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (3, 'Vitória Silvana Rodrigues', 584979651230, 81997451623, 'Francês', 146329, 5, 'ativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (4, 'Rafael Santos Oliveira', 659874123650, 81997452618, 'Espanhol', 163254, 3, 'inativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (5, 'Maurício de Lima Teixeira', 450896123707, 81987632654, 'Inglês', 178692, 3, 'ativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (6, 'Ester Clarice Julia Cavalcanti', 94095747579, 86984093757, 'Espanhol', 162453, 2, 'inativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (7, 'Manoel Vicente Bernardo da Luz', 11520996632, 85993887477, 'Inglês', 146153, 3, 'ativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (8, 'Josefa Bianca Manuela Moraes', 93182939769, 87993539444, 'Alemão', 158746, 4, 'inativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (9, 'Bento Carlos Iago dos Santos', 39278613916, 79984640296, 'Francês', 163542, 3, 'ativo');
INSERT INTO professores (id, nome, cpf, telefone, cuso, matricula, quant, status) VALUES (10, 'Teresinha Isabella Nascimento', 13677607205, 61996978556, 'Inglês', 164253, 4, 'ativo');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
