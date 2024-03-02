-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `cam`
--

DROP TABLE IF EXISTS `cam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cam` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_photo` int NOT NULL,
  `media_path` varchar(255) NOT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cam`
--

LOCK TABLES `cam` WRITE;
/*!40000 ALTER TABLE `cam` DISABLE KEYS */;
INSERT INTO `cam` VALUES (1,1,'2.jpg','2023-11-21 05:43:35','2023-11-21 05:43:35'),(2,1,'375x291.jpg','2023-11-21 05:43:35','2023-11-21 05:43:35'),(3,1,'sample1.jpg','2023-11-21 05:43:35','2023-11-21 05:43:35');
/*!40000 ALTER TABLE `cam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mail_img`
--

DROP TABLE IF EXISTS `mail_img`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mail_img` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `result` varchar(128) DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `path` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mail_img`
--

LOCK TABLES `mail_img` WRITE;
/*!40000 ALTER TABLE `mail_img` DISABLE KEYS */;
INSERT INTO `mail_img` VALUES (1,'undefined','2023-10-30 01:50:09','images.jpg'),(2,'undefined','2023-10-30 01:50:09','images.jpg');
/*!40000 ALTER TABLE `mail_img` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,'someone came into my house!','2023-11-22 11:46:06','2023-11-22 11:46:06');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `research`
--

DROP TABLE IF EXISTS `research`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `research` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `gu_name` varchar(255) NOT NULL,
  `score` float NOT NULL,
  `ranking` int NOT NULL,
  `emoji` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `research`
--

LOCK TABLES `research` WRITE;
/*!40000 ALTER TABLE `research` DISABLE KEYS */;
INSERT INTO `research` VALUES (1,'종로구',76,10,'6-10.png'),(2,'중구',75.6,11,'11-15.png'),(3,'용산구',77.6,4,'1-5.png'),(4,'성동구',73.6,12,'11-15.png'),(5,'광진구',67.6,23,'21-25.png'),(6,'동대문구',67.6,23,'21-25.png'),(7,'중랑구',70.8,21,'21-25.png'),(8,'성북구',80.4,2,'1-5.png'),(9,'강북구',77.6,4,'1-5.png'),(10,'도봉구',86.4,1,'1-5.png'),(11,'노원구',76.4,9,'6-10.png'),(12,'은평구',77.2,7,'6-10.png'),(13,'서대문구',80,3,'1-5.png'),(14,'마포구',71.6,18,'16-20.png'),(15,'양천구',72,16,'16-20.png'),(16,'강서구',76.8,8,'6-10.png'),(17,'구로구',70,22,'21-25.png'),(18,'금천구',77.6,4,'1-5.png'),(19,'영등포구',71.6,18,'16-20.png'),(20,'동작구',73.2,13,'16-20.png'),(21,'관악구',72.8,15,'11-15.png'),(22,'서초구',72,16,'16-20.png'),(23,'강남구',73.2,13,'11-15.png'),(24,'송파구',62.4,25,'21-25.png'),(25,'강동구',71.2,20,'16-20.png');
/*!40000 ALTER TABLE `research` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resident`
--

DROP TABLE IF EXISTS `resident`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resident` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` char(50) NOT NULL,
  `img_path` varchar(255) NOT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resident`
--

LOCK TABLES `resident` WRITE;
/*!40000 ALTER TABLE `resident` DISABLE KEYS */;
/*!40000 ALTER TABLE `resident` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `result` varchar(128) DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `path` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
INSERT INTO `result` VALUES (1,'admin','2023-11-22 08:18:01','2.jpg'),(2,'admin','2023-11-22 08:18:01','375x291.jpg'),(3,'undefined','2023-11-22 06:20:48','sample1.jpg'),(4,'undefined','2023-11-22 08:18:01','portrait-sc1-8.jpg'),(5,'admin','2023-11-22 08:18:01','1200x630.jpg'),(6,'undefined','2023-10-21 11:19:30','img.jpg'),(7,'admin','2023-11-22 08:18:01','2021010600123411270_1609859554.jpg'),(8,'admin','2023-11-22 08:18:01','다운로드.jpg'),(9,'undefined','2023-10-30 01:50:09','images.jpg');
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sending`
--

DROP TABLE IF EXISTS `sending`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sending` (
  `id` int NOT NULL AUTO_INCREMENT,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `receive` varchar(255) NOT NULL,
  `e_mail` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sending`
--

LOCK TABLES `sending` WRITE;
/*!40000 ALTER TABLE `sending` DISABLE KEYS */;
INSERT INTO `sending` VALUES (5,'2023-11-23 05:19:38','이미주','메일주소1'),(6,'2023-11-23 05:19:38','이수빈','메일주소2'),(7,'2023-11-23 05:19:38','손고은','메일주소3'),(8,'2023-11-23 05:19:38','오창훈','메일주소4'),(9,'2023-11-23 05:19:38','이미주','메일주소1'),(10,'2023-11-23 05:19:38','이수빈','메일주소2'),(11,'2023-11-23 05:19:38','손고은','메일주소3'),(12,'2023-11-23 05:19:38','오창훈','메일주소4'),(13,'2023-11-23 05:19:38','이미주','메일주소1'),(14,'2023-11-23 05:19:38','이수빈','메일주소2'),(15,'2023-11-23 05:19:38','손고은','메일주소3'),(16,'2023-11-23 05:19:38','오창훈','메일주소4'),(17,'2023-11-23 05:19:38','이미주','메일주소1'),(18,'2023-11-23 05:19:38','이수빈','메일주소2'),(19,'2023-11-23 05:19:38','손고은','메일주소3'),(20,'2023-11-23 05:19:38','오창훈','메일주소4'),(21,'2023-11-23 05:19:39','이미주','메일주소1'),(22,'2023-11-23 05:19:39','이수빈','메일주소2'),(23,'2023-11-23 05:19:39','손고은','메일주소3'),(24,'2023-11-23 05:19:39','오창훈','메일주소4');
/*!40000 ALTER TABLE `sending` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unknown`
--

DROP TABLE IF EXISTS `unknown`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unknown` (
  `id` bigint NOT NULL DEFAULT '0',
  `result` varchar(128) DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unknown`
--

LOCK TABLES `unknown` WRITE;
/*!40000 ALTER TABLE `unknown` DISABLE KEYS */;
INSERT INTO `unknown` VALUES (0,'undefined','2023-11-22 10:09:32','default.jpg'),(0,'undefined','2023-11-22 10:09:32','default.jpg'),(0,'undefined','2023-11-22 10:09:32','default.jpg'),(0,'undefined','2023-11-22 06:20:48','sample1.jpg'),(0,'undefined','2023-11-22 08:18:01','portrait-sc1-8.jpg');
/*!40000 ALTER TABLE `unknown` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userid` varchar(50) NOT NULL,
  `userpw` varchar(50) NOT NULL,
  `name` char(50) NOT NULL,
  `email` char(50) NOT NULL,
  `home` char(100) NOT NULL,
  `phone` char(100) NOT NULL,
  `sos` char(50) NOT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `last_login_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'miju1218','win8803','이미주','miju1218@naver.com','용마산로8길 29','010-9230-8821','010-4756-5976','2023-11-17 01:37:39','2023-11-17 01:37:39');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-23 14:44:45
