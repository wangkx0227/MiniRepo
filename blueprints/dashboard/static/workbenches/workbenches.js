// 工作台路由-虽然与菜单路由类似,但是还是不同
const WorkbenchesRouteMap = [
    {labelId: "workbenches-overview", url: "/dashboard/workbenches/overview", labelName: ""},
    {labelId: "workbenches-repository", url: "/dashboard/workbenches/repository", labelName: ""},
    {labelId: "workbenches-analysis", url: "/dashboard/workbenches/analysis", labelName: ""},
    {labelId: "workbenches-fragment", url: "/dashboard/workbenches/fragment", labelName: ""},
];

function WorkbenchesTabItem(labelId, url) {
    const el = document.getElementById(labelId);
    if (!el) return;
    el.style.cursor = "pointer"; // 鼠标样式手型提示
    el.addEventListener("click", () => {
        // 等待菜单按钮动画效果结束后执行跳转
        localStorage.setItem("selectionWorkbenchesTab", labelId)
        setTimeout(() => {
            // 执行页面跳转
            window.location.href = url;
        }, 400);
    });
}

// 循环生成或者说赋值点击函数
(function () {
    for (const item of WorkbenchesRouteMap) {
        WorkbenchesTabItem(item.labelId, item.url);
        // tab默认选中
        const selectionWorkbenchesTab = localStorage.getItem("selectionWorkbenchesTab")
        let labelObject = document.getElementById(`${item.labelId}`)
        if (selectionWorkbenchesTab === item.labelId) {
            labelObject.setAttribute("selected", "true")
        } else {
            labelObject.setAttribute("selected", "false")
        }
    }
})();


