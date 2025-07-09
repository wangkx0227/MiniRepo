// 路由
// const username = "{{ username }}";  // 来自 Flask 注入
const username = "wkx0227";  // 来自 Flask 注入
const menuRouteMap = [
    // 用户头像，点击下来框的路由设置
    {labelId: "u-stars", url: `/${username}/stars`, }, // 关注
    {labelId: "u-home", url: `/${username}/home`, },  // 主页
    {labelId: "u-repository", url: `/${username}/repository`}, // 仓库
    {labelId: "u-setting", url: `/${username}/setting` }, // 个人设置
    {labelId: "u-organization", url: `/${username}/organization` }, // 个人设置
    // {labelId: "u-login", url: `/u/repos`}, // 需要再进行确认怎么设置
    // 新建的下拉框路由设置
    {labelId: "n-projects", url: "/n/projects", },  // 新建项目
    {labelId: "n-groups", url: "/n/groups"}, // 新建群组
    {labelId: "n-snippets", url: "/n/snippets", }, // 新建代码片段
];

// 菜单设置点击事件
function createMenuItem(labelId, url) {
    const el = document.getElementById(labelId);
    if (!el) return;
    el.href = url;
    // el.addEventListener("click", () => {
    //     // 等待菜单按钮动画效果结束后执行跳转
    //     setTimeout(() => {
    //         // 执行页面跳转
    //         window.location.href = url;
    //     }, 350);
    // });
}



window.createMenuItem = createMenuItem;


// 循环生成或者说赋值点击函数
(function () {
    for (const item of menuRouteMap) {
        if (window.createMenuItem) {
            window.createMenuItem(item.labelId, item.url);
        }
    }
})();
