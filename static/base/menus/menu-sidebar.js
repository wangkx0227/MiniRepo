// 侧边栏url
const menuSidebarMap = {
    interfaceSidebarWork: "/dashboard/workbenches",
    interfaceSidebarProjects: "/dashboard/projects",
    interfaceSidebarGroups: "/dashboard/groups",
    interfaceSidebarMergeRequests: "/dashboard/merge_requests",
    interfaceSidebarTodos: "/dashboard/todos",
    interfaceSidebarUserSetting: "/dashboard/setting/user_setting",
    interfaceSidebarSecuredSetting: "/dashboard/setting/secured_setting",
};
// 循环生成或者说赋值点击函数
for (const [id, url] of Object.entries(menuSidebarMap)) {
    createMenuItem(id, url);
}

