FROM python:3.9

COPY . /home/OCLettings
WORKDIR /home/OCLettings

RUN pip install --no-cache-dir -r requirements.txt

ENV env=prod

# Tells Docker to open port 8000 and make it accessible from outside the container
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:$PORT"]