// 路由
const menuRouteMap = [
    // 点击网站名称是，跳转
    {labelId: "HeadIndexTile", url: "/dashboard/workbenches?tab=overview", saveToLocal: false},
    // 用户下来框菜单地址
    {labelId: "menuUTodos", url: "/user/todos", saveToLocal: false},
    {labelId: "menuURelated", url: "/user/related", saveToLocal: false},
    {labelId: "menuUSetting", url: "/user/setting", saveToLocal: false},
    {labelId: "menuUStars", url: "/user/stars", saveToLocal: false},
    {labelId: "menuUHome", url: "/user/home", saveToLocal: false},
    {labelId: "menuURepos", url: "/user/repos", saveToLocal: false},
    // 侧边栏菜单地址
    {labelId: "interfaceSidebarWorkbenches", url: "/dashboard/workbenches?tab=overview", saveToLocal: false},
    {labelId: "interfaceSidebarProjects", url: "/dashboard/projects", saveToLocal: false},
    {labelId: "interfaceSidebarGroups", url: "/dashboard/groups", saveToLocal: false},
    {labelId: "interfaceSidebarMergeRequests", url: "/dashboard/merge_requests", saveToLocal: false},
    {labelId: "interfaceSidebarTodos", url: "/dashboard/todos", saveToLocal: false},
    {labelId: "interfaceSidebarUserSetting", url: "/dashboard/setting/user_setting", saveToLocal: false},
    {labelId: "interfaceSidebarSecuredSetting", url: "/dashboard/setting/secured_setting", saveToLocal: false},
    // 新建的菜单地址
    {labelId: "menuAddProjects", url: "/new/projects", saveToLocal: false},
    {labelId: "menuAddOrganizations", url: "/new/organizations", saveToLocal: false},
    {labelId: "menuAddCodes", url: "/new/codes", saveToLocal: false},
    // 工作台-4个tab切换的地址
    {labelId: "workbenches-overview", url: "?tab=overview", saveToLocal: true},
    {labelId: "workbenches-repository", url: "?tab=repository", saveToLocal: true},
    {labelId: "workbenches-analysis", url: "?tab=analysis", saveToLocal: true},
    {labelId: "workbenches-snippet", url: "?tab=snippet", saveToLocal: true},
];

// 循环生成或者说赋值点击函数
(function () {
    for (const item of menuRouteMap) {
        if (window.createMenuItem) {
            window.createMenuItem(item.labelId, item.url, item.saveToLocal);
        }
    }
})();
