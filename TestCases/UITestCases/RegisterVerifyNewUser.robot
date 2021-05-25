*** Settings ***
Library         SeleniumLibrary

Resource        ../../Resources/Common.robot
Resource        ../../Resources/RegisterPage.robot
Resource        ../../Resources/LoginPage.robot
Resource        ../../Resources/MainViewPage.robot

Variables       ../../Code/Testdata.py

Test Setup      Start Browser and Maximize
Test Teardown   Close Browser Window

*** Variables ***

*** Test Cases ***
Default User creation for testing purpose
    [Documentation]         This testcase will create a default user for testing purpose
    Click on RegisterLink
    Fill values in register form   ${default_username}   ${default_password}   ${default_firstname}   ${default_lastname}   ${default_phone}
    Click on RegisterButton

New User Registration with valid details
    [Documentation]         This testcase will  register a new user successfully
    Click on RegisterLink
    Fill values in register form  ${new_username}   ${new_password}   ${new_firstname}   ${new_lastname}   ${new_phone}
    Click on RegisterButton
    Login Page Should be Open

Review the Registered new user details
    [Documentation]         This is to verify the registered new user details from the main view
    Click on LoginLink
    Login Page Should be Open
    Fill values in login Page    ${new_username}   ${new_password}
    Click on LoginButton
    Verify the User Information

Existing User Registration
    [Documentation]         This testcase will try to register existing user/already registered user
    Click on RegisterLink
    Fill values in register form  ${default_username}   ${default_password}   ${default_firstname}   ${default_lastname}   ${default_phone}
    Click on RegisterButton
    Register Page Should be Open
    Display error message in register Page

Review Unregistered user details
    [Documentation]  This is to verify the unregistered new user details
    Click on LoginLink
    Login Page Should be Open
    Fill values in login Page   ${unregistered_username}  ${unregistered_password}
    Click on LoginButton
    Login Failure Page Should be Open
    Display error message in Login Page




#We can include more Testcases like
#1.Field validations for registration,login,mainview pages
#2.Verify navigation between pages
#3.Verify if user gets blocked
#4.Verify blocked user can register again
#and so on