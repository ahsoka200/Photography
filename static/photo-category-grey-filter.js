var picture = $(".bwWrapper");



picture.mouseover(function() {
	var greyFilter = $( this ).find( "div.photoCategoryFilter" );
    greyFilter.fadeIn(400);
});


picture.mouseleave(function() {
  var greyFilter = $( this ).find( "div.photoCategoryFilter" );
  greyFilter.fadeOut(200);
});
