CREATE DATABASE IF NOT EXISTS `mydb`;

USE `mydb`;

CREATE TABLE IF NOT EXISTS `rooms` (
    `username` varchar(255) NOT NULL,
    `msg` varchar(1000) NOT NULL,
    `room_id` varchar(1000) NOT NULL,
    `date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);