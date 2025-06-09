# 断言 关键字 assert condition,message(assert 条件 , 用于在触发异常时提供更多的错误信息)
# 断言 条件(condition)是真的情况下,会输出message消息( 触发AssertionError:message内容)
# 断言抛出的错误是 AssertionError
a = 10
b = 10
# assert a == b, "两个值相同"
# assert a != b, "两个值不同"


"""
# 断言的条件为假才会触发断言。
# assert 语句的作用是检查一个条件是否为真。如果条件为真，程序会继续执行；如果条件为假，程序会抛出 AssertionError 异常。

怎么使用断言在项目中.
    1.在函数或者方法内部,使用断言来检查程序的中间状态是否符合预期。这有助于发现逻辑错误。
    def find_max(number_list):
        # number_list不能为空,内部的元素必须是数字
        assert len(number_list) > 0, "列表不能为空"
        for num in number_list:
            assert isinstance(num, (int, float)), "列表中的元素必须是数字"
            print(num)
    
    2.前置条件和后置条件检查,在函数或方法的入口处检查前置条件，在出口处检查后置条件。这有助于确保函数的正确性。
    def add(a, b):
        assert isinstance(a, (int, float)), "参数a必须是数字"
        assert isinstance(b, (int, float)), "参数b必须是数字"
        result = a + b
        assert isinstance(result, (int, float)), "结果必须是数字"
        return result
    
    3.结合日志,当使用断言,可以结合日志功能进行记录
    import logging
    logging.basicConfig(level=logging.ERROR)
    def process_data(data):
        try:
            assert isinstance(data, list), f"期望data是列表类型，但实际是{type(data)}"
            assert all(isinstance(item, int) for item in data), "列表中的所有元素必须是整数"
        except AssertionError as e:
            logging.error(f"断言失败: {e}")
            raise    

# 注意:
    1.断言失败时，提供清晰、具体的错误信息，有助于快速定位问题。(一定要说明当前断言的错误原因)
    2.断言主要用于调试阶段，不应替代正常的错误处理逻辑。过度使用断言会使代码难以维护，也可能导致在生产环境中隐藏错误。(不要过度使用断言)
    3.禁止断言 python -O main.py ,使用-O 参数断言就会失效


    
"""

