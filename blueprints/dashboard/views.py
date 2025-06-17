from flask import render_template, session, redirect, url_for, request
from resource import redis_link

"""
    # print(session.get("userStatus")) # 登录使用
    # session["userStatus"] = "asdasdasdwxc312313asdqe"
    # print(redis_link.keys())

"""


# 根据标签获取tab的数据
def get_workbenches_data(tab):
    data_dict = {}
    if tab == "overview":
        data_dict["event_list"] = [
            {
                "date": "2025-06-14",  # 日期
                "save_commit_list": [{
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

                }, {
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

                }, {
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

                }]
            }, {
                "date": "2025-06-13",  # 日期
                "save_commit_list": [{
                    "create_at_date": "2025-06-13 15:15:00",  # 日期
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

                }, {
                    "create_at_date": "2025-06-13 01:15:00",  # 日期
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

                }, {
                    "create_at_date": "2025-06-13 01:00:00",  # 日期
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

                }]
            }

        ]
    if tab == "analysis":
        pass
    if tab == "snippet":
        pass
    if tab == "repository":
        pass
    return data_dict


# 工作台
def workbenches():
    tab = request.args.get('tab', 'overview')
    # 工作台tab标签，对应get请求参数对应的模版路径
    template_map = {
        'repository': 'dashboard/workbenches/repository.html',
        'analysis': 'dashboard/workbenches/analysis.html',
        'snippet': 'dashboard/workbenches/snippet.html',
        'overview': 'dashboard/workbenches/overview.html'
    }
    # 默认用 overview，无论是登录跳转还是点击工作台
    template = template_map.get(tab, 'dashboard/workbenches/overview.html')
    data_dict = get_workbenches_data(tab)  # 获取当前数据
    # 传递 tab 让前端的tab标签默认选中
    return render_template(template, tab=tab, data=data_dict)


def projects():
    return render_template("dashboard/projects.html")


def groups():
    return render_template("dashboard/groups.html")


def merge_requests():
    return render_template("dashboard/merge_requests.html")


def todos():
    return render_template("dashboard/todos.html")


def user_setting():
    folded = True  # 用来控制1级菜单展开属性
    return render_template("dashboard/setting/user_setting.html", folded=folded)


def secured_setting():
    folded = True  # 用来控制1级菜单展开属性
    return render_template("dashboard/setting/secured_setting.html", folded=folded)
