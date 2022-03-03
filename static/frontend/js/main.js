$(document).ready(function() {
    $(".memenu").memenu();
});

$(window).load(function() {
    $("#slider-range").slider({
        range: true,
        min: 0,
        max: 400000,
        values: [8500, 350000],
        slide: function(event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        }
    });
    $("#amount").val("$" + $("#slider-range").slider("values", 0) + " - $" + $("#slider-range").slider("values", 1));

}); //]]> 

$(document).ready(function() {

    var dropDownChooser = $('.categories-drop > .categories > ul >li');

    dropDownChooser.hover(function(e) {
        e.preventDefault();
        $('.categories-drop > .categories').toggleClass('first-active');
    })

})

$(window).load(function() {



    $("#homebanner").flexisel({



        visibleItems: 1,

        animationSpeed: 1500,

        autoPlay: true,

        autoPlaySpeed: 2500,

        pauseOnHover: true,

        enableResponsiveBreakpoints: true,

        responsiveBreakpoints: {

            portrait: {

                changePoint: 480,

                visibleItems: 1

            },

            landscape: {

                changePoint: 640,

                visibleItems: 1

            },

            tablet: {

                changePoint: 768,

                visibleItems: 1

            }

        }

    });

});

$(window).load(function() {

    $('.flexslider').flexslider({

        animation: "fade",

        controlNav: "thumbnails",

        start: function(slider) {

            $('body').removeClass('loading');

        }

    });

});