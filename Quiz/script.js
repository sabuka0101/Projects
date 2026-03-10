const answerBtns = document.querySelectorAll(".answerBtn");
const answers = document.querySelectorAll(".answer");
const main = document.querySelector(".main");
const question = document.getElementById("question");
let currentQuestionIndex = 0;

const quizData = [
  {
    question: "What is the capital of France?",
    answers: [
      { text: "New York", correct: false },
      { text: "London", correct: false },
      { text: "Paris", correct: true },
      { text: "Dublin", correct: false },
    ],
  },
  {
    question: "Which city is the capital of Georgia?",
    answers: [
      { text: "Tbilisi", correct: true },
      { text: "Batumi", correct: false },
      { text: "Kutaisi", correct: false },
      { text: "Gori", correct: false },
    ],
  },
];

function showQuestion() {
  const currentQuestion = quizData[currentQuestionIndex];
  question.textContent = currentQuestion.question;
  answers.forEach((span, index) => {
    span.textContent = currentQuestion.answers[index].text;
    span.style.backgroundColor = "";
  });
}

showQuestion();

answers.forEach((btn) => {
  btn.addEventListener("click", function () {
    answers.forEach((b) => (b.style.backgroundColor = ""));
    this.style.backgroundColor = "gray";

    if (!document.getElementById("nextBtn")) {
      const nextBtn = document.createElement("button");
      nextBtn.id = "nextBtn";
      nextBtn.textContent = "Next";
      main.appendChild(nextBtn);
      nextBtn.addEventListener("click", () => {
        currentQuestionIndex++;

        if (currentQuestionIndex < quizData.length) {
          showQuestion();
          nextBtn.remove();
        } else {
          question.textContent = "Quiz Complete!";
          main.innerHTML = "<h2>Final Score: ...</h2>";
        }
      });
    }
  });
});
