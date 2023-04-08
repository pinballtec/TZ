window.addEventListener("DOMContentLoaded", function () {
  var listItems = document.querySelectorAll(".list-item");
  if (listItems.length > 0) {
    listItems.forEach(function (item) {
      item.style.border = "1px solid #000";
      item.style.padding = "10px";
    });
  } else {
    var emptyListMessage = document.createElement("div");
    emptyListMessage.className = "empty-list";
    emptyListMessage.textContent = "No items";
    document.querySelector(".list-items").appendChild(emptyListMessage);
  }
});
