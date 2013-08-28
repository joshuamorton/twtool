from bottle import *
from pages import *

@('/')
def index():
	return htmlStart+"Hello"+htmlEnd