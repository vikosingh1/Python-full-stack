# Dictionary syntax
# 1.var={k:v for in collection}
# 2.var={k:v for i in collection if condition}
#3.var={k:v1 if cond else v2 for i in coll}
#4.var={k.v for i,j in zip(col1,col2)}

#print({i:i**2 for i in range (1,11)})
# l=['hi',5.2,9.3,85,'hello',8+9j]
# print({i:len(i) for i in l if type(i)==str})

# wap to get the following output
# s='Hey guys hello students'
# out={'guys':4, 'students':8}
# print({i:len(i) for i in s.split() if len(i)%2==0})

#wap to map two list collections in the form of dictionary
# l1=['a','b','c','d','e']
# l2=[10,20,30,40,50]
# # out={'a':10,'b':20,'c':30,'d':40,'e':50}
# print({i:j for i,j in zip(l1,l2)})

# wap to get the following output
# l=['abcd','nayan','data','aba']
# out={'abcd':'dcba','nayan':5,'data':'atad','aba':3}
# print({i:len(i) if i==i[::-1] else i[::-1] for})

# wap to get the following output
# range(1:6)
# {1:1,2:4,3:27,4:256,5:3125}
# print({i:i**i for i in range(1,6)})

#range(1,11)
# out={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:100}
# print({i:i*i if i%5==0 else i for i in range(1,11)})