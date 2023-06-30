// Wait for the DOM content to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Get references to the necessary HTML elements

  var dropdown = document.getElementById("productDropdown");
  var price = document.getElementById("price");
  var quantity = document.getElementById("quantity");

  // Add a change event listener to the dropdown element
  dropdown.addEventListener("change", function () {
    $("label").show();
    $("#price").show();
    $("#quantity").show();
    // Get the selected value from the dropdown
    var selectedValue = this.value;

    // Split the selected value into an array of values
    var values = selectedValue.split(";");

    // Assign the first value to the price element's value property
    price.value = values[0];

    // Assign the second value to the quantity element's value property
    quantity.value = values[1];
  });
});

$(document).ready(function () {
  $("label").hide();
  $("#price").hide();
  $("#quantity").hide();
})
