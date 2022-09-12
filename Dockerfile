FROM python:3.8-slim-buster

WORKDIR /opt/app

ENV DJANGO_ENV=dev
ENV DOCKER_CONTAINER=1
ENV DJANGO_HOST=0.0.0.0
ENV DJANGO_ADMIN_USER=pzerzis
ENV DJANGO_ADMIN_PASSWORD=password



RUN apt-get update && \
    apt-get install -y && \
    apt-get install gcc -y && \
    pip3 install uwsgi

RUN mkdir -p /opt/app
COPY requirements.txt /opt/app/
RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY . /opt/app

RUN chmod +x /opt/app/run.sh
CMD ["/opt/app/run.sh"]
