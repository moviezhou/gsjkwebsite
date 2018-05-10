// milestone timeline 

$('#news').slideDown({
	duration: 1000,
	easing: 'easeInBounce',
	complete: function () { }
});

$('.notification').hover(
	function () {
		$('#news1').slideUp({
			duration: 500,
			easing: 'easeInBounce',
			complete: function () { }
		});
	}
);


$('.carousel').carousel();
// jQuery to collapse the navbar on scroll
$(window).scroll(function () {
	if ($(".navbar").offset().top > 50) {
		$(".navbar-fixed-top").addClass("top-nav-collapse");
	} else {
		$(".navbar-fixed-top").removeClass("top-nav-collapse");
	}
});

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function () {
	$('a.page-scroll').bind('click', function (event) {
		var $anchor = $(this);
		$('html, body').stop().animate({
			scrollTop: $($anchor.attr('href')).offset().top
		}, 1500, 'easeInOutExpo');
		event.preventDefault();
	});
});



// Notifications scrolling
jQuery(".txtScroll-top").slide({titCell:".hd ul",mainCell:".bd ul",autoPage:true,effect:"top",autoPlay:true});

// Mobile notifications scrolling 

jQuery(".txtMarquee-left").slide({mainCell:".bd ul",autoPlay:true,effect:"leftMarquee",interTime:30,trigger:"click"});


jQuery(".company-news").slide({ trigger: "mouseover", easing: "easeOutCirc", pnLoop: false });

jQuery(".company-news").slide({ trigger: "mouseover", pnLoop: false });

$(document).ready(function () {
	$(".hk").mouseenter(function () {
		$(this).css("cursor", "pointer");
		$(".tab-indicator").stop();
		$(".tab-indicator").animate({ left: $(this).position().left + 'px' }, 350);
	});


	var summary = '';
	jQuery.each($('.sum p'), function(key, val){
		if(val.innerText){
			if(val.innerText.endsWith('...')){
				val.innerText = val.innerText.slice(0,-3);
			}
			summary += val.innerText;
			val.remove()
		}
	});

	summary += '...';
	var p = document.createElement('p');
	p.innerText = summary;
	$('.sum').append(p);

	// 大图和文字切换
jQuery(".txMovie").slide({ titCell:".focus_nav li", mainCell:".focus_pic", targetCell:".focus_text li", autoPlay:true,delayTime:100,startFun:function(i,p){
	//控制小图自动翻页
	if(i==0){ jQuery(".txMovie .navPrev").click() } else if( i%7==0 ){ jQuery(".txMovie .navNext").click()}
	}
});
// 小图滚动
jQuery(".txMovie").slide({ mainCell:".focus_nav ul",prevCell:".navPrev",nextCell:".navNext",effect:"left",vis:7,scroll:7,delayTime:0,autoPage:true,pnLoop:false});

jQuery(".txMovie").slide({ titCell: ".focus_nav li", mainCell: ".focus_pic", targetCell: ".focus_text li", autoPlay: true, delayTime: 100, startFun: function (i) { if (i == 0) { jQuery(".txMovie .navPrev").click() } else if (i % 7 == 0) { jQuery(".txMovie .navNext").click() } } }); jQuery(".txMovie").slide({ mainCell: ".focus_nav ul", prevCell: ".navPrev", nextCell: ".navNext", effect: "left", vis: 7, scroll: 7, delayTime: 0, autoPage: true, pnLoop: false });


// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function () {
	$('.navbar-toggle:visible').click();
});


$(".submenu a").on('click', function (evt) {
	window.location.href = evt.target.href;
	$("#colSideNav a").each(function () {

		$this = $(this);
		if (this.href == String(window.location.href)) {
			$(this).trigger('click');
			$this.siblings().removeClass('active');
			$this.addClass("active");
			$('#column-title>h5').text($this[0].text);
		}
	});
});


//   Secondary pages

$('.nav-left').on('click', function (evt) {
	$('#column-title>h5').text(evt.target.text);
	$('#current_column').text(evt.target.text);
});

$("#colSideNav a").each(function () {

	$this = $(this);
	if ($this[0].href == String(window.location.href)) {
		$(this).trigger('click');
		$this.siblings().removeClass('active');
		$this.addClass("active");
		$('#column-title>h5').text($this[0].text);
	}
});

// empty p tag generated by richtext filter when images placed in head of content. 
$('.highlight-content p').each(function () {
	if ($(this).text() === '') {
		$(this).remove();
	}
});

$('.news-content p').each(function () {
	if ($(this).text() === '') {
		$(this).remove();
	}
});


$('a.nav-sub').each(function () {
	if (this.href == window.location.href) {
		$(this).trigger('click');
	}
});

// auto hide video control when mouse off
$(".video").hover(function (event) {
	if (event.type === "mouseenter") {
		$(this).attr("controls", "");
	} else if (event.type === "mouseleave") {
		$(this).removeAttr("controls");
	}
});


var status = 0;
function openNav() {

	var colSideNav = document.getElementById("colSideNav");
	var newsList = document.getElementById("newsList");

	if (status == 1) {
		closeNav();
	}
	else {
		colSideNav.style.width = "250px";
		//  document.getElementById("newsList").style.marginLeft = "250px";
		newsList.style.transition = "-webkit-transform 500ms ease-out";

		newsList.style.transform = "translate(250px,0)";
		status = 1;
	}
}

function closeNav() {

	colSideNav.style.width = "0";
	newsList.style.transition = "-webkit-transform 500ms ease-out";
	newsList.style.transform = "translate(0px,0)";
	status = 0;
}
});


$(function() {

	$('#id_captcha_1').prop('required', true);
	$('#id_captcha_1').prop('required', '输入计算结果');
    
	// Click-handler for the refresh-link
	$('.captcha-refresh').click(function(){
		var $form = $(this).parents('form');
		var url = location.protocol + "//" + window.location.hostname + ":"
				  + location.port + "/captcha/refresh/";

		// Make the AJAX-call
		$.getJSON(url, {}, function(json) {
			console.log(json.image_url)
			$form.find('input[name="captcha_0"]').val(json.key);
			// $form.find('img.captcha').attr('src', json.image_url);
			$('.captcha')[0].src = json.image_url;
		});

		return false;
	});

	var form = $('#idform');
    form.submit(function () {
        $.ajax({
            type: 'POST',
            url: location.pathname,
            data: form.serialize(),
            success: function (data) {
				if(data.result) {
					$('.idfund-echo').first().addClass('idfund-success').removeClass('idfund-error');
					$("#idfund-message").html("需求申报成功");
				}
				else{
					$('.idfund-echo').first().addClass('idfund-error').removeClass('idfund-success');
					$("#idfund-message").html("验证码错误，请重新提交！");
					$('.captcha-refresh').click();
				}
            },
            error: function(request, status, error) {
				$("#idfund-message").html(request.responseText);
            }
        });
        return false;
	});
	
});

