FROM httpd:latest

COPY ./home.html /usr/local/apache2/htdocs/

COPY ./docker-to-kube.png /usr/local/apache2/htdocs/
