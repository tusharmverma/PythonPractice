i = 0
gradeTotal = 0
totalPoints = 0
gradeA = 0
totalA = 0
check = 0
while (check != -1):
    totalA = float(input("Enter Total points for Exam {}(Enter (-1) to stop taking Inputs): ".format(i+1)))
    if (totalA == -1 ):
        check = -1
    else:
        gradeA = float(input("Enter Score For Exam {}: ".format(i+1)))
        if (gradeA > totalA):
            print("Error!! You entered score more than Maximum Score ")
            gradeTotal = -1
            totalPoints = -1
        else:
            if (gradeA < 0 or totalA < 0):
                print("Error!!! You entered Score in Negative")
                gradeTotal = -1
                totalPoints = -1
            else:
                gradeTotal = gradeTotal + gradeA
                totalPoints = totalPoints + totalA
                i = i+1

if (gradeTotal < 0 or totalPoints < 0):  
    print()
else:
    average = (gradeTotal/totalPoints)*100
    grade = 0
    if(average >=  72 and average <= 100):
        grade = 'Passed'
    else:
        grade = 'Fail'
    print("The Average of Exam scores is {:.2f} \nStudent {}. \n".format(average,grade))
