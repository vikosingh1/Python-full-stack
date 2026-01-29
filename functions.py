#wap to print all the uppercase alphabte from a given string
'''def up():
    a='PythOn'
    out=''
    for i in a: 
        if 'A'<=i<='Z':
            out+=i
    print(out)
up()'''
#wap add all the numbers present in your email id 
def add_numbers():
    email = 'vikramkumar182591@gmail.com'
    total = 0
    for i in email:
        if '0' <= i <= '9':   
            total += int(i) 
    print(total)

add_numbers()
        
    