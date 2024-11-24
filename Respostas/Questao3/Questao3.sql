SELECT A.nomeAluno, D.nomeDisciplina FROM ALUNOS A JOIN TURMAS T ON A.codTurma = T.codTurma JOIN DISCIPLINA D ON T.codDisciplina = D.codDisciplina WHERE T.ano = 2023;

-- O tempo em segundos é: 0.006s, isso considerando executar pelo terminal mysql, elle arredonda o valor
-- Usando a função profiling: SET profiling = 1; SHOW PROFILES; ele da um tempo de 0.00565150s, podendo variar de acordo com a consulta