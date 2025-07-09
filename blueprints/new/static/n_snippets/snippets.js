let code_editor = null; // 让整个作用域都能访问编辑器实例
let quill_editor = null; // 让整个作用域都能访问编辑器实例
const QuillToolbarOptions = [
    ['bold', 'italic', 'underline', 'blockquote', 'code-block', 'image'],
    [{'list': 'ordered'}, {'list': 'bullet'}, {'list': 'check'}],
    [{'color': []}, {'background': []}],
];
const CodeMirrorHighlight = {
    'go': {'mode': 'go', 'highlight_file': '/static/lib/codemirror/mode/go/go.js'},
    'rs': {'mode': 'text/x-rustsrc', 'highlight_file': '/static/lib/codemirror/mode/rust/rust.js'},
    'php': {'mode': 'php', 'highlight_file': '/static/lib/codemirror/mode/php/php.js'},
    'xml': {'mode': 'xml', 'highlight_file': '/static/lib/codemirror/mode/xml/xml.js'},
    'lua': {'mode': 'lua', 'highlight_file': '/static/lib/codemirror/mode/lua/lua.js'},
    'sql': {'mode': 'sql', 'highlight_file': '/static/lib/codemirror/mode/sql/sql.js'},
    'css': {'mode': 'css', 'highlight_file': '/static/lib/codemirror/mode/css/css.js'},
    'rb': {'mode': 'ruby', 'highlight_file': '/static/lib/codemirror/mode/ruby/ruby.js'},
    'py': {'mode': 'python', 'highlight_file': '/static/lib/codemirror/mode/python/python.js'},
    'md': {'mode': 'md', 'highlight_file': '/static/lib/codemirror/mode/markdown/markdown.js'},
    'sh': {'mode': 'text/x-sh', 'highlight_file': '/static/lib/codemirror/mode/shell/shell.js'},
    'bash': {'mode': 'text/x-sh', 'highlight_file': '/static/lib/codemirror/mode/shell/shell.js'},
    'html': {'mode': 'htmlmixed', 'highlight_file': '/static/lib/codemirror/mode/htmlmixed/htmlmixed.js'},
    'js': {'mode': 'javascript', 'highlight_file': '/static/lib/codemirror/mode/javascript/javascript.js'},
    'ts': {'mode': 'text/typescript', 'highlight_file': '/static/lib/codemirror/mode/javascript/javascript.js'},
    'json': {'mode': 'application/json', 'highlight_file': '/static/lib/codemirror/mode/javascript/javascript.js'},
    'c': {'mode': 'text/x-csrc', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'java': {'mode': 'text/x-java', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'cs': {'mode': 'text/x-csharp', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'csx': {'mode': 'text/x-csharp', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'cxx': {'mode': 'text/x-c++src', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'cpp': {'mode': 'text/x-c++src', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'cc': {'mode': 'text/x-c++src', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'h': {'mode': 'text/x-objectivec', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'm': {'mode': 'text/x-objectivec', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'mm': {'mode': 'text/x-objectivec', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
    'class': {'mode': 'text/x-scala', 'highlight_file': '/static/lib/codemirror/mode/click/click.js'},
};

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        // 这是编辑框样式
        quill_editor = new Quill('#editor', {
            modules: {
                toolbar: QuillToolbarOptions
            },
            theme: 'snow'
        });
        const ql_container = document.querySelector(".ql-container"); // 主体内容
        ql_container && ql_container.classList.add("top-[-6px]"); // 增加白色背景
        const ql_toolbar = document.querySelector(".ql-toolbar"); // 工具栏
        ql_toolbar && ql_toolbar.classList.add("bg-white"); // 增加白色背景
        const ql_editor = document.querySelector(".ql-editor"); // 填写内容
        ql_editor && ql_editor.classList.add('max-h-[200px]', 'overflow-y-auto', 'min-h-[200px]');
        document.getElementById('editor-skeleton').classList.add('hidden');
        document.getElementById('editor').classList.remove('hidden');

        // 这是代码编辑框样式
        code_editor = CodeMirror.fromTextArea(document.getElementById("code-editor"), {
            mode: "text/plain",  // 语法模式
            lineNumbers: true,    // 显示行号
            indentUnit: 4,        // 缩进单位
            theme: "default",     // 主题
        });
        code_editor.setSize(null, "200"); // 高度设为父容器高度
        const code_mirror_table = document.querySelector(".CodeMirror");
        code_mirror_table && code_mirror_table.classList.add('border', 'border-gray-300')
        document.getElementById('code-editor-skeleton').classList.add('hidden');
        document.getElementById('code-editor').classList.remove('hidden');
    }, 500);
});

// 静态加载 语言高亮的 js文件
function loadScript(url, callback) {
    let found = false;
    if (!url) return callback(); // 如果没有url，也会进行重新载入code_editor编辑器
    const scripts = Array.from(document.getElementsByTagName('script')).map(s => s.src); // 获取全部的加载的js
    for (let js_url of scripts) {
        const path = new URL(js_url, location.href).pathname;
        if (path === url) {
            found = true;
            break;
        }
    }
    if (found) {
        return callback(); // 已加载
    }
    const script = document.createElement('script');
    script.src = url;
    script.onload = callback;
    document.head.appendChild(script);
}

// 根据文件名称的后缀进行判断，获取高亮文件并且加载
function getModeFromFilename(filename) {
    const Default = {'mode': 'text/plain', 'highlight_file': ''};

    try {
        if (filename.includes('.') && !filename.endsWith('.') && filename.lastIndexOf('.') !== 0) {
            const ext = filename.split('.').pop().toLowerCase();
            return CodeMirrorHighlight[ext];
        } else {
            return Default;
        }
    } catch (error) {
        return Default;
    }
}

// 输入文件名称焦点事项
document.getElementById("code-file-name").addEventListener("blur", function () {
    const codeFileName = document.getElementById("code-file-name").value
    const config = getModeFromFilename(codeFileName)
    loadScript(config.highlight_file, function () {
        code_editor.setOption('mode', config.mode); // 切换语法高亮
    });
})


