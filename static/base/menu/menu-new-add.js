// 新增字典
const menuAddMap = {
    menuAddProjects: "/u/projects/new",
    menuAddOrganizations: "/u/organizations/new",
    menuAddCodes: "/u/codes/new",
};
// 循环生成或者说赋值点击函数
for (const [id, url] of Object.entries(menuAddMap)) {
    createMenuItem(id, url);
}
