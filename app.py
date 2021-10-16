# Import the dependencies
import datetime as dt
import numpy as np
import pandas as pd

#Import dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#Import the Flask dependency
from flask import Flask
from flask import jsonify

# Access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session link from Python to our database
session = Session(engine)

#Create a New Flask App Instance
app = Flask(__name__)

# Define the welcome route
@app.route("/")

#Create a function welcome() w a return statement
def welcome():
    return(
    f"Welcome to the Climate Analysis API!<br/>"
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/temp/start/end<br/"
    )

# Create precipitation route:
@app.route("/api/v1.0/precipitation")

# Create the precipitation function:
def precipitation():
    # calculates the date 1yr ago from the most recent date
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create station route (to station table)
@app.route("/api/v1.0/stations")

# Create the station function:
def stations():
    # A query to get all of the stations
    results = session.query(Station.station).all()
    # Unravel (untangle) result into a list
    stations = list(np.ravel(results))
    # jsonify the list and return our results
    return jsonify(stations=stations)

# Create temperature route:
@app.route("/api/v1.0/tobs")

# Create temp_monthly function:
def temp_monthly():
    #calculate the date 1 yr ago from the last day in the database:
    prev_year = dt.date(2017, 8, 23)- dt.timedelta(days=365)
    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date>= prev_year).all()
    # Unravel (untangle) result into a list
    temps = list(np.ravel(results))
    #  jsonify the list and return our results
    return jsonify(temps=temps)

# Create statistic route (start & end date)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create function stats w star & end parameters
def stats(start=None, end=None):
    #Create a list sel to select the min, average, max temps from SQLite
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # query our database using the list sel:
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        #  Unravel (untangle) result into a list
        temps = list(np.ravel(results))
        # jsonify the list and return our results
        return jsonify(temps)
    
    # calculate the temps min, average, max w the start & end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))    
    return jsonify(temps=temps)
