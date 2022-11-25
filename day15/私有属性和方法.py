class Animal:


    def __init__(self):
        self.__name = 'Tom'  # 私有属性
        self.age = 3


    def __get_name(self):  ##私有方法
        print("名字是{0}".format(self.__name))


    def get_age(self):  #普通方法,可以调用私有属性和方法
        print("{0} 的年龄是{1}".format(self.__name,self.age))


cat = Animal()
cat.get_age()
# cat.__get_name() #实例直接访问私有方法会抛出异常

cat._Animal__get_name() # 实例直接调用Python内部改名之后的私有方法，就能正常访问