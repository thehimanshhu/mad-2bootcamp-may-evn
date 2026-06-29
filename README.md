# household service applciation 


# find a process running a port
sudo lsof -i :<port>

# stop process running at a port
sudo kill <pid>

# run redis server 
redis-server

# if still doesn't wor

sudo systemctl stop redis

# running celery app
celery -A app.celery worker -loglevel INFO