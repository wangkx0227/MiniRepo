// 进度条
NProgress.configure({ showSpinner: false, trickleSpeed: 200 });

// 侧边栏抽屉控制显示
const Drawer = document.querySelector("#drawer"); // 抽屉
const DrawerTriggerBut = document.getElementById("DrawerTriggerBut"); // 侧边栏按钮
localStorage.setItem("SidebarDisplayProperties", "show"); // 初始化页面侧边栏展示状态
const InterfaceMenuTip = document.getElementById("interface_menu_tip"); // 侧边栏提示
// 侧边栏-按钮 Drawer.toggle();
DrawerTriggerBut.addEventListener("click", () => {
  Drawer.toggle();
  const SidebarDisplayPropertiesStatus = localStorage.getItem(
    "SidebarDisplayProperties"
  );
  if (SidebarDisplayPropertiesStatus === "hide") {
    InterfaceMenuTip.innerText = "隐藏侧边栏";
    localStorage.setItem("SidebarDisplayProperties", "show");
  } else {
    InterfaceMenuTip.innerText = "展开侧边栏";
    localStorage.setItem("SidebarDisplayProperties", "hide");
  }
});

// NProgress加载函数-ajax异步时调用
function NProgressLongin() {
  NProgress.start(); // 开启加载
  return function () {
    // 返回关闭调用函数，当执行返回结果后结束加载
    NProgress.done();
  };
}
