# Importing dependencies/libraries
import datetime as dt
import numpy as np
import pandas as pd

# Importing SQLAlchemy dependencies/libraries
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Creating the flask app
from flask import Flask, jsonify

# Establishing database

engine = create_engine("sqlite:///hawaii.sqlite")

# Reflecting database into different bins
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Creating session link from Python to our database
session = Session(engine)

# Setting up flask app
app = Flask(__name__)

# Creating Routes


@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''') 
# Make sure to run 'export FLASK_APP=app.py' and 'flask run' in terminal
