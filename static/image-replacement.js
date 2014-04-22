
var bottomImages = $(".bottomImages img");
var mainimage = $("img.mainimage");

bottomImages.on( "click", function( event ) {
   mainimage.attr('src', $(this).attr('src'));
});