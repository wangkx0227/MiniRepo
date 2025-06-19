/**
 * 生成模拟贡献数据：返回一个对象 { '2025-05-01': 1, ... }
 * 你可以用后台接口数据替换此处
 */


// 贡献图-根据年获取最后一天
function contributionGetLastDayOfYear(yearStr) {
    // 1. 生成下一年一月一日
    const nextYear = Number(yearStr) + 1;
    const firstDayNextYear = new Date(`${nextYear}-01-01`);
    // 2. 上一年最后一天就是减一天
    firstDayNextYear.setDate(firstDayNextYear.getDate() - 1);
    return firstDayNextYear; // Date对象
}


// 贡献图-级别
function contributionGrade(count) {
    if (count === 0) return '';
    if (count < 2) return 'level-1';
    if (count < 4) return 'level-2';
    if (count < 7) return 'level-3';
    return 'level-4';
}


// 贡献图-数据渲染
function contributionRendering(data, selectYear = null) {
    const calendar = document.getElementById('calendar');
    const months = document.getElementById('months');
    calendar.innerHTML = '';
    months.innerHTML = '';

    // 1. 计算开始和结束日期
    let today = new Date();
    if (selectYear) {
        const year = new Date().getFullYear();
        if (selectYear !== year.toString()) {
            today = contributionGetLastDayOfYear(selectYear);
        }
    }
    let endDate = new Date(today);
    let startDate = new Date(today);
    startDate.setFullYear(today.getFullYear() - 1);

    // 2. 让startDate对齐到周一（如果不是周一，前面补空格）
    // JS getDay()：0=周日，1=周一，...6=周六
    // 假设你的热力图第一列是周一
    let startDay = startDate.getDay();
    let leadingEmpty = (startDay + 6) % 7; // 让周一是第一格

    let current = new Date(startDate);

    let monthLabels = [];
    let lastMonth = -1;

    // 以列为单位循环
    while (current <= endDate || leadingEmpty > 0) {
        const weekColumn = document.createElement('div');
        weekColumn.className = 'week';
        let hasMonthLabel = false;

        for (let i = 0; i < 7; i++) {
            // 首周需要补空格
            if (leadingEmpty > 0) {
                const emptyBox = document.createElement('div');
                emptyBox.className = 'day ';
                emptyBox.style.visibility = "hidden";
                weekColumn.appendChild(emptyBox);
                leadingEmpty--;
                continue;
            }
            // 当前日期超出endDate，补空格
            if (current > endDate) {
                const emptyBox = document.createElement('div');
                emptyBox.className = 'day ';
                emptyBox.style.visibility = "hidden";
                weekColumn.appendChild(emptyBox);
                continue;
            }
            // 正常渲染
            const dateStr = current.toISOString().slice(0, 10);
            const count = data[dateStr] || 0;
            const dayBox = document.createElement('div');
            dayBox.className = 'day ' + contributionGrade(count);
            dayBox.title = `${dateStr}: ${count} 次贡献`;
            dayBox.dataset.date = dateStr;
            weekColumn.appendChild(dayBox);

            // 月份标签
            if (current.getMonth() !== lastMonth && current.getDate() === 1) {
                hasMonthLabel = true;
                lastMonth = current.getMonth();
            }
            // 日期+1
            current.setDate(current.getDate() + 1);
        }
        calendar.appendChild(weekColumn);

        // 记录月份名或空字符串
        if (hasMonthLabel) {
            monthLabels.push(`${lastMonth + 1}月`);
        } else {
            monthLabels.push('');
        }
    }

    // 渲染月份标签
    for (let i = 0; i < monthLabels.length; i++) {
        const monthDiv = document.createElement('div');
        monthDiv.className = 'month-label';
        monthDiv.innerHTML = monthLabels[i] ? monthLabels[i] : '&nbsp;';
        months.appendChild(monthDiv);
    }
}


// 动态 - 展开查看 与 收回 点击按钮事项
document.querySelectorAll('.toggle-btn').forEach(function (btn) {
    btn.onclick = function () {
        const liAll = this.parentElement.parentElement.querySelectorAll('li');
        if (this.classList.contains('show')) {
            liAll.forEach((li) => {
                if (li.classList.contains("time-line-item-hide")) {
                    li.classList.remove("time-line-item-hide")
                }
            })
            // 展开逻辑
            this.classList.remove('show');
            this.classList.add('hide');
            this.innerText = '收起';
            this.parentElement.querySelector('span').innerText = `已显示全部推送信息，`;
        } else if (this.classList.contains('hide')) {
            // 收起逻辑
            liAll.forEach((li, idx) => {
                if (li.contains(this)) return;
                if (idx > 1) li.classList.add('time-line-item-hide');
            })
            this.classList.remove('hide');
            this.classList.add('show');
            this.innerText = '展开查看';
            this.parentElement.querySelector('span').innerText = `已隐藏${liAll.length - 2}条推送信息，`;
        }
    }
});


// 贡献度-日期选择框事项
document.getElementById('contribute-year-select').addEventListener('change', function () {
    const year = this.value;
    fetch(`/dashboard/user/contribution_data?year=${year}`)
        .then(res => res.json())
        .then(data => {
            let selectYear = year
            contributionRendering(data, selectYear); // 热力图数据
            // renderActivityList(data.activities); // 动态列表数据
        });
});


// 动态区域-加载更多按钮
const TimeLineLoadMore = document.getElementById("TimeLineLoadMore")
TimeLineLoadMore.addEventListener("click", () => {
    TimeLineLoadMore.innerHTML = `<s-circular-progress indeterminate="true" slot="start"></s-circular-progress>`

    setTimeout(() => {
        TimeLineLoadMore.innerText = "加载更多"
    }, 2000)
})


// 页面初始化加载贡献图
document.addEventListener('DOMContentLoaded', function () {
    const contribute_data_dict = document.getElementById("contribute_data_dict").dataset.info;
    const contributeData = JSON.parse(contribute_data_dict);
    contributionRendering(contributeData);
});