#!/usr/bin/env python
import subprocess

DOCKER_OPTIONS = [
    ('--rm', ''),
    ('-it', ''),
    ('-d', ''),
    ('-p', '8001:80'),
    ('--name', 'toyproject'),
]
DOCKER_IMAGE_TAG = 'devsuji/toyproject'

subprocess.run('poetry export -f requirements.txt > requirements.txt', shell=True)
subprocess.run(f'docker build -t {DOCKER_IMAGE_TAG} -f Dockerfile .', shell=True)
subprocess.run(f'docker stop toyproject', shell=True)

subprocess.run('docker run {options} {tag} /bin/bash'.format(
    options=' '.join([
        f'{key} {value}' for key, value in DOCKER_OPTIONS
    ]),
    tag=DOCKER_IMAGE_TAG,
), shell=True)

subprocess.run('docker cp secrets.json toyproject:/srv/toyproject', shell=True)

subprocess.run('docker exec -it toyproject /bin/bash', shell=True)