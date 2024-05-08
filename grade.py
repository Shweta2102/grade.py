score = float(input("Enter your score (0-100): "))
def calculate_grade(score):
    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score <= 89:
        return 'B'
    elif score >= 70 and score <= 79:
        return 'C'
    else:
        return 'Invalid score'
