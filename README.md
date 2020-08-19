## DRF auction


To start application: 

```docker-compose up```

To perform migration: 

```docker exec -it {container_id} python /code/manage.py migrate```

To create superuser: 

```docker exec -it {container_id} python /code/manage.py createsuperuser```

