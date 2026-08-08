async function analyzeComment() {

    const text = document.getElementById("comment").value.trim();

    if (text === "") {
        alert("Please enter a comment.");
        return;
    }

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text
            })
        });

        const result = await response.json();

        let color = "#42B72A";

        if (result.prediction === "Offensive Language")
            color = "#F39C12";

        if (result.prediction === "Hate Speech")
            color = "#E74C3C";

        let explanationHTML = "";

        if (result.explanation && result.explanation.length > 0) {

            explanationHTML = `
                <h4>🧠 AI Explanation (LIME)</h4>
                <ul>
            `;

            result.explanation.forEach(item => {

                explanationHTML += `
                    <li>
                        <strong>${item.word}</strong>
                        : ${item.weight}
                    </li>
                `;

            });

            explanationHTML += "</ul>";
        }

        document.getElementById("postResult").innerHTML = `

        <div class="facebookPost">

            <div class="profile">

                👤 Hannah

            </div>

            <div class="content">

                ${text}

            </div>

            <div class="aiResult"
                 style="background:${color};">

                <h3>

                ${result.prediction}

                </h3>

                <p>

                Confidence:
                ${result.confidence}%

                </p>

                ${explanationHTML}

            </div>

        </div>

        `;

    }

    catch(err){

        console.error(err);

        alert(err);

    }

}