function showToast(message) {

    const toast = document.createElement("div");

    toast.textContent = message;

    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.background = "#28a745";
    toast.style.color = "#fff";
    toast.style.padding = "12px 18px";
    toast.style.borderRadius = "8px";
    toast.style.fontSize = "14px";
    toast.style.fontWeight = "bold";
    toast.style.zIndex = "999999";
    toast.style.boxShadow = "0 2px 10px rgba(0,0,0,0.3)";

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 2500);
}
let isUpdatingComment = false;
console.log("✅ HaTiSo Extension Loaded");

// =====================================================
// Create Floating HaTiSo Panel
// =====================================================
function createHaTiSoPanel() {

    if (document.getElementById("hatiso-ai-panel")) return;

    const panel = document.createElement("div");
    panel.id = "hatiso-ai-panel";

    panel.innerHTML = `
        <span id="hatiso-close">✕</span>

        <h2>🛡 HaTiSo AI</h2>

        <div class="hatiso-section">
            <div class="hatiso-label">Prediction</div>
            <div id="prediction" class="hatiso-result">
                Waiting for comment...
            </div>
        </div>

        <div class="hatiso-section">
            <div class="hatiso-label">Confidence</div>
            <div id="confidence" class="hatiso-result">
                --
            </div>
        </div>

        <div class="hatiso-section">
            <div class="hatiso-label">Explanation</div>
            <div id="explanation" class="hatiso-result">
                --
            </div>
        </div>

        <div class="hatiso-section">

            <div class="hatiso-label">
                Suggested Comment
            </div>

            <div id="suggestion" class="hatiso-result">
                Waiting...
            </div>

            <button id="useSuggestion" class="hatiso-btn">
                ✓ Use Suggestion
            </button>

            <button id="keepOriginal" class="hatiso-btn secondary">
                Keep Original
            </button>

        </div>
    `;

    document.body.appendChild(panel);

    // Close panel
    document.getElementById("hatiso-close").onclick = function () {
        panel.remove();
    };

    // ==========================================
    // Use Suggestion
    // ==========================================
   document.getElementById("useSuggestion").onclick = function () {

    if (!currentCommentBox) {
        alert("No comment box selected.");
        return;
    }

    const suggestion = document
        .getElementById("suggestion")
        .textContent
        .trim();

    // Prevent the next input event from triggering analysis
    isUpdatingComment = true;

    currentCommentBox.focus();

        const span = currentCommentBox.querySelector(
        'span[data-lexical-text="true"]'
    );

    if (span) {
        span.textContent = suggestion;
    } else {
        currentCommentBox.textContent = suggestion;
    }

    currentCommentBox.dispatchEvent(
        new InputEvent("input", {
            bubbles: true
        })
    );
    // Trigger Facebook's input handling
    currentCommentBox.dispatchEvent(
        new Event("input", { bubbles: true })
    );

    this.innerHTML = "✔ Suggestion Applied";
    this.disabled = true;

    showToast("✅ Suggestion applied successfully!");
};

    // ==========================================
    // Keep Original
    // ==========================================
    document.getElementById("keepOriginal").onclick = function () {

        console.log("User kept original comment.");
        
       const  btn = document.getElementById("useSuggestion");
        btn.disabled = false;

    };

}

createHaTiSoPanel();


// =====================================================
// Send Text to Flask
// =====================================================
async function analyzeText(text) {

    console.log("📤 Sending:", text);

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    text: text
                })
            }
        );

        if (!response.ok) {
            throw new Error("Server Error");
        }

        const result = await response.json();

        console.log("Suggestion From Flask:", result.suggestion);

        console.log("✅ API Result:", result);

        showResult(result);

    }
    catch (error) {

        console.error("❌ Fetch Error:", error);

    }

}


// =====================================================
// Update Panel
// =====================================================
function showResult(result) {

    // Reset button every new prediction
    const btn = document.getElementById("useSuggestion");

    btn.innerHTML = "✓ Use Suggestion";
    btn.disabled = false;

    // Prediction
    document.getElementById("prediction").textContent =
        result.prediction || "--";

    // Confidence
    document.getElementById("confidence").textContent =
        (result.confidence ?? "--") + "%";

    // Explanation
    if (result.explanation && result.explanation.length > 0) {

        const explanation = result.explanation
            .map(item => item.word)
            .join(", ");

        document.getElementById("explanation").textContent =
            explanation;

    } else {

        document.getElementById("explanation").textContent =
            "No explanation";

    }

    // Suggestion
    document.getElementById("suggestion").textContent =
        result.suggestion || "No suggestion available";

}


// =====================================================
// Detect Facebook Comment Boxes
// =====================================================
function attachBoxes() {

    const boxes = document.querySelectorAll(
        '[contenteditable="true"]'
    );

    boxes.forEach((box) => {

        if (box.dataset.hatisoAttached) return;

        box.dataset.hatisoAttached = "true";

        let timeout;

        box.addEventListener("input", () => {

            // Ignore the input event caused by applying our own suggestion
            if (isUpdatingComment) {
                isUpdatingComment = false;
                return;
            }

            clearTimeout(timeout);

            timeout = setTimeout(() => {

                currentCommentBox = box;

                const text = box.innerText.trim();

                if (text.length > 2) {

                    analyzeText(text);

                }

            }, 800);

        });

    });

}

setInterval(attachBoxes, 1000);