import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement=Base.classes.measurement
Station=Base.classes.station

# Flask Setup

app = Flask(__name__)

# Flask Routes
@app.route("/")
def index():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )
        
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    data_prcp=session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    prcp_list = []
    for date, precipitation in data_prcp:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = precipitation
        prcp_list.append(precipitation_dict)

    return jsonify(prcp_list)    
    
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_data=session.query(Measurement.station).group_by(Measurement.station).all()

    session.close()

    all_stations = list(np.ravel(station_data))

    return jsonify(all_stations)    

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    date_filter='2016-08-22'
    data_tobs=session.query(Measurement.date, Measurement.tobs).filter(func.strftime("%Y-%m-%d", Measurement.date) > date_filter).filter(Measurement.station=='USC00519281').all()
    session.close()
    tobs_list= [r[1] for r in data_tobs[:]]
    return jsonify(tobs_list)    

if __name__ == '__main__':
    app.run(debug=True)