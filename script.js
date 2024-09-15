document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput) {
        const chatBox = document.getElementById('chat-box');
        const userMessage = document.createElement('div');
        userMessage.textContent = userInput;
        userMessage.className = 'user-message';
        chatBox.appendChild(userMessage);

        // Send user input to the chatbot logic
        getBotResponse(userInput);

        document.getElementById('user-input').value = '';
    }
});

document.getElementById('ar-button').addEventListener('click', function() {
    startAR();
});
