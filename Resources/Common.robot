*** Settings ***
Library         SeleniumLibrary
#Library         C:/Users/nitin/PycharmProjects/TaskDemo/Code/Locator.py
Library         ../Code/Locator.py

*** Variables ***
${Browser}      ff
${URL}          http://127.0.0.1:8080/

*** Keywords ***
Start Browser and Maximize
    [Documentation]     This keyword is used to open browser and maximize it.
    Open Browser        ${URL}  ${Browser}
    Maximize Browser Window

Close Browser Window
    [Documentation]     This keyword is used to close the browser
    Close Browser

Read Element Locator
    [Documentation]     This keyword is used to fetch the locator from jsonfile
    [Arguments]         ${JsonPath}
    ${result}=  read_locator_from_json   ${JsonPath}
    [return]  ${result}

Click on RegisterLink
    [Documentation]     This keyword is used to click register link in home page
    ${lRegistorlink}  Read Element Locator   Home.register_link_xpath
    Click Link  xpath:${lRegistorlink}

Click on RegisterButton
    [Documentation]     This keyword is used to click register button in register page
    ${lRegisterbutton}  Read Element Locator   Registration.register_button_xpath
    Click Button   xpath:${lRegisterbutton}

Click on LoginLink
    [Documentation]     This keyword is used to click login link in home page
    ${lLoginlink}  Read Element Locator   Home.login_link_xpath
    Click Link  xpath:${lLoginlink}

Click on LoginButton
    [Documentation]     This keyword is used to click register link in login page
    ${lLoginbutton}  Read Element Locator    Login.login_button_xpath
    Click Button  xpath:${lLoginbutton}

Insert User from DB
    Connect To Database Using Custom Params    sqlite3    database="${db_path}${db_name}", isolation_level=None
    Execute Sql String    sqlString=insert into user  VALUES ('abcd' ,'meow','mickey','woof',7654333));
