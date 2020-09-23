"""
loop: for, while
iterate: visit all elements in the linear data structure, eg list, array
traversal: visit all elements in non-linear data structure, eg binary tree
recursion: a method call itself
*/
"""

def recursive_factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * recursive_factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

print('this is recursive')
result1 = recursive_factorial(4)
print(result1)

print('this is iterative')
result2 = iterative_factorial(4)
print(result2)
