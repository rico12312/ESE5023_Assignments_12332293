#Junleizhou and Junhongcai explained to me what is recursion algorithm
import random
def Least_moves(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + Least_moves(n/2)
    else:
        return 1 + Least_moves(n-1)
b = random.randint(1,100)
print("The smallest number of moves from 1 to ",b,"is:",Least_moves(b))