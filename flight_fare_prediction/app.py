from flask import Flask, request, render_template, redirect
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_fare_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date of Journey
        date_dep = request.form["dep_time"]
        journey_day = int(pd.to_datetime(
            date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(
            date_dep, format="%Y-%m-%dT%H:%M").month)

        # Departure time
        dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        dep_mins = int(pd.to_datetime(
            date_dep, format="%Y-%m-%dT%H:%M").minute)

        # Arrival time
        date_arr = request.form["arrival_time"]
        arr_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        arr_mins = int(pd.to_datetime(
            date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Duration
        dur_hour = abs(arr_hour - dep_hour)
        dur_min = abs(arr_mins - dep_mins)

        # Total Stops
        total_stops = int(request.form["stops"])

        # Airline
        airline = request.form["airline"]
        if(airline == "Jet Airways"):
            jet_airways = 1
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "IndiGo"):
            jet_airways = 0
            indigo = 1
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Air India"):
            jet_airways = 0
            indigo = 0
            air_india = 1
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Mutiple Carriers"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 1
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Spice Jet"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 1
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Vistara"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 1
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Go Air"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 1
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Multiple Carriers Premium Economy"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 1
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Jet Airways Business"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 1
            vistara_prem_eco = 0
            trujet = 0

        elif(airline == "Vistara Premium Economy"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 1
            trujet = 0

        elif(airline == "Tru Jet"):
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 1

        else:
            jet_airways = 0
            indigo = 0
            air_india = 0
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_prem_eco = 0
            jet_airways_business = 0
            vistara_prem_eco = 0
            trujet = 0

        # Source
        source = request.form["source"]
        if (source == "delhi"):
            s_delhi = 1
            s_kolkata = 0
            s_mumbai = 0
            s_chennai = 0

        elif (source == "kolkata"):
            s_delhi = 0
            s_kolkata = 1
            s_mumbai = 0
            s_chennai = 0

        elif (source == "mumbai"):
            s_delhi = 0
            s_kolkata = 0
            s_mumbai = 1
            s_chennai = 0

        elif (source == "chennai"):
            s_delhi = 0
            s_kolkata = 0
            s_mumbai = 0
            s_chennai = 1

        else:
            s_delhi = 0
            s_kolkata = 0
            s_mumbai = 0
            s_chennai = 0

        # Destination
        destination = request.form["destination"]
        if(destination == "cochin"):
            d_cochin = 1
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 0

        elif(destination == "delhi"):
            d_cochin = 0
            d_delhi = 1
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 0

        elif(destination == "hyderabad"):
            d_cochin = 0
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 1
            d_kolkata = 0

        elif(destination == "kolkata"):
            d_cochin = 0
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 1

        else:
            d_cochin = 0
            d_delhi = 0
            d_new_delhi = 0
            d_hyderabad = 0
            d_kolkata = 0

        prediction = model.predict([[

            total_stops,
            journey_day,
            journey_month,
            dep_hour,
            dep_mins,
            arr_hour,
            arr_mins,
            dur_hour,
            dur_min,
            air_india,
            goair,
            indigo,
            jet_airways,
            jet_airways_business,
            multiple_carriers,
            multiple_carriers_prem_eco,
            spicejet,
            trujet,
            vistara,
            vistara_prem_eco,
            s_chennai,
            s_delhi,
            s_kolkata,
            s_mumbai,
            d_cochin,
            d_delhi,
            d_hyderabad,
            d_kolkata,
            d_new_delhi

        ]])

        output = round(prediction[0], 2)

        return render_template("result.html", prediction_text="Your flight price is Rs. {}".format(output))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
