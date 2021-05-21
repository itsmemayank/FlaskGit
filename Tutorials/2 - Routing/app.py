from flask import Flask
app = Flask(__name__)


# Home Route
@app.route('/')
def hello_world():
   return 'Hello World!'

# Home Route -> python
@app.route('/python')
def python():
   return 'Hello Python!'


if __name__ == '__main__':
   app.run(debug = True)


