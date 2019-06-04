To run django server: 
py -3 manage.py runserver

To rebuild db:
py -3 manage.py makemigrations
py -3 manage.py migrate

Admin credentials:
    username = admin
    password = admin
    email = admin@admin.com
    
To get users list use GET request on `http://127.0.0.1:8000/users/`