# Homework 5: Databases

![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/JohnSV18/web-homework-5)

![Website](https://img.shields.io/website?down_color=red&down_message=Offline&up_color=green&up_message=Online&url=http%3A%2F%2Fplants-app.dev.johnmarcos.me%2F)

## Welcome to the Plants Site!

This is a site where you can post about plants that you know as well as search up on plants you don't know about. Feel free to take a look at it and make changes in your own machine if you want. You will be using Docker so please make sure that is installed in your machine.

# Instructions to run
To clone simply run the command below:
```Terminal command
git clone https://github.com/JohnSV18/web-homework-5.git
```
You then want to run the docker compose file by running:
```Terminal command
docker-compose up -d
```
Once the containers are up and running, go to your browser and paste this:
```Http command
http://localhost:5000/
```
Once you've finished working with the containers just run:
```Terminal command
docker-compose down
```