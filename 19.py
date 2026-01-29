#wap a=[10.'Hai',[1,2,3],3.5,3+5j] then print op= [(10,1),('Hai',3),([1,2,3],3),(3.5,1),(3+5j,1)]
'''def fun1(a):
    out=[]
    for i in a:
        if type(i) in [str,set,dict,list,tuple]:
            out+=[(i,len(i))]
        else:
            out+=[(i,1)]
    print(out)
fun1([10,'Hai',[1,2,3],3.5,3+5j])'''

'''#join() function
a='abc' 'def' 'ghi'
'#'.join(a)
print('#'.join(a))'''

#a='how','are','you','all' then op = 'H0w','Are','You','All' using concatination
'''a='how','are','you','all'
out=[]
for i in a:
    out+=[i.capitalize()]
print(' '.join(out))'''



    
