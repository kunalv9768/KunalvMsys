#pattern program:
totalrows =int(input("Enter the no.of row: "))

for row in range (1, totalrows+1):
   #display spaces
   for space in range(1,(totalrows-row)+1):
    
    print(" ",end="")
#diaplay

    for symbol in range (1,row+1):
        print("*",end="")
    print()

# for row in range (1, no_row-1):
#     for coloum in range(1,row+1):
#         print("*",end=' ')
#     print()    

# for row in range (no_row-1,0,-1):
#         for coloum in range(1,row+1):
#             print("*",end=' ')
#         print()
