from flask import render_template,request


def get_overview_data():
    """
     获取overview需要的数据
    """
    data_dict = {
        "event_data_list": [
            {
                "date": "2025-06-14",  # 日期
                "hide_number": 1,
                "commits": [
                    {
                        "create_at_date": "2025-06-17 16:47:00",  # 日期
                        "profile_photo_link": "https://avatars.githubusercontent.com/u/3369400?v=4",  # 头像
                        "name_with_namespace": "不会换牙的鲨鱼/MiniRepo",  # 项目命名空间
                        "project_tree_path": "/wangkx0227/MiniRepo/tree/master",  # 推送项目地址
                        "branch_name": "master",  # 推送的分支
                        "message": "更新了css样式",  # 推送的commit信息
                        "is_push_with_commits": "d960e14bc58e5679bf4d5cb076eb321c8c8932a8",  # 推送的长id
                        "commit_to": "8c879a0",  # 上一次简写id
                        "commit_from": "d960e14",  # 简写id
                        # 差异详情记录
                        "project_commit_path": "/wangkx0227/MiniRepo/commit/d960e14bc58e5679bf4d5cb076eb321c8c8932a8",
                        "action": "push",
                        "action_human_name": "推送了",

                    },
                    {
                        "create_at_date": "2025-06-14 14:15:00",  # 日期
                        "profile_photo_link": "https://avatars.githubusercontent.com/u/3369400?v=4",  # 头像
                        "name_with_namespace": "不会换牙的鲨鱼/MiniRepo",  # 项目命名空间
                        "project_tree_path": "/wangkx0227/MiniRepo/tree/master",  # 推送项目地址
                        "branch_name": "master",  # 推送的分支
                        "message": "更新了js样式",  # 推送的commit信息
                        "is_push_with_commits": "d960e14bc58e5679bf4d5cb076eb321c8c8932a8",  # 推送的长id
                        "commit_to": "8c879a0",  # 上一次简写id
                        "commit_from": "d960e14",  # 简写id
                        # 差异详情记录
                        "project_commit_path": "/wangkx0227/MiniRepo/commit/d960e14bc58e5679bf4d5cb076eb321c8c8932a8",
                        "action": "push",
                        "action_human_name": "推送了",

                    },
                    {
                        "create_at_date": "2025-06-14 16:00:00",  # 日期
                        "profile_photo_link": "https://avatars.githubusercontent.com/u/3369400?v=4",  # 头像
                        "name_with_namespace": "不会换牙的鲨鱼/MiniRepo",  # 项目命名空间
                        "project_tree_path": "/wangkx0227/MiniRepo/tree/master",  # 推送项目地址
                        "branch_name": "master",  # 推送的分支
                        "message": "更新html内容",  # 推送的commit信息
                        "is_push_with_commits": "d960e14bc58e5679bf4d5cb076eb321c8c8932a8",  # 推送的长id
                        "commit_to": "8c879a0",  # 上一次简写id
                        "commit_from": "d960e14",  # 简写id
                        # 差异详情记录
                        "project_commit_path": "/wangkx0227/MiniRepo/commit/d960e14bc58e5679bf4d5cb076eb321c8c8932a8",
                        "action": "push",
                        "action_human_name": "推送了",

                    }]
            },
        ],
        "contribute_data_dict": {"2025-06-15": 10},
        "contribute_total": 150,
        "contribute_continuous_day": 10,
        "contribute_continuous_longest_day": 20,
    }
    return data_dict


def get_repository_data():
    """
    获取repository需要的数据
    """
    data = [
        {
            "repository_type_name": "公有（根据仓库的属性决定）",
            "repository_type_value": 0,
            "user_name": "不会换牙的鲨鱼",
            "repository_path_name": "MiniRepo",
            "repository_path_url": "#",
            "see_repository_number": 15,
            "start_repository_number": 10,
            "fork_repository_number": 6,
            "repository_description": "代码仓库项目",
            "repository_code_language": "Python",
            "repository_recently_time": "6分钟前",
        },
        {
            "repository_type_name": "私有（根据仓库的属性决定）",
            "repository_type_value": 1,
            "user_name": "不会换牙的鲨鱼",
            "repository_path_name": "MiniRepo",
            "repository_path_url": "#",
            "see_repository_number": 15,
            "start_repository_number": 10,
            "fork_repository_number": 6,
            "repository_description": "代码仓库项目",
            "repository_code_language": "Python",
            "repository_recently_time": "6分钟前",
        },
        {
            "repository_type_name": "公有（根据仓库的属性决定）",
            "repository_type_value": 0,
            "user_name": "不会换牙的鲨鱼",
            "repository_path_name": "MiniRepo",
            "repository_path_url": "#",
            "see_repository_number": 15,
            "start_repository_number": 10,
            "fork_repository_number": 6,
            "repository_description": "代码仓库项目",
            "repository_code_language": "Python",
            "repository_recently_time": "6分钟前",
        }
    ]
    return data


def get_analysis_data():
    """
    获取analysis需要的数据
    """
    return {}


def get_snippet_data():
    """
    获取snippet需要的数据
    """
    return {}


# 工厂函数/分发器
def get_workbenches_data(tab):
    data_func_map = {
        'overview': get_overview_data,
        'repository': get_repository_data,
        'analysis': get_analysis_data,
        'snippet': get_snippet_data,
    }
    func = data_func_map.get(tab, get_overview_data)
    return func()

# 用户主页
def home():
    tab = request.args.get('tab', 'overview')
    # 工作台tab标签，对应get请求参数对应的模版路径
    template_map = {
        'repository': 'home/repository.html',
        'analysis': 'home/analysis.html',
        'snippet': 'home/snippet.html',
        'overview': 'home/overview.html',
    }
    # 默认用 overview，无论是登录跳转还是点击工作台
    template = template_map.get(tab, 'home/overview.html')
    data = get_workbenches_data(tab)  # 获取当前数据
    return render_template(template, tab=tab, data=data)


def setting():
    return render_template("setting.html")


def todos():
    return render_template("todos.html")


def related():
    return render_template("related.html")


def stars():
    return render_template("stars.html")


def repos():
    return render_template("repos.html")
