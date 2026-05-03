async function checkPassword() {
    const password = document.getElementById("password").value;

    const response = await fetch("/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ password })
    });

    const data = await response.json();

    document.getElementById("strength").textContent = data.strength;
    document.getElementById("strength").style.color = data.color;

    document.getElementById("score").textContent = `Score: ${data.score}%`;
    document.getElementById("entropy").textContent = `Entropy: ${data.entropy} bits`;

    const progress = document.getElementById("progress");
    progress.style.width = `${data.score}%`;
    progress.style.background = data.color;

    const feedbackList = document.getElementById("feedback");
    feedbackList.innerHTML = "";

    data.feedback.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        feedbackList.appendChild(li);
    });
}

function togglePassword() {
    const passwordInput = document.getElementById("password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}