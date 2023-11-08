
#Junleizhou, Junhongcai and Zhouzhou explained to me what is recursion and inspired me to solve the problem.
import random
import numpy as np
def Find_expression(N):
    n=0 #record the number of expression
    list=[] #record the every expression
    def NEXT(a,b,end):
        nonlocal n
        if b>9:
           if eval(a)==end:
            list.append(a)
            n=n+1
        else:
            NEXT(str(a)+"+"+str(b),b+1,end)
            NEXT(str(a)+"-"+str(b),b+1,end)
            NEXT(str(a)+str(b),b+1,end)
    NEXT(1,2,N)
    return [n,list]

n=random.randint(1,101)
print("The nymber of expressions which equal",n,"is",Find_expression(n)[0],"\nThey are:")
for i in Find_expression(n)[1]:
    print(i,"=",n)

for i in range(100):
    if i == 0:
        T=[]
        T.append(Find_expression(i+1)[0])
    else:
        T.append(Find_expression(i+1)[0])#record the number of expression that equal i+1
T=np.array(T)
print("The maximum number of expressions is",np.max(T),"when n is")
for i in np.where(T==np.max(T))[0]:
    print (i+1)
print("The minimum number of expressions is",np.min(T),"when n is")
for i in np.where(T==np.min(T))[0]:
    print (i+1)
