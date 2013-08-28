from bottle import route, run, error
from pages import *
import os

@route('/')
def index():
	return htmlHead+"hello world"+htmlEnd

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

