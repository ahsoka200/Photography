
var bottomImages = $(".bottomImages img");
var mainimage = $("img.mainimage");


bottomImages.first().addClass('border');

bottomImages.on( "click", function( event ) {
	var bigimage = $(this).attr('src').replace("zzz", "");
   mainimage.attr('src', bigimage);
   var picInfo = getimageinfo(bigimage);
   
   bottomImages.removeClass('border');
   $(this).addClass('border');
   updatebox(picInfo);
});


//javascript function that returns object in array that matches path


function getimageinfo(path){
	for (var i = 0; i < all_photos.length; i++) {
    
	    if(path == all_photos[i].path){
	    	return all_photos[i];
	    }
	}
}

function updatebox(info){

	var imagetitle = $("#title");
	var imageplace = $("#place");
	var imageyear = $("#year");


	imagetitle.text(info.title);
	imageplace.text(info.place);
	imageyear.text(info.year);
 
}


$(document).ready(function() {
   alert('Page fully loaded.');
  });









