// 进度条
NProgress.configure({showSpinner: false, trickleSpeed: 200});

// NProgress加载函数-ajax异步时调用-加载效果
function NProgressLongin() {
    NProgress.start(); // 开启加载
    const mainContent = document.querySelector("body");
    const overlay = document.createElement('div');
    overlay.classList.add("overlay-loader");
    const circular = document.createElement('s-circular-progress');
    circular.indeterminate = true;
    circular.classList.add("circular");
    overlay.appendChild(circular);
    mainContent.appendChild(overlay)
    return function () {
        // 返回关闭调用函数，当执行返回结果后结束加载
        mainContent.removeChild(overlay);
        NProgress.done();
    };
}

async function apiRequest(url, options = {}) {
    const loader = NProgressLongin(); // 开启加载
    const headers = {
        'Content-Type': 'application/json',
        ...(options.headers || {})
    };
    // 设置默认选项
    const defaultOptions = {
        method: options.method || 'GET',
        headers,
        credentials: options.credentials || 'include', // 携带 cookie,允许外部定义
        ...options,
    };
    try {
        const response = await fetch(url, defaultOptions);
        // 检查响应状态
        if (!response.ok) {
            const error = new Error(`HTTP error! status: ${response.status}`);
            error.status = response.status;
            throw error; // 输出错误，被catch捕获
        }
        // 解析响应数据
        return await response.json();
    } catch (error) {
        throw error; // 向上传递，被调用函数的catch捕获
    } finally {
        setTimeout(() => {
            loader();
        }, 2000) // 测试
    }
}