# 用户定义函数对象可通过函数定义来创建 (参见 函数定义 小节)。它被调用时应附带一个参数列表，其中包含的条目应与函数所定义的形参列表一致。
def outer(value=12):
    x = value

    def inner():
        return x

    return inner


closure_function = outer()


# 特殊的只读属性
# print(closure_function.__globals__)  # 函数定义时所在的作用域中的全局变量字典。这个字典包含了函数定义时所在模块中的所有全局变量，包括函数、类、模块级别的变量等。
# print(closure_function.__closure__)  # 它返回一个函数的闭包（closure）信息
# """
# 闭包的基本概念
# 闭包是函数式编程中的一个重要概念。在 Python 中，闭包是指一个函数内部定义了另一个函数，并且内部函数引用了外部函数的局部变量。当外部函数返回时，内部函数仍然可以访问这些局部变量，这些局部变量被称为闭包变量。
#
# """
# # 特殊的可写属性
# print(closure_function.__doc__)  # 函数的说明
# print(closure_function.__name__)  # 函数的名称
# print(closure_function.__module__)  # 该函数所属模块的名称，没有则为 None。
# print(closure_function.__code__)  # 代表已编译的函数体的 代码对象，函数所在位置，文件位置，函数的对象。
def my_function(a,  b=2, *, c=3, d=4):  # 使用 * 来区分关键字参数与位置参数，只能在函数中使用
    pass


print(my_function.__kwdefaults__)  # 是一个字典，包含函数的关键字参数的默认值，不包含位置参数的默认值。没有使用 * 来定义关键字参数，就会返回None。 输出：{'c': 3, 'd': 4}


def my_function():
    pass


my_function.custom_attribute = "Hello, World!"
print(my_function.__dict__)  # 是一个字典，包含函数对象的命名空间。你可以在这个字典中存储和访问函数的任意属性。


def my_function(a: int, b: str) -> float:
    return float(a) + float(b)


print(my_function.__annotations__)  # 包含函数的参数和返回值的类型注解，需要进行声明参数类型


def my_function(a, b, c=3):
    pass


print(my_function.__defaults__)  # 是一个元组，包含函数的位置参数的默认值，将全部的默认值打印出来。 输出 (3,)


def my_function():
    pass


print(my_function.__qualname__)  # 表示函数的限定名称（qualified name）。它包括函数所在的模块、类和嵌套函数的名称。
