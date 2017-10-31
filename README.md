# proj5-map
## Overview
Make a map application (using LeafletJS or another mapping API) that is initially focused on the on the location of the user
When the user clicks (or taps on a mobile device), application creates a marker at that location. In 'open' state that marker displays the address

## Feature

use https protocol to get user location
generate sever ssl certificate ca.crt and server.key unser ssl dictory
for 2 command:
    openssl req -nodes -newkey rsa:2048 -sha256 -keyout myserver.key
    openssl req -new -x509 -key myserver.key -out ca.crt -days 3650

## Authors
Jilun Li

## Access
for locate user location, we just use https protocol to access the application
URL: https://ip:8000/

## To run automated tests 
* `nosetests`

rules test for rules.py to nose tests
    make test
to test all test cases

## To Install and Run
    bash ./configure
    make test    # make all test, should pass 
    make service # service run background



