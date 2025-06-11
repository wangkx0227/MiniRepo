// 新增字典
const menuAddMap = {
    menuAddProjects: "/new/projects",
    menuAddOrganizations: "/new/organizations",
    menuAddCodes: "/new/codes",
};
// 循环生成或者说赋值点击函数
for (const [id, url] of Object.entries(menuAddMap)) {
    createMenuItem(id, url);
}
