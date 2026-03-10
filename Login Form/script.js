const text = document.getElementById("text");
const password = document.getElementById("password");
const message = document.getElementById("error-message");

const database = [
  { username: "alice", password: "alice123" },
  { username: "bob", password: "bob123" },
  { username: "charlie", password: "charlie123" },
];

function LogIn(event) {
  event.preventDefault();

  if (text.value === "" && password.value === "") {
    message.textContent = "Enter your Username and Password";
    message.style.color = "rgb(238, 56, 56)";
  } else if (text.value === "") {
    message.textContent = "Enter your Username";
    message.style.color = "rgb(238, 56, 56)";
  } else if (password.value === "") {
    message.textContent = "Enter your Password";
    message.style.color = "rgb(238, 56, 56)";
  } else {
    message.textContent = "Login is Invalid";
    message.style.color = "rgb(238, 56, 56)";
  }

  for (let i = 0; i < database.length; i++) {
    if (
      database[i].username === text.value &&
      database[i].password === password.value
    ) {
      message.textContent = "Login successful";
      message.style.color = "rgb(28, 179, 28)";
    }
  }
}
