from flask import Flask, render_template, request,redirect, url_for,session
import requests

app = Flask(__name__)  # "dunder name".
app.secret_key = 'sadfsdfdsfdsafdsafsadfadsfadsfdsafdsfa'

def get_the_search_location():
    # to get the search address fully
    addressName = request.form["thelocation"]
    return addressName

def get_the_name_form_search_text(addressName):
    ##split the address into list
    str_list = addressName.split(',')
    # display only the name from tha address.
    building_name_send = str_list[0]

    session['building_name_send'] = building_name_send
    return building_name_send

def check_if_searched_address_in_db(building_name_send):
    found = False
    total_numebr_send = None
    url = 'https://projecteih.firebaseio.com/carlowIT.json'
    r = requests.get(url)
    x= r.json()
    if (x['buildingID'] == building_name_send):
        total_numebr_send = str(x['numberOfPeopleINDetect']) + " Person"
        found = True
    session['address_founded'] = True

    session['total_numebr_send'] = total_numebr_send
    return found, total_numebr_send



@app.route("/")
def route():
    session.clear()
    return redirect(url_for('display_form'))
@app.route("/displayform")
def display_form():
    if not session.get('address_founded') is None:
        return render_template("index.html", the_title="" , show_Alert="YES" ,building_name= session['building_name_send'])
    else:
        return render_template("index.html", the_title="" , show_Alert="NO" ,building_name= "building_name_send")

# @app.route("/displayformwithalert")
# def display_form_with_alert(building_name_send):
#     return render_template("index.html", the_title="" , show_Alert="YES" ,building_name= building_name_send) 


@app.route("/displayResults", methods=["POST"])
def displayResults():

    addressName = get_the_search_location()
    building_name_send = get_the_name_form_search_text(addressName)

    found, total_numebr_send = check_if_searched_address_in_db(building_name_send)
    print("found" , found)
    if not found:
        return redirect(url_for('display_form'))
    else:
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

    return render_template(
        "sentMsg.html"
    )




app.run(debug=True)
