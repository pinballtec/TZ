document.getElementById("login-form").addEventListener("submit", function(event) {
    var errorMsg = document.getElementById("error-msg");
    var username = document.getElementById("id_username").value;
    var password = document.getElementById("id_password").value;

    if (!username || !password) {
        event.preventDefault();
        errorMsg.textContent = "Please fill in all the fields.";
    } else {
        errorMsg.textContent = "";
    }
});
