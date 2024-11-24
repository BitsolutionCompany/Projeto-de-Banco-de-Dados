SELECT A.codAluno, A.nomeAluno, N.nota FROM ALUNOS A JOIN NOTAS N ON A.codAluno = N.codAluno WHERE N.codDisciplina = 3;

-- Saida: +----------+------------+------+
| codAluno | nomeAluno  | nota |
+----------+------------+------+
|        3 | Jo?o Silva | 6.00 |
+----------+------------+------+