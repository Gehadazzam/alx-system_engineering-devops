# Application Server Project

## Project Overview
This project aims to set up and configure an application server to serve dynamic content for an Airbnb clone project. The server will be integrated with Nginx for proxying requests and serving web pages.

## Concepts Covered
- Web Server
- Server
- Web stack debugging

## Background Context
The existing web infrastructure is already serving web pages via Nginx. However, dynamic content needs to be served by an application server. In this project, an application server will be added to the infrastructure to serve the Airbnb clone project.

## Resources
- [Application server vs web server](#)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](#)
- [Running Gunicorn](#)
- [Be careful with the way Flask manages slash in route - strict_slashes](#)
- [Upstart documentation](#)

## Requirements
### General
- A `README.md` file is mandatory
- Python-related tasks must be done using `python3`
- All config files must have comments

### Bash Scripts
- Interpreted on Ubuntu 16.04 LTS
- End with a new line
- Executable
- Pass Shellcheck without any error
- First line should be `#!/usr/bin/env bash`


## Tasks
### 0. Set up development with Python
#### Requirements:
- Ensure task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
- Install the `net-tools` package on your server: `sudo apt install -y net-tools`
- Git clone your `AirBnB_clone_v2` on your `web-01` server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
- Your Flask application object must be named `app` (This will allow us to run and check your code).


### 1. Set up production with Gunicorn

#### Requirements:
- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called `app`. (This will allow us to run and check your code)
- Serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.
- In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.

### 2. Serve a page with Nginx

#### Requirements:
- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.
- Include your Nginx config file as `2-app_server-nginx_config`.

#### Notes:
- In order to test this you’ll have to spin up either your production or development application server (listening on port 5000)
- In an actual production environment, the application server will be configured to start upon startup in a system initialization script. This will be covered in the advanced tasks.
- You will probably need to reboot your server (by using the command `$ sudo reboot`) to have Nginx publicly accessible


### 3. Add a route with query parameters

#### Requirements:
- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to the process listening on port 5001.
- Include your Nginx config file as `3-app_server-nginx_config`.

#### Tips:
- Check out these articles/docs for clues on how to configure Nginx: Understanding Nginx Server and Location Block Selection Algorithms, Understanding Nginx Location Blocks Rewrite Rules, Nginx Reverse Proxy.
- In order to spin up a Gunicorn instance as a detached process, you can use the terminal multiplexer utility `tmux`. Enter the command `tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 web_flask.6-number_odd_or_even:app'` and if successful you should see no output to the screen. You can verify that the process has been created by running `pgrep gunicorn` to see its PID. Once you’re ready to end the process you can either run `tmux a` to reattach to the processes, or you can run `kill <PID>` to terminate the background process by ID.

### 4. Let's do this for your API

#### Requirements:
- Git clone your `AirBnB_clone_v3`
- Setup Nginx so that the route `/api/` points to a Gunicorn instance listening on port 5002
- Nginx must serve this page both locally and on its public IP on port 80
- To test your setup, you should bind Gunicorn to `api/v1/app.py`
- It may be helpful to import your data (and environment variables) from this project
- Upload your Nginx config file as `4-app_server-nginx_config`

### 5. Serve your AirBnB clone

#### Requirements:
- Git clone your `AirBnB_clone_v4`
- Your Gunicorn instance should serve content from `web_dynamic/2-hbnb.py` on port 5003
- Setup Nginx so that the route `/` points to your Gunicorn instance
- Setup Nginx so that it properly serves the static assets found in `web_dynamic/static/` (this is essential for your page to render properly)
- For your website to be fully functional, you will need to reconfigure `web_dynamic/static/scripts/2-hbnb.js` to the correct IP
- Nginx must serve this page both locally and on its public IP and port 5003
- Make sure to pull up your Developer Tools on your favorite browser to verify that you have no errors
- Upload your Nginx config as `5-app_server-nginx_config`

