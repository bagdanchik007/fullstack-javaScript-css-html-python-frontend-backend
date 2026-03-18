const signUpBtn = document.querySelector('.signUpBtn-link');
const signInBtn = document.querySelector('.signInBtn-link');
const wrapper = document.querySelector('.wrapper');

// Animation
signUpBtn.addEventListener('click', () => wrapper.classList.add('active'));
signInBtn.addEventListener('click', () => wrapper.classList.remove('active'));

// Login AJAX
const loginForm = document.getElementById("loginForm");
loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    const res = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    const msg = document.getElementById("loginMessage");
    msg.innerText = data.message;
});

// Register AJAX
const registerForm = document.getElementById("registerForm");
registerForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = registerForm.username.value;
    const email = registerForm.email.value;
    const password = registerForm.password.value;

    const res = await fetch("/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, email, password })
    });

    const data = await res.json();
    const msg = document.getElementById("registerMessage");
    msg.innerText = data.message;
});