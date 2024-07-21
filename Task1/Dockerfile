FROM python:3.10

WORKDIR /opt

COPY requirements.txt .
RUN pip install -r requirements.txt --trusted-host pypi.python.org --no-cache-dir
COPY dags /dags

CMD [ "python", "/dags/task1.py" ]