// Na spokojnie przesuwa stronę na sam dół.
/*function hop()
{
  var WH = $(window).height();
  var SH = $('body').prop("scrollHeight");
  $('html, body').stop().animate({scrollTop: SH-WH}, 1000);
}*/

function toggleelement(class_name)
{
 var x = document.getElementById(class_name);
  if (x.style.display === 'none') {
    x.style.display = 'block';
  }
  else {
    x.style.display = 'none';
}
}

$(document).ready(function()
{
 $('#add_remove_div').click(function() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
 {
   toggleelement("hidden_row_div");
   hop();
});

});
