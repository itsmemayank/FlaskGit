from flask import *
from flask_mail import *

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mayanknagora1999.mn@gmail.com'
app.config['MAIL_PASSWORD'] = '#programmer@10'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'mayanknagora1999.mn@gmail.com', recipients = ['mayankn@sjcem.edu.in','vidhinagora@gmail.com'])
   msg.body = '''
               This is a Test message sent from Flask Mail.
               Do Not Reply.
            '''
   mail.send(msg)
   return "<h1>Successfully Send...</h1>"

if __name__ == '__main__':
   app.run(debug = True)
