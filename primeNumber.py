# Program to check if a number is prime or not
import time

start=time.time()
num1 = 10000
num = 20000
a = 0 
b = []
# To take input from the user
#num = int(input("Enter a number: "))

for j in range(num1,num):
    # define a flag variable
    flag = False

    # check for factors
    for i in range(2, int(j/2)+1):
#    for i in range(2, j):

        if (j % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if not flag:
        a = a + 1
        b = b + [j]
        #print(j, "is a prime number")

print("found ", a, " prime numbers, more than ",num1," and less than ", num)
print(b)
print(time.time()-start)