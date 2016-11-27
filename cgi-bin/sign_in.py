<<<<<<< HEAD
#!/usr/bin/python

# use cookie for persistant data storage
# if no cookie, return the login page
# if has cookie, return the main page and change the 
# name_logo field with user_name

import cgitb
import cgi
import Cookie
import os

cgitb.enable()

login_form = cgi.FieldStorage()

# this function prints a blank line (which must follow the header) and then
# prints an HTML message that includes the specified message in the body
def print_html(msg):
    print
    print "<html>"
    print "  <head><title>Lecture 05 Cookie Test</title></head>"
    print "  <body>" + msg + "</body>"
    print "</html>"


# must include at least one header
print "Content-Type: text/html"
# get the stored cookie
stored_cookie_string = os.environ.get('HTTP_COOKIE')

# the client didn't send a cookie
if not stored_cookie_string:
    # the remember me func was on
    if 'remember' in login_form.keys(): 
        # make a new cookie and stuff the username & password into it
        cookie = Cookie.SimpleCookie()
        cookie['username'] = login_form['user_id'].value
        cookie['password'] = login_form['password'].value
        # print the cookie as an HTTP Set-Cookie header
        print cookie
        # the printed message includes the cookie timestamp
        message = "<h2>Hello, your username is: " + cookie['username'].value + "</h2>"
        message += "<h2>Hello, your password is: " + cookie['password'].value + "</h2>"
        message += "<h1>I am sending a cookie to you!</h1>"
    else:
        message = "<h2>Hello, your username is: " + login_form['user_id'].value + "</h2>"
        message += "<h2>Hello, your passowrd is: " + login_form['password'].value + "</h2>"
        message += "<h1>I won't send you a cookie</h1>"
    
    print_html(message)

# else the client DID send a cookie...
else:
    # get the cookie
    cookie = Cookie.SimpleCookie(stored_cookie_string)
    # start building the message
    message = "<h1>Hello, I received your cookie.</h1>"
    # if it contains the time stamp...
    if 'username' in cookie:
        # add it to the message
        message += "<h2>Its saved user name is: " + cookie['username'].value + "</h2>"
    if 'password' in cookie:
    	# add it to the message
    	message += "<h2>Its saved password is: " + cookie['password'].value + "</h2>"

    # otherwise, we don't understand that cookie...
    else:
        # this is some other cookie and we didn't get what we expected.  print an error message
        message += "<h2>Sorry, I don't understand your cookie.  Looking for 'current_time' but found: </h2>"
        
    print_html(message)

=======
#!C:\Users\nevgivin\Anaconda2\python.exe

import cgi
import cgitb
import database
import datetime
import hashlib

cgitb.enable()

form = cgi.FieldStorage()


print 'Content-Type: text/html'
print

#USER ID
user_id = form['user_id'].value

#USER PASSPWORD
password = form['password'].value

database.create_table(database.create_user_table)

query = 'select password , salt from user_account where user_ID = \'%s\'' %user_id
result = database.query_table(query)

if result == None:
	info = 'Sorry , we could find your user_ID'
else:
	salt = result[1]
	hasher = hashlib.md5()
	hasher.update(str(password))
	hasher.update(salt)
	encrypted = hasher.hexdigest()
	if encrypted == result[0]:
		info = 'Congratulations, you have logged in'
	else:
		info = 'Wrong password'

	


print '''
<html>
    <head>
        <title>Created Account</title>
    </head>
    <body>
    '''
if info == 'Congratulations, you have logged in':
	print '''
        %s</br>
        You will be redirected to the log_in html </br>
        <meta http-equiv="refresh" content="2;url=../log_in.html">
        '''%info
else:
	print '''
        %s</br>
        Please try again </br>
        <meta http-equiv="refresh" content="2;url=../index.html">
        '''%info
print '''
    </body>
</html>''' 
>>>>>>> a42a48019255840c2fe50ee20937a288879871d6
