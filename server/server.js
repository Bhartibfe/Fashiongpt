const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static('../'));

app.post('/chatbot', (req, res) => {
    const userMessage = req.body.message;

    // Here you would integrate your AI model to get the response
    // For now, we'll just send a mock response
    const botResponse = `This is a response to "${userMessage}"`;

    res.json({ response: botResponse });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
