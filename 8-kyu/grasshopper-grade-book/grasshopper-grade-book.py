def get_grade(s1, s2, s3):
    a = (s1+s2+s3)/3
    
    
    if (90 <= a and a <= 100):    
        return 'A'
    elif (80 <= a and a < 90):
        return 'B'
    elif (70 <= a and a < 80):
        return 'C'
    elif (60 <= a and a < 70):
        return 'D'
    else:
        return 'F'
    