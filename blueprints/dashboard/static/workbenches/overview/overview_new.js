/**
 * 生成模拟贡献数据：返回一个对象 { '2025-05-01': 1, ... }
 * 你可以用后台接口数据替换此处
 */
const months = document.getElementById('months');
const calendar = document.getElementById('calendar');
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
    calendar.innerHTML = '';
    months.innerHTML = '';

    // 1. 计算开始和结束日期
    let today = new Date();
    // 传递有值的情况下，需要判断这个值是 当年 还是其他年
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
        weekColumn.classList = "grid grid-rows-7 gap-1 "
        let hasMonthLabel = false;
        for (let i = 0; i < 7; i++) {
            // 首周需要补空格
            if (leadingEmpty > 0) {
                const emptyBox = document.createElement('div');
                emptyBox.className = ' w-5 h-5 ';
                weekColumn.appendChild(emptyBox);
                leadingEmpty--;
                continue;
            }
            // 当前日期超出endDate，补空格
            if (current > endDate) {
                const emptyBox = document.createElement('div');
                emptyBox.className = ' w-5 h-5 ';
                weekColumn.appendChild(emptyBox);
                continue;
            }
            // 正常渲染
            const dateStr = current.toISOString().slice(0, 10);
            const count = data[dateStr] || 0;
            const dayBox = document.createElement('div');
            dayBox.className = 'tooltip mr-0.5 w-5 h-5 box-border transition-colors cursor-pointer rounded-sm';
            // 根据数据计算，贡献图的颜色显示深度
            if (count === 0) {
                dayBox.classList.add("level-0");
            } else {
                dayBox.classList.add(contributionGrade(count));
            }
            dayBox.setAttribute("data-tip", `${count} 个贡献：${dateStr}`)
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
        }
    }
    // 渲染月份标签
    for (let i = 0; i < monthLabels.length; i++) {
        const monthDiv = document.createElement('div');
        if (monthLabels[i]) {
            monthDiv.classList.add("w-1")
        }
        monthDiv.innerHTML = monthLabels[i];
        months.appendChild(monthDiv);

    }
}


// 动态 - 展开查看 与 收回 点击按钮事项
document.querySelectorAll('.toggle-btn').forEach(function (btn) {
    btn.onclick = function () {
        const liAll = this.parentElement.parentElement.querySelectorAll('li');
        // 给动态记录的li标签添加隐藏属性
        if (this.classList.contains('show')) {
            liAll.forEach((li) => {
                if (li.classList.contains("hidden")) {
                    li.classList.remove("hidden")
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
                if (idx > 1) li.classList.add('hidden');
            })
            this.classList.remove('hide');
            this.classList.add('show');
            this.innerText = '展开查看';
            this.parentElement.querySelector('span').innerText = `已隐藏${liAll.length - 2}条推送信息，`; // liAll.length - 3 2个初始显示和1个展开查看按钮 3个li
        }
    }
});


// 动态 - 加载更多按钮 - 将数据插入 结构需要变更
function EventLineRendering(LineDataList, dataExists = false) {

    // LineDataList 数据 dataExists 代表更新或者插入，
    let eventLine = document.querySelector('.event-line');
    if (!eventLine) return;
    if (!LineDataList && dataExists) {
        let dynamicsContent = document.querySelector('.dynamics-content');
        dynamicsContent.innerHTML = '<s-empty style="min-height: 300px">暂时没有数据</s-empty>';
    } else {
        // 创建外层的div
        LineDataList.forEach((item) => {
            let commits = item.commits;
            let timeLineUlli_s = '';
            for (let i = 0; i < commits.length; i++) {
                let hideAttribute = i > 1 ? 'time-line-item-hide' : ''; // 隐藏属性
                let timeLineLi = `
                <li class="time-line-item ${hideAttribute}">
                    <!--更新上传信息-->
                    <div class="time-line-content fonts-color-routine">
                        <div>
                            <span>${commits[i].action_human_name}</span>
                            <a href="${commits[i].project_tree_path}">${commits[i].name_with_namespace}</a>
                            <span>需要后台传递参数</span>
                        </div>
                            <div>
                                <s-avatar src="${commits[i].profile_photo_link}"></s-avatar><!--头像-->
                                <span><a href="${commits[i].project_commit_path}">${commits[i].commit_from}</a></span>
                                <span>${commits[i].message}</span>
                            </div>
                        </div>
                    <div class="time-line-meta fonts-color-minor">需要后台传递参数</div>
                </li>
            `
                timeLineUlli_s += timeLineLi;
            }
            let timeLineGroup = `
            <div class="time-line-group">
                <div class="fonts-color-major">${item.date}</div>
                <ul class="time-line-items fonts-color-major">
                        ${timeLineUlli_s}
                    <li style=" font-size: 14px;margin-top: 5px" class="fonts-color-minor">
                        <span>已隐藏 ${commits.length - 1} 条推送信息，</span>
                        <a href="javascript:void(0);" class="fonts-color-routine toggle-btn show">展开查看</a>
                    </li>
                </ul>
            </div>
        `
            if (!dataExists) {
                eventLine.insertAdjacentHTML("beforeend", timeLineGroup);
            } else {
                eventLine.innerHTML = timeLineGroup;
            }

        })
    }

}


// 贡献度-日期选择框事项（根据日期，展示贡献度-动态） - 请求后端
contributeYearSelect.addEventListener('change', function () {
    const year = this.value;
    let url = `/dashboard/api/annual_contribution_data?year=${year}`;
    apiRequest(url)
        .then(response => {
            let contributionData = response.data.contribution_data;
            let eventData = response.data.event_data;
            contributionRendering(contributionData, year); // 热力图数据
            EventLineRendering(eventData, true); // 动态列表数据
        })
        .catch((error) => {
            console.log(error)
        })
});

// 动态 - 加载更多按钮 - 请求后端
TimeLineLoadMore?.addEventListener("click", () => {
    let hasMore = true;
    TimeLineLoadMore.disabled = true;
    // 插入加载状态
    TimeLineLoadMore.insertAdjacentHTML("afterbegin", `<span class="loading loading-spinner loading-md"></span>`);
    let contributeYearSelectValue = contributeYearSelect.value; // 是否选中年的value值
    let url = "/dashboard/api/dynamic_time_line_data?limit=20"
    if (contributeYearSelectValue) {
        url = url + `&year=${contributeYearSelectValue}`
    }
    // 新增一个变量用于标记是否还有更多
    apiRequest(url)
        .then(response => {
            let LineDataList = response.data;
            if (Array.isArray(LineDataList) && LineDataList.length === 0) {
                TimeLineLoadMore.disabled = true;
                TimeLineLoadMore.innerText = "没有更多";
                hasMore = false; // 没有更多数据了
            } else {
                EventLineRendering(LineDataList);
            }
        })
        .catch((error) => {
            console.log(error)
        })
        .finally(() => {
            if (hasMore) {
                setTimeout(() => {
                    TimeLineLoadMore.disabled = false;
                    TimeLineLoadMore.innerText = "加载更多";
                }, 2000)
            }
        });
})

// 页面初始化只加载贡献图
document.addEventListener('DOMContentLoaded', function () {
    const contribute_data_dict = document.getElementById("contribute_data_dict").dataset.info;
    const contributeData = JSON.parse(contribute_data_dict);
    contributionRendering(contributeData);
});