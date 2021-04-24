# image for python
FROM python:3.9

# Install binary python dependencies
#RUN apk add --no-cache \
#    build-base \
#    mailcap \
#    libxslt-dev \
#    linux-headers \
#    pcre-dev \
#    python3-dev



# Add requirements and install dependencies
WORKDIR /app/
ADD requirements.txt /app/requirements.txt
ADD requirements-prod.txt /app/requirements-prod.txt

# install all the python runtime dependencies
RUN mkdir -p /var/www/static/ \
    && pip install -r requirements.txt \
    && pip install -r requirements-prod.txt


ADD . /app/


# default settings are in MemberManagement
ENV DJANGO_SETTINGS_MODULE "jay.docker_settings"

### ALL THE CONFIGURATION

# The secret key used for django
ENV DJANGO_SECRET_KEY ""

# A comma-seperated list of allowed hosts
ENV DJANGO_ALLOWED_HOSTS "localhost"

# Database settings
## Use SQLITE out of the box
ENV DJANGO_DB_ENGINE "django.db.backends.sqlite3"
ENV DJANGO_DB_NAME "/data/jay.db"
ENV DJANGO_DB_USER ""
ENV DJANGO_DB_PASSWORD ""
ENV DJANG_DB_HOST ""
ENV DJANGO_DB_PORT ""


# GSuite Auth file should be in the data volume
ENV GSUITE_AUTH_FILE /data/credentials.json


# Collect all the static files at build time
RUN DJANGO_SECRET_KEY=setup python manage.py collectstatic --noinput

# Volume and ports
VOLUME /data/
EXPOSE 80

ENTRYPOINT ["/app/docker/entrypoint.sh"]
CMD ["uwsgi", "--ini", "/app/docker/uwsgi.ini"]