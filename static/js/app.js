document.addEventListener('DOMContentLoaded', function () {
    let questionIndex = 0;
    const questionText = document.getElementById('questionText');
    const speakQuestionButton = document.getElementById('speakQuestion');
    const nextQuestionButton = document.getElementById('nextQuestion');
    const repeatQuestionButton = document.getElementById('repeatQuestion');
    const timerElement = document.getElementById('timer');
    const ratingScore = document.getElementById('ratingScore');
    const cameraFeed = document.getElementById('cameraFeed');
    let timer;

    async function getNextQuestion() {
        try {
            const response = await fetch(`/get-question/${questionIndex}`);
            const data = await response.json();

            if (data.status === "Interview completed") {
                alert("Interview completed!");
                return;
            }

            questionText.textContent = data.question;
            questionIndex = data.index;

            startTimer();

        } catch (error) {
            console.error("Error getting question:", error);
        }
    }

    function startTimer() {
        let timeLeft = 45;
        timerElement.textContent = `${timeLeft}s`;
        clearInterval(timer);
        timer = setInterval(() => {
            timeLeft -= 1;
            timerElement.textContent = `${timeLeft}s`;
            if (timeLeft <= 0) {
                clearInterval(timer);
                alert("Time's up for this question!");
            }
        }, 1000);
    }

    speakQuestionButton.addEventListener('click', () => {
        const utterance = new SpeechSynthesisUtterance(questionText.textContent);
        speechSynthesis.speak(utterance);
    });

    nextQuestionButton.addEventListener('click', async () => {
        await processAnswer();
        questionIndex += 1;
        await getNextQuestion();
    });

    repeatQuestionButton.addEventListener('click', () => {
        const utterance = new SpeechSynthesisUtterance(questionText.textContent);
        speechSynthesis.speak(utterance);
        startTimer();
    });

    async function processAnswer() {
        const response = await fetch('/process-answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index: questionIndex })
        });
        const data = await response.json();
        ratingScore.textContent = `Rating: ${data.rating.toFixed(2)}%`;
    }

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            cameraFeed.srcObject = stream;
        })
        .catch(error => {
            console.error("Error accessing camera:", error);
            alert("Camera access is needed for this feature.");
        });

    getNextQuestion();
});
