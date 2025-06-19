/**
 * 生成模拟贡献数据：返回一个对象 { '2025-05-01': 1, ... }
 * 你可以用后台接口数据替换此处
 */


// 根据已知的年获取当前的最后一天
function getLastDayOfYear(yearStr) {
    // 1. 生成下一年一月一日
    const nextYear = Number(yearStr) + 1;
    const firstDayNextYear = new Date(`${nextYear}-01-01`);
    // 2. 上一年最后一天就是减一天
    firstDayNextYear.setDate(firstDayNextYear.getDate() - 1);
    return firstDayNextYear; // Date对象
}


// 热力图-根据后端数据,区分每天的颜色
function getColorLevel(count) {
    if (count === 0) return '';
    if (count < 2) return 'level-1';
    if (count < 4) return 'level-2';
    if (count < 7) return 'level-3';
    return 'level-4';
}


// 热力图-数据渲染
function drawCalendar(data, selectYear) {
    const calendar = document.getElementById('calendar');
    const months = document.getElementById('months');
    calendar.innerHTML = '';
    months.innerHTML = '';

    // 1. 计算开始和结束日期
    let today = new Date();
    if (selectYear) {
        const year = new Date().getFullYear();
        if (selectYear !== year.toString()) {
            today = getLastDayOfYear(selectYear);
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
            dayBox.className = 'day ' + getColorLevel(count);
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


// 贡献度-日期选择框事项
document.getElementById('contribute-year-select').addEventListener('change', function () {
    const year = this.value;
    fetch(`/dashboard/user/contribution_data?year=${year}`)
        .then(res => res.json())
        .then(data => {
            let selectYear = year
            drawCalendar(data, selectYear); // 热力图数据
            // renderActivityList(data.activities); // 动态列表数据
        });
});

// 动态-加载更多按钮
const TimeLineLoadMore = document.getElementById("TimeLineLoadMore")
TimeLineLoadMore.addEventListener("click", () => {
    TimeLineLoadMore.innerHTML = `<s-circular-progress indeterminate="true" slot="start"></s-circular-progress>`

    setTimeout(() => {
        TimeLineLoadMore.innerText = "加载更多"
    }, 2000)
})


// 页面初始化加载贡献图
document.addEventListener('DOMContentLoaded', function () {
    drawCalendar({"2025-06-15": 10});
});