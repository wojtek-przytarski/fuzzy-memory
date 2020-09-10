# fuzzy-memory

The application calculates second tetration (n ^ n) of the number 
and stores the result in DB.


To run the application use these commands:

1. `docker-compose build`
2. `docker-compose run web python manage.py migrate`
3. `docker-compose up -d`
