// 菜单函数
function createMenuItem(menuItemId, url) {
  const el = document.getElementById(menuItemId);
  if (!el) return;
  el.style.cursor = "pointer"; // 鼠标样式手型提示
  el.addEventListener("click", () => {
    window.location.href = url;
  });
}
// 菜单字典
const menuUMap = {
  HeadIndex: "/",
  menuUTodos: "/u/todos",
  menuURelated: "/u/related",
  menuUSetting: "/u/setting",
  menuUStars: "/u/stars",
  menuUHome: "/u/home",
  menuURepos: "/u/repos",
};
// 循环生成或者说赋值点击函数
for (const [id, url] of Object.entries(menuUMap)) {
  createMenuItem(id, url);
}
