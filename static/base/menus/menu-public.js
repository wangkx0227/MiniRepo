function createMenuItem(menuItemId, url) {
    const el = document.getElementById(menuItemId);
    if (!el) return;
    el.style.cursor = "pointer"; // 鼠标样式手型提示
    el.addEventListener("click", () => {
        window.location.href = url;
    });
}

window.createMenuItem = createMenuItem