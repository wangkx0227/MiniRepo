/**
 * 生成模拟贡献数据：返回一个对象 { '2025-05-01': 1, ... }
 * 你可以用后台接口数据替换此处
 */
const TimeLineLoadMore = document.getElementById("TimeLineLoadMore")
const contributeYearSelect = document.getElementById('contributeYearSelect')

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
            this.parentElement.querySelector('span').innerText = `已隐藏${liAll.length - 3}条推送信息，`; // liAll.length - 3 2个初始显示和1个展开查看按钮 3个li
        }
    }
});

// 贡献度-日期选择框事项 - 请求后端
contributeYearSelect.addEventListener('change', function () {
    const year = this.value;
    fetch(`/dashboard/api/annual_contribution_data?year=${year}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(res => res.json())
        .then(data => {
            let contributionData = data.data.contribution_data;
            contributionRendering(contributionData, year); // 热力图数据
            // renderActivityList(data.activities); // 动态列表数据
        });
});


// 动态 - 加载更多按钮 - 将数据插入
function appendToEventLine(LineDataList) {
    let eventLine = document.querySelector('.event-line');
    if (!eventLine) return;
    // 创建外层的div
    LineDataList.forEach((item) => {
        console.log(item)
        let timeLineGroup = document.createElement('div');
        timeLineGroup.classList.add("time-line-group");
        let timeLineDate = document.createElement('div');
        timeLineDate.classList.add("fonts-color-major");
        timeLineDate.innerText = item.date;
        let timeLineUl = document.createElement('ul');
        timeLineUl.classList.add("time-line-items");
        timeLineUl.classList.add("fonts-color-major");
        let commits = item.commits;
        for (let i = 0; i < item.commits.length; i++) {
            let timeLineLi = document.createElement('li');
            timeLineLi.classList.add("time-line-item");
            let timeLineContent = document.createElement('div');
            timeLineContent.classList.add("time-line-content");
            timeLineContent.classList.add("fonts-color-routine");

            let timeLineContentCommitDiv = document.createElement('div');
            let span_1 = document.createElement('span');
            span_1.innerText = item.commits[i].action_human_name;
            timeLineContentCommitDiv.appendChild(span_1);
            let a = document.createElement('a');
            a.href = item.commits[i].project_tree_path;
            a.innerText = item.commits[i].name_with_namespace;
            timeLineContentCommitDiv.appendChild(a);
            let span_2 = document.createElement('span');
            span_2.innerText = "的 master 分支"; // 需要后端传递数据
            timeLineContentCommitDiv.appendChild(span_2);
            let timeLineContentDescribeDiv = document.createElement('div');
            timeLineContentDescribeDiv.insertAdjacentHTML("beforeend", `<s-avatar src="${item.commits[i].profile_photo_link}"></s-avatar>`)
            timeLineContentDescribeDiv.insertAdjacentHTML("beforeend", `<span><a href="${item.commits[i].project_commit_path}">${item.commits[i].commit_from}</a></span><span>${item.commits[i].message}</span>`)
            timeLineLi.appendChild(timeLineContentCommitDiv);
            timeLineLi.appendChild(timeLineContentDescribeDiv);

            let timeLineMeta = document.createElement('div');
            timeLineMeta.classList.add("time-line-meta");
            timeLineMeta.classList.add("fonts-color-minor");
            timeLineMeta.innerText = "10天前"; // 需要从后台传递

            timeLineLi.appendChild(timeLineContent);
            timeLineLi.appendChild(timeLineMeta);
            timeLineUl.appendChild(timeLineLi);
        }

        timeLineGroup.appendChild(timeLineDate);
        timeLineGroup.appendChild(timeLineUl);
        eventLine.appendChild(timeLineGroup);
    })


}


// 动态 - 加载更多按钮 - 请求后端
TimeLineLoadMore.addEventListener("click", () => {
    TimeLineLoadMore.disabled = true;
    TimeLineLoadMore.innerHTML = `<s-circular-progress indeterminate="true" slot="start"></s-circular-progress>`
    let contributeYearSelectValue = contributeYearSelect.value; // 是否选中年的value值
    let url = "/dashboard/api/dynamic_time_line_data?limit=20"
    if (contributeYearSelectValue) {
        url = url + `&year=${contributeYearSelectValue}`
    }
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(res => res.json())
        .then(data => {
            appendToEventLine(data.data)
        })
        .finally(() => {
            setTimeout(() => {
                TimeLineLoadMore.disabled = false;
                TimeLineLoadMore.innerText = "加载更多";
            }, 2000)
        });

})


// 页面初始化只加载贡献图
document.addEventListener('DOMContentLoaded', function () {
    const contribute_data_dict = document.getElementById("contribute_data_dict").dataset.info;
    const contributeData = JSON.parse(contribute_data_dict);
    contributionRendering(contributeData);
});