// 进度条
NProgress.configure({ showSpinner: false, trickleSpeed: 200 });

// 搜索框
const SearchInput = document.getElementById("SearchInput");
const clearBtn = document.getElementById("clearBtn");
// 清除框
clearBtn.addEventListener("click", () => {
  // 如果是标准 Web Component，最好设置属性和属性同步
  SearchInput.value = "";
});
// 回车进行搜索
SearchInput.addEventListener("keydown", () => {
  if (event.key === "Enter") {
    // Snackbar.builder('hello world')
    alert(SearchInput.value);
  }
});

// 侧边栏控制
const Drawer = document.querySelector("#drawer"); // 抽屉
const DrawerTriggerBut = document.getElementById("DrawerTriggerBut"); // 侧边栏按钮
localStorage.setItem("interface_menu", "show"); // 初始化页面侧边栏展示状态
const InterfaceMenuTip = document.getElementById("interface_menu_tip"); // 侧边栏提示
// 侧边栏-按钮 Drawer.toggle();
DrawerTriggerBut.addEventListener("click", () => {
  Drawer.toggle();
  const interface_menu = localStorage.getItem("interface_menu");
  if (interface_menu === "hide") {
    InterfaceMenuTip.innerText = "隐藏侧边栏";
    localStorage.setItem("interface_menu", "show");
  } else {
    InterfaceMenuTip.innerText = "展开侧边栏";
    localStorage.setItem("interface_menu", "hide");
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

