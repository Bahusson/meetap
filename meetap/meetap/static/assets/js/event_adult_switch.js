// Na spokojnie przesuwa stronę na sam dół.
function hop()
{
  var WH = $(window).height();
  var SH = $('body').prop("scrollHeight");
  $('html, body').stop().animate({scrollTop: SH-WH}, 1000);
}

function toggleelement(class_name)
{
  var x = document.getElementById(class_name);
  alert("test");
  if (x.style.display === 'none') {
    x.style.display = 'block';
  }
  else {
    x.style.display = 'none';
  }
}

$(document).ready(function()
{
 $('#id_is_sex_party').click(function() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
{
  toggleelement("id_is_for_straight");
  hop();
});
});
