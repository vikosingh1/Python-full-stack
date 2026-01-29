# property decorator

class A:
    def __init__(self, sal):
        self.__sal = sal

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self, new_value):
        self.__sal = new_value


obj = A(2345)
print(obj.sal)
obj.sal = 9876543
print(obj.sal)
