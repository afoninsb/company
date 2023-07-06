sudo docker stop infra_web_1 infra_db_1 infra_nginx_1
sudo docker rm infra_web_1 infra_db_1 infra_nginx_1
sudo docker image rm infra_web nginx:1.25.1-alpine postgres:15.3-alpine
sudo docker volume rm infra_media_value infra_postgres_value infra_static_value
