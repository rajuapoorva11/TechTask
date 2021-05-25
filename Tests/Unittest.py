import unittest
import requests
import json
import Code.Testdata

class Demoapp(unittest.TestCase):
    def setUp(self):
        """
        SetUp contains all variables and token authentication with user
        name and password.
        """
        self.registered_username = Code.Testdata.default_username
        self.registered_password = Code.Testdata.default_password
        self.registered_firstname = Code.Testdata.default_firstname
        self.registered_lastname = Code.Testdata.default_lastname
        self.registered_phone = Code.Testdata.default_phone
        self.unregistered_username = Code.Testdata.unregistered_username
        self.update_firstname = Code.Testdata.update_firstname
        self.update_lastname = Code.Testdata.update_lastname
        self.update_phonenumber = Code.Testdata.update_phone
        response = requests.get('http://127.0.0.1:8080/api/auth/token', auth=(self.registered_username, self.registered_password))
        json_response = response.json()
        self.access_token = (json_response["token"])
        self.users_headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer' + self.access_token}
        self.user_information_headers = {'Content-Type': 'application/json', 'token': self.access_token}
        self.url_users = ('http://127.0.0.1:8080/api/users')
        self.update_payload = json.dumps({"firstname" : self.update_firstname , "lastname": self.update_lastname , "phone" : self.update_phonenumber})
        self.default_payload = json.dumps({"firstname" : self.registered_firstname , "lastname" : self.registered_lastname , "phone" : self.registered_phone})

    def test_update_defaultuser_information(self):
        """
        test_update_defaultuser_information is used to update the default user information for testing purpose.
        """
        response = requests.put((self.url_users + '/' + self.registered_username), headers=self.user_information_headers,data = self.default_payload)
        self.assertEqual(response.status_code, 201)

    def test_generate_users(self):
        """
        test_generate_users is used to get list of registered users
        """
        response = requests.get(self.url_users, headers= self.users_headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'SUCCESS')

    def test_generate_user_information_authenticated(self):
        """
        To get information details of registered user when authenticated(positive scenario)
        """
        response = requests.get((self.url_users + '/' + self.registered_username), headers=self.user_information_headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'SUCCESS')
        self.assertEqual(response.json()['message'], 'retrieval succesful')
        self.assertEqual(response.json()['payload']['firstname'], self.registered_firstname)
        self.assertEqual(response.json()['payload']['lastname'], self.registered_lastname)

    def test_generate_user_information_not_authenticated(self):
        """
        To get information details of registered user when not authenticated(negative scenario)
        """
        response = requests.get((self.url_users + '/' + self.registered_username), headers=self.users_headers)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()['status'], 'FAILURE')

    def test_generate_user_information_servererror(self):
        """
        To get information details of registered user when Internal server error occurs(negative scenario)
        """
        response = requests.get((self.url_users + '/' + 're43tyrf'), headers=self.user_information_headers)
        self.assertEqual(response.status_code, 500)

    def test_update_registereduser_information_validdata_firstname(self):
        """
        To Update registered user Information when authenticated(positive scenario)
        """
        response = requests.put((self.url_users + '/' + self.registered_username), headers=self.user_information_headers,data = self.update_payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['status'], 'SUCCESS')
        self.assertEqual(response.json()['message'], 'Updated')
        response1 = requests.get((self.url_users + '/' + self.registered_username), headers=self.user_information_headers)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.json()['status'], 'SUCCESS')
        self.assertEqual(response1.json()['payload']['firstname'], self.update_firstname)
        self.assertEqual(response1.json()['payload']['lastname'], self.update_lastname)
        self.assertEqual(response1.json()['payload']['phone'], self.update_phonenumber)
        response = requests.put((self.url_users + '/' + self.registered_username),headers=self.user_information_headers, data=self.default_payload)
        self.assertEqual(response.status_code, 201)

    def test_update_unregistereduser_information(self):
        """
        To Update non registered user details when not authenticated(negative scenario)
        """
        response = requests.put((self.url_users + '/' + self.unregistered_username), headers=self.user_information_headers,data = json.dumps({"usernamie" : "hfgftdt"}))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['status'], 'FAILURE')

    def test_update_registereduser_information_invaliddata_username(self):
        """
        To Update registered user username when authenticated(negative scenario)
        """
        response = requests.put((self.url_users + '/' + self.registered_username), headers=self.user_information_headers,data = json.dumps({"username" : "tresdf" }))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['status'], 'FAILURE')

    def tearDown(self):
        pass

#We can include some more Test scenarios for updating and retriving user information details like,
#1.Updating firstname,lastname and phone fields with just numbers,special characters,existing details and etc
#2.to check some more error codes with invalid content type,invalid payloads and etc