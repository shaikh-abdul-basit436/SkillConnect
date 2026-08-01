document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.getElementById("sidebar");
    const menuBtn = document.getElementById("menu-btn");
    const body = document.body;

    // ===========================
    // Sidebar
    // ===========================

    if (menuBtn) {

        menuBtn.addEventListener("click", () => {

            sidebar.classList.toggle("collapsed");

            body.classList.toggle("sidebar-collapsed");

        });

    }

    // ===========================
    // Theme
    // ===========================

    const themeBtn = document.getElementById("theme-toggle");
    const icon = document.getElementById("theme-icon");

    function setTheme(mode){

        if(mode==="dark"){

            body.classList.remove("light-theme");
            body.classList.add("dark-theme");

            if(icon)
                icon.className="fa-solid fa-sun";

        }else{

            body.classList.remove("dark-theme");
            body.classList.add("light-theme");

            if(icon)
                icon.className="fa-solid fa-moon";

        }

        localStorage.setItem("theme",mode);

    }

    const savedTheme = localStorage.getItem("theme") || "light";

    setTheme(savedTheme);

    if(themeBtn){

        themeBtn.addEventListener("click",()=>{

            if(body.classList.contains("dark-theme")){

                setTheme("light");

            }else{

                setTheme("dark");

            }

        });

    }

});