daemon = False
chdir = '/src/toyproject/app'
bind = 'unix:/run/toyproject.sock'
accesslog = '/var/log/gunicorn/toyproject-access.log'
errorlog = '/var/log/gunicorn/toyproject-error.log'
capture_output = True