// 路由
const menuRouteMap = [
  { labelId: "HeadIndexTile", url: "/dashboard/workbenches", labelName: "" }, // 需要修改
  { labelId: "menuUTodos", url: "/user/todos", labelName: "" },
  { labelId: "menuURelated", url: "/user/related", labelName: "" },
  { labelId: "menuUSetting", url: "/user/setting", labelName: "" },
  { labelId: "menuUStars", url: "/user/stars", labelName: "" },
  { labelId: "menuUHome", url: "/user/home", labelName: "" },
  { labelId: "menuURepos", url: "/user/repos", labelName: "" },
  { labelId: "interfaceSidebarWork", url: "/dashboard/workbenches", labelName: "" },
  { labelId: "interfaceSidebarProjects", url: "/dashboard/projects", labelName: "" },
  { labelId: "interfaceSidebarGroups", url: "/dashboard/groups", labelName: "" },
  { labelId: "interfaceSidebarMergeRequests", url: "/dashboard/merge_requests", labelName: "" },
  { labelId: "interfaceSidebarTodos", url: "/dashboard/todos", labelName: "" },
  { labelId: "interfaceSidebarUserSetting", url: "/dashboard/setting/user_setting", labelName: "" },
  { labelId: "interfaceSidebarSecuredSetting", url: "/dashboard/setting/secured_setting", labelName: "" },
  { labelId: "menuAddProjects", url: "/new/projects", labelName: "" },
  { labelId: "menuAddOrganizations", url: "/new/organizations", labelName: "" },
  { labelId: "menuAddCodes", url: "/new/codes", labelName: "" }
];

// 循环生成或者说赋值点击函数
(function () {
  for (const item of menuRouteMap) {
    if (window.createMenuItem) {
      window.createMenuItem(item.labelId, item.url);
    }
  }
})();
