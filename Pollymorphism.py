# METHOD OVERLOADING
# MONKEY PATCHING: Here we store the function (reference) in a variable to avoide updation to method with same name. Used to achieve overloading.
# def sample():
#     print('Method Overloading')
# a=sample
# def sample(a):
#     print(a)
# b=sample
# def sample(a,b):
#     print(a+b)
# c=sample
# a()
# b('Hello Python')
# c(10,20)

# OPERATOR OVERLOADING:Not possible for user defined class so we have to create magic method
# MAGIC METHOD

# class A:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#         return self.a+other.a
#     def __sub__(self,other):
#         return self.a-other.a
#     def __mul__(self,other):
#         return self.a*other.a
#     def __floordiv__(self,other):
#         return self.a//other.a
# ob1=A(21)
# ob2=A(10)
# print(ob1//ob2)
print(dir(int))

# class bitwise:
#     def __init__(self,a):
#         self.a=a
#     def __and__(self,other):
#         return self.a&other.a
#     def __or__(self,other):
#         return self.a|other.a
#     def __invert__(self):
#         return ~(self.a)
# ob1=bitwise(10)
# ob2=bitwise(20)
# print(ob1|ob2)
# print(~ob1)
# print(~ob2)
# print(dir(int))

# class relation:
#     def __init__(self,a):
#         self.a=a
#     def __eq__(self):

# class library:
#     lname='Pustak'
#     lloc='Delhi'
    
    