// 搜索框
const SearchInput = document.getElementById("SearchInput");
const clearBtn = document.getElementById("clearBtn");
// 清除框
clearBtn.addEventListener("click", () => {
    // 如果是标准 Web Component，最好设置属性和属性同步
    SearchInput.value = "";
});
// 回车进行搜索
SearchInput.addEventListener("keydown", () => {
    if (event.key === "Enter") {
        // Snackbar.builder('hello world')
        alert(SearchInput.value);
    }
});

// 下拉框
const repositoryTypeSelect = document.getElementById("repositoryTypeSelect");
repositoryTypeSelect.addEventListener("change", function () {
    const repositoryType = this.value;
    console.log(repositoryType)

})


sober.Snackbar.align = "top";
console.log(sober.Snackbar.arguments)
console.log(sober.Snackbar.prototype)
sober.Snackbar.builder("111")
