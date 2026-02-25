const textbox = document.getElementById("textbox");
const submitBtn = document.getElementById("submitBtn");
const list = document.getElementById("list");
const taskCount = document.getElementById("taskCount");
const warnText = document.getElementById("warnText");
const completedTasksCount = document.getElementById("completedTasksCount");
taskCount.textContent = 0;
completedTasksCount.textContent = 0;
let count = 0;
let completeCount = 0;

textbox.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    submitBtn.click();
  }
});

submitBtn.onclick = function () {
  const text = textbox.value;
  if (list.children.length >= 5) {
    warnText.innerHTML = "Maximum 5 tasks allowed";
    return false;
  }

  if (text.trim() === "") {
    warnText.innerHTML = "Please enter the task";
    return false;
  } else if (text.length > 20) {
    warnText.innerHTML = "Maximum 20 characters allowed";
    return false;
  } else {
    taskCount.textContent = ++count;
    warnText.innerHTML = "";
  }

  const listItem = document.createElement("li");
  listItem.className = "listItem";

  const taskText = document.createElement("span");
  taskText.id = "taskText";
  taskText.innerText = text;

  const doneBtn = document.createElement("button");
  const deleteBtn = document.createElement("button");
  doneBtn.className = "doneBtn";
  doneBtn.innerHTML = '<i class="fa-solid fa-check"></i>';
  deleteBtn.className = "deleteBtn";
  deleteBtn.innerHTML = '<i class="fa-solid fa-trash"></i>';
  doneBtn.style.backgroundColor = "rgb(113, 218, 87)";
  deleteBtn.style.backgroundColor = "rgb(218, 87, 87)";
  doneBtn.style.color = "white";
  deleteBtn.style.color = "white";
  doneBtn.style.border = "none";
  deleteBtn.style.border = "none";
  doneBtn.style.borderRadius = "3px";
  deleteBtn.style.borderRadius = "3px";
  doneBtn.style.cursor = "pointer";
  deleteBtn.style.cursor = "pointer";
  doneBtn.style.padding = "5px 10px";
  deleteBtn.style.padding = "5px 10px";
  doneBtn.style.fontSize = "18px";
  deleteBtn.style.fontSize = "18px";

  doneBtn.onclick = function () {
    if (!listItem.completed) {
      taskText.style.textDecoration = "line-through";
      taskText.style.textDecorationColor = "black";
      completedTasksCount.textContent = ++completeCount;
      listItem.completed = true;
    }
  };

  deleteBtn.onclick = function () {
    taskCount.textContent = --count;
    listItem.remove();
    warnText.textContent = "";
    if (completeCount === 0) {
      return false;
    } else {
      completedTasksCount.textContent = --completeCount;
    }
  };

  listItem.appendChild(taskText);
  listItem.appendChild(doneBtn);
  listItem.appendChild(deleteBtn);
  list.appendChild(listItem);

  textbox.value = "";
};
