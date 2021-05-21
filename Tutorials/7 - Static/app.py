# This static file refering to index.html in templates folder and hello.js in static folder.

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # Home Route
def index():
   return render_template("index.html") # call index.html

if __name__ == '__main__':
   app.run(debug = True)