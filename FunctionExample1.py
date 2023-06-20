##def add(a,b):
##    return a+b
##def add(a):
##    return a

##def add(*a):
##    print(type(a))
##    return a
##print(add(10,50,50,8,5,65))
##
##def fullName(a,b,c="india"):
##    print(c)
##    return a+b
##
##print(fullName(10,20,30))

def string(*a):
    result=""
    if(len(a)!=0):
        for i in a:
            result+=i
    return a

ab=string("May the force be with you",)
##print(type(ab))
var="".join(ab)
##print(type(var))
##print(var)
##
##
##def string(a,b,c,d=10):
##    a+b==c
##    c=c+d
##    return c
##
####print(string(10,20,30))
##
##def values(*a):
##    val=1
##    for i in a:
##        val=val*i
##    return val
##
##
##
##print(values(2,3,4,5))
        


