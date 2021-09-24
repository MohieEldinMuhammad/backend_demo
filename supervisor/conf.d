[program:hello_world]
directory=/home/ec2-user/users/hello_world
command=/home/ec2-user/users/.env/bin/gunicorn flask_app:app -b localhost:8000
autostart=true
autorestart=true
stderr_logfile=/var/log/hello_world/hello_world.err.log
stdout_logfile=/var/log/hello_world/hello_world.out.log
