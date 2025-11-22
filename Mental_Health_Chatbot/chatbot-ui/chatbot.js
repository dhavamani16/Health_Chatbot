// Chat history management
let userData = JSON.parse(localStorage.getItem('userData')) || null;
let chats = [];
let currentChatId = null;
let messageCount = 0;
let dataset = "";

// Load user-specific chat history
function loadUserChats() {
    if (userData) {
        const userChatKey = `chatHistory_${userData.name}`;
        chats = JSON.parse(localStorage.getItem(userChatKey)) || [];
    }
}

// Save user-specific chat history
function saveUserChats() {
    if (userData) {
        const userChatKey = `chatHistory_${userData.name}`;
        localStorage.setItem(userChatKey, JSON.stringify(chats));
    }
}

// Load all datasets from data/ folder
let allDatasets = {};

async function loadAllDatasets() {
    const datasetFiles = ['stress_management.txt', 'depression.txt', 'anxiety.txt', 'sleep.txt'];
    
    for (let file of datasetFiles) {
        try {
            const response = await fetch(`../data/${file}`);
            const text = await response.text();
            const key = file.replace('.txt', '');
            allDatasets[key] = text;
            console.log(`✓ Loaded dataset: ${key}`);
        } catch (e) {
            console.log(`⚠ Could not load dataset: ${file}`);
        }
    }
}

// Load chats on page load
window.addEventListener('load', async () => {
    // If no user data, treat visitor as Guest (don't force redirect)
    if (!userData) {
        userData = { name: 'Guest', email: 'guest', isLoggedIn: false };
        localStorage.setItem('userData', JSON.stringify(userData));
    }

    // Load user-specific chat history
    loadUserChats();

    // Display user name in header
    displayUserName();

    // Load all available datasets
    await loadAllDatasets();
    
    displayChatHistory();
    if (chats.length === 0) {
        startNewChat();
    } else {
        loadChat(chats[0].id);
    }
});

function displayUserName() {
    const chatTitle = document.getElementById('chatTitle');
    if (chatTitle && userData) {
        chatTitle.innerHTML = `Welcome, ${userData.name}! 👋`;
    }
}

function startNewChat() {
    const newChatId = 'chat_' + Date.now();
    const newChat = {
        id: newChatId,
        title: 'New Chat',
        messages: [],
        timestamp: new Date().toLocaleString()
    };
    chats.unshift(newChat);
    saveChatHistory();
    loadChat(newChatId);
    displayChatHistory();
}

function saveChatHistory() {
    saveUserChats();
}

function displayChatHistory() {
    const historyContainer = document.getElementById('chatHistory');
    historyContainer.innerHTML = '';
    
    chats.forEach(chat => {
        const item = document.createElement('div');
        item.className = `history-item ${chat.id === currentChatId ? 'active' : ''}`;
        item.textContent = chat.title || 'Untitled Chat';
        item.onclick = () => loadChat(chat.id);
        historyContainer.appendChild(item);
    });
}

function loadChat(chatId) {
    currentChatId = chatId;
    const chat = chats.find(c => c.id === chatId);
    
    const chatBox = document.getElementById('chatBox');
    chatBox.innerHTML = '';
    
    if (chat && chat.messages.length > 0) {
        chat.messages.forEach(msg => {
            appendMessage(msg.role, msg.text);
        });
    }
    
    displayChatHistory();
    document.getElementById('chatInput').focus();
}

function updateChatTitle() {
    const chat = chats.find(c => c.id === currentChatId);
    if (chat && chat.messages.length > 0) {
        const firstUserMessage = chat.messages.find(m => m.role === 'user');
        if (firstUserMessage) {
            chat.title = firstUserMessage.text.substring(0, 30) + (firstUserMessage.text.length > 30 ? '...' : '');
            saveChatHistory();
            displayChatHistory();
        }
    }
}

function startChat() {
    const welcomeSection = document.querySelector('.welcome-section');
    const chatContainer = document.getElementById('chatContainer');
    
    if (welcomeSection) {
        welcomeSection.style.display = 'none';
    }
    chatContainer.style.display = 'flex';
    document.getElementById('chatInput').focus();
}

function toggleChat() {
    const chatContainer = document.getElementById('chatContainer');
    const welcomeSection = document.querySelector('.welcome-section');
    
    if (chatContainer.style.display === 'none' || !chatContainer.style.display) {
        chatContainer.style.display = 'flex';
        if (welcomeSection) {
            welcomeSection.style.display = 'none';
        }
        document.getElementById('chatInput').focus();
    } else {
        chatContainer.style.display = 'none';
        if (welcomeSection) {
            welcomeSection.style.display = 'flex';
        }
    }
}

function appendMessage(role, text) {
    const box = document.getElementById("chatBox");
    const mess = document.createElement("div");
    mess.className = `message ${role}`;
    mess.innerHTML = `<strong>${role}:</strong> ${text}`;
    box.appendChild(mess);
    box.scrollTop = box.scrollHeight;
    
    // Save to current chat
    const chat = chats.find(c => c.id === currentChatId);
    if (chat) {
        chat.messages.push({ role, text });
        saveChatHistory();
    }
}

// Enhanced demo responses for mental health support
const demoResponses = {
    "default": [
        "I'm here to listen. Tell me more about what you're experiencing.",
        "Thank you for sharing. Your feelings are valid and important.",
        "I understand. What would help you feel better right now?",
        "I'm here for you. What's on your mind?",
        "That's important. How long have you been feeling this way?",
        "You're not alone in this. Let's talk about it.",
        "I'm listening. Tell me more.",
        "Your wellbeing matters. What can I help with?",
        "I appreciate you sharing this with me. What would help?",
        "You're being brave by reaching out. I'm here to support you."
    ],
    "depression": [
        "I hear that you're feeling depressed. That's a real and valid emotion. Have you talked to anyone close to you about how you're feeling?",
        "Depression is serious, and I'm glad you're talking about it. Please consider reaching out to a mental health professional or counselor who can provide proper support.",
        "What you're feeling is understandable. Many people experience depression. Would it help to talk about what's triggering these feelings?"
    ],
    "anxiety": [
        "Anxiety can feel overwhelming. I'm here to listen. What's making you anxious right now?",
        "It's okay to feel anxious. These feelings are temporary. What helps you calm down usually?",
        "Have you tried any grounding techniques when anxiety strikes?"
    ],
    "suicide": [
        "I'm very concerned about what you just shared. Your life has value. Please reach out to a crisis helpline immediately:\n🇮🇳 India: 9152987821 or 1800-599-0019\n🇺🇸 USA: 988\n🇬🇧 UK: 116 123",
        "If you're having thoughts of suicide, please contact emergency services or a crisis helpline right now. You don't have to face this alone.",
        "Your life matters. Please reach out to a professional: India 9152987821, USA 988, UK 116 123"
    ],
    "help": [
        "I'm here to help. What's troubling you?",
        "Of course, I'm here to listen and support you. What do you need help with?",
        "I'm ready to listen. Tell me what's going on."
    ]
};

function searchDatasets(message) {
    const lower = message.toLowerCase();
    
    // Define keyword-to-dataset mapping for better matching
    const keywordMap = {
        'stress': ['stress_management'],
        'anxiety': ['anxiety'],
        'panic': ['anxiety'],
        'worried': ['anxiety'],
        'afraid': ['anxiety'],
        'depression': ['depression'],
        'depressed': ['depression'],
        'sad': ['depression'],
        'sleep': ['sleep'],
        'insomnia': ['sleep'],
        'tired': ['sleep'],
        'relax': ['stress_management'],
        'meditation': ['stress_management'],
        'exercise': ['stress_management'],
    };
    
    // Try to find a matching dataset based on keywords
    for (let keyword in keywordMap) {
        if (lower.includes(keyword)) {
            let datasetNames = keywordMap[keyword];
            
            for (let datasetName of datasetNames) {
                if (allDatasets[datasetName]) {
                    const content = allDatasets[datasetName];
                    
                    // Split into sections and find one with the keyword
                    const sections = content.split(/\n\s*\n+/);
                    for (let section of sections) {
                        if (section.toLowerCase().includes(keyword) && section.length > 50) {
                            const cleaned = section.trim().replace(/\n+/g, ' ').substring(0, 400);
                            const displayName = datasetName.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
                            return `[From ${displayName}]\n\n${cleaned}${cleaned.length === 400 ? '...' : ''}`;
                        }
                    }
                }
            }
        }
    }
    
    return null;
}

function getResponse(message) {
    const lower = message.toLowerCase();
    
    // Check for crisis keywords first
    if (lower.includes("suicide") || lower.includes("kill myself") || lower.includes("end my life") || lower.includes("want to die")) {
        return demoResponses.suicide[Math.floor(Math.random() * demoResponses.suicide.length)];
    }
    
    // Search datasets first for relevant information
    const datasetResponse = searchDatasets(message);
    if (datasetResponse) {
        console.log(`Dataset matched for: ${message.substring(0, 30)}...`);
        return datasetResponse;
    }
    
    // Fallback to demo responses
    if (lower.includes("depressed") || lower.includes("depression")) {
        return demoResponses.depression[Math.floor(Math.random() * demoResponses.depression.length)];
    }
    
    if (lower.includes("anxiety") || lower.includes("panic")) {
        return demoResponses.anxiety[Math.floor(Math.random() * demoResponses.anxiety.length)];
    }
    
    return demoResponses.default[Math.floor(Math.random() * demoResponses.default.length)];
}

function sendMessage() {
    const input = document.getElementById("chatInput");
    const message = input.value.trim();
    if (message === "") return;
    
    appendMessage("user", message);
    updateChatTitle();
    input.value = "";

    // Simulate thinking time and always reply for the current message
    setTimeout(() => {
        const botResponse = getResponse(message);
        appendMessage("bot", botResponse);

        // Increment after responding and then optionally show login prompt for guests
        messageCount++;
        if (messageCount >= 3 && userData && !userData.isLoggedIn) {
            // show prompt a moment after the bot reply
            setTimeout(() => {
                showLoginPrompt();
            }, 800);
        }
    }, 600);
}

function showLoginPrompt() {
    const chatBox = document.getElementById('chatBox');
    
    const promptDiv = document.createElement('div');
    promptDiv.className = 'message bot';
    promptDiv.innerHTML = `
        <strong>bot:</strong> 
        <div style="margin-top: 10px;">
            To continue and save your progress, please sign in with your name.
            <div style="margin-top: 10px; display: flex; gap: 10px;">
                <button onclick="goToLogin()" style="padding: 8px 16px; background: #2d5a5a; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Sign In</button>
                <button onclick="skipLogin()" style="padding: 8px 16px; background: #999; color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold;">Continue as Guest</button>
            </div>
        </div>
    `;
    chatBox.appendChild(promptDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function goToLogin() {
    localStorage.removeItem('userData');
    window.location.href = 'login.html';
}

function skipLogin() {
    const response = "Great! You can continue chatting. Sign in anytime to save your progress and personalize your experience.";
    appendMessage("bot", response);
}

function logout() {
    if (confirm('Are you sure you want to logout?')) {
        localStorage.removeItem('userData');
        window.location.href = 'login.html';
    }
}
