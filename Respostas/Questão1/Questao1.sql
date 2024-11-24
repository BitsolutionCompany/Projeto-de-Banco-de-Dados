create database if not exists escola;
use escola;

create table if not exists ALUNOS(
    codAluno int not null primary key auto_increment,
    nomeAluno text not null,
    nomeMae text not null,
    nomePai text not null,
    cpf varchar(15) not null,
    telefone varchar(15) not null,
    cep varchar(14) not null,
    cidade varchar(100) not null,
    estado varchar(100) not null,
    logradouro varchar(100) not null,
    numero int not null,
    email varchar(100) not null,
    senha text not null,
    codTurma int not null,
    foreign key (codTurma) references TURMAS(codTurma)
)engine=InnoDB;

create table if not exists TURMAS(
    codTurma int not null primary key auto_increment,
    nomeTurma varchar(100) not null,
    ano int not null,
    semestre int not null,
    codDisciplina int not null,
    codAluno int not null,
    foreign key (codDisciplina) references DISCIPLINA(codDisciplina),
    foreign key (codAluno) references ALUNOS(codAluno)

)engine=InnoDB;

create table if not exists DISCIPLINA(
    codDisciplina int not null primary key auto_increment,
    nomeDisciplina varchar(100) not null,
    cargaHoraria int not null
)engine=InnoDB;

create table if not exists EMENTAS(
    codEmenta int not null primary key auto_increment,
    codDisciplina int not null,
    conteudo text not null,
    foreign key (codDisciplina) references TURMAS(codDisciplina)
)engine=InnoDB;

create table if not exists PAGAMENTOS(
    codPagamento int not null primary key auto_increment,
    codAluno INTEGER,
    dataPag DATE NOT NULL,
    valor decimal(10, 2) NOT NULL,
    tipoPag TEXT NOT NULL,
    FOREIGN KEY (codAluno) REFERENCES ALUNOS(codAluno)
)engine=InnoDB;

CREATE TABLE Notas (
    CodNota INT PRIMARY KEY not null auto_increment,
    codAluno INT not null,
    codDisciplina INT not null,
    nota decimal(10, 2) NOT NULL,
    dataAval DATE NOT NULL,
    FOREIGN KEY (codAluno) REFERENCES ALUNOS(codAluno),
    FOREIGN KEY (codDisciplina) REFERENCES DISCIPLINA(codDisciplina)
)engine=InnoDB;