from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import pyrebase
import time
from datetime import timedelta
import datetime
import os
from dotenv import load_dotenv


## to load all the env vriables from the .env file
project_folder = os.path.expanduser('~/')  # 
load_dotenv(os.path.join(project_folder, '.env'))

app = Flask(__name__)  # "dunder name".

DEBUG = True
## Configureation for flask
app.config.from_object(__name__)
## external configuration stores in external file
app.config.from_pyfile("configuration/myconfig.cfg")
## update flask config to set the life time of session to 15, if no actions the session will be logout.
app.config.update(
    ## time out logged in session after minutes=5 time
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=15)
)
## Generate a random String as secret key wach time we run the app for more secuity.
app.secret_key = os.urandom(32)

## Set up the DB url to be able to read the public data.
def get_all_data_from_firebase():
    db_file_url = os.environ['DB_FILE_URL']
    r = requests.get(db_file_url)
    x = r.json()
    return x

## function to return the location has been searched by the user input on the main page.
def get_the_search_location():
    # to get the search address fully
    addressName = request.form["thelocation"].upper()
    return addressName

## function to split the address and return the first part as the surched name.
def get_the_name_form_search_text(addressName):
    ##split the address into list
    str_list = addressName.split(",")
    # display only the name from tha address.
    building_name_send = str_list[0]
    session["building_name_send"] = building_name_send
    return building_name_send

## function to congifure the database ## this information should be secret.
#   export GOOGLE_API_KEY=AIzaSyBa_oAgm7dmE-sFGGm8XG7HYs0gWxVFyJ8
#   echo "export GOOGLE_API_KEY=AIzaSyBa_oAgm7dmE-sFGGm8XG7HYs0gWxVFyJ8" >> .env
def db_config():
    config = {
        "apiKey": os.environ['GOOGLE_API_KEY'],
        "authDomain": os.environ['AUTH_DOMAIN'],
        "databaseURL": os.environ['DB_URL'],
        "storageBucket": os.environ['STOREG_BUKET'],
        "serviceAccount": os.environ['SERVICE_ACCOUNT'],
    }
    firebasePy = pyrebase.initialize_app(config)

    return firebasePy


def reset_to_zero(id_to_reset):
    db = db_config().database()
    db.child("locations").child(id_to_reset).update({"numberOfPeopleINDetect": 0})


def add_new_builiding(data):
    data_stored = get_all_data_from_firebase()
    if check_if_address_added_already(data_stored, data["address"]):
        session["address_found_in_DB"] = True
        return False
    else:
        db = db_config().database()
        id_generated = db.child("locations").push(data)
        session["id_generated"] = id_generated["name"]
        return id_generated


def check_if_searched_address_in_db(building_name_send):
    data_stored = get_all_data_from_firebase()

    return check_if_address_added_already(data_stored, get_the_search_location())


def check_if_address_added_already(data_stored, data):
    if data_stored is None:
        pass
    else:
        for key, value in data_stored.items():

            if str(value["address"]) == str(data):
                session["number_inside"] = str(value["numberOfPeopleINDetect"])
                return True
    session["address_not_found_in_DB"] = False
    return False


def delete_row(id_to_reset):

    db = db_config().database()
    db.child("locations").child(id_to_reset).update({"active": False})


def update_row(id_to_update, data):
    db = db_config().database()
    x = db.child("locations").child(id_to_update).update(data)


def login_check():
    email = request.form["loginInput"]
    password = request.form["loginPass"]
    firebasePy = db_config()
    # Get a reference to the auth service
    auth = firebasePy.auth()
    # Log the user in
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        session["logged_in_email"] = email
        session["loged_in"] = True
        session.permanent = True
        return True
    except IOError:
        session["login_attempts"] += 1
        return False

    return email, password


@app.route("/")
def route():
    return redirect(url_for("display_form"))


@app.route("/logout")
def logout():
    ##clear all the session set already
    session.clear()
    # The key is secure enough, and each time you launch your system the key changes invalidating all sessions.
    app.secret_key = os.urandom(32)
    # return display_form()
    return redirect(url_for("display_form"))


@app.route("/displayform")
def display_form():
    if not session:
        session["login_attempts"] = 1
        session["locked_status"] = False
        session["request_ip_address_locked"] = ""
    elif session["request_ip_address_locked"] == request.remote_addr:
        if (
            session["locked_status"] is True
            and (time.time() - session["time_locked"]) > 500
        ):
            session["locked_status"] = False
            session.clear()
    return render_template("index.html", API_KEY=os.environ['GOOGLE_API_KEY'])


@app.route("/displayResults", methods=["POST"])
def displayResults():

    addressName = get_the_search_location()
    building_name_send = get_the_name_form_search_text(addressName)

    found = check_if_searched_address_in_db(building_name_send)
    if not found:
        return redirect(url_for("display_form"))
    else:
        return render_template(
            "results.html",
            person_name="osama",
            searched_text=addressName,
            building_name=building_name_send,
            total_numebr=session["number_inside"],
        )


@app.route("/contactForm")
def contactForm():

    return render_template("contactUs.html")


@app.route("/emailMsg")
def emailMsg():

    return render_template("sentMsg.html")


@app.route("/allLocations")
def allLocations():
    items_send = get_all_data_from_firebase()
    if items_send is None:
        return render_template("allLocations.html", items=dict(), x={} , API_KEY=os.environ['GOOGLE_API_KEY'])
    else:
        return render_template("allLocations.html", items=items_send, x=items_send, API_KEY=os.environ['GOOGLE_API_KEY'])


@app.route("/login", methods=["POST"])
def login():

    if session["login_attempts"] == 5:
        session["time_locked"] = time.time()
        session["request_ip_address_locked"] = request.remote_addr
        session["locked_status"] = True
        return redirect(url_for("route"))
    logPass = login_check()
    if logPass:
        return redirect(url_for("allLocations"))
    else:
        session["fail_login"] = True
        return redirect(url_for("display_form"))


@app.route("/resetLocation", methods=["POST"])
def resetLocation():
    selected = request.form.get("selected_radio")

    if request.form.get("action") == "Reset":
        reset_to_zero(selected)
    elif request.form.get("action") == "Delete":
        delete_row(selected)
    elif request.form.get("action") == "Update":
        data = {
            "known_name": request.form.get("known_name_update").upper(),
            "address": request.form.get("address_update").upper(),
            "eircode": request.form.get("eircode_update").upper(),
            "timeUpdated": time.strftime("%X %x %Z"),
        }

        update_row(selected, data)
    elif request.form.get("action") == "Add":
        data = {
            "deviceId": "none",
            "known_name": request.form.get("new_row_name").upper(),
            "address": request.form.get("new_row_address").upper(),
            "eircode": request.form.get("new_row_eircode").upper(),
            "numberOfPeopleINDetect": 0,
            "timeUpdated": time.strftime("%X %x %Z"),
            "active": True,
        }
        add_new_builiding(data)
    return redirect(url_for("allLocations"))


if __name__ == "__main__":
    app.run()
