class Person:
    def __init__(self):
        self.name = "Tom"
        self.age = 25

    def __delattr__(self, name):
        if name == "name":
            raise AttributeError("不能删除 name 属性")
        # del self.name  # 触发递归操作
        super().__delattr__(name)  # 调用父类避免递归错误，正常删除其他属性


p = Person()
print(p.__dict__)  # {'name': 'Tom', 'age': 25}

del p.age  # 删除 age
print(p.__dict__)  # {'name': 'Tom'}

del p.name  # 抛出异常
# AttributeError: 不能删除 name 属性
