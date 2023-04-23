#FROM python:3
#
## Allow statements and log messages to immediately appear in the Knative logs
#ENV PYTHONUNBUFFERED True
#
## Copy local code to the container image.
#ENV APP_HOME /app
#WORKDIR $APP_HOME
#COPY . ./
#
## Install production dependencies.
#RUN pip install -r requirements.txt
#RUN pip install gunicorn
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

FROM python:3

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

RUN pip install --upgrade pip
COPY ./requirements.txt .

# Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY . .
EXPOSE 5000
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app