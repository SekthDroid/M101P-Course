__author__ = 'SekthDroid'

import bottle

@bottle.route('/')
def home():
    mythings = ["apple", "orange", "banana", "peach"]
    return bottle.template('hello_world', username="SekthDroid", things=mythings)

bottle.debug(True)
bottle.run(host='localhost', port=8080)