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
});

