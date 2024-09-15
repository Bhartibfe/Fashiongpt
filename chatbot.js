function getBotResponse(userInput) {
    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById('chat-box');
        const botMessage = document.createElement('div');
        botMessage.textContent = data.response;
        botMessage.className = 'bot-message';
        chatBox.appendChild(botMessage);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
