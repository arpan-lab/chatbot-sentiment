const chat = document.getElementById('chat');
const form = document.getElementById('form');
const text = document.getElementById('text');


function addLine(role, textContent, meta) {
const d = document.createElement('div');
d.className = role;
d.innerHTML = `<div>${textContent}</div>` + (meta ? `<div class="meta">${meta}</div>` : '');
chat.appendChild(d);
chat.scrollTop = chat.scrollHeight;
}


form.onsubmit = async (e) => {
e.preventDefault();
const t = text.value.trim();
if (!t) return;
addLine('user', t);
text.value = '';
const res = await fetch('/api/message', {
method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({text: t})
});
const j = await res.json();
if (j.error) {
addLine('bot', 'Error: ' + j.error);
return;
}
addLine('bot', j.reply, `Statement sentiment: ${j.statement_sentiment.label} (${j.statement_sentiment.scores.compound.toFixed(3)})`);
// show conversation-level label
addLine('bot', `Conversation sentiment: ${j.conversation_sentiment.label} (avg ${j.conversation_sentiment.average_compound.toFixed(3)})`, `Trend: ${j.trend.trend}`);
}


document.getElementById('clear').onclick = async () => {
// for demo: reload page to clear server-side memory
location.reload();
}