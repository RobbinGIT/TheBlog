from flask_mail import Message
from flask import render_template
from app import mail
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)

sender_email = 'robbinmwas@gmail.com'
subject_pref = 'Blog'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'robbin.githimbo@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'Shizzle27!'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


def mail_message(subject, template, to, **kwargs):
    email = Message(subject_pref + " : " + subject,sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)


   
    email.html = render_template(template + ".html",**kwargs)
   


def sub_message(subject, template, to, **kwargs):
    email = Message(subject_pref + " : " + subject,sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    mail.send(email)


if __name__ == '__main__':
    app.run()
