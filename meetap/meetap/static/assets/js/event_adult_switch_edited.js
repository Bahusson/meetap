/*Funkcja podobna do event adult switch, tylko tutaj wychodzimy z rozwiniętej
listy i ją potem zwijamy, żeby użytkownik od początku widział swoje "dorosłe"
wybory*/


//Na spokojnie przesuwa stronę na sam dół.
function hop()
{
  var WH = $(window).height();
  var SH = $('body').prop("scrollHeight");
  $('html, body').stop().animate({scrollTop: SH-WH}, 1000);
}

// Zmień wyświetlanie elementu
function toggleelements(class_name, row_name)
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

function element_uncheck(class_name, row_name, element_id){
  if (row_name === false) {
    element_id.checked = false;
    class_name.style.display = 'none';
  }
}

//funkcja zwija wnuki i odznacza checkbox dziecka
function rollbackelement(class_name, row_name, check1, check2, check3)
{
  var x = document.getElementById(class_name);
  var y = document.getElementById(row_name).checked;
  let z = document.getElementById(check1);
  let n = document.getElementById(check2);
  let m = document.getElementById(check3);
  element_uncheck(x,y,z);
  element_uncheck(x,y,m);
  element_uncheck(x,y,n);
}

// Funkcja odznacza dzieci/wnuki checkboxa
function child_uncheck(parent_id, child_id)
{
  var y = document.getElementById(parent_id).checked;
  let z = document.getElementById(child_id);
  if (y === false) {
    z.checked = false;
  }
}

function uncheck_all_children(parent_id)
{
  child_uncheck(parent_id, "id_is_for_straight");
  child_uncheck(parent_id, "id_is_for_gay");
  child_uncheck(parent_id, "id_is_for_bi");
  child_uncheck(parent_id, "id_is_for_trans");
  child_uncheck(parent_id, "id_is_for_other");
  child_uncheck(parent_id, "id_is_for_passive");
  child_uncheck(parent_id, "id_is_for_r_passive");
  child_uncheck(parent_id, "id_is_for_switch");
  child_uncheck(parent_id, "id_is_for_r_active");
  child_uncheck(parent_id, "id_is_for_active");
  child_uncheck(parent_id, "id_is_for_submisive");
  child_uncheck(parent_id, "id_is_for_r_submissive");
  child_uncheck(parent_id, "id_is_for_neutral");
  child_uncheck(parent_id, "id_is_for_r_dominant");
  child_uncheck(parent_id, "id_is_for_dominant");
}

$(document).ready(function()
{
 if ($('#id_is_adult_only').not(':checked'))
 {
  toggleelements("id_is_adult_only_row", "id_is_adult_only");
  rollbackelement(
    "id_is_sex_party_row", "id_is_adult_only", "id_is_sex_party",
    "id_is_alcohol", "id_is_tobacco")
  uncheck_all_children("id_is_adult_only")
 };
if ($('#id_sex_party').not(':checked'))
{
  toggleelements("id_is_sex_party_row", "id_is_sex_party");
  uncheck_all_children("id_is_sex_party")
};
 $('#id_is_adult_only').click(function() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
 {
   toggleelements("id_is_adult_only_row", "id_is_adult_only");
   rollbackelement(
     "id_is_sex_party_row", "id_is_adult_only", "id_is_sex_party",
     "id_is_alcohol", "id_is_tobacco")
   uncheck_all_children("id_is_adult_only")
   hop();
});
 $('#id_is_sex_party').click(function() // Po zaznaczeniu zgody udostępnij przycisk wyślij.
{
  toggleelements("id_is_sex_party_row", "id_is_sex_party");
  uncheck_all_children("id_is_sex_party")
  hop();
});
});
