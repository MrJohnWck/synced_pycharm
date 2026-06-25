# import math
# for i in range(1,(359000*359000)+1):
#     print(sum((2*i)+1)))

# i = 179500
# sum = (i * (2 * i - 1) * (2 * i + 1)) // 3
# print(sum)
################################################################################################



# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# i=100
# sumsqr=(i * (i + 1)*(2 * i + 1))//6
# print(sumsqr)
#
# sumnum=i*(i+1)//2
# print(sumnum)
# sumnumsqr=sumnum*sumnum
# print(sumnumsqr)
#
# print(sumnumsqr-sumsqr)
################################################################################################



# find sum of all multiples of 3 OR 5 below 1000
# result=0
# for n in range(1,1000):
#  if n % 3 == 0 or n % 5 == 0:
#     result += n
#     print(result)




#Sum of Even fibonacci numbers, (code does not work)
# a=1
# b=2
# sum_even=0
# while b<=4000000:
#     if b%2==0:
#      sum_even+=b
#     a=b
#     b=a+b
#     print(sum_even)
#
# print(sum_even)


#Even Fibonacci numbers

#Initialising variables (a,b, sum_even)
# a=1
# b=2
# sum_even=0
# generating loop with conditions(number less than 4 mil,numer is even.)
# while a<=4000000:
#     if a%2==0:
# adding the number to a if the conditions are met
     # sum_even+=a
# updating the variable so that loop can continue moving ahead.
    # a, b=b, a+b

# print(sum_even)




#Pythagorean triplet
#conditions involving limits of a,b
# for a in range(1,1000):
#         for b in range(1,1000):
#c is equal to 1000-a-b (a+b+c=1000)
         # c=1000-a-b
         # if c>b:
#final given condition
          # if a*a+b*b==c*c:
          #  print(a * b * c)




def prime_factor(n):
    divisors





