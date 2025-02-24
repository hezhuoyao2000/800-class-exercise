"""
This program can convert between Fahrenheit and Celsius and retains two decimal places, and can identify incorrect inputs and provides a solution.

e.g.:
right inputs and outcomes:
1. input: f88, outcome: 31.11
2. input: c33, outcome: 91.40

wrong inputs and outcomes:
1. input: f88/, outcome: invalid temperature number, please only enter the number instead of symbols or letters.
2. input: g33, outcome: invalid scale, please enter letters 'F' or 'C'(case insensitive).
3. input: g33#, outcome: invalid scale and temperature number, please enter letters 'F' or 'C'(case insensitive), and only enter the number instead of symbols or letters.
"""


def converter_to_celsius(degree_f) :     #converte the Fahrenheit degree to Celsius degree, and rounding to two decimal places
    return round((degree_f - 32)/1.8 , 2)

def converter_to_fahrenheit(degree_c):   #converte the Celsius degree to Fahrenheit degree, and rounding to two decimal places
    return round(32 + degree_c*1.8 , 2)

def recognize_input(user_input):         #Check the input format: if the initial letter is capital C or F and the rest are pure numbers
    if user_input.startswith('C') and user_input[1:].isdigit():     #right format, right scale and right numbers
        return 'C', int(user_input[1:])
    elif user_input.startswith('F') and user_input[1:].isdigit():   #right format, right scale and right numbers
        return 'F', int(user_input[1:])
    elif (not user_input.startswith('F') and not user_input.startswith('C')) and user_input[1:].isdigit():  #wrong format, wrong scale but right numbers
        return 'scaleerror', user_input[1:]
    elif not user_input[1:].isdigit() and (user_input.startswith('F') or user_input.startswith('C')):       #wrong format, right scale but wrong numbers
        return 'numerror', user_input[1:]
    else:                                                                                                   #wrong format, both are wrong
        return 'botherror', user_input[1:]


user_input = input("Enter the temperature, (e.g., ‘F51' for Fahrenheit, ‘C11' for Celsius): ").upper().strip()      #Convert letters to uppercase, remove spaces
scale, temp = recognize_input(user_input)

if scale == 'F':
    converted_temp = converter_to_celsius(temp)
    print(f"{user_input} fahrenheit degrees equals {converted_temp:.2f} celsius degrees.")
elif scale == 'C':
    converted_temp = converter_to_fahrenheit(temp)
    print(f"{user_input} celsius degrees equals {converted_temp:.2f} fahrenheit degrees.")      #output the right outcomes
elif scale == 'scaleerror':
    print("invalid scale, please enter letters 'F' or 'C'(case insensitive).")                  #report errors
elif scale == 'numerror':
    print("invalid temperature number, please only enter the number instead of symbols or letters.")
else:
    print("invalid scale and temperature number, please enter letters 'F' or 'C'(case insensitive), and only enter the number instead of symbols or letters.")