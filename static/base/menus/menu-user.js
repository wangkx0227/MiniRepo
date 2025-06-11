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
