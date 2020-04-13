from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests
import pyrebase
import time
from datetime import timedelta
import datetime
import os
from dotenv import load_dotenv


## to load all the env vriables from the .env file
project_folder = os.path.expanduser("~/")  #
load_dotenv(os.path.join(project_folder, ".env"))

app = Flask(__name__)  # "dunder name".

DEBUG = True
## Configureation for flask
app.config.from_object(__name__)
## external configuration stores in external file
app.config.from_pyfile("configuration/myconfig.cfg")
## update flask config to set the life time of session to 15, if no actions the session will be logout.
app.config.update(
    ## time out logged in session after minutes=15 time
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=45),
)
## Generate a random String as secret key wach time we run the app for more secuity.
app.secret_key = os.urandom(32)

## Set up the DB url to be able to read the public data.
def get_all_data_from_firebase():
    db_file_url = os.environ["DB_FILE_URL"]
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
## all enviroument veriables are stored in other secret file
def db_config():
    config = {
        "apiKey": os.environ["GOOGLE_API_KEY"],
        "authDomain": os.environ["AUTH_DOMAIN"],
        "databaseURL": os.environ["DB_URL"],
        "storageBucket": os.environ["STOREG_BUKET"],
        "serviceAccount": os.environ["SERVICE_ACCOUNT"],
    }
    firebasePy = pyrebase.initialize_app(config)

    return firebasePy


## reset the locations selected to zero
def reset_to_zero(id_to_reset):
    db = db_config().database()
    db.child("locations").child(id_to_reset).update({"numberOfPeopleINDetect": 0})


## to add the new building detailes entered by the user.
## and return the new KEY after registration to by linked by the hardware.
def add_new_builiding(data):
    data_stored = get_all_data_from_firebase()
    if check_if_address_added_already(data_stored, data["address"]):
        session["address_found_in_DB"] = True
        return False
    else:
        db = db_config().database()
        id_generated = db.child("locations").push(data)
        session["id_generated"] = id_generated["name"]
        ## the Key returned is to be added to the hardware
        return id_generated


## to returm false or True is the searched address is in the DB.
def check_if_searched_address_in_db(building_name_send):
    data_stored = get_all_data_from_firebase()
    return check_if_address_added_already(data_stored, get_the_search_location())


## ## to returm false or True is the searched address is in the DB.
## set all sesssion when founded.
def check_if_address_added_already(data_stored, data):
    ## Error Pass is none data in the DB.
    if data_stored is None:
        pass
    else:
        ## To loop inside the json file coming back from the API.
        ## Key is the building id and the value its detailes.
        for key, value in data_stored.items():
            if str(value["address"]) == str(data):
                session["number_inside"] = str(value["numberOfPeopleINDetect"])
                session["building_Status"] = value['active']
                return True
    session["address_not_found_in_DB"] = False
    return False


## To delete the selected raw from the DB.
def delete_row(id_to_reset):
    db = db_config().database()
    db.child("locations").child(id_to_reset).update({"active": False})
## To activate the selected raw from the DB.
def active_row(id_to_reset):
    db = db_config().database()
    db.child("locations").child(id_to_reset).update({"active": True})


## To update the selected raw from the DB.
def update_row(id_to_update, data):
    db = db_config().database()
    x = db.child("locations").child(id_to_update).update(data)


## to check if the login was successful or not
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
        ## Increment the session["login_attempts"] at each time the login failing.
        session["login_attempts"] += 1
        return False
    ## return the email and the password attepming to log in with.
    return email, password

# ## the application route.
# @app.before_request
# def before_request():
#     if not session:
#         session["login_attempts"] = 1
#         session["locked_status"] = False
#         session["request_ip_address_locked"] = ""

@app.route("/")
def route():
    ## redirevt to the main bage index in the display_form function.
    return redirect(url_for("display_form"))


@app.route("/logout")
def logout():
    ##clear all the session set already
    session.clear()
    # The key is secure enough, and each time you launch your system the key changes invalidating all sessions.
    # app.secret_key = os.urandom(32)
    # return display_form()
    return redirect(url_for("display_form"))


@app.route("/displayform")
def display_form():
    ## for the first time running the webapp, if no session set aleady that mean
    ## this is the first time then the session get initialized.
    if not session:
        session["login_attempts"] = 1
        session["locked_status"] = False
        session["request_ip_address_locked"] = ""
    ## if the session were set already, and the ip was blocked.
    elif session["request_ip_address_locked"] == request.remote_addr:
        ## to check when the IP is blocke after the 5 time failing login attempts.
        ## and check if the time at lock out was greater than 5 minutes then re allow to login.
        if (
            session["locked_status"] is True
            and (time.time() - session["time_locked"]) > 500
        ):
            session["locked_status"] = False
            session.clear()
    ## return the GOOGLE_API_KEY saved in .env file to the index page. for more security.
    return render_template("index.html", API_KEY=os.environ["GOOGLE_API_KEY"], alert=session.pop('address_not_found_in_DB', None)  )


## route to display the results page.
##when the user enter the location in the search input
@app.route("/displayResults", methods=["POST"])
def displayResults():
    ### get the location searched by the user.
    addressName = get_the_search_location()
    ### split the name of the location from the first part of the address.
    building_name_send = get_the_name_form_search_text(addressName)
    ### if the addcess was found in the DB.
    found = check_if_searched_address_in_db(building_name_send)
    if not found:
        return redirect(url_for("display_form"))
    else:
        return render_template(
            "results.html",
            searched_text=addressName,
            building_name=building_name_send,
            total_numebr=session["number_inside"],
            building_Status=session["building_Status"],
            GOOGLE_MAP_API=os.environ['GOOGLE_MAP_API'],
        )


@app.route("/contactForm")
def contactForm():
    ### contact US form to be done by the organizations it selfs.
    ## if any one start using this project in the future they will be abke to set the contact and methods they prefare.
    return render_template("contactUs.html")


@app.route("/emailMsg")
def emailMsg():
    ### once the contact msg has been sent than you page will be shown and redirect to the main page in 5 seconds.
    return render_template("sentMsg.html")


## route to display all the data in the database.
@app.route("/allLocations")
def allLocations():
    ### to get all the data from the data set
    items_send = get_all_data_from_firebase()
    if items_send is None:
        ## if the data was none an empty dictionary will be sent.
        ### Error handeling.
        return render_template(
            "allLocations.html",
            items=dict(),
            x={},
            API_KEY=os.environ["GOOGLE_API_KEY"],
            alert=session.pop('address_not_found_in_DB', None)
        )
    else:
        return render_template(
            "allLocations.html",
            items=items_send,
            x=items_send,
            API_KEY=os.environ["GOOGLE_API_KEY"],
            alert=session.pop('address_not_found_in_DB', None)
        )


## login route
@app.route("/login", methods=["POST"])
def login():
    ### to check if the user attempts is 5.
    if session['login_attempts'] is not None:
        if session["login_attempts"] == 5:
            session["time_locked"] = time.time()
            session["request_ip_address_locked"] = request.remote_addr
            session["locked_status"] = True
            return redirect(url_for("route"))
    else:
        session['login_attempts'] = 1
    ## if attempts less than 5 then the login email,and password get checked.
    logPass = login_check()
    if logPass:
        return redirect(url_for("allLocations"))
    else:
        session["fail_login"] = True
        return redirect(url_for("display_form"))


@app.route("/resetLocation", methods=["POST"])
def resetLocation():
    ### getting the value of the radio button on the admin board>
    ### for all locations table.
    selected = request.form.get("selected_radio")
    ### if the user select the reset option
    if request.form.get("action") == "Reset":
        reset_to_zero(selected)
    ### if the user select the Delete option
    elif request.form.get("action") == "Delete":
        delete_row(selected)
    elif request.form.get("action") == "Activate":
        active_row(selected)
    ### if the user select the Update option
    elif request.form.get("action") == "Update":
        ### the data has been updated get collected and formatted
        ### then the data json sent tp update_row() fuction.
        data = {
            "known_name": request.form.get("known_name_update").upper(),
            "address": request.form.get("address_update").upper(),
            "eircode": request.form.get("eircode_update").upper(),
            "timeUpdated": time.strftime("%X %x %Z"),
        }
        update_row(selected, data)
    ### if the user select the Add option
    elif request.form.get("action") == "Add":
        ### the data has been added get collected and formatted
        ### then the data json sent tp add_new_builiding() fuction.
        data = {
            'active' : True,
            "deviceId": "none",
            "known_name": request.form.get("new_row_name").upper(),
            "address": request.form.get("new_row_address").upper(),
            "eircode": request.form.get("new_row_eircode").upper(),
            "numberOfPeopleINDetect": 0,
            "timeUpdated": time.strftime("%X %x %Z")
        }
        #to be display at after the registration compete
        session['new_row_name']=request.form.get("new_row_name").upper()
        add_new_builiding(data)
    return redirect(url_for("allLocations"))

## route to about Us bage
@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html",)


@app.after_request
def apply_caching(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    # response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'

    return response


# the application start
if __name__ == "__main__":
    app.run()
