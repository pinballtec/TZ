$(document).ready(function () {
  $('input[type="text"]').addClass("custom-input");
  $("textarea").addClass("custom-textarea");
  $('input[type="checkbox"]').addClass("custom-checkbox");
  $('input[type="submit"]').addClass("custom-submit");

  $('input[type="submit"]').on("click", function () {
    alert("Form submitted!");
    console.log("submitted");
  });

  $(".form-group input, .form-group textarea").css("width", "100%");
  $(".form-group label").css("margin-bottom", "5px");

  $(".form-group input, .form-group textarea")
    .on("focus", function () {
      $(this).addClass("focused");
    })
    .on("blur", function () {
      $(this).removeClass("focused");
    });

  $(".custom-submit").on("click", function () {
    alert("Form submitted successfully!");
  });
});
