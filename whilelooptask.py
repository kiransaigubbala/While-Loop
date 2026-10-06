# sum of the digits of a number
n=int(input("Enter a number: "))
sum=0
while(n!=0):
    ld=n%10
    sum=sum+ld
    n=n//10
print("sum of the digits is ",sum)

# average of the digits of a number
n = int(input("Enter a number: "))
sum=0
avg=0
count=0
while(n!=0):
    ld=n%10
    sum=sum+ld
    count=count+1
    n=n//10
avg=sum/count
print("average of the digits is ",avg)

# sum of first and last digit of a number
n = int(input("Enter a number: "))
last_digit = n % 10
while n >= 10:
    n = n // 10
first_digit = n
sum = first_digit + last_digit
print("Sum of first and last digit is ", sum)

# average of digits that are divisible by 5 in a number
n = int(input("Enter a number: "))
sum = 0
count = 0
while n != 0:
    ld = n % 10
    if ld // 5 :
        sum = sum + 5
        count = count + 1
    n = n // 10
if count > 0:
    avg = sum // count
    print("Average of digits divisible by 5 is ", avg)
else:
    print("No digits divisible by 5 found.")


# difference between largest digit and smallest digit in a number
n = int(input("Enter a number: "))
largest_digit = 0
smallest_digit = 9
while n != 0:
    ld = n % 10
    if ld > largest_digit:
        largest_digit = ld
    if ld < smallest_digit:
        smallest_digit = ld
    n = n // 10
difference = largest_digit - smallest_digit
print("Difference between largest and smallest digit is ", difference)
