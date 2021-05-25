*** Settings ***
Library         SeleniumLibrary
#Library         C:/Users/nitin/PycharmProjects/TaskDemo/Code/Locator.py
Library         ../Code/Locator.py
Resource        Common.robot

*** Variables ***


*** Keywords ***
Register Page Should be Open
    [Documentation]     This Keyword is used to check the register page is open
    Title Should be     Register - Demo App

Fill values in register form
    [Documentation]      This Keyword is used to fill all the  fields in the registeration form
    [Arguments]          ${Username}  ${Password}  ${Firstname}  ${Familyname}  ${Phone}

    ${lusername}     Read Element Locator   Registration.username_textbox_id
    ${lpassword}     Read Element Locator   Registration.password_textbox_id
    ${lfirstname}    Read Element Locator   Registration.firstname_textbox_id
    ${llastname}     Read Element Locator   Registration.lastname_textbox_id
    ${lphone}        Read Element Locator   Registration.phone_textbox_id

    Input Text   id:${lusername}    ${Username}
    Input Text   id:${lpassword}    ${Password}
    Input Text   id:${lfirstname}   ${Firstname}
    Input Text   id:${llastname}    ${Familyname}
    Input Text   id:${lphone}       ${Phone}


Display error message in Register Page
    [Documentation]   This Keyword is used to check the error message in Register page
    ${lregerrortext}  Read Element Locator     Registration.errormessage_xpath
    ${message}        Get Text  xpath: ${lregerrortext}
    Log   ${message}


