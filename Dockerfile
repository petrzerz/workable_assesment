FROM python:3.8-slim-buster

WORKDIR /opt/app

ENV DJANGO_ENV=dev
ENV DOCKER_CONTAINER=1
ENV DJANGO_HOST=0.0.0.0
ENV DJANGO_ADMIN_USER=wings
ENV DJANGO_ADMIN_PASSWORD=wings



RUN apt-get update && \
    apt-get install -y && \
    apt-get install gcc -y && \
    pip3 install uwsgi

RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/requirements.txt
RUN pip3 install -r /opt/app/requirements.txt

EXPOSE 8000

COPY . /opt/app

RUN chmod +x /opt/app/run.sh
CMD ["/opt/app/run.sh"]
#CMD ['python', 'manage.py', 'runserver','0.0.0.0:8000']
