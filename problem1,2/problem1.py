while True:
    try:
        num1 = float(input("please input the number 1:"))
        break
    except ValueError:
        print("Invalid format,please try again")     #when an incorrect number format is entered,re-enter

while True:
    try:
        num2 = float(input("please input the number 2:"))
        break
    except ValueError:
        print("Invalid format,please try again")
   #input two numbers

sum = num1 + num2           #Compute the sum of the numbers
product = num1 * num2       #compute the product of the numbers

print("the sum of the two numbers is:", sum)            #print the sum
print("the product of the two numbers is:", product)    #print the product