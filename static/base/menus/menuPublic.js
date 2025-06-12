// 菜单默认选中设置
const sMenuItemList = document.getElementsByTagName("s-menu-item");

function MenuItemSelection(labelId) {
  for (let i = 0; i < sMenuItemList.length; i++) {
    sMenuItemList[i].setAttribute("checked", "false");
  }
  document.getElementById(labelId).setAttribute("checked", "true");
}

// 菜单设置点击事件
function createMenuItem(labelId, url) {
  const el = document.getElementById(labelId);
  if (!el) return;
  el.style.cursor = "pointer"; // 鼠标样式手型提示
  el.addEventListener("click", () => {
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
    }, 200);
  });
}

// 菜单默认选中
function autoSelectMenu() {
  const MenuID = localStorage.getItem("selectionMenu");
  if (MenuID) {
    MenuItemSelection(MenuID);
  }
}
// 跟路由跳转，默认菜单选中
document.addEventListener("DOMContentLoaded", function () {
  // 如果 localStorage 没有选中项，且当前url是 "/dashboard/workbenches"
  if (
    !localStorage.getItem("selectionMenu") !== "interfaceSidebarWork" &&
    window.location.pathname === "/dashboard/workbenches"
  ) {
    localStorage.setItem("selectionMenu", "interfaceSidebarWork");
  }
  autoSelectMenu(); // 触发选中函数
});

window.createMenuItem = createMenuItem;
window.autoSelectMenu = autoSelectMenu;
