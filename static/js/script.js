document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM Loaded!");

  const container = document.querySelector(".container");
  const registerBtn = document.querySelector(".register-btn");
  const loginBtn = document.querySelector(".login-btn");

  console.log(container, registerBtn, loginBtn); // Check if elements exist

  if (!container || !registerBtn || !loginBtn) {
    console.error("One or more elements are missing!");
    return;
  }

  registerBtn.addEventListener("click", () => {
    container.classList.add("active");
    console.log("Register button clicked");
  });

  loginBtn.addEventListener("click", () => {
    container.classList.remove("active");
    console.log("Login button clicked");
  });
});
