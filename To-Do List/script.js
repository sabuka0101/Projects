const textbox = document.getElementById("textbox");
const submitBtn = document.getElementById("submitBtn");
const list = document.getElementById("list");

submitBtn.onclick = function () {
  const text = textbox.value;

  if (text.trim() === "") {
    return false;
  }

  const listItem = document.createElement("li");
  listItem.className = "listItem";

  const taskText = document.createElement("span");
  taskText.innerText = text;

  const deleteBtn = document.createElement("button");
  deleteBtn.innerText = "Delete";
  deleteBtn.style.backgroundColor = "rgb(218, 87, 87)";
  deleteBtn.style.color = "white";
  deleteBtn.style.border = "none";
  deleteBtn.style.borderRadius = "3px";
  deleteBtn.style.cursor = "pointer";
  deleteBtn.style.padding = "5px 10px";
  deleteBtn.style.fontSize = "18px";

  deleteBtn.onclick = function () {
    listItem.remove();
  };

  listItem.appendChild(taskText);
  listItem.appendChild(deleteBtn);
  list.appendChild(listItem);

  textbox.value = "";
};
