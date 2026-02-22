async function sendQuery() {
    const input = document.getElementById("queryInput");
    const query = input.value.trim();

    if (!query) return;

    addMessage(query, "user");
    input.value = "";

    try {
        const response = await fetch(`http://localhost:8000/query?query=${encodeURIComponent(query)}`);
        const data = await response.json();
        const evaluatorDiv = document.getElementById("evaluator-text")

        if (data.flags && data.flags.length > 0) {
            evaluatorDiv.className = "evaluator warn"
            evaluatorDiv.innerText = `⚠️ Flags detected: ${data.flags.join(", ")}`
        } else {
            evaluatorDiv.className = "evaluator good"
            evaluatorDiv.innerText = "✅ No issues detected"
        }
        addMessage(data.answer, "bot");

        document.getElementById("modelUsed").innerText = data.model_used || "-";
        document.getElementById("confidence").innerText = data.confidence || "-";
        document.getElementById("latency").innerText = data.latency_ms || "-";

    } catch (error) {
        addMessage("Error connecting to backend.", "bot");
        console.log("Error:", error);
    }
}

function addMessage(text, sender) {
    const chatBox = document.getElementById("chatBox");
    const msg = document.createElement("div");

    msg.className = `message ${sender}`;
    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}