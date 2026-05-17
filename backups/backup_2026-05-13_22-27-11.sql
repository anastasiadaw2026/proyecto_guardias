-- MySQL dump 10.13  Distrib 9.7.0, for Linux (x86_64)
--
-- Host: localhost    Database: gestion_guardias
-- ------------------------------------------------------
-- Server version	9.7.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aulas.txt`
--

DROP TABLE IF EXISTS `aulas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aulas` (
  `nombre` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aulas.txt`
--

LOCK TABLES `aulas` WRITE;
/*!40000 ALTER TABLE `aulas.txt` DISABLE KEYS */;
INSERT INTO `aulas` VALUES ('102'),('103'),('104'),('105'),('120'),('1ASIR'),('1DAW'),('2SMR'),('AULA DE MÚSICA'),('LABORATORIO DE QUÍMICA');
/*!40000 ALTER TABLE `aulas.txt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `nombre` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES ('1BACH-CS\n'),('1BACH-GL\n'),('1BACH-HCS\n'),('1CFGB-IC\n'),('1CFGM-SMR\n'),('1CFGS-ASIR\n'),('1CFGS-DAW\n'),('﻿1ESO-A\n'),('﻿1ESO-B\n'),('﻿1ESO-C\n'),('﻿1ESO-D\n'),('﻿1ESO-E\n'),('2BACH-CS\n'),('2BACH-GL\n'),('2BACH-HCS\n'),('2CFGB-IC\n'),('2CFGM-SMR\n'),('2CFGS-ASIR\n'),('2CFGS-DAW\n'),('2ESO-A\n'),('2ESO-B\n'),('2ESO-C\n'),('2ESO-D\n'),('2ESO-E\n'),('2ESO-F\n'),('3ESO-A\n'),('3ESO-B\n'),('3ESO-C\n'),('4ESO-A\n'),('4ESO-B\n'),('4ESO-C\n'),('4ESO-D\n'),('CE-CIB\n'),('CE-IABD\n');
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guardias`
--

DROP TABLE IF EXISTS `guardias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guardias` (
  `id` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `dia` date NOT NULL,
  `hora` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL DEFAULT '',
  `curso` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL DEFAULT '',
  `aula` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL DEFAULT '',
  `tarea` varchar(1) COLLATE utf8mb3_spanish2_ci NOT NULL DEFAULT 'N',
  `ficheros` mediumtext COLLATE utf8mb3_spanish2_ci,
  PRIMARY KEY (`id`,`dia`,`hora`),
  KEY `FK_horas` (`hora`),
  KEY `FK_curso` (`curso`),
  KEY `FK_aulas` (`aula`),
  CONSTRAINT `FK_aulas` FOREIGN KEY (`aula`) REFERENCES `aulas` (`nombre`),
  CONSTRAINT `FK_curso` FOREIGN KEY (`curso`) REFERENCES `cursos` (`nombre`),
  CONSTRAINT `FK_horas` FOREIGN KEY (`hora`) REFERENCES `horas` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guardias`
--

LOCK TABLES `guardias` WRITE;
/*!40000 ALTER TABLE `guardias` DISABLE KEYS */;
INSERT INTO `guardias` VALUES ('napellido_1aapellido_1b','2026-02-02','8:55 - 9:50','1BACH-GL','103','N','2'),('napellido_2aapellido_2b','2026-05-01','12:10 - 13:05','1CFGS-ASIR','102','S','tarea.pdf'),('napellido_3aapellido_3b','2026-03-02','9:50 - 10:45','1BACH-HCS','104','N',''),('napellido_3aapellido_3b','2026-06-30','11:15 - 12:10','2ESO-D','1DAW','S','');
/*!40000 ALTER TABLE `guardias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horas.txt`
--

DROP TABLE IF EXISTS `horas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horas` (
  `nombre` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horas.txt`
--

LOCK TABLES `horas` WRITE;
/*!40000 ALTER TABLE `horas.txt` DISABLE KEYS */;
INSERT INTO `horas` VALUES ('11:15 - 12:10'),('12:10 - 13:05'),('13:05 - 14:00'),('8:00 - 8:55'),('8:55 - 9:50'),('9:50 - 10:45');
/*!40000 ALTER TABLE `horas.txt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesores`
--

DROP TABLE IF EXISTS `profesores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesores` (
  `id` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `apellidos` varchar(255) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `clave` varchar(255) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesores`
--

LOCK TABLES `profesores` WRITE;
/*!40000 ALTER TABLE `profesores` DISABLE KEYS */;
INSERT INTO `profesores` VALUES ('napellido_1aapellido_1b','Nombre 1','Apellido_1a Apellido_1b','$2b$12$JSQM1j/qIYln/7PypeOYqOzL/N/MqjCDW47uxAC2ZCeGQpoytCdge'),('napellido_2aapellido_2b','Nombre2','Apellido_2a Apellido_2b','$2b$12$ehydfcrYLMJXq3fCW8cf5etrPKQltmRggF5WTY10FMB3gI76d8fKi'),('napellido_3aapellido_3b','Nombre 3','Apellido_3a Apellido_3b','$2b$12$wJKCcp96LuYecuceD5TlueOWv.P76iDUS8AkNKE35DY0HZV2pBccq'),('ndeapellido_4aapellido_4b','Nombre 4','de Apellido_4a Apellido_4b','$2b$12$bSsgATrvSivfTgqF5kuE.egkVyMTKK5m8xibLrG53fAdQsW8dUIkK');
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

-- Dump completed on 2026-05-13 20:27:11
