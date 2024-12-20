use escola;

-- Inserir na tabela ALunos
INSERT INTO ALUNOS (nomeAluno, nomeMae, nomePai, cpf, telefone, cep, cidade, estado, logradouro, numero, email, senha, codTurma) VALUES ('João Silva', 'Maria Silva', 'Carlos Silva', '123.456.789-00', '(11) 91234-5678', '12345-678', 'São Paulo', 'SP', 'Rua A', 123, 'joao.silva@email.com', 'senha123', 1);
INSERT INTO ALUNOS (nomeAluno, nomeMae, nomePai, cpf, telefone, cep, cidade, estado, logradouro, numero, email, senha, codTurma) VALUES('Ana Oliveira', 'Fernanda Oliveira', 'Roberto Oliveira', '987.654.321-00', '(11) 98765-4321', '87654-321', 'São Paulo', 'SP', 'Rua B', 456, 'ana.oliveira@email.com', 'senha456', 1);
INSERT INTO ALUNOS (nomeAluno, nomeMae, nomePai, cpf, telefone, cep, cidade, estado, logradouro, numero, email, senha, codTurma) VALUES('Pedro Santos', 'Clara Santos', 'José Santos', '456.789.123-00', '(11) 99876-5432', '23456-789', 'São Paulo', 'SP', 'Rua C', 789, 'pedro.santos@email.com', 'senha789', 2);

-- Iserir Disciplina
INSERT INTO DISCIPLINA (nomeDisciplina, cargaHoraria) VALUES('Matemática', 60);
INSERT INTO DISCIPLINA (nomeDisciplina, cargaHoraria) VALUES('Português', 60);
INSERT INTO DISCIPLINA (nomeDisciplina, cargaHoraria) VALUES('História', 45);
INSERT INTO DISCIPLINA (nomeDisciplina, cargaHoraria) VALUES('Ciências', 45);
INSERT INTO DISCIPLINA (nomeDisciplina, cargaHoraria) VALUES('Educação Física', 30);

-- Inserir Turma
INSERT INTO TURMAS (nomeTurma, ano, semestre, codDisciplina) VALUES ('1º Ano A', 2023, 1, 1);
INSERT INTO TURMAS (nomeTurma, ano, semestre, codDisciplina) VALUES ('1º Ano A', 2023, 1, 2);
INSERT INTO TURMAS (nomeTurma, ano, semestre, codDisciplina) VALUES ('1º Ano B', 2023, 1, 3);
INSERT INTO TURMAS (nomeTurma, ano, semestre, codDisciplina) VALUES ('1º Ano B', 2023, 1, 4);
INSERT INTO TURMAS (nomeTurma, ano, semestre, codDisciplina) VALUES ('2º Ano A', 2023, 1, 5);

-- Inserir Ementa
INSERT INTO EMENTAS (codDisciplina, conteudo) VALUES(1, 'Conteúdo de Matemática: Números, Operações, Geometria.');
INSERT INTO EMENTAS (codDisciplina, conteudo) VALUES(2, 'Conteúdo de Português: Leitura, Escrita, Gramática.');
INSERT INTO EMENTAS (codDisciplina, conteudo) VALUES(3, 'Conteúdo de História: História do Brasil, História Geral.');
INSERT INTO EMENTAS (codDisciplina, conteudo) VALUES(4, 'Conteúdo de Ciências: Biologia, Química, Física.');
INSERT INTO EMENTAS (codDisciplina, conteudo) VALUES(5, 'Conteúdo de Educação Física: Esportes, Atividades Físicas.');

-- Inserir Pagamentos
INSERT INTO PAGAMENTOS (codAluno, dataPag, valor, tipoPag) VALUES(4, '2023-01-15', 200.00, 'Mensalidade');
INSERT INTO PAGAMENTOS (codAluno, dataPag, valor, tipoPag) VALUES(5, '2023-01-15', 200.00, 'Mensalidade');
INSERT INTO PAGAMENTOS (codAluno, dataPag, valor, tipoPag) VALUES(3, '2023-01-15', 200.00, 'Mensalidade');

-- Inserir notas
INSERT INTO NOTAS (codAluno, codDisciplina, nota, dataAval) VALUES(3, 1, 8.5, '2023-05-10');
INSERT INTO NOTAS (codAluno, codDisciplina, nota, dataAval) VALUES(4, 2, 9.0, '2023-05-11');
INSERT INTO NOTAS (codAluno, codDisciplina, nota, dataAval) VALUES(4, 1, 7.0, '2023-05-10');
INSERT INTO NOTAS (codAluno, codDisciplina, nota, dataAval) VALUES(5, 2, 8.5, '2023-05-11');
INSERT INTO NOTAS (codAluno, codDisciplina, nota, dataAval) VALUES(3, 3, 6.0, '2023-05-10');