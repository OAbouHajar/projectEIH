# EIH Python unit test
# AUTHOR: OSAMA ABOU HAJAR
# Institute of Technology Carlow
# STUDENT ID: C002201315
# DATE: 20/04/2020
# Emergency Info Hub (EIH), Is a central website helps the emergency services to prepare for,
#      respond to & recover from disaster, by providing all needed data for the targeted building
#      (E.g. Number of people, area size and emergency exits).
# The main objective of this project is giving the number of trapped people under rubbles or inside a building,
#  by tracking their number using a simple movement sensor fitted on the main gate and face detection technology,
#  and save this number to the cloud to be used when a disaster happens.

### To run the rest you have to export the following env veriable
    #  export GOOGLE_API_KEY='GOOGLE-API-KEY-FOR-THE-CREATED-PROJECT-ON-THE-FIREBASE'
    #  export GOOGLE_MAP_API='GOOGLE-MAPS-API-KEY-TO-SHOW-THE-MAP-ON-RESULTS'
    #  export AUTH_DOMAIN='<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com'
    #  export DB_URL='https://<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com'
    #  export STOREG_BUKET='<YOU-PROJECT-NAME-ON-FIREBASE>.appspot.com'
    #  export SERVICE_ACCOUNT='<THE-PATH-TO-THE-DB-CONFIG-JSON-FILE>/projecteih-firebase-adminsdk-dmd9b-dfbc30ba25.json'
    #  export DB_FILE_URL='https://<YOU-PROJECT-NAME-ON-FIREBASE>.firebaseio.com/<THE-JSON-FILE-NAME-ON-FIREBASE>.json'


import unittest
import app
from unittest.mock import patch
from app import app as web
from flask import Flask, request, session
from flask import json, jsonify
import flask
import os
webF = flask.Flask(__name__)


class TestApp(unittest.TestCase):
    ##1 test the web load
    def test_main_page_load(self):
        tester = web.test_client()
        response = tester.get("/displayform", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    ##2 test the all location page load
    def test_all_locations_page(self):
        tester = web.test_client()
        response = tester.get("/allLocations", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    ##3 test the aboutus page load
    def test_about_us_page(self):
        tester = web.test_client()
        response = tester.get("/aboutus", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    ##4 test the contact us page load
    def test_contact_us_page(self):
        tester = web.test_client()
        response = tester.get("/contactForm", content_type="html/text")
        self.assertEqual(response.status_code, 200)

    ##5 test the logout redirect to main page load
    def test_logout_page(self):
        tester = web.test_client()
        response = tester.get("/logout", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ##6 test the display Results page load with the tested address in the database
    def test_search_results_page(self):
        tester = web.test_client()
        address = "Institute of Technology Carlow, Kilkenny Road, Moanacurragh, Carlow, Ireland"
        response = tester.post(
            "/displayResults", data=dict(thelocation=address), follow_redirects=True
        )
        self.assertIn(b"People Inside", response.data)

    ##7 test fail login
    def test_fail_login(self):
        tester = web.test_client(self)
        userlogin = "test@test.com"
        password = "noPassword"
        response = tester.post(
            "/login",
            data=dict(loginInput=userlogin, loginPass=password),
            follow_redirects=True,
        )

        self.assertIn(b"Email Address OR Password", response.data)

    # ##8 test login
    # def test_login(self):
    #     tester = web.test_client(self)
    #     userlogin="test@test.com"
    #     password = "<passwork_to_be_set>"
    #     response = tester.post('/login',
    #                            data=dict( loginInput=userlogin,
    #                                      loginPass=password),
    #                             follow_redirects=True)

    #     self.assertIn(b'Right Click To Show The Options Menu', response.data)

    ##9 test to check the connections is good to the Database
    def test_get_data_from_db(self):
        result = app.get_all_data_from_firebase()
        self.assertIsNotNone(result)

    ##10 test the data type coming form the database
    def test_get_data_from_db_type(self):
        result = app.get_all_data_from_firebase()
        self.assertTrue(type(result) is dict)

    ##11 test database configuration
    def test_db_config(self):
        result = app.db_config()
        self.assertIsNotNone(result)

    # ##12 test delete row
    # def test_delete_row(self):
    #     self.assertIsNone(app.delete_row('RANDOM_ID'))

    # ##13 test active_row
    # def test_active_row(self):
    #     self.assertIsNone(app.active_row('RANDOM_ID'))

    # ##14 test delete row
    # def test_update_row(self):
    #     self.assertIsNone(app.update_row('RANDOM_ID',None))


if __name__ == "__main__":
    unittest.main()
