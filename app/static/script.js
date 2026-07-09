// =====================================
// DOM ELEMENTS
// =====================================

const pdfFile = document.getElementById("pdfFile");
const uploadBtn = document.getElementById("uploadBtn");
const uploadStatus = document.getElementById("uploadStatus");
const currentPdf = document.getElementById("currentPdf");

const chatBox = document.getElementById("chatBox");

const question = document.getElementById("question");
const askBtn = document.getElementById("askBtn");

const clearChatBtn = document.getElementById("clearChatBtn");



// =====================================
// UPLOAD PDF
// =====================================

uploadBtn.addEventListener("click", uploadPDF);

async function uploadPDF() {

    if (pdfFile.files.length === 0) {

        alert("Please select a PDF.");

        return;

    }

    uploadBtn.disabled = true;

    uploadBtn.innerHTML = "Uploading...";

    uploadStatus.innerHTML = "Processing PDF...";

    const formData = new FormData();

    formData.append(
        "file",
        pdfFile.files[0]
    );

    try {

        const response = await fetch(
            "/upload",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        uploadBtn.disabled = false;

        uploadBtn.innerHTML = "⬆ Upload PDF";

        uploadStatus.innerHTML =
            "✅ PDF Uploaded Successfully";

        currentPdf.innerHTML =
            data.filename;

        addSystemMessage(
            "📄 " +
            data.filename +
            " uploaded successfully."
        );

    }

    catch (error) {

        uploadBtn.disabled = false;

        uploadBtn.innerHTML = "⬆ Upload PDF";

        uploadStatus.innerHTML =
            "❌ Upload Failed";

    }

}

// =====================================
// ASK AI
// =====================================

askBtn.addEventListener("click", askQuestion);

async function askQuestion() {

    const userQuestion = question.value.trim();

    if (userQuestion === "") {

        alert("Please enter a question.");

        return;

    }

    // User Message
    addUserMessage(userQuestion);

    question.value = "";

    // Thinking Message
    addThinkingMessage();

    askBtn.disabled = true;

    askBtn.innerHTML = "Thinking...";

    try {

        const response = await fetch(
            "/ask",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    question: userQuestion

                })

            }

        );

        const data = await response.json();

        removeThinkingMessage();

        addAIMessage(data.answer);

    }

    catch (error) {

        removeThinkingMessage();

        addAIMessage("❌ Something went wrong.");

    }

    askBtn.disabled = false;

    askBtn.innerHTML = "🚀 Ask AI";

}



// =====================================
// USER MESSAGE
// =====================================

function addUserMessage(message){

    const div = document.createElement("div");

    div.className = "user-message";

    div.innerHTML = `
        <strong>👤 You</strong>
        <br><br>
        ${message}
    `;

    chatBox.appendChild(div);

    scrollBottom();

}



// =====================================
// AI MESSAGE
// =====================================

function addAIMessage(message){

    const div = document.createElement("div");

    div.className = "ai-message";

    div.innerHTML = `
        <strong>🤖 AI</strong>
        <br><br>
        ${message}
    `;

    chatBox.appendChild(div);

    scrollBottom();

}



// =====================================
// SYSTEM MESSAGE
// =====================================

function addSystemMessage(message){

    const div = document.createElement("div");

    div.className = "ai-message";

    div.innerHTML = `
        <strong>📄 System</strong>
        <br><br>
        ${message}
    `;

    chatBox.appendChild(div);

    scrollBottom();

}



// =====================================
// AI THINKING...
// =====================================

function addThinkingMessage(){

    const div = document.createElement("div");

    div.className = "ai-message";

    div.id = "thinking";

    div.innerHTML = `
        <strong>🤖 AI</strong>
        <br><br>
        AI is thinking...
    `;

    chatBox.appendChild(div);

    scrollBottom();

}



function removeThinkingMessage(){

    const thinking = document.getElementById("thinking");

    if(thinking){

        thinking.remove();

    }

}

// =====================================
// AUTO SCROLL
// =====================================

function scrollBottom(){

    chatBox.scrollTop = chatBox.scrollHeight;

}



// =====================================
// CLEAR CHAT
// =====================================

clearChatBtn.addEventListener("click", () => {

    chatBox.innerHTML = `

        <div class="welcome-card">

            <div class="welcome-icon">

                🤖

            </div>

            <h3>

                Welcome to AI PDF Chatbot

            </h3>

            <p>

                Upload a PDF from the left panel and start asking questions.

            </p>

            <div class="welcome-tags">

                <span>Fast</span>

                <span>Private</span>

                <span>Offline AI</span>

                <span>RAG Powered</span>

            </div>

        </div>

    `;

});



// =====================================
// PRESS ENTER TO ASK
// =====================================

question.addEventListener("keydown", function(event){

    if(event.key === "Enter" && !event.shiftKey){

        event.preventDefault();

        askQuestion();

    }

});



// =====================================
// FILE NAME CHANGE
// =====================================

pdfFile.addEventListener("change", () => {

    if(pdfFile.files.length > 0){

        currentPdf.innerHTML = pdfFile.files[0].name;

    }

});



// =====================================
// PAGE LOADED
// =====================================

window.onload = () => {

    uploadStatus.innerHTML = "Ready";

};