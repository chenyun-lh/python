# # 学习装饰器目的: 对已有函数进行额外的功能扩展， 装饰器本质上一个闭包函数，也就是说他也是一个函数嵌套
#
# # 装饰器的特点:
# # 1. 不修改已有函数的源代码
# # 2. 不修改已有函数的调用方式
# # 3. 给以后函数添加额外的功能



# def check(fn):
#     def inner():
#         print("请先登录....")
#         fn()
#     return inner
#
# # @check
# def comment():
#     print("发表评论")
#
# # 使用装饰器来装饰函数
#
# comment = check(comment)
# comment()


# # 定义装饰器
# def decorator(func):  # 如果闭包函数的参数有且只有一个并且是函数类型，那么这个闭包函数称为装饰器
#     print("装饰器执行了")
#     def inner():
#         # 在内部函数里面对已有函数进行装饰
#         print("已添加登陆验证")
#         func()
#     return inner
#
#
# # 装饰器的语法糖写法: @装饰器名称，装饰器的语法糖就是在装饰以后函数的时候写法更加简单
# @decorator  # comment = decorator(comment) 装饰器语法糖对该代码进行了封装  comment=inner
# def comment():
#     print("发表评论")
#
# # 已添加登陆验证
# # 发表评论
#
# # # 调用装饰器对已有函数进行装饰  ， comment=inner
# # comment = decorator(comment)
#
# # 调用方式不变
# comment()
#
# # 装饰器的执行时机： 当当前模块加载完成以后，装饰器会立即执行，对已有函数进行装饰


# 使用闭包来做装饰器，装饰器只有一个函数参数
def B(f):
    def C():
        print("xixi")
        f()
    return C



@B
# 函数内部不变
def A():
    print("haha")

# 使用装饰器装饰函数A1（创建闭包实例）
# A = B(A)
# 调用方式不变（执行闭包）
A()
