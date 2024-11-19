def determine_health_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal"
    elif 24.9 <= bmi < 30:
        return "overweight"
    else:
        return "obesity"                #Determining Health Status based on bmi values

while True:
    try:
        height = float(input("please input the height(m):"))                    #input the height
        if 0 <= height <3:
            break
        else:
            print("Invalid format of height, please try again and make sure the value is between 0.5 and 3 meters.")
                                                                                #If the user does not enter the number in the unit of meters, re-enter
    except ValueError:
        print("Invalid format,please try again and make sure using \".\" ")     #If the user enters something that is not a number or or enters non-”.” symbol

while True:
    try:
        weight = float(input("please input the weight(kg):"))                   #input the weight
        break
    except ValueError:
        print("Invalid format,please try again and make sure using \".\" ")     #If the user enters something that is not a number or or enters non-”.” symbol


bmi = weight / (height ** 2)        #compute the BMI       underweight  Normal  Overweight  Obesity
health_statues = determine_health_status(bmi)

print(f"your BMI is:{bmi:.2f},{health_statues}")

