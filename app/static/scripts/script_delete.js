document
  .getElementById("delete-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    if (confirm("Are you sure you want to delete this task?")) {
      // If user confirms, submit the form
      event.target.submit();
    }
  });
