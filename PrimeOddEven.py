num=int(input(('What is the number you want to check?:')))

for i in range(2,num):
    #If the remainder is equal to zero, that means it can be divided
    if num % i==0:
        print(num,'is not a prime number')
        break
else:
    print(num,'is a prime number')

if num % 2!=0:
    print(num,'is an odd number')
elif num % 2==0:
    print(num,'is an even number')
    