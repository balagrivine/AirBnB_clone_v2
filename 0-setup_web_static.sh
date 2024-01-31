#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

sudo apt update
sudo apt install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
	<head>
	</head>
	<body>
          Holberton School
	</body>
	</html>" > /data/web_static/releases/test/index.html

#create  asymbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

#create user and group if not already exist
#sudo adduser ubuntu
#sudo addgroup ubuntu

#change ownership of user and group
chown -R ubuntu:ubuntu /data/

#configure nginx server to serve content
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

#restart nginx server
sudo service nginx restart
