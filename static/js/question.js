let questionIndex = 0;
const questionText = document.getElementById('questionText');
const timerElement = document.getElementById('timer');
const cameraFeed = document.getElementById('cameraFeed');
let timer;

// Fetch and Display the Next Question
async function getNextQuestion() {
    try {
        const response = await fetch(`/get-question/${questionIndex}`);
        const data = await response.json();

        if (data.status === "Interview completed") {
            window.location.href = "result.html";
            return;
        }

        questionText.textContent = data.question;
        questionIndex = data.index;
        startTimer();

    } catch (error) {
        console.error("Error getting question:", error);
    }
}

// Start 45-second Timer
function startTimer() {
    let timeLeft = 45;
    timerElement.textContent = `Time Left: ${timeLeft}s`;
    clearInterval(timer);
    timer = setInterval(() => {
        timeLeft -= 1;
        timerElement.textContent = `Time Left: ${timeLeft}s`;
        if (timeLeft <= 0) {
            clearInterval(timer);
            processAnswer().then(getNextQuestion);
        }
    }, 1000);
}

// Process Answer and Move to the Next Question
async function processAnswer() {
    const response = await fetch('/process-answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ index: questionIndex })
    });
    const data = await response.json();
    console.log("Rating for question:", data.rating);
}

// Load the Camera Feed
async function requestCameraPermissions() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        cameraFeed.srcObject = stream;
    } catch (error) {
        console.error("Error accessing camera:", error);
        alert("Camera and microphone access are required.");
    }
}

// Initialize
document.getElementById('speakQuestion').addEventListener('click', () => {
    const utterance = new SpeechSynthesisUtterance(questionText.textContent);
    speechSynthesis.speak(utterance);
});

document.getElementById('nextQuestion').addEventListener('click', () => {
    clearInterval(timer);
    processAnswer().then(getNextQuestion);
});

requestCameraPermissions();
getNextQuestion();
