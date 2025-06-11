// 菜单默认选中设置
const sMenuItemList = document.getElementsByTagName("s-menu-item")

function MenuItemSelection(menuItemId) {
    for (let i = 0; i < sMenuItemList.length; i++) {
        sMenuItemList[i].setAttribute("checked", "false");
        // 如果存在二级菜单，当前属性时默认展开作用，每次需要进行重置
        sMenuItemList[i].setAttribute("folded", "true");
    }
    document.getElementById(menuItemId).setAttribute("checked", "true");
}


// 菜单设置点击事件
function createMenuItem(menuItemId, url) {
    const el = document.getElementById(menuItemId);
    if (!el) return;
    el.style.cursor = "pointer"; // 鼠标样式手型提示
    el.addEventListener("click", () => {
        localStorage.setItem("selection_menu", menuItemId);
        // 等待菜单按钮动画效果结束后执行跳转
        setTimeout(() => {
            // 执行页面跳转
            window.location.href = url;
        }, 200);
    });
}


window.createMenuItem = createMenuItem
window.MenuItemSelection = MenuItemSelection