$(document).ready(function() {
    
    /*Sticky navigation*/
    
    $('.js--section-features').waypoint(function(direction) {
        if (direction == "down"){
            $('nav').addClass('sticky');
            
        } else {
            $('nav').removeClass('sticky');
            
        }
    }, {
    offset: '60px;'
    });

    $('.js--section-result').waypoint(function(direction) {
        if (direction == "down"){
            $('.other-nav').addClass('sticky');
            $('.inside-nav').addClass('tool-relative');

        } else {
            $('.other-nav').removeClass('sticky');
            $('.inside-nav').removeClass('tool-relative');
        }
    }, {
    offset: '60px;'
    });

    $(".main-nav li").click(function() {
            $(".main-nav li").removeClass('active');
    });

    $('.js--section-result').waypoint(function() {
            $('table').addClass('sortable');
    });
    
    /*scroll on buttons*/
    $('.js--scroll-to-plan').click(function(){
        $('.html, body').animate({scrollTop: $('.js--section-plans').offset().top}, 1000); 
        });
    
    $('.js--scroll-to-start').click(function(){
        $('.html, body').animate({scrollTop: $('.js--section-features').offset().top}, 1000); 
        });
    
    /*Navigation scroll*/
    $(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});
    
/*Anmate upon scroll*/    
    $('.js--vp-1').waypoint(function(direction){
        $('.js--vp-1').addClass('animated fadeIn');
    }, {
  offset: '50%'
})
    
    $('.js--vp-2').waypoint(function(direction){
        $('.js--vp-2').addClass('animated fadeInUp');
    }, {
  offset: '50%'
})
    $('.js--vp-3').waypoint(function(direction){
        $('.js--vp-3').addClass('animated fadeIn');
    }, {
  offset: '50%'
})
    $('.js--vp-4').waypoint(function(direction){
        $('.js--vp-4').addClass('animated pulse');
    }, {
  offset: '50%'
})

    $('.js--vp-5').waypoint(function(direction){
        $('.js--vp-5').addClass('animated bounceInRight');
    }, {
  offset: '50%'
})
    
    $('#submit-button').click(function() {
        $(this).val('Loading...');
    return true; // allow regular form submission
});

    $('.report-btn').click(function() {
        $('.report-btn').text("Loading...");
        $('.network-btn').hide();
    return true; // allow regular form submission
});
    $('.network-btn').click(function() {
        $('.network-btn').text("Loading...");
        $('.report-btn').hide();
    return true; // allow regular form submission
});
    
     /*Mobile Navigation*/
    
    $('.js--nav-icon').click(function() {
        var nav = $('.js--main-nav');
        var icon = $('.js--nav-icon i');
        nav.animate({width: 'toggle'});
        nav.addClass('animated slideInLeft');
        
        if (icon.hasClass('ion-navicon-round')){
            icon.addClass('ion-close-round');
            icon.removeClass('ion-navicon-round');
        }else{
            icon.addClass('ion-navicon-round');
            icon.removeClass('ion-close-round');
        }
    });

    $(document).ready( function () {
    $('#table_id').DataTable();
} );
    
});

