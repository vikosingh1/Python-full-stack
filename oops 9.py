# gather and setter method
class A:
    def __init__(self, sal):
        self.__sal = sal

    def get_sal(self):
        return self.__sal

    def set_sal(self, new_value):
        self.__sal = new_value


obj = A(58000)
print(obj.get_sal())
obj.set_sal(85000)  # private method
print(obj.get_sal())
