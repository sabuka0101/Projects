const textbox = document.getElementById("textbox");
const submitBtn = document.getElementById("submitBtn");
const list = document.getElementById("list");
const listItem = document.getElementsByClassName("listItem");
const deleteBtn = document.getElementById("deleteBtn");

submitBtn.onclick = function () {
  const text = textbox.value;
  const listItem = document.createElement("li");
  const deleteBtn = document.createElement("button");
  deleteBtn.innerText = "Delete";
  deleteBtn.style.backgroundColor = "rgb(218, 87, 87)";
  deleteBtn.style.color = "white";
  deleteBtn.style.border = "none";
  deleteBtn.style.borderRadius = "3px";
  deleteBtn.style.cursor = "pointer";
  deleteBtn.style.marginLeft = "240px";
  deleteBtn.style.fontSize = "18px";
  listItem.className = "listItem";
  listItem.innerText = text;
  list.appendChild(listItem);
  listItem.appendChild(deleteBtn);
  textbox.value = "";
};
deleteBtn.onclick = function () {
  deleteBtn.style.transform = "scale(0.92)";
  listItem.remove();
};
