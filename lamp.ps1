﻿#!/bin/bash
sudo apt update && sudo apt upgrade -y
sudo apt install apache2 -y
sudo chmod -R 777 /var/www/html
sudo apt-get install php libapache2-mod-php -y
sudo apt-get install mysql-server php-mysql -y
sudo mysql_secure_installation
sudo service apache2 restart
mysql -u root -p
sudo mysql -u root
USE mysql;
UPDATE user SET plugin='azerty' WHERE User='JoelPi';
FLUSH PRIVILEGES;
quit
service mysql restart
sudo apt-get install phpmyadmin
include /etc/phpmyadmin/apache.conf
sudo /etc/init.d/apache2 restart
sudo apt-get install filezilla