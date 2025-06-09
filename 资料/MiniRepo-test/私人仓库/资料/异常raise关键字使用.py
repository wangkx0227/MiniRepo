"""
    raise关键字介绍:
        raise 用于主动抛出一个异常。它可以抛出任何类型的异常（包括内置异常和自定义异常）。
        通常用于在程序运行过程中，当遇到某些不符合预期或者错误的情况时，主动中断程序的正常执行流程，并提示错误信息。

    简单理解,就是主动抛出异常.

    语法:
        raise exception  # exception是一个异常类
"""

自定义异常类
class MyCustomError(Exception):
    """自定义异常类"""
    pass


def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")  # 通过raise 主动抛出异常,然后终止程序
    elif age > 150:
        raise MyCustomError("年龄过高，不符合实际情况")
    else:
        print("年龄正常")


check_age(160)


"""
    自定义异常类使用:
        class CustomError(Exception):
        '''自定义异常类的描述'''
        def __init__(self, message, code=None):
            super().__init__(message)  # 调用父类的构造方法
            self.code = code  # 添加自定义属性

"""


class MyError(Exception):
    '''自定义异常类的描述'''

    def __init__(self, message, code=None):
        # 接受,错误的消息 message,交给父类调用,异常爆出错误
        super().__init__(message)  # 调用父类的构造方法
        self.code = code # 添加自定义属性


# 函数中主动触发错误信息
def add():
    raise MyError("sadadsad", code=10500)  # 使用raise 主动触发抛出自定义异常


# 通过try 捕获错误信息
try:
    add()
except MyError as e:
    print(f"自定义属性code: {e.code}")  # 可以通过e这个对象获取自定义的属性
    print(f"自定义错误信息: {e}")
