FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /myapp
COPY requirements.txt /myapp/
RUN pip install -r requirements.txt
COPY . /myapp/