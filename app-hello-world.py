import bottle
 
@bottle.route('/')
def home_page():
    return "Hello everyone - listening on port 5000 with my even newer feature\n"
 
bottle.run(host='0.0.0.0',port=5000)
