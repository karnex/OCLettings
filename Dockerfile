FROM python:3.9

COPY . /home/OCLettings
WORKDIR /home/OCLettings

RUN pip install --no-cache-dir -r requirements.txt

ENV env=prod

# Tells Docker to open port 80 and make it accessible from outside the container
EXPOSE 80

CMD ["gunicorn", "--bind", ":80", "--workers", "1", "oc_lettings_site.wsgi"]