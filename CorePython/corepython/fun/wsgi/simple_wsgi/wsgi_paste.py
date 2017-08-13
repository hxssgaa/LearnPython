import os
import sys

from paste import httpserver
from paste.deploy import loadapp

ini_path = os.path.normpath(
    os.path.join(os.path.abspath(sys.argv[0]),
                 os.pardir,
                 'api-paste.ini')
)

if not os.path.isfile(ini_path):
    print("Cannot find api-paste.ini.\n")
    exit(1)

wsgi_app = loadapp('config:' + ini_path)
httpserver.serve(wsgi_app, host='127.0.0.1', port=8080)
