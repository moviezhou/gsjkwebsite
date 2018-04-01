// milestone timeline 

$('#news').slideDown({
	duration: 1000, 
	easing: 'easeInBounce', 
	complete: function(){}});

$('.notification').hover(
	function(){
		$('#news1').slideUp({
			duration: 500, 
			easing: 'easeInBounce', 
			complete: function(){}});
	}
);


$('.carousel').carousel();
// jQuery to collapse the navbar on scroll
$(window).scroll(function() {
  if ($(".navbar").offset().top > 50) {
      $(".navbar-fixed-top").addClass("top-nav-collapse");
  } else {
      $(".navbar-fixed-top").removeClass("top-nav-collapse");
  }
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
  $('a.page-scroll').bind('click', function(event) {
      var $anchor = $(this);
      $('html, body').stop().animate({
          scrollTop: $($anchor.attr('href')).offset().top
      }, 1500, 'easeInOutExpo');
      event.preventDefault();
  });
});


// news-tab mouse over effect
$('.title-company').mouseover(function(e){
	$(this).addClass('focus');
	$(this).siblings().each(function(){
		$(this).removeClass('focus');
	});

	// e.target.id
	$('.news-list').children().each(function(){
		if($(this)[0].dataset.category === e.target.id) {
			$(this)[0].style.display = 'block'; 
			$(this).siblings().each(function(){
				// console.log($(this));
				$(this)[0].style.display = 'none';
			});
		}
	});

});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
  $('.navbar-toggle:visible').click();
});


$(".submenu a").on('click', function(evt){
	window.location.href = evt.target.href;
	$("#colSideNav a").each(function(){  

		$this = $(this);  
		if(this.href==String(window.location.href)){
			$(this).trigger('click');
			$this.siblings().removeClass('active');
			$this.addClass("active");
			$('#column-title>h5').text($this[0].text);   
		}  
	});  	
});


//   Secondary pages

$('.nav-left').on('click', function(evt){
	$('#column-title>h5').text(evt.target.text);
	$('#current_column').text(evt.target.text);
});

$("#colSideNav a").each(function(){  

	$this = $(this);  
	if($this[0].href==String(window.location.href)){
		$(this).trigger('click');
		$this.siblings().removeClass('active');
		$this.addClass("active");
		$('#column-title>h5').text($this[0].text);   
	}  
});  

// empty p tag generated by richtext filter when images placed in head of content. 
$('.highlight-content p').each(function() {
	if ($(this).text() === '') {
	  $(this).remove();
	}
  });

$('.news-content p').each(function() {
	if ($(this).text() === '') {
	  $(this).remove();
	}
  });


$('a.nav-sub').each(function (){ 
	if(this.href == window.location.href){
		$(this).trigger('click');
	}
});

// auto hide video control when mouse off
$(".video").hover(function(event) {
	if(event.type === "mouseenter") {
		$(this).attr("controls", "");
	} else if(event.type === "mouseleave") {
		$(this).removeAttr("controls");
	}
});


var status = 0;
function openNav() {

	var colSideNav =  document.getElementById("colSideNav");
	var newsList =  document.getElementById("newsList");

    if(status == 1){
    closeNav();
    }
    else{
		colSideNav.style.width = "250px";
		//  document.getElementById("newsList").style.marginLeft = "250px";
		newsList.style.transition="-webkit-transform 500ms ease-out";

		newsList.style.transform = "translate(250px,0)";
    	status = 1;
    }
}

function closeNav() {
    
	colSideNav.style.width = "0";
	newsList.style.transition="-webkit-transform 500ms ease-out";
	newsList.style.transform = "translate(0px,0)";
	status = 0;
}