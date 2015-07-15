import bottle
port=5000

f=file('/usr/lib/dockerdemo/branch', 'r')
branch=f.read()
f.close
if branch=='':
   branch='local'
 
f=file('/usr/lib/dockerdemo/' + branch, 'r')
greeting=f.read()
f.close
 
@bottle.route('/')
def home_page():
    return "Hello World (branch " + branch + ") listening on port " + str(port) + ": " + greeting + "\n"
 
bottle.run(host='0.0.0.0',port=port)
