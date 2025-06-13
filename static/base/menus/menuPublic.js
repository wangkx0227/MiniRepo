// 菜单设置点击事件
function createMenuItem(labelId, url, saveToLocal) {
    const el = document.getElementById(labelId);
    if (!el) return;
    el.style.cursor = "pointer"; // 鼠标样式手型提示
    el.addEventListener("click", () => {
        // 默认工作台-tab选中属性
        if (saveToLocal) {
            localStorage.setItem("selectionWorkbenchesTab", labelId)
        }
        // 菜单默认选中
        if (labelId === "HeadIndexTile") {
            localStorage.setItem("selectionMenu", "interfaceSidebarWork");
        } else {
            localStorage.setItem("selectionMenu", labelId);
        }
        // 等待菜单按钮动画效果结束后执行跳转
        setTimeout(() => {
            // 执行页面跳转
            window.location.href = url;
        }, 300);
    });
}


// 侧边栏菜单默认选中
function autoSelectMenu() {
    const MenuID = localStorage.getItem("selectionMenu");
    if (MenuID) {
        const sMenuItemList = document.getElementsByTagName("s-menu-item");
        for (let i = 0; i < sMenuItemList.length; i++) {
            sMenuItemList[i].setAttribute("checked", "false");
        }
        document.getElementById(MenuID).setAttribute("checked", "true");
    }
}

// 当访问 / 路由是进行跳转，默认菜单选中
document.addEventListener("DOMContentLoaded", function () {
    // 如果 localStorage 没有选中项，且当前url是 "/dashboard/workbenches"
    if (localStorage.getItem("selectionMenu") !== "interfaceSidebarWork" &&
        window.location.pathname === "/dashboard/workbenches"
    ) {
        localStorage.setItem("selectionMenu", "interfaceSidebarWork");
    }
    autoSelectMenu(); // 触发选中函数
});

window.createMenuItem = createMenuItem;
window.autoSelectMenu = autoSelectMenu;
