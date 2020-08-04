// Prosta funkcja przerzucająca wartość listy rozwijanej do ukrytego formularza.
function gender_set()
{
  var x = document.getElementById("Genderselector").value;
  document.getElementById("id_gender").value = x;
}

function sex_preference_set()
{
  var x = document.getElementById("Sex_preference_selector").value;
  document.getElementById("id_sex_preference").value = x;
}

function sex_activity_set()
{
  var x = document.getElementById("Sex_activity_selector").value;
  document.getElementById("id_sex_role_activity").value = x;
}

function sex_dominance_set()
{
  var x = document.getElementById("Sex_dominance_selector").value;
  document.getElementById("id_sex_role_dominance").value = x;
}

function alcohol_set()
{
  var x = document.getElementById("Alcohol_selector").value;
  document.getElementById("id_alcohol").value = x;
}

function tobacco_set()
{
  var x = document.getElementById("Tobacco_selector").value;
  document.getElementById("id_tobacco").value = x;
}

$(document).ready(function()
{
  $('#send').click(function()
 {
  gender_set()
  sex_preference_set()
  sex_activity_set()
  sex_dominance_set()
  alcohol_set()
  tobacco_set()
  });
});
