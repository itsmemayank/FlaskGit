from flask import Flask
app = Flask(__name__)


# Home Route
@app.route('/')
def hello_world():
   return 'Hello World!'

# Home Route -> Dynamic Route
# <name> dynamic name 
@app.route('/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# Variable Type (int, string, float)
# Home Route -> Blog Route -> Dynamic Route(int)
@app.route('/blog/<int:postID>')
def int_blog(postID):
   return 'Blog Number: %d' % postID

# Home Route -> Blog Route -> Dynamic Route(string)
@app.route('/blog/<string:name>')
def string_blog(name):
   return 'Blog Title: %s' % name

if __name__ == '__main__':
   app.run(debug = True)


   




