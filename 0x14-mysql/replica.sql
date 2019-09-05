-- setup users
DROP USER IF EXISTS 'replica_user'@'%';
CREATE USER 'replica_user'@'localhost' IDENTIFIED BY '';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
GRANT SELECT ON *.* TO 'holberton_user'@'localhost';
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE `nexus6` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(127) NOT NULL, PRIMARY KEY (`id`));
INSERT INTO `nexus6` (name) VALUES ("Ernesto");

