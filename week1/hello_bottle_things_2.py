__author__ = 'SekthDroid'

import bottle


@bottle.route('/')
def home():
    mythings = ["apple", "orange", "banana", "peach"]
    return bottle.template('templates/hello_fruits_with_input', username="SekthDroid", things=mythings)


@bottle.post('/favourite_fruit')
def favourite_fruit():
    fruit = bottle.request.forms.get("fruit")
    if fruit is None or fruit == "":
        fruit = "No fruit selected"
    return bottle.template('templates/fruit_selection', {'fruit': fruit})


bottle.debug(True)
bottle.run(host='localhost', port=8080)