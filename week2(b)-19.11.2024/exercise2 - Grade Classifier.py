"""
This program takes the input scores and grades them
"""

def determine_score_grade(score):
    if score < 60:
        return "F"
    elif 60 <= score < 69:
        return "D"
    elif 70 <= score < 79:
        return "C"
    elif 80 <= score < 89:
        return "B"
    else:
        return "A"                      #


input_scores = [int(score) for score in input("enter the scores separated by space: ").split()]

for score in input_scores:
    print("score: ",score,"grade： ",determine_score_grade(score))
