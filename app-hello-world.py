import bottle
 
@bottle.route('/')
def home_page():
    return "Hello world - listening on port 5000\n"
 
bottle.run(host='0.0.0.0',port=5000)
