#table using the FOR LOOP
number = int(input('Enter the number which multiplication you want'))
print('multiplication of table number',number)
for count in range(1,11):
    print(number ,'X', count ,'=',number*count)