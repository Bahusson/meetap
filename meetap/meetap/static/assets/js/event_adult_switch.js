// Na spokojnie przesuwa stronę na sam dół.
function hop()
{
  var WH = $(window).height();
  var SH = $('body').prop("scrollHeight");
  $('html, body').stop().animate({scrollTop: SH-WH}, 1000);
}

function toggleelement(class_name, row_name)
{
 var x = document.getElementById(class_name);
 var y = document.getElementById(row_name).checked;
  if (x.style.display === 'none', y === true) {
    x.style.display = 'block';
  }
  else {
    x.style.display = 'none';
}
}

function rollbackelement(class_name, row_name, row_name2)
{
  var x = document.getElementById(class_name);
  var y = document.getElementById(row_name).checked;
  let z = document.getElementById(row_name2);
  if (y === false) {
    z.checked = false;
    x.style.display = 'none';
  }
}

$(document).ready(function()
{
 $('#id_is_adult_only').click(function() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
 {
   toggleelement("id_is_adult_only_row", "id_is_adult_only");
   rollbackelement("id_is_sex_party_row", "id_is_adult_only", "id_is_sex_party")
   hop();
});
 $('#id_is_sex_party').click(function() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
{
  toggleelement("id_is_sex_party_row", "id_is_sex_party");
  hop();
});
});
