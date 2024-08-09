drop table if exists partida;
drop table if exists reserva;
drop table if exists jogador;
drop table if exists time;
drop table if exists local;
drop table if exists usuario;



CREATE TABLE usuario(
    id_usuario INT NOT NULL UNIQUE,
    nome VARCHAR(255),
    email VARCHAR(255),
    senha VARCHAR(255) UNIQUE,
    -- nascimento DATE,
    telefone INT,
    -- data_criacao TIMESTAMP,
    PRIMARY KEY(id_usuario)
);

CREATE TABLE local(
    id_local INT NOT NULL,
    nome VARCHAR(255),
    endereco VARCHAR(255),
    tipo_quadra VARCHAR(255),
    disponibilidade VARCHAR(255),
    PRIMARY KEY (id_local)
);

CREATE TABLE time(
    id_time INT NOT NULL,
    nome VARCHAR(255),
    descricao VARCHAR(255),
    PRIMARY KEY (id_time)
);

CREATE TABLE jogador(
    id_jogador INT NOT NULL,
    id_usuario INT,
    id_time INT,
    posicao VARCHAR (255),
    num_camisa INT,
    PRIMARY KEY (id_jogador),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_time) REFERENCES time(id_time)
);

CREATE TABLE reserva(
    id_reserva INT NOT NULL,
    id_usuario INT,
    id_local INT,
    data_reserva DATE,
    hora_inicio TIME,
    hora_fim TIME,
    PRIMARY KEY(id_reserva),
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY(id_local) REFERENCES local(id_local)
);

CREATE TABLE partida(
    id_partida INT NOT NULL,
    id_time_casa INT,
    id_time_fora INT,
    id_local INT,
    data_jogo DATE,
    hora_início TIME,
    hora_fim TIME,
    resultado VARCHAR(255),
    PRIMARY KEY(id_partida),
    FOREIGN KEY(id_local) REFERENCES local(id_local), 
    FOREIGN KEY(id_time_casa) REFERENCES time(id_time),
    FOREIGN KEY (id_time_fora) REFERENCES  time(id_time)
);

