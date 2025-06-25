/**
 * 封装的基础 fetch 请求
 * @param {string} url - 请求地址
 * @param {object} options - 请求配置
 * @returns {Promise} 返回 Promise
 */
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
            throw error;
        }

        // 解析响应数据
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
        throw error;
    } finally {
        setTimeout(() => {
            loader();
        }, 2000) // 测试
    }
}

apiRequest("/dashboard/api/annual_contribution_data?year=2024", {
    method: 'GET', headers: {}
})
    .then((res) => {
        console.log(res)
    })