let mode = "basic";

function setMode(m) {
    mode = m;
}

function newChat() {
    document.getElementById("chatbox").innerHTML = "";
}

async function sendMessage() {

    let input = document.getElementById("message");
    let msg = input.value;
    if (!msg) return;

    let chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `<div class="user"><b>You:</b> ${msg}</div>`;

    input.value = "";

    let res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg, mode: mode})
    });

    let data = await res.json();

    chatbox.innerHTML += `<div class="bot"><b>AeroLite:</b> ${data.text}</div>`;
}