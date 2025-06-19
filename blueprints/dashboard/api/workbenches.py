from flask import request, session
from resource.api_base import BaseResource


# 年度贡献数据接口
class AnnualContributionDataApi(BaseResource):
    def get(self):
        user_info = session.get("user_info")
        print(user_info)
        year = request.args.get('year', type=int)
        return {"year": year, "contribution_data": {f"{year}-11-12": 10}}
