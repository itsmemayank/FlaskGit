from flask import render_template, Flask, request, make_response, redirect, url_for
  
app = Flask(__name__)  
 
@app.route('/error')  
def error():  
    return "<h1><strong>Invalid Password</strong></h1>"  
 
@app.route('/')  
def login():  
    return render_template("login.html")  
 
@app.route('/success',methods = ['POST'])  
def success():  
    if request.method == "POST":  
        email = request.form['email']  
        password = request.form['pass']  
      
    if password=="test123":  
        resp = make_response(render_template('success.html'))  
        resp.set_cookie('email',email)  
        return resp  
    else:  
        return redirect(url_for('error'))  
 
@app.route('/viewprofile')  
def profile():  
    email = request.cookies.get('email')  
    resp = make_response(render_template('profile.html',name = email))  
    return resp  
  
if __name__ == "__main__":  
    app.run(debug = True)  