from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        flash('File uploaded successfully.')# for displaying messages like alert in javascript.
        return redirect(url_for('upload'))
		
if __name__ == '__main__':
   app.run(debug = True)