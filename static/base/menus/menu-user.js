// 菜单字典
const menuUMap = {
  HeadIndexTile: "/dashboard/workbenches",
  menuUTodos: "/user/todos",
  menuURelated: "/user/related",
  menuUSetting: "/user/setting",
  menuUStars: "/user/stars",
  menuUHome: "/user/home",
  menuURepos: "/user/repos",
};
// 循环生成或者说赋值点击函数
for (const [id, url] of Object.entries(menuUMap)) {
  createMenuItem(id, url);
}
