FROM python:stretch
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
WORKDIR /code
COPY . /code
CMD gunicorn  -w 1 -b 0.0.0.0:8001 --worker-class gevent --chdir my_budget/backend/ wsgi:app
