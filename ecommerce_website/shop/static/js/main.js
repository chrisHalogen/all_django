console.log('Hello From JS')
var updateButtons = document.getElementsByClassName('update-cart')

for (i = 0; i < updateButtons.length; i++){
	updateButtons[i].addEventListener('click', function () {
		var productID = this.dataset.product
		var action = this.dataset.action
		console.log(productID, action)
		
		console.log('User = ', user)

		if (user == 'AnonymousUser') {
			console.log('Not Logged In')

		}
		else {
			console.log('Logged In')
			updateUserOrder(productID, action)
		}
	})
}

function updateUserOrder(productID, action) {
	console.log('User is Logged In')

	var url = '/update_item/'
	fetch(
		url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': csrftoken,
			},
			body: JSON.stringify({
				'productId': productID,
				'action': action
			})

		}
	).then((data) => {
		console.log('Data: ', data)
		location.reload()
	})
}


// $(function () {

//   var siteSticky = function() {
// 		$(".js-sticky-header").sticky({topSpacing:0});
// 	};
// 	siteSticky();

// 	var siteMenuClone = function() {

// 		$('.js-clone-nav').each(function() {
// 			var $this = $(this);
// 			$this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
// 		});


// 		setTimeout(function() {
			
// 			var counter = 0;
//       $('.site-mobile-menu .has-children').each(function(){
//         var $this = $(this);
        
//         $this.prepend('<span class="arrow-collapse collapsed">');

//         $this.find('.arrow-collapse').attr({
//           'data-toggle' : 'collapse',
//           'data-target' : '#collapseItem' + counter,
//         });

//         $this.find('> ul').attr({
//           'class' : 'collapse',
//           'id' : 'collapseItem' + counter,
//         });

//         counter++;

//       });

//     }, 1000);

// 		$('body').on('click', '.arrow-collapse', function(e) {
//       var $this = $(this);
//       if ( $this.closest('li').find('.collapse').hasClass('show') ) {
//         $this.removeClass('active');
//       } else {
//         $this.addClass('active');
//       }
//       e.preventDefault();  
      
//     });

// 		$(window).resize(function() {
// 			var $this = $(this),
// 				w = $this.width();

// 			if ( w > 768 ) {
// 				if ( $('body').hasClass('offcanvas-menu') ) {
// 					$('body').removeClass('offcanvas-menu');
// 				}
// 			}
// 		})

// 		$('body').on('click', '.js-menu-toggle', function(e) {
// 			var $this = $(this);
// 			e.preventDefault();

// 			if ( $('body').hasClass('offcanvas-menu') ) {
// 				$('body').removeClass('offcanvas-menu');
// 				$this.removeClass('active');
// 			} else {
// 				$('body').addClass('offcanvas-menu');
// 				$this.addClass('active');
// 			}
// 		}) 

// 		// click outisde offcanvas
// 		$(document).mouseup(function(e) {
// 	    var container = $(".site-mobile-menu");
// 	    if (!container.is(e.target) && container.has(e.target).length === 0) {
// 	      if ( $('body').hasClass('offcanvas-menu') ) {
// 					$('body').removeClass('offcanvas-menu');
// 				}
// 	    }
// 		});
// 	}; 
// 	siteMenuClone();

// });

