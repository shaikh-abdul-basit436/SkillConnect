document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.getElementById("sidebar");
    const menuBtn = document.getElementById("menu-btn");

    if (!sidebar || !menuBtn) return;

    // Restore previous sidebar state
    if (localStorage.getItem("sidebar") === "collapsed") {
        sidebar.classList.add("collapsed");
        document.body.classList.add("sidebar-collapsed");
    }

    // Toggle Sidebar
    menuBtn.addEventListener("click", () => {

        sidebar.classList.toggle("collapsed");
        document.body.classList.toggle("sidebar-collapsed");

        if (sidebar.classList.contains("collapsed")) {
            localStorage.setItem("sidebar", "collapsed");
        } else {
            localStorage.setItem("sidebar", "expanded");
        }

    });

});