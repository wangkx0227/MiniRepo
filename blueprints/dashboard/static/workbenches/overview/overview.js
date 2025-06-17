/**
 * 生成模拟贡献数据：返回一个对象 { '2025-05-01': 1, ... }
 * 你可以用后台接口数据替换此处
 */
// 假数据
function generateData() {
    const data = {};
    const today = new Date();
    for (let i = 0; i < 364; i++) {
        const d = new Date(today);
        d.setDate(today.getDate() - i);
        const dateStr = d.toISOString().slice(0, 10);
        data[dateStr] = Math.random() < 0.8 ? Math.floor(Math.random() * 5) : 0;
    }
    return data;
}

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

// 热力图-根据后端数据,区分每天的颜色
function getColorLevel(count) {
    if (count === 0) return '';
    if (count < 2) return 'level-1';
    if (count < 4) return 'level-2';
    if (count < 7) return 'level-3';
    return 'level-4';
}

// 热力图-数据渲染
function drawCalendar(data) {
    const calendar = document.getElementById('calendar');
    const months = document.getElementById('months');
    calendar.innerHTML = '';
    months.innerHTML = '';

    // 计算开始日期（向前推364天，补齐到周日）
    const today = new Date();
    let start = new Date(today);
    start.setDate(today.getDate() - 364);
    while (start.getDay() !== 0) start.setDate(start.getDate() - 1);

    // 生成每一列（每周），每列放7天
    let monthLabels = []; // 月列表
    let lastMonth = null;
    for (let week = 0; week < 53; week++) {
        const weekColumn = document.createElement('div');
        weekColumn.className = 'week';
        let hasMonthLabel = false;
        for (let day = 0; day < 7; day++) {
            const d = new Date(start);
            d.setDate(start.getDate() + week * 7 + day);
            const dateStr = d.toISOString().slice(0, 10);
            const count = data[dateStr] || 0;
            const dayBox = document.createElement('div');
            dayBox.className = 'day ' + getColorLevel(count);
            dayBox.title = `${dateStr}: ${count} 次贡献`;
            dayBox.dataset.date = dateStr;
            dayBox.dataset.count = count;
            weekColumn.appendChild(dayBox);

            // 只在本周第一个格子且是1号时，显示月份
            if (day === 0) {
                const curMonth = d.getMonth();
                if (curMonth !== lastMonth) {
                    hasMonthLabel = true;
                    lastMonth = curMonth;
                }
            }
        }
        calendar.appendChild(weekColumn);
        // 记录月份名或空字符串
        if (hasMonthLabel) {
            const d = new Date(start);
            d.setDate(start.getDate() + week * 7);
            monthLabels.push(`${d.getMonth() + 1}月`);
        }
    }
    // 渲染月份
    for (let i = 0; i < monthLabels.length; i++) {
        const monthDiv = document.createElement('div');
        monthDiv.className = 'month-label';
        monthDiv.innerHTML = monthLabels[i] ? monthLabels[i] : '&nbsp;';
        months.appendChild(monthDiv);
    }
}

// 初始化
const data = generateData();
drawWeekdays();
drawCalendar(data);