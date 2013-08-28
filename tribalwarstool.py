from bottle import *
from pages import *

@route('/')
def index():
	return htmlStart+"Hello"+htmlEnd
	
run(host="http://twtool.herokuapp.com/", port=int(os.environ.get("PORT", 5000)))