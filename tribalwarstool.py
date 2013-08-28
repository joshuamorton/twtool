from bottle import route, run, error

global startCode
global endCode
css = "p {color:red;text-align:center;text-size:25}"
startCode = "<html>\n<head>\n<style type=\"text/css\">\n"+css+"\n</style>\n</head>\n<body>\n"
endCode = "\n</body>\n</body>"

@route('/')
def index():
	return "hello world"


@route('/mchammer/<post_id>')
def cantTouchThis(post_id):
	return startCode+" <p />You can\'t touch this, even with a " +post_id+"."+endCode

@error(404)
def notFound(error):
	return startCode+" <p />This is not the page you are looking for."+endCode


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

