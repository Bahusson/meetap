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
 var y = document.getElementById("id_is_sex_party").checked;
  if (x.style.display === 'none', y === true) {
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
  toggleelement("id_is_sex_party_row1");
  toggleelement("id_is_sex_party_row2");  
  hop();
});
});
