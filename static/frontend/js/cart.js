$(document).ready(function() {

    var dropDownChooser = $('.categories-drop > .categories > ul >li');

    dropDownChooser.hover(function(e) {
        e.preventDefault();
        $('.categories-drop > .categories').toggleClass('first-active');
    })

})

$('.profile-menuopner').click(function(){
    $('.profileusermenu').toggleClass('active');
});

$(document).ready(function(c) {

							

    $('.close1').on('click', function(c){

            $('.cart-header').fadeOut('slow', function(c){

            $('.cart-header').remove();

        });

    });	  

});

$(document).ready(function(c) {

							

    $('.close2').on('click', function(c){

            $('.cart-header1').fadeOut('slow', function(c){

            $('.cart-header1').remove();

    });

});	  

});




