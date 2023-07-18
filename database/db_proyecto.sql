CREATE DATABASE  IF NOT EXISTS `db_proyecto` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_proyecto`;
-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: db_proyecto
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `creador_job` int NOT NULL,
  `usuario_id` int unsigned DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_job_user_idx` (`usuario_id`),
  CONSTRAINT `fk_job_user` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (2,'CARTAJENA 2444224','RIOS23434344 22424222','OSORNO',2,2,'2023-07-10 14:12:57','2023-07-10 15:38:48'),(3,'LOS RIOS','LAGOS','CHILLAN. ',2,2,'2023-07-10 14:13:10','2023-07-10 15:37:44'),(5,'adsdsd','sddssd','sdsdds',1,2,'2023-07-10 14:58:12','2023-07-10 15:46:41'),(6,'xxxvx','xvvxvxvxvx','xvxvvxvx',1,2,'2023-07-10 14:59:10','2023-07-10 15:46:41'),(7,'fvdfbd3353535','bdbbdbdf353535353535','bfddbdfbdbd3535353535',1,2,'2023-07-10 15:03:13','2023-07-10 15:46:41'),(8,'s3r33434543234t43','sfssf3453434534','sdsddssd3453445',1,2,'2023-07-10 15:05:41','2023-07-10 15:46:41'),(9,'fsfdd','sdfdfss','dsdsdfs',1,2,'2023-07-10 15:17:36','2023-07-10 15:46:41'),(10,'vceee4','35c','c3334c',2,2,'2023-07-10 15:23:52','2023-07-10 15:46:41'),(11,'eeer','eerere','eee',2,2,'2023-07-10 15:24:16','2023-07-10 15:46:41'),(12,'mascottasw22222','sdsdds','23ewd',2,2,'2023-07-10 15:42:52','2023-07-10 15:46:41'),(13,'PRUEBA DE DATOS ','DPODODDFDF','DDFFDDFDF',2,2,'2023-07-10 15:45:33','2023-07-10 15:46:41'),(14,'PRUEBA1SSSSS','PRUEBA1SSS','PRUEBA1SSSS',2,2,'2023-07-10 15:45:59','2023-07-10 15:46:41'),(15,'DSSDDSSDSD','SDSDDSDS','SDSDSDDS',2,2,'2023-07-10 15:46:07','2023-07-10 15:46:41'),(16,'PRUEBA DE ADD 1','PRUEBA DE ADD 1','PRUEBA DE ADD 1',2,NULL,'2023-07-10 15:47:10','2023-07-10 15:47:10'),(17,'hola','hola','ddssd',1,NULL,'2023-07-10 15:52:04','2023-07-10 15:52:04'),(18,'sddsds','sdsdds','sdsdsd',1,NULL,'2023-07-10 15:52:11','2023-07-10 15:52:11');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'MARCOS ','RIQUELME ','MARCOS@GMAIL.COM','$2b$12$SYzlY4eBzCoCBtDRMbj5kOLuafVBC69CVQAkm.1ytgcNb.Or3tqH6'),(2,'ANDRES','ROMAN','AMRPERRES@GMAIL.COM','$2b$12$T8lrMpCENHq9D8L0WBkEOeJqjZn9fEkdH73.zEOL/EOx/kJaR0okK');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-10 11:58:31
