#Junleizhou and Junhongcai explained to me what is recursion algorithm.
def Pascal_triangle(n):
    if n == 1:
        return [1]
    else:
        result = [1]
        lastline = Pascal_triangle(n-1)
        for i in range(1, len(lastline)):
            result.append(lastline[i-1]+lastline[i])
        result.append(1)
        return result
print("The 100th line of Pascal's triangle is:", Pascal_triangle(100), end="\n\n")
print("The 200th line of Pascal's triangle is:", Pascal_triangle(200))