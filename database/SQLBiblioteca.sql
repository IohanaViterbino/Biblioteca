CREATE DATABASE biblioteca
USE biblioteca

CREATE TABLE usuario 
( 
 matricula VARCHAR(10) PRIMARY KEY,  
 nome VARCHAR(100) NOT NULL,  
 telefone VARCHAR(11) NOT NULL,  
 endereco VARCHAR(100) NOT NULL,  
 limiteLivros INT NOT NULL,  
 inadimplente INT NOT NULL,  
 ativo INT NOT NULL, 
 tipo INT NOT NULL, 
); 

CREATE TABLE tablet 
( 
 codigoTablet VARCHAR(10) PRIMARY KEY,  
 marca VARCHAR(30) NOT NULL,  
 modelo VARCHAR(50) NOT NULL,  
 memoria VARCHAR(20) NOT NULL,  
 so VARCHAR(30) NOT NULL,  
); 

CREATE TABLE livro 
( 
 codigoLivro VARCHAR(10) PRIMARY KEY,  
 titulo VARCHAR(50) NOT NULL,  
 autor VARCHAR(20) NOT NULL,  
 editora VARCHAR(20) NOT NULL,  
 categoria VARCHAR(30) NOT NULL,  
 edicao VARCHAR(10) NOT NULL,  
); 

CREATE TABLE item 
( 
 codigoItem INT PRIMARY KEY,  
 disponibilidade INT NOT NULL,  
 dataAquisicao DATE NOT NULL,  
 idLivro VARCHAR(10),  
 idTablet VARCHAR(10),  
); 

CREATE TABLE ResgistroEmprestimo 
( 
 idRegistro INT PRIMARY KEY AUTOINCREMENT,  
 limiteDevolucao INT NOT NULL,  
 valorMulta FLOAT NOT NULL,  
 dataEmprestimo DATE NOT NULL,  
 dataEsperada DATE NOT NULL,  
 iditem INT NOT NULL,  
 idUsuario VARCHAR(10), 
); 

CREATE TABLE Reserva 
( 
 idReserva INT PRIMARY KEY AUTOINCREMENT, 
 idUsuario VARCHAR(10) NOT NULL,  
 idItem INT NOT NULL,  
); 

ALTER TABLE item ADD FOREIGN KEY(idLivro) REFERENCES livro (codigo)
ALTER TABLE item ADD FOREIGN KEY(idTablet) REFERENCES tablet (codigo)
ALTER TABLE ResgistroEmprestimo ADD FOREIGN KEY(iditem) REFERENCES item (codigo)
ALTER TABLE ResgistroEmprestimo ADD FOREIGN KEY(idUsuario) REFERENCES usuario (matricula)
ALTER TABLE Reserva ADD FOREIGN KEY(idUsuario) REFERENCES usuario (matricula)
ALTER TABLE Reserva ADD FOREIGN KEY(idItem) REFERENCES item (codigo)