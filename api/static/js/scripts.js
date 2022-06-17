// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
    document.getElementById("navbar-left").style.marginTop= "-20px";
    document.getElementById("navbar-right").style.marginTop = "-20px ";

  } else {
    document.getElementById("navbar-right").style ='none'
    document.getElementById("navbar-left").style ='none'
  }
}

$(document).ready(function() {
  $("form#subscribeForm").submit(function() {
      var name = $("input#user-name").val();
      var email = $("input#user-email").val();
      var message = $("input#user-message").val();
      var $form = $('form#subscribeForm');
      if (name != "" && email != "" && message != "") {
          register($form);
          alert("Hello " + name + " we have received your message. Thank you for reaching out to us!");
      };
      event.preventDefault();
  });
});

function register($form) {
  $.ajax({
      type: $form.attr('method'),
      url: $form.attr('action'),
      data: $form.serialize(),
      cache: false,
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      error: function(err) {},
      success: function(data) {
          $("#subscribeForm").val('subscribe')
          if (data.result === 'success') {
              //Success
              $('#subscribe-result').html('<p>Thank you!</p>');
          };
      }
  });
};