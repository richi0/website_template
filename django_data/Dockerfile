FROM python:3.7
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# This variables are just needed for collectstatic
# They are overridden by the heroku variables 
ENV DJANGO_ALLOWED_HOSTS *
ENV DJANGO_SECRET_KEY EMPTY
ENV DJANGO_DEBUG False
# Set work directory
WORKDIR /code/django_data/
# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy project
COPY . .
# Make migrations
RUN python manage.py collectstatic --noinput