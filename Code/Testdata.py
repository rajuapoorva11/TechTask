import string
import random



def random_string (length=10):
    character_set  = string.ascii_letters
    return ''.join(random.choice(character_set) for i in range(length))
random1 =  random_string(10)


# new registeration details
new_username = random1
new_password = 'test1234'
new_firstname = 'test'
new_lastname = 'tdf'
new_phone = '764443322'

#default user details
default_username = 'firstuser9'
default_password = 'password'
default_firstname = 'first'
default_lastname = 'user'
default_phone = '876543219'

#unregistered user
unregistered_username = 'unregistered'
unregistered_password = 'unregpassword'

#update user details
update_firstname = 'updatefirstuser'
update_lastname = 'updatefirst'
update_phone = '123456789'

#databasepath
db_path = 'C:/Users/nitin/Desktop/Signant/Flasky-master/instance/'
db_name = 'demo_app.sqlite'