// 增强封装：支持 token、loading 等
async function apiRequest(url, options = {}) {
    const {
        useToken = true,
        showLoading = false,
        parseResponse = true,
        ...restOptions
    } = options;

    // 显示 loading
    if (showLoading) {
        // 你的全局 loading 控制，比如 vuex/全局变量
        window.showLoading && window.showLoading();
    }

    // 默认 headers
    const headers = {
        'Content-Type': 'application/json',
        ...restOptions.headers,
    };
    if (useToken) {
        const token = localStorage.getItem('token');
        if (token) headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(url, {
            ...restOptions,
            headers,
        });
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.message || '网络请求错误');
        }
        // 根据自定义需求解析 response
        return parseResponse ? await response.json() : response;
    } finally {
        if (showLoading) {
            window.hideLoading && window.hideLoading();
        }
    }
}