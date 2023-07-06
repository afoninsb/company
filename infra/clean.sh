sudo docker stop infra_web_1 infra_db_1
sudo docker rm infra_web_1 infra_db_1
sudo docker volume rm infra_postgres_value
sudo docker rmi infra_web postgres:15.3-alpine
