$(document).ready(function () {
    $("#name").on("change", function () {
        var productName = $(this).val();
        $("#productform").attr("action", "/show-product/" + productName);
    });
});