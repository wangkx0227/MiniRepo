// 菜单默认选择设置
function MenuItemSelection(menuItemId) {
    const s_menu_item = document.getElementsByTagName("s-menu-item")
    for (let i = 0; i < s_menu_item.length; i++) {
        s_menu_item[i].setAttribute("checked", "false")
    }
    document.getElementById(menuItemId).setAttribute("checked", "true")
}


// 菜单设置点击事件
function createMenuItem(menuItemId, url) {
    const el = document.getElementById(menuItemId);
    if (!el) return;
    el.style.cursor = "pointer"; // 鼠标样式手型提示
    el.addEventListener("click", () => {
        window.location.href = url;
        localStorage.setItem("selection_menu", menuItemId)
    });
}


window.createMenuItem = createMenuItem
window.MenuItemSelection = MenuItemSelection