# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement #station,date,prcp,tobs
Station = Base.classes.station #station,name,latitude,longitude,elevation

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Perform the precipitation analysis and retrieve data
    # Convert the data into a dictionary
    # Return JSON representation of the dictionary
    return jsonify(rain_db)

@app.route("/api/v1.0/stations")
def stations():
    # Query and retrieve station data
    # Return JSON list of station data
    return jsonify(station_db)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query temperature observations for the most-active station
    # Return JSON list of temperature observations
    return jsonify(temp_observ_data)

@app.route("/api/v1.0/<start>")
def temp_stats_start(start):
    # Calculate temperature statistics for dates greater than or equal to the start date
    # Return JSON with temperature statistics
    return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def temp_stats_start_end(start, end):
    # Calculate temperature statistics for dates within the start and end date range
    # Return JSON with temperature statistics
    return jsonify(temp_stats)

if __name__ == "__main__":
    app.run(debug=True)