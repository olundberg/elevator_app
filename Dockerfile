# Set base image (host OS)
FROM python:3.9

USER root

# Set the working directory in the container
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt && apt-get update

# Install dependencies
COPY ./ ./

EXPOSE 5000

#CMD ["gunicorn", "-b", "0.0.0.0:5000", "index:server", "-t", "200"]
