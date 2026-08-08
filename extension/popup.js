document.getElementById("predict").addEventListener("click", async () => {

    const text = document.getElementById("text").value;

    if(text===""){

        alert("Please enter a comment.");

        return;

    }

    const response = await fetch("http://127.0.0.1:5000/predict",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            text:text

        })

    });

    const result = await response.json();

    document.getElementById("result").innerHTML =

    `
    <h3>${result.prediction}</h3>

    Confidence: ${result.confidence}%
    `;

});