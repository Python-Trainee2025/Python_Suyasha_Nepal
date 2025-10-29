# Take an input n and print the first n numbers in the fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21

# Regular method
# n= abs(int(input("Enter the number of Fibonacci elements: ")))
#
# x=0
# y=1
#
# print(x)
# print(y)
#
# for i in range(n-2):
#     t=x+y
#     print(t)
#     x=y
#     y=t

#Recursive method
n= abs(int(input("Enter the number of Fibonacci elements: ")))

def fib(x):
    if x <= 1:
        return x
    return fib(x - 1) + fib(x - 2)

for i in range(n):
    print(fib(i))