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
    url = 'https://projecteih.firebaseio.com/carlowIT.json'
    r = requests.get(url)
    x= r.json()
    if (x['buildingID'] == building_name_send):
        total_numebr_send = str(x['numberOfPeopleIN']) + " Person"
    else:
        total_numebr_send = "NO DATA FOR THIS ADDRESS"

    return render_template(
        "results.html", person_name="osama", searched_text=addressName , building_name= building_name_send , total_numebr = total_numebr_send
    )

@app.route("/contactForm")
def contactForm():

    return render_template(
        "contactUs.html"
    )

@app.route("/emailMsg")
def emailMsg():
    print('Hi')
    return render_template(
        "sentMsg.html"
    )

app.run(debug=True)
