// Generate random number
const secretNumber = Math.floor(Math.random() * 100) + 1;

let attempts = 0;
const maxAttempts = 3;

function checkGuess() {
    const guessInput = document.getElementById("guess");
    const result = document.getElementById("result");
    const userGuess = Number(guessInput.value);

    if (!userGuess || userGuess < 1 || userGuess > 100) {
        result.innerHTML = "⚠️ Enter a number between 1 and 100";
        return;
    }

    attempts++;

    if (userGuess === secretNumber) {
        result.innerHTML = "🎉 YOU WIN 🎉";
        document.getElementById("winSound").play();
        endGame();
    } 
    else {
        if (attempts < maxAttempts) {
            result.innerHTML = `❌ Wrong answer! Attempts left: ${maxAttempts - attempts}`;
            document.getElementById("wrongSound").play();
        } 
        else {
            result.innerHTML = `💀 GAME OVER! Number was ${secretNumber}`;
            document.getElementById("loseSound").play();
            endGame();
        }
    }
}

function endGame() {
    document.getElementById("guess").disabled = true;
}
