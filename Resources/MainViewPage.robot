*** Settings ***
Library         SeleniumLibrary

*** Variables ***

*** Keywords ***
Verify the User Information
    [Documentation]           This keyword is used to verify the user details on main view page
    ${lMainview_Username}     Read Element Locator   MainView.username_id
    ${lMainview_firstname}    Read Element Locator   MainView.firstname_id
    ${lMainview_lastname}     Read Element Locator   MainView.lastname_id
    ${lMainview_phone}        Read Element Locator   MainView.phone_id

    ${Mainview_username}      Get Text   id:${lMainview_Username}
    ${Mainview_firstname}     Get Text   id:${lMainview_firstname}
    ${Mainview_lastname}      Get Text   id:${lMainview_lastname}
    ${Mainview_phone}         Get Text   id:${lMainview_phone}

    Should Be Equal AS Strings   ${Mainview_username}   ${new_username}
    Should Be Equal AS Strings   ${Mainview_firstname}  ${new_firstname}
    Should Be Equal AS Strings   ${Mainview_lastname}   ${new_lastname}
    Should Be Equal AS Strings   ${Mainview_phone}      ${new_phone}