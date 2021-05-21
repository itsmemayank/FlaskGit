from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'random string'
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      if request.form['username'] == 'admin' and request.form['password'] == 'admin':
         flash('You were successfully logged in')
         return redirect(url_for('index'))
      else:
          error = 'Invalid username or password. Please try again!'
			
   return render_template('login.html', error = error)

if __name__ == "__main__":
   app.run(debug = True)