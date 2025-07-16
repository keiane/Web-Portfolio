from flask import Flask, render_template, redirect, url_for, request, send_file
from flask_bootstrap import Bootstrap5
from flask_mail import Mail, Message
from forms import Contact
import smtplib
from datetime import datetime
import os

'''
python -m pip install -r requirements.txt
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

RECAPTCHA_SECRET_KEY = os.environ.get("RECAPTCHA_SECRET_KEY")
RECAPTCHA_SITE_KEY = os.environ.get("RECAPTCHA_SITE_KEY")

mail = Mail(app)

Bootstrap5(app)

current_year = datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", current_year=current_year)


@app.route('/about')
def about():
    return render_template('about.html', current_year=current_year)


@app.route('/experience')
def experience():
    return render_template('experience.html', current_year=current_year)

@app.route("/success")
def contact_success():
    return render_template("contact_success.html", current_year=current_year)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        msg = Message(subject=f"Portfolio message from {data['name']}", 
                      body=f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['number']}\n\n{data['message']}", sender=os.environ.get('MAIL_USERNAME'), recipients=[os.environ.get('MAIL_RECIPIENT')])


        try:
            mail.send(msg)
            return redirect(url_for("contact_success"))
        except Exception as e:
            print(f"Failed to send email: {e}")
            return render_template("contact.html", current_year=current_year)
    return render_template("contact.html", current_year=current_year)

@app.route('/projects')
def projects():
    return render_template('projects.html', current_year=current_year)

@app.route('/resume')
def resume():
    return render_template('resume.html', current_year=current_year)


if __name__ == '__main__':
    app.run(debug=False)