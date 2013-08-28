from bottle import route, run, error
from pages import *
import os

@route('/')
def index():
	return htmlHead+"hello world"+htmlEnd

@route('/gargareth/')
def gargPage():
	return "Hello garg, how are you doing? add something to the url like /gargareth/soemthing"

@route('/gargareth/<gargThing>')
def gargPageTool(gargThing):
	return "for a nuclear fusion generator, you need a {{gargthing}}"

#this is a change

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

