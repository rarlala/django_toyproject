# python:3.7-slim에 사용하는걸 모두 쓰겠다.
FROM        python:3.7-slim
# RUN 마다 컨테이너 하나가 생긴다.
RUN         apt -y update && apt -y dist-upgrade && apt -y autoremove

# requirements를 /tmp에 복사 후, pip install실행
COPY        ./requirements.txt /tmp/
RUN         pip install -r /tmp/requirements.txt

# 소스코드 복사 후 runserver
COPY        . /srv/toyproject
# WORKDIR는 cd의 의미이다.
WORKDIR     /srv/toyproject/app
CMD         python manage.py runserver 0:8000