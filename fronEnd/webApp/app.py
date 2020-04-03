from flask import Flask, render_template, request,redirect, url_for,session
import requests
import pyrebase


app = Flask(__name__)  # "dunder name".
app.secret_key = 'sadfsdfdsfdsafdsafsadfadsfadsfdsafdsfa'

def get_all_data_from_firebase():
    r = requests.get('https://projecteih.firebaseio.com/locations.json')
    x= r.json()
    return x

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
    url = 'https://projecteih.firebaseio.com/locations.json'
    r = requests.get(url)
    x= r.json()
    if building_name_send in x:
        total_numebr_send = str(x[building_name_send]['numberOfPeopleINDetect']) + " Person"
        found = True
        session['address_founded'] = True

    session['total_numebr_send'] = total_numebr_send
    return found, total_numebr_send

def db_config():
    config = {
    "apiKey": "AIzaSyBa_oAgm7dmE-sFGGm8XG7HYs0gWxVFyJ8",
    "authDomain": "projecteih.firebaseio.com",
    "databaseURL": "https://projecteih.firebaseio.com",
    "storageBucket": "projecteih.appspot.com",
    "serviceAccount": "/home/osama/Desktop/projectEIH/body-detect/cred/projecteih-firebase-adminsdk-dmd9b-dfbc30ba25.json"
    }
    firebasePy = pyrebase.initialize_app(config)

    return firebasePy


def reset_to_zero(id_to_reset):
    
    db = db_config().database()
    auth = db_config().auth()
    db.child("locations").child(id_to_reset).update({'numberOfPeopleINDetect': 0})



def login_check():
    email = request.form["loginInput"]
    password = request.form["loginPass"]
    config = db_config()
    firebasePy = pyrebase.initialize_app(config)
    # Get a reference to the auth service
    auth = firebasePy.auth()
    # Log the user in
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session['logged_in_email'] = email
        session['loged_in'] = True
        return True
    except IOError:
        return False

    return email,password


@app.route("/")
def route():
    session.clear()
    return redirect(url_for('display_form'))
@app.route("/displayform")
def display_form():
    if not session.get('address_founded') is None:
        return render_template("index.html", the_title="" , show_Alert="YES" ,building_name= session['building_name_send'], fail_login= "NO")
    elif session.get('fail_login') is True:
        return render_template("index.html", the_title="" , show_Alert="NO" ,building_name= "building_name_send", fail_login="YES")
    else:
        return render_template("index.html", the_title="" , show_Alert="NO" ,building_name= "building_name_send",fail_login="NO")

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

@app.route("/allLocations")
def allLocations():
    items_send = get_all_data_from_firebase()
    return render_template(
        "allLocations.html",
        items= items_send,
        x= items_send
    )
    
@app.route("/login", methods=["POST"])
def login():

    logPass= login_check()
    
    if logPass: 
        return redirect(url_for('allLocations'))
    else:  
        session['fail_login'] = True
        return redirect(url_for('display_form'))



@app.route("/resetLocation", methods=["POST"])
def resetLocation():
    selected = request.form.getlist('reset_checkbox')
    print(selected)
    for id_to_reset in selected:
        reset_to_zero(id_to_reset)       
    return redirect(url_for('allLocations'))




app.run(debug=True)
