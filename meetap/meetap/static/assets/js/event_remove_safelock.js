/*function toggleelement(class_name, element_value, form_name)
{
 var x = document.getElementsByName(form_name)[element_value]
 x.document.getElementsByClassName(class_name)[element_value];

  if (x.style.display === 'none') {
    x.style.display = 'block';
  }
  else {
    x.style.display = 'none';
}
}*/

function toggleshort(class_name, element_value)
{
 var x = document.getElementsByName(class_name[element_value]

  if (x.style.display === 'none') {
    x.style.display = 'block';
  }
  else {
    x.style.display = 'none';
}
}

$(document).ready(function()
{
var safety_valve = $("[name='safety_valve']");
safety_valve.click(function(event); // Po zaznaczeniu zgody udostępnij przycisk wyślij.
 {
   var element_value = $(event.target).val();
   alert(element_value);
   toggleshort("untoggle", element_value);
   toggleshort("toggle", element_value);

});

});
