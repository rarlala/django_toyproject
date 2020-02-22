#!/usr/bin/env sh
IDENTIFY_FILE="$HOME/.ssh/project.pem"
HOST="ubuntu@13.124.94.217"
ORIGIN_SOURCE="$HOME/projects/wps12th/toyproject"
DEST_SOURCE="/home/ubuntu/projects/toyproject"
SSH_CMD="ssh -i ${IDENTIFY_FILE} ${HOST}"

echo "==runserver 배포=="
# 기존 폴더 삭제
echo "1. 기존 폴더 삭제"
${SSH_CMD} sudo rm -rf ${DEST_SOURCE}

# 로컬에 있는 파일 업로드
echo "2. 로컬 파일 업로드"
scp -q -i "${IDENTIFY_FILE}" -r "${ORIGIN_SOURCE}" ${HOST}:${DEST_SOURCE}

echo "Screen 설정"
# 실행중이던 screen 종료
${SSH_CMD} -C 'screen -X -S runserver quit'

# screen 실행
${SSH_CMD} -C 'screen -S runserver -d -m'

# 실행중인 세션에 명령어 전달
${SSH_CMD} -C "screen -r runserver -X stuff 'sudo python3 /home/ubuntu/projects/toyproject/app/manage.py runserver 0:80\n'"

echo "배포완료!"