/**
 * Created by Fangzhou Liu on 10/20/2016.
 *
 * Javascript for Login page for cookie check
 * 
 */
$(document).ready(function(){  
     // alert("Hello World");  
     send_cookie();
     $('#login_btn').click(login);
     $('#logout_btn').click(logout);

});  



// send the cookie to the server before the page was loaded
// 
var send_cookie = function () {
    // .ajax is the core Ajax function supported by jQuery and requires the following parameters:
    //  url: the URL of the resource to send the request to
    //  data: the data to send along with the request; encoded as a query string for GET
    //  dataType: the expected format of the data coming back in the response
    //  success: a function to execute if the request is successful
    //  error: a function to execute if the request fails for any reason
    $.ajax({
        url: '../cgi-bin/main_page_test.py',  // lecture 8 script to query the pizza database

        type: "GET",                  // GET or POST

        dataType: "json",             // json format

        success: function( data ) {   // function to execute upon a successful request

        	if (data.user_name != "nil") { // return a cookie
                success_handler(data)
        	}
        	else { // no cookie
	           error_handler();
            }
        },

        error: function(request) {   // function to call when the request fails, other errors
            error_handler();
        }
    });
}

// when the user click the login button on the screen
// this login method will be triggeerd
var login = function () {

  var user_id = $('#username').val();
  var pwd = $('#pwd').val();
  var remember = $('#remember_me').prop("checked");
  console.log(user_id);
  console.log(pwd);
  console.log(remember);
  if (user_id == "" ||pwd == "") {
    $('#error_log').html("Your Username or Password cannot be left empty!!!")
  }

  $.ajax({

    url: "../cgi-bin/sign_in_test.py",

    type: "POST",

    data: {
      user_id: user_id,
      password: pwd,
      remember_me: remember
    },

    dataType: "json",

    // when successfully login
    success: function (data) {
        console.log("Success Login");
        success_handler(data);
    },

    error: function (request) {
        console.log("Error Login");
        console.log(request)
        error_handler()
    }
  });
}

// when the user click the logout button on the screen
// this logout method will be triggeerd
var logout = function() {

    $.ajax( {

        url: "../cgi-bin/logout_test.py",

        type: "POST",

        dataType: "json",

        success: function (data) {
            console.log("Success Logout");
            error_handler()
        },

        error: function (request) {
            console.log("Error Logout");
            console.log(request);
        }

    });

}

var success_handler = function(data) {

    console.log("success!");
    console.log(data);
    $('#home').html("<a class='active' href='#home'>Home</a>");
    $('#news').html("<a href='#home'>News</a>");
    $('#pokemon').html("<a href='#pokemon'>Pokemon</a>");
    $('#contact').html("<a href='#home'>Contact</a>");
    $('#profile').html("<a href='#home'>Profile</a>");
    $('#logout').html("<a href='#home'>Logout</a>");
    $('#signup').empty();
    $('#name_logo').html('Welcome! ' + data.user_name);
    $('#login_panel').empty();

    console.log(data.password)

}

var error_handler = function() {
    $('#home').empty();
    $('#news').empty();
    $('#contact').empty();
    $('#profile').empty();
    $('#logout').empty();
     // $('#login').html("<a href='../sign_in.html'>Log In</a>");
    $('#signup').html("<a href='../sign_up.html'>Sign Up</a>");        
    $('#name_logo').html("Welcome! Sommoner");
}