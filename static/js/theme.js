document.addEventListener("DOMContentLoaded", () => {

    const body = document.body;
    const themeBtn = document.getElementById("theme-toggle");

    // Load saved theme
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        body.classList.remove("light-theme");
        body.classList.add("dark-theme");

        if (themeBtn) {
            themeBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
        }
    } else {
        body.classList.remove("dark-theme");
        body.classList.add("light-theme");

        if (themeBtn) {
            themeBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
        }
    }

    // Toggle Theme
    if (themeBtn) {

        themeBtn.addEventListener("click", () => {

            body.classList.toggle("dark-theme");
            body.classList.toggle("light-theme");

            if (body.classList.contains("dark-theme")) {

                localStorage.setItem("theme", "dark");

                themeBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';

            } else {

                localStorage.setItem("theme", "light");

                themeBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';

            }

        });

    }

});

/* ================= PAGE TITLE ================= */

const pageTitle = document.getElementById("pageTitle");

if (pageTitle) {

    const path = window.location.pathname;

    const titles = {

        "/dashboard": "Dashboard",

        "/profile": "My Profile",

        "/skills": "Manage Skills",

        "/matches": "Matches",

        "/requests": "Requests",

        "/sessions": "Sessions",

        "/reviews": "Reviews",

        "/weekly_report": "Weekly Report"

    };

    pageTitle.textContent = titles[path] || "SkillConnect";

}