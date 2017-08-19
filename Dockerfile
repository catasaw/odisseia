FROM python

RUN apt-get update

RUN apt-get install -y mysql-client

CMD sleep infinity

