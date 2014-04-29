var picture = $(".bwWrapper");



picture.mouseover(function() {
	var greyFilter = $( this ).find( "div" );
    greyFilter.fadeIn(400);
});


picture.mouseleave(function() {
  var greyFilter = $( this ).find( "div" );
  greyFilter.fadeOut(200);
});
