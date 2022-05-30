FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install apt packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python3-dev build-essential pkg-config git

WORKDIR /fastapi-github-popularity

# copy code
COPY . /fastapi-github-popularity

# install python requirements
RUN pip install --upgrade pip
RUN pip install pydantic[dotenv]
RUN pip install -r requirements.txt

# start project
ENTRYPOINT ["python", "main.py"]