from bottle import route, run, error
import os

@route('/')
def index():
	return "hello world"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

