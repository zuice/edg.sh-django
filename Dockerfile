FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 5555

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Add whitenoise`
RUN sed -i "s/MIDDLEWARE = \[/MIDDLEWARE = [\n    'whitenoise.middleware.WhiteNoiseMiddleware',/" /app/edgsh/settings.py

# Add WhiteNoise storage configuration
RUN echo "STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'" >> /app/edgsh/settings.py

# Run migrations
RUN python manage.py migrate

# Run gunicorn
CMD gunicorn edgsh.wsgi:application --bind 0.0.0.0:$PORT