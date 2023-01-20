def scholarship_bak(score):
    if score == 5:
        return (3000)
    elif 4 <= score <= 5:
        return (2000)
    elif 3 <= score <= 4:
        return (1500)

def scholarship_asp(score):
    if score == 5:
        return (5000)
    elif 4 <= score < 5:
        return (4500)
    elif 3 <= score < 4:
        return (3500)


def pay(student_type,score):
    if  student_type == 1:
       print (scholarship_bak(score))
    else:
       print (scholarship_asp(score))

# "Тип студента": Бакалавриат - 1, Аспирантура - 0
pay(1, 4.5 )
