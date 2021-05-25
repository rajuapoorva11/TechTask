*** Settings ***
Library         SeleniumLibrary

*** Variables ***
*** Keywords ***
Login Page Should be Open
    [Documentation]     This keyword is check if login page is open
    Title should be     Log In - Demo App

Fill values in login page
    [Documentation]     This keyword is used to fill all the field values in login page
    [Arguments]         ${UserName}   ${Password}
    Input Text  id:username  ${UserName}
    Input Text  id:password  ${Password}

Display error message in Login Page
    [Documentation]     This keyword is used fetch error message from login page
    ${lerrorheader}     Read Element Locator   Login.errormessageheader_xpath
    ${lerrortext}       Read Element Locator   Login.errormessagetext_xpath
    ${message1}         Get Text  xpath:${lerrorheader}
    ${message2}         Get Text  xpath:${lerrortext}
    Log   ${message1}
    Log   ${message1}

Login Failure Page Should be Open
    [Documentation]     This keyword is check if login error page is open
    Title should be  Login Failure - Demo App