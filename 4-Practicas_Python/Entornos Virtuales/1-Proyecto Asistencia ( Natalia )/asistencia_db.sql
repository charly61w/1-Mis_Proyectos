/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.11-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: asistencia_db
-- ------------------------------------------------------
-- Server version	10.11.11-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumno_profesor`
--

DROP TABLE IF EXISTS `alumno_profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno_profesor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_alumno` int(11) NOT NULL,
  `id_profesor` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_alumno` (`id_alumno`),
  KEY `id_profesor` (`id_profesor`),
  CONSTRAINT `alumno_profesor_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id`) ON DELETE CASCADE,
  CONSTRAINT `alumno_profesor_ibfk_2` FOREIGN KEY (`id_profesor`) REFERENCES `profesores` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno_profesor`
--

LOCK TABLES `alumno_profesor` WRITE;
/*!40000 ALTER TABLE `alumno_profesor` DISABLE KEYS */;
/*!40000 ALTER TABLE `alumno_profesor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumnos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_documento` enum('DNI','LC','LE','CI') NOT NULL DEFAULT 'DNI',
  `documento` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `instancia` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `documento` (`documento`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
INSERT INTO `alumnos` VALUES
(1,'DNI','35004550','Adriana','AGUILERA','aguileraadriana813@gmail.com','3764895660','Regularidad/Promoción'),
(2,'DNI','44652980','Pablo','ALEMAN','aleman18pablo@gmail.com','3764765679','Regularidad/Promoción'),
(3,'DNI','36059363','Alexis Fernando','ALVEZ DA SILVA','alvezdasilvaalexisfernando@gmail.com','3764864659','Regularidad/Promoción'),
(4,'DNI','43702678','Luciano','BALBUENA','lucianodavidbalbuena17@gmail.com','3764827902','Regularidad/Promoción'),
(5,'DNI','46389575','Cintia Carolina','BAREIRO','carolinabareiro083@gmail.com','3765055273','Regularidad/Promoción'),
(6,'DNI','47109350','Daniela','CABRAL','gimenezdaniela796@gmail.com','3758551674','Regularidad/Promoción'),
(7,'DNI','44279686','Natalia','CHAMUA','abi.unicc@gmail.com','3765211934','Regularidad/Promoción'),
(8,'DNI','46979230','Elias','CHAMULA','hunter.elias1980@gmail.com','3765192517','Regularidad/Promoción'),
(9,'DNI','42381122','José Luis','DIAZ','diazjoseluisenrique@gmail.com','3764292953','Regularidad/Promoción'),
(10,'DNI','47728965','Vanesa Janet','DOS SANTOS','vanesadossantos95@gmail.com','3764150683','Regularidad/Promoción'),
(11,'DNI','46979204','Micaela Rita','ENRIQUEZ','micaelae445@gmail.com','3764363618','Regularidad/Promoción'),
(12,'DNI','23359723','Claudia Susana','ESCUDERO','claudiaescudero191@gmail.com','3764902828','Regularidad/Promoción'),
(13,'CI','5749229','Luana','FRIEDERICH','friederichluanaayelen@gmail.com',NULL,'Regularidad/Promoción'),
(14,'DNI','43753582','Daiana Belen','GALARZA','daianagalarzag@gmail.com',NULL,'Regularidad/Promoción'),
(15,'DNI','43088080','Karen','GAMARRA','gamarrakaren37@gmail.com','3765082623','Regularidad/Promoción'),
(16,'DNI','47592538','Daniel','GONZÁLEZ','danigon8080@gmail.com','3743437336','Regularidad/Promoción'),
(17,'DNI','47108800','Florencia Luisana','GONZÁLEZ','florgonzalez1234512@gmail.com',NULL,'Regularidad/Promoción'),
(18,'DNI','44717006','Roman Javier','GONZALEZ','rg8689350@gmail.com','3764884202','Regularidad/Promoción'),
(19,'DNI','93948527','Benjamin','HERRERA MELGAREJO','notnotbenjamin@gmail.com','3764250275','Regularidad/Promoción'),
(20,'DNI','41418791','Agustina Anyeliz','KLEINüBING','agustina99anyeliz@gmail.com',NULL,'Regularidad/Promoción'),
(21,'DNI','34395664','Martin Ivan','KRAWCZUK','martinkrawczuk5@gmail.com','3764618891','Regularidad/Promoción'),
(22,'DNI','46552175','Ariel Hernán','LEAL','arielhleal@gmail.com','3764386734','Regularidad/Promoción'),
(23,'DNI','37705999','Araceli Eliana','MARTINEZ','santimiabauti15@gmail.com',NULL,'Regularidad/Promoción'),
(24,'DNI','44717260','Franco Ismael','OLIVERA','francobloggger6@gmail.com','3764533880','Regularidad/Promoción'),
(25,'DNI','44237527','Natalia Camila','OLMOS','camilaolmos1202@gmail.com','2944639294','Regularidad/Promoción'),
(26,'DNI','46479225','Cecilia','RAMIREZ','chechuramirez914@gmail.com','3764680233','Regularidad/Promoción'),
(27,'DNI','46303980','Victoria Antonela','REIS','victoriareiss515@gmail.com','3743448394','Regularidad/Promoción'),
(28,'DNI','39705010','Jorge Anibal','RUIZ','jorgitoruiz27@gmail.com','3765007480','Regularidad/Promoción'),
(29,'DNI','44717192','Anibal Adrian','SANABRIA','anibaladriansanabria90@gmail.com','3764327575','Regularidad/Promoción'),
(30,'DNI','46478444','Florencia Gabriela','SILVEIRA MARQUEZ','flor.smarquez05@gmail.com','3754478308','Regularidad/Promoción'),
(31,'DNI','37748261','Leonor Isabel','TALAVERA','talaveraleonor01@gmail.com',NULL,'Regularidad/Promoción'),
(32,'DNI','47593315','Eliana Florencia','TECHEIRA','techeiraeliana@gmail.com','3758521989','Regularidad/Promoción'),
(33,'DNI','41091127','Jorge Francisco','VAZQUEZ','jorgefranc200@gmail.com','3751218249','Regularidad/Promoción'),
(34,'DNI','46551446','Daniel Omar','VIERA','danielviera971@gmail.com',NULL,'Regularidad/Promoción'),
(35,'DNI','43548235','Juan Agustin','VILLAR','agustinvillar235@gmail.com',NULL,'Regularidad/Promoción'),
(36,'DNI','48266658','Samira','WESSELY','wesselysamira@gmail.com','3743558070','Regularidad/Promoción'),
(37,'DNI','43832398','Gabriel','ZARZA','gabrielzarza68@gmail.com','3764168895','Regularidad/Promoción'),
(38,'DNI','44129976','Pedro Fabricio','ZORRILLA','pedrofzorrilla@gmail.com',NULL,'Regularidad/Promoción');
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistencia`
--

DROP TABLE IF EXISTS `asistencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `asistencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_alumno` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `presente` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  KEY `id_alumno` (`id_alumno`),
  CONSTRAINT `asistencia_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia`
--

LOCK TABLES `asistencia` WRITE;
/*!40000 ALTER TABLE `asistencia` DISABLE KEYS */;
/*!40000 ALTER TABLE `asistencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carreras`
--

DROP TABLE IF EXISTS `carreras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `carreras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carreras`
--

LOCK TABLES `carreras` WRITE;
/*!40000 ALTER TABLE `carreras` DISABLE KEYS */;
/*!40000 ALTER TABLE `carreras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesores`
--

DROP TABLE IF EXISTS `profesores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesores`
--

LOCK TABLES `profesores` WRITE;
/*!40000 ALTER TABLE `profesores` DISABLE KEYS */;
INSERT INTO `profesores` VALUES
(1,'Natalia Silvina','Zadorozne','nataliazadorozne@gmail.com');
/*!40000 ALTER TABLE `profesores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-10  0:17:58
