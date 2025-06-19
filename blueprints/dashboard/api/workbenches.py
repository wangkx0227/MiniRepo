from flask import request
from core.api_base import BaseResource


# 年度贡献数据接口
class AnnualContributionDataApi(BaseResource):
    def get(self):
        print(self.user_info)  # 用户信息
        year = request.args.get('year', type=int)
        return {"year": year, "contribution_data": {f"{year}-11-12": 10}}


# 动态数据加载接口
class DynamicTimelineDataApi(BaseResource):
    def get(self):
        print(self.user_info)  # 用户信息
        year = request.args.get('year', type=int)
        return {"year": year, "contribution_data": {f"{year}-11-12": 10}}
