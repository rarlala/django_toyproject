# python:3.7-slim에 사용하는걸 모두 쓰겠다.
FROM        python:3.7-slim
# RUN 마다 컨테이너 하나가 생긴다.
RUN         apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN         apt -y install nginx

# requirements를 /tmp에 복사 후, pip install실행
# 2. poetry export로 생성된 requirements.txt를 적절히 복사
COPY        ./requirements.txt /tmp/
RUN         pip install -r /tmp/requirements.txt

# 소스코드 복사 후 runserver
COPY        . /srv/toyproject
WORKDIR     /srv/toyproject/app

# nginx 설정파일 복사
RUN         rm /etc/nginx/sites-enabled/default
RUN         cp /srv/toyproject/.config/toyproject.nginx /etc/nginx/sites-enabled/

# 로그폴더 생성
RUN     mkdir /var/log/gunicorn

#CMD         python manage.py runserver 0:8000

CMD         /bin/bash