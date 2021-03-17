import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///titanic.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)


app = Flask(__name__)

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
   

@app.route("/api/v1.0/stations")
def stations():


@app.route("/api/v1.0/tobs")
def tobs():




if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    app.run(debug=True)