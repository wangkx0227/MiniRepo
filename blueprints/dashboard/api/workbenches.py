from flask import request, session
from resource.api_base import BaseResource

from core.variable import USER_SESSION_KEY


# 年度贡献数据接口
class AnnualContributionDataApi(BaseResource):
    def get(self):
        user_info = session.get(USER_SESSION_KEY)  # 用户信息

        year = request.args.get('year', type=int)
        return {"year": year, "contribution_data": {f"{year}-11-12": 10}}
