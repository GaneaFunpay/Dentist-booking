# Dentist-Booking
# Requirements:
Python: 3.8.0 
# 1) Database
Database is ready to use for your convenience.
# 2) Django
`pip3 install -r requiremets.txt`
`python manage.py migrate`
`python manage.py runserver`
# 3) Mail sending
In settings.py:
```
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your email password (if gmail https://support.google.com/mail/answer/185833?hl=en-GB)'
```
For 1 day before notify you should run background_tasks
```
python manage.py process_tasks
```
# FAQ
Admin:
```
username: aboba 
password: aboba
```
Dentist:
```
username: doctor1 (up to doctor5)
password: 069921505qwerty
```
Client:
```
username: client1 
password: 069921505qwerty
```
The way I chose to check the availability of a doctor is bad practice.
I have been chosen this because had no enough time. 
For statistics I made possibility to export in different file formats