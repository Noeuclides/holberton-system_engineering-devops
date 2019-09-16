-- setup users
DROP USER IF EXISTS 'holberton_user'@'localhost';
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
GRANT SELECT ON *.* TO 'holberton_user'@'localhost';
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS `nexus6` (`id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(127) NOT NULL, PRIMARY KEY (`id`));
INSERT INTO `nexus6` (name) VALUES ("Ernesto");
GRANT SELECT ON `tyrell_corp`.`nexus6` TO 'holberton_user'@'localhost';

