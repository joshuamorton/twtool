from bottle import *
from pages import *

@route('/')
def index():
	return htmlStart+"Hello"+htmlEnd
	
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))