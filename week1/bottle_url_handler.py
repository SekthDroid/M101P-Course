__author__ = 'SekthDroid'

import bottle

@bottle.route('/')
def home():
    return "Hello World\n"

@bottle.route('/test_page')
def test_page():
    return "This is a test page"

bottle.debug(True)
bottle.run(host='localhost', port=8080)