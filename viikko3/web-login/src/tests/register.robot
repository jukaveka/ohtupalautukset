*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ok
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Fail With Message  Invalid username. User name be at least 3 characters long, and contain only letters within a-z

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  abcd123
    Set Password Confirmation  abcd123
    Submit Registration
    Registration Should Fail With Message  Invalid password. Password must be at least 8 characters long, and contain at least one number or special character

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  abcdefghij
    Set Password Confirmation  abcdefghij
    Submit Registration
    Registration Should Fail With Message  Invalid password. Password must be at least 8 characters long, and contain at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  acbd1234
    Set Password Confirmation  efgh5678
    Submit Registration
    Registration Should Fail With Message  Invalid password. Password confirmation does not match the given password

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Succeed

    Logout After Registration And Go To Register Page

    Set Username  kalle
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Fail With Message  Username already in use. Select another username

Login After Successful Registration
    Set Username  kalle
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Registration
    Registration Should Succeed

    Logout After Registration And Go To Login Page

    Set Username  kalle
    Set Password  abcd1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  acbd1234
    Set Password Confirmation  efgh5678
    Submit Registration
    Registration Should Fail With Message  Invalid password. Password confirmation does not match the given password

    Click Link  Login

    Set Username  kalle
    Set Password  abcd1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

Logout After Registration And Go To Register Page
    Click Link  Continue to main page
    Click Button  Logout
    Go To Register Page

Logout After Registration And Go To Login Page
    Click Link  Continue to main page
    Click Button  Logout
    Go To Login Page

Registration Should Succeed
    After Registration Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kulli  abcd1234
    Go To Register Page