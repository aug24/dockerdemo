import bottle
import os
port=5000

dirname, filename = os.path.split(os.path.abspath(__file__))
print "running from", dirname
print "file is", filename

try:
   f=file(dirname + '/branch', 'r')
   branch=f.read()
   f.close
except IOError:
   branch=''

if branch=='':
   branch='local'
 
try:
   f=file(dirname + '/' + branch, 'r')
   greeting=f.read()
   f.close
except IOError:
   greeting='No greeting found'
 
@bottle.route('/')
def home_page():
    return "Hello World (branch " + branch + ") listening on port " + str(port) + ": " + greeting + "\n"
 
bottle.run(host='0.0.0.0',port=port)
