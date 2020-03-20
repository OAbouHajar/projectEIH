from flask import Flask, render_template, request
import requests

app = Flask(__name__)  # "dunder name".


@app.route("/")
@app.route("/displayform")
def display_form():
    return render_template("index.html", the_title="")


@app.route("/displayResults", methods=["POST"])
def displayResults():

    # to get the search address fully
    addressName = request.form["thelocation"]
    ##split the address into list
    str_list = addressName.split(',')
    # display only the name from tha address.
    building_name_send = str_list[0]
     
    return render_template(
        "results.html", person_name="osama", searched_text=addressName , building_name= building_name_send , total_numebr = "10"
    )


app.run(debug=True)
