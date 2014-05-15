var rightarrow = $(".rightarrow");
var infodiv = $(".info");
var text = $(".fadeText");
var leftarrow = $(".leftarrow");



rightarrow.on( "click", function( event ) {
	
	text.fadeOut(400, function() {
		infodiv.animate({ "height": "50px", "width": "50px" }, 1000 );
		leftarrow.show();
		rightarrow.hide();
	});

	


});



leftarrow.on( "click", function( event ) {
	infodiv.animate({ "height": "189px", "width": "170px" }, 1000, function() {

		text.fadeIn(400);

	leftarrow.hide();
	rightarrow.show();
});
	

});


