# Pull base image
FROM python:3.8
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy project
COPY . /code/

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
