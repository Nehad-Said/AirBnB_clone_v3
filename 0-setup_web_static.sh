#!/usr/bin/env bash
# Setting up the webserver

# Install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create directories
mkdir -p /data/web_static/{releases/test,shared}

# Create "index.html" with hello, wordl
echo "Hello, World" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Set ownership and permissions
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sh -c 'echo "server {
    listen 80;
    listen [::]:80 default_server;
    server_name abdul17.tech;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'

# restart nginx
sudo service nginx restart
