const API_URL = 'http://127.0.0.1:8000/api/chat/';

async function loadMessages() {
    const response = await fetch(API_URL);
    const messages = await response.json();
    const container = document.getElementById('messages');
    
    container.innerHTML = '';
    messages.forEach(msg => {
        const div = document.createElement('div');
        div.className = 'message';
        div.innerHTML = `<strong>${msg.name}:</strong> ${msg.message}`;
        container.appendChild(div);
    });
}

async function sendMessage(name, message) {
    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, message })
    });
    document.getElementById('messageInput').value = '';
    loadMessages();
}

document.getElementById('chatForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('nameInput').value;
    const message = document.getElementById('messageInput').value;
    sendMessage(name, message);
});

loadMessages();
