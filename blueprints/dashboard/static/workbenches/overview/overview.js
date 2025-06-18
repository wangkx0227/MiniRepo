/**
 * 生成模拟贡献数据：返回一个对象 { '2025-05-01': 1, ... }
 * 你可以用后台接口数据替换此处
 */
// 热力图-星期展示
function drawWeekdays() {
    // 只显示“周一/三/五”示例
    const weekdays = ['周一', '周二', '周三', '周四', '周五', '周六', '周日'];
    const showIdx = [0, 3, 6]; // 只显示周一/四/日
    let html = '';
    for (let i = 0; i < 7; i++) {
        if (showIdx.includes(i)) {
            html += `<span >${weekdays[i]}</span>`;
        }
    }
    document.getElementById('weekdays').innerHTML = html;
}

drawWeekdays();

// 热力图-根据后端数据,区分每天的颜色
function getColorLevel(count) {
    if (count === 0) return '';
    if (count < 2) return 'level-1';
    if (count < 4) return 'level-2';
    if (count < 7) return 'level-3';
    return 'level-4';
}


// 根据已知的年获取当前的最后一天
function getLastDayOfYear(yearStr) {
    // 1. 生成下一年一月一日
    const nextYear = Number(yearStr) + 1;
    const firstDayNextYear = new Date(`${nextYear}-01-01`);
    // 2. 上一年最后一天就是减一天
    firstDayNextYear.setDate(firstDayNextYear.getDate() - 1);
    return firstDayNextYear; // Date对象
}

// 热力图-数据渲染
function drawCalendar(data, selectYear) {
    const calendar = document.getElementById('calendar');
    const months = document.getElementById('months');
    calendar.innerHTML = '';
    months.innerHTML = '';

    // 1.计算开始日期 - 结束日期
    let today = new Date();
    if (selectYear) {
        // 判断当前传递的年,如果是今年,那么从当天日期进行计算,如果不是那么从12-31号推算到上一年的12-31
        const year = new Date().getFullYear();
        if (selectYear !== year.toString()) {
            today = getLastDayOfYear(selectYear);
        }
    }
    let endDate = new Date(today); // 当天时间-结束日期
    const startDate = new Date(today); // 开始日期
    startDate.setFullYear(today.getFullYear() - 1);

    // 2.计算总天数
    const totalDays = Math.floor((endDate - startDate) / 86400000) + 1;
    // 3.计算周 开始日期是周几 - 结束日期是周几
    const startDayOfWeek = startDate.getDay(); // 0(周日),1(周一)...6(周六)

    const totalWeeks = Math.ceil((startDayOfWeek + totalDays) / 7);
    // 4. 渲染每一列（每周）
    let monthLabels = [];
    let lastMonth = -1;
    for (let week = 0; week < totalWeeks; week++) {
        const weekColumn = document.createElement('div');
        weekColumn.className = 'week';
        let hasMonthLabel = false;
        for (let day = 0; day < 7; day++) {
            // 当前格子的实际显示日期范围
            const dayOffset = week * 7 + day - startDayOfWeek; // 可能为负数
            const current = new Date(startDate);
            current.setDate(startDate.getDate() + dayOffset);
            // 只渲染在范围内的格子
            if (current >= startDate && current <= endDate) {
                const dateStr = current.toISOString().slice(0, 10);
                const count = data[dateStr] || 0;
                const dayBox = document.createElement('div');
                dayBox.className = 'day ' + getColorLevel(count);
                dayBox.title = `${dateStr}: ${count} 次贡献`;
                dayBox.dataset.date = dateStr;
                weekColumn.appendChild(dayBox);
            } else {
                // 在范围之外的只占位置不显示
                const emptyBox = document.createElement('div');
                emptyBox.className = 'day '
                emptyBox.style.visibility = "hidden"
                weekColumn.appendChild(emptyBox);
            }
            // 只有一周中,存在1号,并且 lastMonth 不等于 原赋值的月
            if (current.getMonth() !== lastMonth && current.getDate() === 1) {
                hasMonthLabel = true;
                lastMonth = current.getMonth();
            }
        }
        calendar.appendChild(weekColumn);
        // 记录月份名或空字符串
        if (hasMonthLabel) {
            monthLabels.push(`${lastMonth + 1}月`);
        } else {
            monthLabels.push('');
        }
        // 重置
        hasMonthLabel = false;
        lastMonth = -1
    }
    // 渲染月份标签
    for (let i = 0; i < monthLabels.length; i++) {
        const monthDiv = document.createElement('div');
        monthDiv.className = 'month-label';
        monthDiv.innerHTML = monthLabels[i] ? monthLabels[i] : '&nbsp;';
        months.appendChild(monthDiv);
    }

}

// drawCalendar(data);


// 假数据 函数
// function generateData() {
//     const data = {};
//     const today = new Date();
//     for (let i = 0; i < 364; i++) {
//         const d = new Date(today);
//         d.setDate(today.getDate() - i);
//         const dateStr = d.toISOString().slice(0, 10);
//         data[dateStr] = Math.random() < 0.8 ? Math.floor(Math.random() * 5) : 0;
//     }
//     return data;
// }