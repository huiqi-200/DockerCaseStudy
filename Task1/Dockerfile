FROM python:3.10
RUN apt-get update && apt-get -y install cron vim
WORKDIR /app
COPY crontab /etc/cron.d/crontab
COPY requirements.txt .
COPY dags task1/dags
COPY Datasets task1/Datasets

RUN mkdir -p task1/Processed_Datasets
RUN pip install pandas

RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

CMD /usr/sbin/cron -f

# source: https://github.com/adiii717/docker-python-cronjob/blob/master/Dockerfile