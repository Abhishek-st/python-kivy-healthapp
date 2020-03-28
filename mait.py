from flask import Flask, render_template, request
from flask_mail import Mail
# import requests 

app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'ankit2632000@gmail.com',
    MAIL_PASSWORD=  ''
)

mail = Mail(app)


@app.route("/", methods = ['GET', 'POST'])
def contact():
    mail.send_message('New message from ',
                        sender='ankit2632000@gmail.com',
                        recipients = ['abhisheksunil.tiwari2018@vitstudent.ac.in'],
                        body = "hello how r u ,7000479567"
                        )

def mai():
    app.run()
    

# def got():
#     requests.get(url = 'localhost:5000/') 
