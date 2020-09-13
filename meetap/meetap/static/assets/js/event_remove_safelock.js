function toggleelement(class_name)
{
 var x = document.getElementsByClassName(class_name);
  if (x.style.display === 'none') {
    x.style.display = 'block';
  }
  else {
    x.style.display = 'none';
}
}

$(document).ready(function()
{
 $('.untoggle').click(function(event) // Po zaznaczeniu zgody udostępnij przycisk wyślij.
 {
   var element_value = $(event.target).value();
   toggleelement(".toggle", element_value);
   toggleelement(".untoggle", element_value);
   hop();
});

});
