
var bottomImages = $(".bottomImages img");
var mainimage = $("img.mainimage");

bottomImages.first().addClass('border');

bottomImages.on( "click", function( event ) {
   mainimage.attr('src', $(this).attr('src'));
   bottomImages.removeClass('border');
   $(this).addClass('border');
});