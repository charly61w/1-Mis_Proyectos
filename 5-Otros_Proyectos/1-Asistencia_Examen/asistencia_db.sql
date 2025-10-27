
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS asistencia_db;
USE asistencia_db;

-- Crear tabla alumnos con tipo_documento
CREATE TABLE IF NOT EXISTS alumnos (
    id_alumno INT AUTO_INCREMENT PRIMARY KEY,
    tipo_documento ENUM('DNI', 'LC', 'LE') NOT NULL DEFAULT 'DNI',
    documento INT(10) UNSIGNED NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    email VARCHAR(50),
    telefono VARCHAR(20) NULL,
    carrera VARCHAR(50),
    instancia VARCHAR(50) NOT NULL
);

-- Crear tabla asistencia
CREATE TABLE IF NOT EXISTS asistencia (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    id_alumno INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    profesor VARCHAR(100),
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno) ON DELETE CASCADE
);

-- Insertar datos de prueba
INSERT INTO alumnos (tipo_documento, documento, nombre, apellido, email, telefono, carrera, instancia) VALUES
('DNI', '35004550', 'ADRIANA', 'AGUILERA', 'aguileraadriana813@gmail.com', NULL, 'Ingenieria Quimica', 'Regularidad/Promoción'),	
('LC', '4567890', 'María', 'González', 'Instrumentación Quirúrgica'),
('LE', '3456789', 'Pedro', 'López', 'Kinesiología');

INSERT INTO alumnos (tipo_documento, documento, nombre, apellido, email, telefono, carrera, instancia) VALUES
('DNI', '35004550', 'ADRIANA', 'AGUILERA', 'aguileraadriana813@gmail.com', NULL, 'Ingenieria Quimica', 'Regularidad/Promoción'),
('DNI', '44652980', 'PABLO', 'ALEMAN', 'aleman18pablo@gmail.com', '3764765679', NULL, 'Regularidad/Promoción'),
('DNI', '36059363', 'ALEXIS FERNANDO', 'ALVEZ DA SILVA', 'alvezdasilvaalexisfernando@gmail.com', '3764864659', NULL, 'Regularidad/Promoción');
