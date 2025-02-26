document.addEventListener("DOMContentLoaded", function () {
    document.querySelector(".log-in-button").addEventListener("click", async function (event) {
        event.preventDefault();

        const usernameOrEmail = document.getElementById("usernameOrEmail").value.trim();
        const password = document.getElementById("password").value.trim();

        if (!usernameOrEmail || !password) {
            alert("Please enter your username/email and password!");
            return;
        }

        try {
            const response = await fetch("https://lakshya507-instagram-clone-with-backend.onrender.com/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ usernameOrEmail, password }),
            });

            const data = await response.json();

            if (response.ok) {
                alert("Login successful!");
                window.location.href = data.redirect;
            } else {
                alert(data.message);
            }
        } catch (error) {
            console.error("Login Error:", error);
            alert("Something went wrong. Please try again later.");
        }
    });

    document.getElementById("signUpLink").addEventListener("click", async function (event) {
        event.preventDefault();

        const usernameOrEmail = prompt("Enter your email or username:");
        if (!usernameOrEmail) return alert("Username/email cannot be empty!");

        const password = prompt("Enter a password:");
        if (!password) return alert("Password cannot be empty!");

        try {
            const response = await fetch("http://localhost:5000/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ usernameOrEmail, password }),
            });

            const data = await response.json();

            if (response.ok) {
                alert("Account created successfully!");
                window.location.href = data.redirect;
            } else {
                alert(data.message);
            }
        } catch (error) {
            console.error("Signup Error:", error);
            alert("Something went wrong. Please try again later.");
        }
    });
});
