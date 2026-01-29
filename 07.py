'''num=int(input("enter the num:"))
if num%2==0:
    print("even number",num)
else:
    print("odd",num)'''
#wap to check the data is multivalue datatype or single value data type
'''data = eval(input("Enter a value: "))
if type(data) in [str,list, tuple, set, dict]:
    print('This is a multivalue datatype',data)
else:
    print('single value data type')'''
#wap to check the character is vowel or consonant
'''char = input("Enter a character: ")
if char in 'aeiouAEIOU':
    print('Vowel character')
else:
    print('Consonant character')'''
#wap to check the data is list or not
'''data = eval(input("Enter a value: "))
if type(data) == list:
    print('This is a list')
else:
    print('This is not a list')'''
#wap tocheck no. is even or add if even print qube of it else print squar of it.
'''num = int(input("Enter a number: "))
if num % 2 == 0:
    print('Even number, cube:', num ** 3)'''
#wap
'''char= input("Enter a character: ")
if 'A' <= char <= 'Z':
    print('Uppercase character')
elif 'a' <= char <= 'z':
    print('Lowercase character')
elif '0' <= char <= '9':
    print('Digit character')
else:
    print('Special character')'''
#wap to check the number is one digit or two digit or three digit or four digit
'''num = int(input("Enter a number: "))
if 0 <= num < 9:
    print('One digit number')
elif 10 <= num < 99:
    print('Two digit number')
elif 100 <= num < 999:
    print('Three digit number')
elif 1000 <= num < 9999:
    print('Four digit number')'''
#wap to print if the number divisible by 3 then print fizz if divide by 5 then buzz if divide by both then fizzbuzz
num= int(input("Enter a number: "))
if num % 3==0 and num% 5==0:
    print('FIZZBUZZ')
elif num % 5 == 0:
    print('Buzz')
elif num%3==0:
    print("FIZZ")
    