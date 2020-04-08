from flask import Flask, render_template, request,redirect, url_for,session, jsonify
import requests
import pyrebase
import time
from datetime import timedelta
import datetime
import os

app = Flask(__name__)  # "dunder name".

DEBUG = True

app.config.from_object(__name__)
#app.config.from_envvar('EIH_SETTINGS')
#app.secret_key = 'sadfsdfdsfdsafdsafsadfad4sfadsfdsafdsfa'
app.config.from_pyfile('configuration/myconfig.cfg')
app.config.update(
#     ## time out logged in session after minutes=5 time
     PERMANENT_SESSION_LIFETIME =  timedelta(minutes=15)

)
app.secret_key = os.urandom(32)

def get_all_data_from_firebase():
    r = requests.get('https://projecteih.firebaseio.com/locations.json')
    x= r.json()
    return x

def get_the_search_location():
    # to get the search address fully
    addressName = request.form["thelocation"].upper()
    return addressName

def get_the_name_form_search_text(addressName):
    ##split the address into list
    str_list = addressName.split(',')
    # display only the name from tha address.
    building_name_send = str_list[0]
    session['building_name_send'] = building_name_send
    return building_name_send

def db_config():
    config = {
    "apiKey": "AIzaSyBa_oAgm7dmE-sFGGm8XG7HYs0gWxVFyJ8",
    "authDomain": "projecteih.firebaseio.com",
    "databaseURL": "https://projecteih.firebaseio.com",
    "storageBucket": "projecteih.appspot.com",
    "serviceAccount": "configuration/projecteih-firebase-adminsdk-dmd9b-dfbc30ba25.json"
}
    firebasePy = pyrebase.initialize_app(config)

    return firebasePy


def reset_to_zero(id_to_reset):
    db = db_config().database()
    db.child("locations").child(id_to_reset).update({'numberOfPeopleINDetect': 0})

def add_new_builiding(data):
    data_stored = get_all_data_from_firebase()
    if(check_if_address_added_already(data_stored,data['address'])):
        session['address_found_in_DB'] = True
        return False
    else:
        db = db_config().database()
        id_generated = db.child("locations").push(data)
        session['id_generated']=id_generated['name']
        return id_generated


def check_if_searched_address_in_db(building_name_send):
    data_stored = get_all_data_from_firebase()

    return check_if_address_added_already(data_stored,get_the_search_location())



def check_if_address_added_already(data_stored,data):
    if data_stored is None:
        pass
    else:
        for key, value in data_stored.items():

            if(str(value['address']) == str(data)):
                session["number_inside"] = str(value['numberOfPeopleINDetect'])
                return True
    session['address_not_found_in_DB'] = False
    return False

def delete_row(id_to_reset):

    db = db_config().database()
    db.child("locations").child(id_to_reset).update({'active' : False})
    
def update_row(id_to_update,data):
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
        session['logged_in_email'] = email
        session['loged_in'] = True
        session.permanent = True
        return True
    except IOError:
        session['login_attempts'] += 1
        return False

    return email,password


@app.route("/")
def route():
    return redirect(url_for('display_form'))

@app.route("/logout")
def logout():
    ##clear all the session set already
    session.clear()
    #The key is secure enough, and each time you launch your system the key changes invalidating all sessions.
    app.secret_key = os.urandom(32)
    #return display_form()
    return redirect(url_for('display_form'))


@app.route("/displayform")
def display_form():
    if not session:
        session['login_attempts'] = 1
        session['locked_status'] = False
        session['request_ip_address_locked'] = ''
    elif session['request_ip_address_locked'] == request.remote_addr:
        if session['locked_status'] is True and (time.time() - session['time_locked']) > 500:
            session['locked_status'] = False
            session.clear()
    return render_template("index.html" )


@app.route("/displayResults", methods=["POST"])
def displayResults():

    addressName = get_the_search_location()
    building_name_send = get_the_name_form_search_text(addressName)

    found = check_if_searched_address_in_db(building_name_send)
    if not found:
        return redirect(url_for('display_form'))
    else:
        return render_template(
            "results.html", person_name="osama", searched_text=addressName , building_name= building_name_send , total_numebr = session["number_inside"] 
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
    if items_send is None:
        return render_template(
        "allLocations.html",
        items= dict(),
        x= {}
        )
    else:
        return render_template(
        "allLocations.html",
        items= items_send,
        x= items_send
        )
    
@app.route("/login", methods=["POST"])
def login():
    
    if session['login_attempts'] == 5:
        session['time_locked'] = time.time()
        session['request_ip_address_locked'] = request.remote_addr
        session['locked_status'] = True
        return redirect(url_for('route'))
    logPass= login_check()
    if logPass: 
        return redirect(url_for('allLocations'))
    else:  
        session['fail_login'] = True
        return redirect(url_for('display_form'))


@app.route("/resetLocation", methods=["POST"])
def resetLocation():
    selected = request.form.get('selected_radio')

    if request.form.get('action') == 'Reset':
        reset_to_zero(selected)
    elif request.form.get('action') == 'Delete':
            delete_row(selected)
    elif request.form.get('action') == 'Update':
        data =    {
            'known_name': request.form.get('known_name_update').upper(),
            'address' : request.form.get('address_update').upper(),
            'eircode' : request.form.get('eircode_update').upper(),
            'timeUpdated': time.strftime('%X %x %Z')
            }

        update_row(selected,data)
    elif request.form.get('action') == 'Add':
        data =    {
        'deviceId': 'none',
        'known_name': request.form.get('new_row_name').upper(),
        'address' : request.form.get('new_row_address').upper(),
        'eircode' : request.form.get('new_row_eircode').upper(),
        'numberOfPeopleINDetect': 0,
        'timeUpdated': time.strftime('%X %x %Z'),
        'active' : True
        }
        add_new_builiding(data)                                    
    return redirect(url_for('allLocations'))


if __name__ == '__main__':
    app.run()
