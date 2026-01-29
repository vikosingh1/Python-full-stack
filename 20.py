'''def ext_char():
    a='PYTHON IS PROGRAMMING LANGUAGE'
    out=''
    c=0
    for i in range(0,len(a),2):
        if 'A'<=a[i]<='Z' and ord(a[i])%3==0:
            out+=a[i]
            c+=1
    return out,c
print(ext_char())'''

#wap a='python is programing language' then print op= {'P':['python','programming'], 'i':['is'], 'l':['language']}
'''def fun2():
    a='python is programing language'.split()
    out={}
    for i in a:
        if i[0] not in out:
            out[i[0]]=[i]
        else:
            out[i[0]]+=[i]
    return out
print(fun2())'''

    
