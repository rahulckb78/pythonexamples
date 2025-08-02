n = int(input("Enter number of rows: "))
for i in range(n):
    ## For the spaces in the row
    for j in range(n-i-1):
        print(" ",end="")
    ## For the stars to be print
    for j in range(i+1):
        print("*",end="")
    print()
        