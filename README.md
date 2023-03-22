<h1 align="center">Store DjangoApp</h1>

<h2 align="center">
<p align="center">

<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >
  
<img src="https://img.shields.io/badge/Django-4.1.7-green">

<img src="https://img.shields.io/badge/Postgres-14-green" >

<img src="https://img.shields.io/badge/Redis-4.5-green">

<img src="https://img.shields.io/badge/Celery-5.2-green">

<img src="https://img.shields.io/badge/Stripe-5.2-green">

<img src="https://img.shields.io/badge/OAuth-2.0-green">

<img src="https://img.shields.io/badge/Docker-4.17-blue">

<img src="https://img.shields.io/badge/Docker--Compose-3.8-blue">

</p>
</h2>

## Description

<p align="center">
<img src="https://github.com/LatikDesu/store-djangoapp/blob/master/store/static/vendor/StoreGif.gif?raw=true" width="60%"></p>

## About the project.

A Python Django application running in a Docker container.

### Implemented:
- back end of web applications developed using Django framework
- model the database and work with the database through Django ORM
- Apply Django templates
- configured admin panel using Django Admin
- Apply and develop your own mixins
- Program authorization and registration, including through social networks
- Logging and caching data
- Connect payment gateway
- Program sending emails
- Apply CBV for better code organization

## Project setup

Create .env using 'env_exemple'
```
docker build .
docker-compose up
```
- For Stripe working you need to add "stripe_id" for the products using a loop .save()
- You may comment migrations in 'entrypoint.sh' after runserver

## Future scope

- Filling Database
- nginx
