#!/usr/bin/env python

import cgitb
import cgi
import Cookie
import os
import json # used to send data back in JSON format
import datetime # used to generate the system time

# enable the cgi
cgitb.enable()

login_form = cgi.FieldStorage()

# check the validation of the username and password
data = {}
usrname = login_form["user_id"].value # get the username from the table
pwd = login_form["password"].value # get the password from the table
remember = login_form["remember_me"].value # get whether use status saving

print "Content-type: application/json"
print  # without printing a blank line, the "end of script output before headers" error will occur
# if the remember me checkbox was clicled, set the cookie
if remember:
    # print "Hello, I send you a new cookie"

    cookie = Cookie.SimpleCookie()

    cookie['user_name'] = usrname
    cookie['password'] = pwd

    # set the expire date
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    cookie["expire"] = expires

    # print cookie
    print json.dumps(data)

# no cookie, user have to login again during the next visit
else:
    # print "Hello, I won't send you a cookie."
    data['user_name'] = usrname
    print json.dumps(data)




