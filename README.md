# photography-website

Build the docker image:
docker build -t django_photo_web_app .

Run the docker container:
docker run --network=host -p 8000:8000 django_photo_web_app
