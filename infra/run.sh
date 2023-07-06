#!/bin/sh
echo "##### НАЧИНАЕМ РАБОТУ #####"
echo " "
echo "### 1. Собираем статику ###"
sudo docker-compose exec web python3 manage.py collectstatic --no-input
echo " "
echo "### 2. Выполняем миграции ###"
sudo docker-compose exec web python3 manage.py migrate
echo " "
echo "### 3. Загружаем тестовые данные ###"
sudo docker-compose exec web python3 manage.py loaddata dump.json
echo " "
echo "### 4. Создаём суперпользователя ###"
sudo docker-compose exec web python3 manage.py createsuperuser
echo " "
echo "##### РАБОТА ЗАВЕРШЕНА #####"
