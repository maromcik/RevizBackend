#!/bin/bash
build=false
superuser=false
down=false
up=false
collect=false
migrate=false

while getopts ":bsducm" option; do
  case $option in
    h) echo "usage: $0 [-h] [-b] [-s]"; exit ;;
    b) build=true ;;
    s) superuser=true ;;
    d) down=true ;;
    u) up=true ;;
    c) collect=true ;;
    m) migrate=true ;;
    ?) echo "error: option -$OPTARG does not exist - specify -b if you want to build for the first time or -s if you want to create a superuser"; exit ;;
  esac
done
shift $(( OPTIND - 1 ))

if [ "$build" = true ] ; then
  sudo docker-compose build
fi

if [ "$superuser" = true ] ; then
  docker-compose run app python3 manage.py createsuperuser
fi

if [ "$collect" = true ] ; then
  docker-compose run app python3 manage.py collectstatic
fi

if [ "$up" = true ] ; then
  docker-compose up -d
fi

if [ "$migrate" = true ] ; then
  docker-compose up -d 
  docker-compose run app python3 manage.py makemigrations audit
	docker-compose run app python3 manage.py migrate
  docker-compose down 
fi

if [ "$down" = true ] ; then
  docker-compose down
fi


