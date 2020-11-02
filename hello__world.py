

def sumfun(marks):
    sum_num = sum(marks)
    leght = len(marks)
    print("sum = ", sum_num)
    print("lenght = ", leght)
    avarage_mark = sum_num / leght
    return avarage_mark


def grademark(avgvalue):
    if avgvalue <= 65:
        grade = 'A'
    else:
        grade = 'B'
    return grade


marks = [50, 100, 70, 80]

avgvalue = sumfun(marks)
print("avarage mark is", avgvalue)


grade_mark = grademark(avgvalue)
print("your grade is", grade_mark)
