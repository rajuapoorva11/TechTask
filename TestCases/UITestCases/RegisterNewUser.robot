*** Settings ***
Library         SeleniumLibrary

Resource        ../../Resources/Common.robot
Resource        ../../Resources/RegisterPage.robot
Resource        ../../Resources/LoginPage.robot
Resource        ../../Resources/MainViewPage.robot

Variables       ../../Code/Testdata.py


Test Setup      Start Browser and Maximize
Test Teardown   Close Browser Window
Test Template   User creation for testing purpose

*** Variables ***

*** Test Cases ***                  username       password     firstname    lastname    phone
Register with valid details          user1          password1    first1      last1      2323434
Blank fields                         ${Empty}       ${Empty}     ${Empty}     ${Empty}   ${Empty}
Register with alphabets              test            desff      sdfdfg        dgfhghf    sfdfd
Register with numbers               23344           4545         35454        454554     35346
Register with specialcharacters     $%^$£"          *(&^^       !"£$%&         £$$$%     %^$£
Register with no details            resd            ty56        ${Empty}      ${Empty}   ${Empty}

***Keywords***

User creation for testing purpose
    [Documentation]         This testcase will create a default user for testing purpose
    [Arguments]             ${datadriven_username}   ${datadriven_password}   ${datadriven_firstname}   ${datadriven_lastname}   ${datadriven_phone}
    Click on RegisterLink
    Fill values in register form   ${datadriven_username}   ${datadriven_password}   ${datadriven_firstname}   ${datadriven_lastname}   ${datadriven_phone}
    Click on RegisterButton




