# 实例方法用于结合类、类实例和任何可调用对象 (通常为用户定义函数)。
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        """
        123132132
        :return:
        """
        return self.value


# 创建一个实例
obj = MyClass(10)

# 获取绑定方法
bound_method = obj.my_method


print(bound_method.__self__)  # 指向方法所 绑定 的类实例对象。
print(bound_method.__func__)  # 指向原来的函数对象。
print(bound_method.__doc__)  # 函数文档。
print(bound_method.__name__)  # 函数名。
print(bound_method.__module__)  # 函数所在的模块，所在的文件。