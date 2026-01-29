# wap  to find numbers is even number
#num =int(input("Enter a number: "))
#if num % 2 == 0:
 #   print('even number')
#wap to check the data is multivalue datatype
#eval is used to evaluate the expression in list, tuple, set, dict
'''data = eval(input("Enter a value: "))
if type(data) in [list, tuple, set, dict]:
    print('This is a multivalue datatype')'''
#wap to check the character is uppercase
'''char = input("Enter a character: ")
if 'A' <= char <= 'Z':
    print('Uppercase character')'''
''''a'<= char <= 'z'
'0' <= char <= '9' '''
#wap to check character is special character
'''char = input("Enter a character: ")
if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9'):
    print('Special character')'''
#wap to print last value from the list but it should be string and is lenghth is more then 3
a = [1,2,3,'hello']
if type(a[-1]) == str and len(a[-1]) > 3:
    print('done', a[-1])

