from resource.api_base import BaseResource


# 你可以在这里添加API资源
class UserResource(BaseResource):
    def get(self):
        return {"msg": "hello"}
