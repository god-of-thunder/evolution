FROM python:3.8

WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY django_shop_web .

CMD [ "/bin/sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000" ]