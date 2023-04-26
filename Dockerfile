FROM python:3.9

COPY . /home/OCLettings
WORKDIR /home/OCLettings

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]