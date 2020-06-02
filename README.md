pip install -r requirements.txt

сделать свой .env файл с переменными окружения

python3 manage.py runserver

--------------------------

Конфигурация для nginx:

server {
    listen XX;
    server_name XXX.XXX.XXX.XXX;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        proxy_pass http://127.0.0.1:8000;
    }

    location /static/ {
        root /home/user/projects/Skillfactory-E5-10;
    }

}