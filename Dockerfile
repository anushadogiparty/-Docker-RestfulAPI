FROM python:latest
MAINTAINER ANUSHA DOGIPARTHY "anushadogiparty@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD app.py /
COPY . /requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python","./app.py"]