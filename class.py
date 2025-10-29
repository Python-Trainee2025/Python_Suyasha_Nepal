# for i in range(0,11,2): #start, stop-1, step (optional, default=1)
#     print(i)

#pass (placeholder statement), break, continue

# for i in range(5):
#     if i==3:
#         pass
#     print("pass case: ", i)
#
# for i in range(5):
#     if i==3:
#         break
#     print("break case: ", i)
#
# for i in range(5):
#     if i==3:
#         continue
#     print("continue case: ", i)

#Prime Number
num= int(input("Enter a number: "))

count=0

for i in range(1, num+1):
    if num % i == 1:
        count+=1


if count==2:
    print("The number is prime.")
else:
    print("The number is not prime.")

    #push to gitHub

#global, non-local