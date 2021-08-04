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

# Creating Welcome Page
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

# Creating Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Creating Stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Creating Tempurate Observation route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Make sure to run 'export FLASK_APP=app.py' and 'flask run' in terminal
