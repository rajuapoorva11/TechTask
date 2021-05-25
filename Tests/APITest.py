import json
import Code.Testdata
import requests

class DemoApp():
    def __init__(self):
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
        self.update_payload = json.dumps({"firstname" : self.update_firstname , "lastname": self.update_lastname , "phone" : self.update_phonenumber})
        self.default_payload = json.dumps(
            {"firstname": self.registered_firstname, "lastname": self.registered_lastname, "phone": self.registered_phone})
        self.url_users= ('http://127.0.0.1:8080/api/users')


    def generate_users(self):
        response = requests.get(self.url_users, headers= self.users_headers)
        assert response.status_code == 200
        assert response.json()['status'] == 'SUCCESS'
        print(response.text)

    def generate_user_information_authenticated(self):
        """
        To get information details of registered user when authenticated
        """
        response = requests.get((self.url_users + '/' + self.registered_username), headers=self.user_information_headers)
        assert response.status_code == 200
        print(response.text)
        assert response.json()['status'] == 'SUCCESS'
        assert response.json()['message'] == 'retrieval succesful'

    def update_registereduser_information_validdata_firstname(self):
        """
        To Update registered user Information when authenticated and reviewing the results reverting back the changes for testing purpose
        """
        response = requests.put((self.url_users + '/' + self.registered_username), headers=self.user_information_headers,data = self.update_payload)
        assert response.status_code == 201
        assert response.json()['status'] == 'SUCCESS'
        print(response.text)

        response1 = requests.get((self.url_users + '/' + self.registered_username), headers=self.user_information_headers)
        print(response1.text)
        assert response1.status_code == 200
        assert response.json()['status'] == 'SUCCESS'

        response = requests.put((self.url_users + '/' + self.registered_username),headers=self.user_information_headers, data=self.default_payload)
        print(response.text)
        assert response.status_code == 201
        assert response.json()['status'] == 'SUCCESS'

if __name__ == '__main__':
    Demo = DemoApp()
    Demo.generate_users()
    Demo.generate_user_information_authenticated()
    Demo.update_registereduser_information_validdata_firstname()


