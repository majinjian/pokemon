var post_array = new Array();


/**
 * retrieve posts
 */
function load_posts() {
	$.ajax({
		url: "/cgi-bin/postHandler.py",
			
		type: "POST",

		dataType: "json",

		success: function(data) {
			posts = JSON.parse(data);
			if(posts.length > 0) {
				posts.forEach(function(element){
					post_array.push(element);
				});
				display_posts();
			}
		},

		error: function(data) {
			alert(data);
		}
	});
}




/**
 * send one post to server
 */
$("#post-send").click(function() {
	$.ajax({
		url: "/cgi-bin/postHandler.py",
		
		type: "POST",
		
		data: "post-content=" + $('textarea').val() +
			   "&new=true",

		dataType: "json",
		success: function(data) {
			insertpost = "<div id='user-post'>" +
							"<a id='post-user'>" + data.author + "</a>" +
							"<a id= 'delete'> x </a>" +
							"<div id='content'>" + data.content + "</div>" +
							"<div id= 'date'>" + data.date + "</div>" +
						 "</div>"
			$("#posts").prepend(insertpost);
			post_array.push(data);
		},

		error: function(data) {
			alert("failed");
			console.log(data);
		}
	});
});


/**
 * display_post - show all the posts
 */
 function display_posts() {
 	post_array.forEach(function(item){
 		insertpost = "<div id='user-post'>" +
							"<a id='post-user'>" + item.author + "</a>" +
							"<a id= 'delete'> x </a>" +
							"<div id='content'>" + item.content + "</div>" +
							"<div id= 'date'>" + item.date + "</div>" +
						 "</div>"
		$("#posts").append(insertpost);
 	});
 }