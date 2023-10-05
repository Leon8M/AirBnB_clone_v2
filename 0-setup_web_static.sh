#!/usr/bin/env bash

# script that sets up web servers for the deployment of web_static

# Update package list and install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Allow Nginx HTTP traffic through the firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directory structure
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link (forcefully recreate if it already exists)
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Set ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve web_static content
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/; }' /etc/nginx/sites-enabled/default

# Restart Nginx to apply the configuration changes
sudo service nginx restart
