from flask import request
from utils.api_base import BaseResource


# 年度贡献数据接口
class AnnualContributionDataApi(BaseResource):
    def get(self):
        """
            根据选择的年将贡献度与动态信息进行渲染
        """
        print(self.user_info)  # 用户信息
        year = request.args.get('year', type=int)
        return {"year": year, "contribution_data": {f"{year}-11-12": 10}, "event_data": [
            {
                "date": f"{year}-06-13",  # 日期
                "hide_number": 1,
                "commits": [
                    {
                        "create_at_date": f"{year}-06-13 16:47:00",  # 日期
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
                        "create_at_date": f"{year}-06-13 14:15:00",  # 日期
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
                        "create_at_date": f"{year}-06-13 16:00:00",  # 日期
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
        ]}


# 动态时间线数据加载接口-获取与自己相关或者自己创建仓库相关的数据
class DynamicTimelineDataApi(BaseResource):
    def get(self):
        """
            需要注意：需要记录上一次的查询数据的位置，可以通过前端进行传递。
            假设：2024年，那么触发这个请求时，就只查2024年的时间线
            如果是今年的，就差全部的数据
        :return:
        """
        print(self.user_info)  # 用户信息
        year = request.args.get('year')
        if not year:
            print("就不根据年份进行获取动态时间线，如果根据年份的情况下，就差当前的数据")
        limit = request.args.get('limit', 20)  # 最多一次性获取多少条数据
        return [
            # {
            #     "date": "2025-06-13",  # 日期
            #     "hide_number": 1,
            #     "commits": [
            #         {
            #             "create_at_date": "2025-06-13 16:47:00",  # 日期
            #             "profile_photo_link": "https://avatars.githubusercontent.com/u/3369400?v=4",  # 头像
            #             "name_with_namespace": "不会换牙的鲨鱼/MiniRepo",  # 项目命名空间
            #             "project_tree_path": "/wangkx0227/MiniRepo/tree/master",  # 推送项目地址
            #             "branch_name": "master",  # 推送的分支
            #             "message": "更新了css样式",  # 推送的commit信息
            #             "is_push_with_commits": "d960e14bc58e5679bf4d5cb076eb321c8c8932a8",  # 推送的长id
            #             "commit_to": "8c879a0",  # 上一次简写id
            #             "commit_from": "d960e14",  # 简写id
            #             # 差异详情记录
            #             "project_commit_path": "/wangkx0227/MiniRepo/commit/d960e14bc58e5679bf4d5cb076eb321c8c8932a8",
            #             "action": "push",
            #             "action_human_name": "推送了",
            #
            #         },
            #         {
            #             "create_at_date": "2025-06-13 14:15:00",  # 日期
            #             "profile_photo_link": "https://avatars.githubusercontent.com/u/3369400?v=4",  # 头像
            #             "name_with_namespace": "不会换牙的鲨鱼/MiniRepo",  # 项目命名空间
            #             "project_tree_path": "/wangkx0227/MiniRepo/tree/master",  # 推送项目地址
            #             "branch_name": "master",  # 推送的分支
            #             "message": "更新了js样式",  # 推送的commit信息
            #             "is_push_with_commits": "d960e14bc58e5679bf4d5cb076eb321c8c8932a8",  # 推送的长id
            #             "commit_to": "8c879a0",  # 上一次简写id
            #             "commit_from": "d960e14",  # 简写id
            #             # 差异详情记录
            #             "project_commit_path": "/wangkx0227/MiniRepo/commit/d960e14bc58e5679bf4d5cb076eb321c8c8932a8",
            #             "action": "push",
            #             "action_human_name": "推送了",
            #
            #         },
            #         {
            #             "create_at_date": "2025-06-13 16:00:00",  # 日期
            #             "profile_photo_link": "https://avatars.githubusercontent.com/u/3369400?v=4",  # 头像
            #             "name_with_namespace": "不会换牙的鲨鱼/MiniRepo",  # 项目命名空间
            #             "project_tree_path": "/wangkx0227/MiniRepo/tree/master",  # 推送项目地址
            #             "branch_name": "master",  # 推送的分支
            #             "message": "更新html内容",  # 推送的commit信息
            #             "is_push_with_commits": "d960e14bc58e5679bf4d5cb076eb321c8c8932a8",  # 推送的长id
            #             "commit_to": "8c879a0",  # 上一次简写id
            #             "commit_from": "d960e14",  # 简写id
            #             # 差异详情记录
            #             "project_commit_path": "/wangkx0227/MiniRepo/commit/d960e14bc58e5679bf4d5cb076eb321c8c8932a8",
            #             "action": "push",
            #             "action_human_name": "推送了",
            #
            #         }]
            # },
        ]

# 仓库搜索与下拉框
