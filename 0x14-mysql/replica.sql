-- setup users
DROP USER IF EXISTS 'replica_user'@'%';
CREATE USER 'replica_user'@'%' IDENTIFIED BY '';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY '';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

