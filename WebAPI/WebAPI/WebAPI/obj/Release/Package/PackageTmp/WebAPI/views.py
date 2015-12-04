from datetime import datetime
from flask import render_template
from flask import request
from WebAPI import app
import peewee
from peewee import *

db = MySQLDatabase("lightsensor", host="us-cdbr-azure-west-c.cloudapp.net", port=3306, user="b21cc3c823533a", passwd="f5270036")

def before_request_handler():
    db.connect()

def after_request_handler():
    db.close()

class SensorData(peewee.Model):
    timestamp = peewee.DateTimeField(default=datetime.now)
    data = peewee.DoubleField()
    class Meta:
        database = db

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/insert_sensor_data')
def insert_sensor_data():

    data = request.args.get('data')
    
    sensor_data = SensorData(data=float(data))
    sensor_data.save()
    return "Success!"