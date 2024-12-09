FROM python:3.11-slim

WORKDIR /aa

COPY . .

RUN pip install django

RUN python manage.py migrate

EXPOSE 9999

CMD ["python","manage.py","runserver","0"]