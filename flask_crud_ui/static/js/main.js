const FASTAPI_BASE = "http://192.168.1.100:8000"; // Change to your FastAPI IP

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("loginForm");
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      const res = await fetch(`${FASTAPI_BASE}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      if (res.ok) {
        const data = await res.json();
        // Store JWT in sessionStorage
        fetch("/save_token", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ token: data.access_token }),
        }).then(() => {
          window.location.href = "/";
        });
      } else {
        document.getElementById("error").innerText = "Invalid credentials.";
      }
    });
  }
});
